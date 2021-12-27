# flake8: noqa
#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.model.advanced_auth import AdvancedAuth
from openapi_client.model.airbyte_catalog import AirbyteCatalog
from openapi_client.model.airbyte_stream import AirbyteStream
from openapi_client.model.airbyte_stream_and_configuration import AirbyteStreamAndConfiguration
from openapi_client.model.airbyte_stream_configuration import AirbyteStreamConfiguration
from openapi_client.model.attempt_info_read import AttemptInfoRead
from openapi_client.model.attempt_read import AttemptRead
from openapi_client.model.attempt_status import AttemptStatus
from openapi_client.model.auth_specification import AuthSpecification
from openapi_client.model.check_connection_read import CheckConnectionRead
from openapi_client.model.check_operation_read import CheckOperationRead
from openapi_client.model.complete_destination_o_auth_request import CompleteDestinationOAuthRequest
from openapi_client.model.complete_o_auth_response import CompleteOAuthResponse
from openapi_client.model.complete_source_oauth_request import CompleteSourceOauthRequest
from openapi_client.model.connection_create import ConnectionCreate
from openapi_client.model.connection_id_request_body import ConnectionIdRequestBody
from openapi_client.model.connection_read import ConnectionRead
from openapi_client.model.connection_read_list import ConnectionReadList
from openapi_client.model.connection_schedule import ConnectionSchedule
from openapi_client.model.connection_search import ConnectionSearch
from openapi_client.model.connection_state import ConnectionState
from openapi_client.model.connection_status import ConnectionStatus
from openapi_client.model.connection_update import ConnectionUpdate
from openapi_client.model.data_type import DataType
from openapi_client.model.db_migration_execution_read import DbMigrationExecutionRead
from openapi_client.model.db_migration_read import DbMigrationRead
from openapi_client.model.db_migration_read_list import DbMigrationReadList
from openapi_client.model.db_migration_request_body import DbMigrationRequestBody
from openapi_client.model.db_migration_state import DbMigrationState
from openapi_client.model.destination_auth_specification import DestinationAuthSpecification
from openapi_client.model.destination_core_config import DestinationCoreConfig
from openapi_client.model.destination_create import DestinationCreate
from openapi_client.model.destination_definition_create import DestinationDefinitionCreate
from openapi_client.model.destination_definition_id_request_body import DestinationDefinitionIdRequestBody
from openapi_client.model.destination_definition_read import DestinationDefinitionRead
from openapi_client.model.destination_definition_read_list import DestinationDefinitionReadList
from openapi_client.model.destination_definition_specification_read import DestinationDefinitionSpecificationRead
from openapi_client.model.destination_definition_update import DestinationDefinitionUpdate
from openapi_client.model.destination_id_request_body import DestinationIdRequestBody
from openapi_client.model.destination_oauth_consent_request import DestinationOauthConsentRequest
from openapi_client.model.destination_read import DestinationRead
from openapi_client.model.destination_read_list import DestinationReadList
from openapi_client.model.destination_search import DestinationSearch
from openapi_client.model.destination_sync_mode import DestinationSyncMode
from openapi_client.model.destination_update import DestinationUpdate
from openapi_client.model.health_check_read import HealthCheckRead
from openapi_client.model.import_read import ImportRead
from openapi_client.model.import_request_body import ImportRequestBody
from openapi_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_client.model.invalid_input_property import InvalidInputProperty
from openapi_client.model.job_config_type import JobConfigType
from openapi_client.model.job_id_request_body import JobIdRequestBody
from openapi_client.model.job_info_read import JobInfoRead
from openapi_client.model.job_list_request_body import JobListRequestBody
from openapi_client.model.job_read import JobRead
from openapi_client.model.job_read_list import JobReadList
from openapi_client.model.job_status import JobStatus
from openapi_client.model.job_with_attempts_read import JobWithAttemptsRead
from openapi_client.model.known_exception_info import KnownExceptionInfo
from openapi_client.model.log_read import LogRead
from openapi_client.model.log_type import LogType
from openapi_client.model.logs_request_body import LogsRequestBody
from openapi_client.model.namespace_definition_type import NamespaceDefinitionType
from openapi_client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_client.model.notification import Notification
from openapi_client.model.notification_read import NotificationRead
from openapi_client.model.notification_type import NotificationType
from openapi_client.model.o_auth2_specification import OAuth2Specification
from openapi_client.model.o_auth_config_specification import OAuthConfigSpecification
from openapi_client.model.o_auth_consent_read import OAuthConsentRead
from openapi_client.model.operation_create import OperationCreate
from openapi_client.model.operation_id_request_body import OperationIdRequestBody
from openapi_client.model.operation_read import OperationRead
from openapi_client.model.operation_read_list import OperationReadList
from openapi_client.model.operation_update import OperationUpdate
from openapi_client.model.operator_configuration import OperatorConfiguration
from openapi_client.model.operator_dbt import OperatorDbt
from openapi_client.model.operator_normalization import OperatorNormalization
from openapi_client.model.operator_type import OperatorType
from openapi_client.model.pagination import Pagination
from openapi_client.model.resource_requirements import ResourceRequirements
from openapi_client.model.set_instancewide_destination_oauth_params_request_body import SetInstancewideDestinationOauthParamsRequestBody
from openapi_client.model.set_instancewide_source_oauth_params_request_body import SetInstancewideSourceOauthParamsRequestBody
from openapi_client.model.slack_notification_configuration import SlackNotificationConfiguration
from openapi_client.model.slug_request_body import SlugRequestBody
from openapi_client.model.source_auth_specification import SourceAuthSpecification
from openapi_client.model.source_core_config import SourceCoreConfig
from openapi_client.model.source_create import SourceCreate
from openapi_client.model.source_definition_create import SourceDefinitionCreate
from openapi_client.model.source_definition_id_request_body import SourceDefinitionIdRequestBody
from openapi_client.model.source_definition_read import SourceDefinitionRead
from openapi_client.model.source_definition_read_list import SourceDefinitionReadList
from openapi_client.model.source_definition_specification_read import SourceDefinitionSpecificationRead
from openapi_client.model.source_definition_update import SourceDefinitionUpdate
from openapi_client.model.source_discover_schema_read import SourceDiscoverSchemaRead
from openapi_client.model.source_id_request_body import SourceIdRequestBody
from openapi_client.model.source_oauth_consent_request import SourceOauthConsentRequest
from openapi_client.model.source_read import SourceRead
from openapi_client.model.source_read_list import SourceReadList
from openapi_client.model.source_search import SourceSearch
from openapi_client.model.source_update import SourceUpdate
from openapi_client.model.sync_mode import SyncMode
from openapi_client.model.synchronous_job_read import SynchronousJobRead
from openapi_client.model.upload_read import UploadRead
from openapi_client.model.web_backend_connection_create import WebBackendConnectionCreate
from openapi_client.model.web_backend_connection_read import WebBackendConnectionRead
from openapi_client.model.web_backend_connection_read_list import WebBackendConnectionReadList
from openapi_client.model.web_backend_connection_request_body import WebBackendConnectionRequestBody
from openapi_client.model.web_backend_connection_search import WebBackendConnectionSearch
from openapi_client.model.web_backend_connection_update import WebBackendConnectionUpdate
from openapi_client.model.web_backend_operation_create_or_update import WebBackendOperationCreateOrUpdate
from openapi_client.model.workspace_create import WorkspaceCreate
from openapi_client.model.workspace_give_feedback import WorkspaceGiveFeedback
from openapi_client.model.workspace_id_request_body import WorkspaceIdRequestBody
from openapi_client.model.workspace_read import WorkspaceRead
from openapi_client.model.workspace_read_list import WorkspaceReadList
from openapi_client.model.workspace_update import WorkspaceUpdate
