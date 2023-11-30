/*
 * Copyright (c) 2023 Airbyte, Inc., all rights reserved.
 */

package io.airbyte.integrations.destination.redshift.operations;

import static io.airbyte.cdk.integrations.base.JavaBaseConstants.COLUMN_NAME_AB_EXTRACTED_AT;
import static io.airbyte.cdk.integrations.base.JavaBaseConstants.COLUMN_NAME_AB_ID;
import static io.airbyte.cdk.integrations.base.JavaBaseConstants.COLUMN_NAME_AB_LOADED_AT;
import static io.airbyte.cdk.integrations.base.JavaBaseConstants.COLUMN_NAME_AB_RAW_ID;
import static io.airbyte.cdk.integrations.base.JavaBaseConstants.COLUMN_NAME_DATA;
import static io.airbyte.cdk.integrations.base.JavaBaseConstants.COLUMN_NAME_EMITTED_AT;
import static org.jooq.impl.DSL.*;

import com.google.common.collect.Iterables;
import io.airbyte.cdk.db.jdbc.JdbcDatabase;
import io.airbyte.cdk.integrations.base.JavaBaseConstants;
import io.airbyte.cdk.integrations.destination.jdbc.JdbcSqlOperations;
import io.airbyte.cdk.integrations.destination.jdbc.SqlOperationsUtils;
import io.airbyte.cdk.integrations.destination_async.partial_messages.PartialAirbyteMessage;
import java.sql.SQLException;
import java.sql.Timestamp;
import java.time.Instant;
import java.util.List;
import java.util.UUID;
import org.jooq.BatchBindStep;
import org.jooq.DSLContext;
import org.jooq.SQLDialect;
import org.jooq.impl.DSL;
import org.jooq.impl.DefaultDataType;
import org.jooq.impl.SQLDataType;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class RedshiftSqlOperations extends JdbcSqlOperations {

  private static final Logger LOGGER = LoggerFactory.getLogger(RedshiftSqlOperations.class);
  public static final int REDSHIFT_VARCHAR_MAX_BYTE_SIZE = 65535;
  public static final int REDSHIFT_SUPER_MAX_BYTE_SIZE = 1000000;

  public RedshiftSqlOperations() {}

  private DSLContext getDslContext() {
    return using(SQLDialect.POSTGRES);
  }

  @Override
  protected String createTableQueryV1(final String schemaName, final String tableName) {
    return String.format("""
                         CREATE TABLE IF NOT EXISTS %s.%s (
                          %s VARCHAR PRIMARY KEY,
                          %s SUPER,
                          %s TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP)
                          """, schemaName, tableName,
                         JavaBaseConstants.COLUMN_NAME_AB_ID,
                         JavaBaseConstants.COLUMN_NAME_DATA,
                         JavaBaseConstants.COLUMN_NAME_EMITTED_AT);
  }

  @Override
  protected String createTableQueryV2(final String schemaName, final String tableName) {
    final DSLContext dsl = getDslContext();
    return dsl.createTableIfNotExists(name(schemaName, tableName))
        .column(COLUMN_NAME_AB_RAW_ID, SQLDataType.VARCHAR(36).nullable(false))
        .column(COLUMN_NAME_AB_EXTRACTED_AT,
            SQLDataType.TIMESTAMPWITHTIMEZONE.defaultValue(DSL.function("GETDATE", SQLDataType.TIMESTAMPWITHTIMEZONE)))
        .column(COLUMN_NAME_AB_LOADED_AT, SQLDataType.TIMESTAMPWITHTIMEZONE)
        .column(COLUMN_NAME_DATA, new DefaultDataType<>(null, String.class, "super").nullable(false))
        .getSQL();
  }

  @Override
  public void insertRecordsInternal(final JdbcDatabase database,
                                    final List<PartialAirbyteMessage> records,
                                    final String schemaName,
                                    final String tmpTableName)
      throws SQLException {
    LOGGER.info("actual size of batch: {}", records.size());

    // query syntax:
    // INSERT INTO public.users (ab_id, data, emitted_at) VALUES
    // (?, ?::jsonb, ?),
    // ...
    final String insertQueryComponent = String.format(
        "INSERT INTO %s.%s (%s, %s, %s) VALUES\n",
        schemaName,
        tmpTableName,
        JavaBaseConstants.COLUMN_NAME_AB_ID,
        JavaBaseConstants.COLUMN_NAME_DATA,
        JavaBaseConstants.COLUMN_NAME_EMITTED_AT);
    final String recordQueryComponent = "(?, JSON_PARSE(?), ?),\n";
    SqlOperationsUtils.insertRawRecordsInSingleQuery(insertQueryComponent, recordQueryComponent, database, records);
  }

  @Override
  protected void insertRecordsInternalV2(final JdbcDatabase database,
                                         final List<PartialAirbyteMessage> records,
                                         final String schemaName,
                                         final String tableName) {
    LOGGER.info("Total records received to insert: {}", records.size());
    for (List<PartialAirbyteMessage> batch : Iterables.partition(records, 5_000)) {
      try {
        // Execute only a subset of prepared statements on each connection. This code hangs (or rather runs
        // very slow) in redshift with batch size more than 10K records.
        database.execute(connection -> {
          LOGGER.info("Prepared batch size: {}, {}, {}", batch.size(), schemaName, tableName);
          final DSLContext create = using(connection, SQLDialect.POSTGRES);
          final BatchBindStep batchInsertStep = create.batch(create
              .insertInto(table(name(schemaName, tableName)),
                  field(COLUMN_NAME_AB_RAW_ID, SQLDataType.VARCHAR(36)),
                  field(COLUMN_NAME_DATA,
                      new DefaultDataType<>(null, String.class, "super")),
                  field(COLUMN_NAME_AB_EXTRACTED_AT, SQLDataType.TIMESTAMPWITHTIMEZONE),
                  field(COLUMN_NAME_AB_LOADED_AT, SQLDataType.TIMESTAMPWITHTIMEZONE))
              .values(null, function("JSON_PARSE", String.class, val((String) null)), null,
                  null)); // Jooq needs dummy values for batch binds
          for (PartialAirbyteMessage record : batch) {
            batchInsertStep.bind(val(UUID.randomUUID().toString()), val(record.getSerialized()), val(Timestamp.from(
                Instant.ofEpochMilli(record.getRecord().getEmittedAt()))), null);
          }
          batchInsertStep.execute();
          LOGGER.info("Executed batch size: {}, {}, {}", batch.size(), schemaName, tableName);
        });
      } catch (Exception e) {
        LOGGER.error("Error while inserting records", e);
        throw new RuntimeException(e);
      }
    }
  }

}
