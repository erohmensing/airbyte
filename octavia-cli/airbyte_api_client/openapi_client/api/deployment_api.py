#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#
"""
    Airbyte Configuration API

    Airbyte Configuration API [https://airbyte.io](https://airbyte.io).  This API is a collection of HTTP RPC-style methods. While it is not a REST API, those familiar with REST should find the conventions of this API recognizable.  Here are some conventions that this API follows: * All endpoints are http POST methods. * All endpoints accept data via `application/json` request bodies. The API does not accept any data via query params. * The naming convention for endpoints is: localhost:8000/{VERSION}/{METHOD_FAMILY}/{METHOD_NAME} e.g. `localhost:8000/v1/connections/create`. * For all `update` methods, the whole object must be passed in, even the fields that did not change.  Change Management: * The major version of the API endpoint can be determined / specified in the URL `localhost:8080/v1/connections/create` * Minor version bumps will be invisible to the end user. The user cannot specify minor versions in requests. * All backwards incompatible changes will happen in major version bumps. We will not make backwards incompatible changes in minor version bumps. Examples of non-breaking changes (includes but not limited to...):   * Adding fields to request or response bodies.   * Adding new HTTP endpoints.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@airbyte.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient
from openapi_client.api_client import Endpoint as _Endpoint
from openapi_client.model.import_read import ImportRead
from openapi_client.model.import_request_body import ImportRequestBody
from openapi_client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_client.model.upload_read import UploadRead
from openapi_client.model.workspace_id_request_body import WorkspaceIdRequestBody
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)


class DeploymentApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.export_archive_endpoint = _Endpoint(
            settings={
                "response_type": (file_type,),
                "auth": [],
                "endpoint_path": "/v1/deployment/export",
                "operation_id": "export_archive",
                "http_method": "POST",
                "servers": None,
            },
            params_map={"all": [], "required": [], "nullable": [], "enum": [], "validation": []},
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {},
                "attribute_map": {},
                "location_map": {},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/x-gzip"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.export_workspace_endpoint = _Endpoint(
            settings={
                "response_type": (file_type,),
                "auth": [],
                "endpoint_path": "/v1/deployment/export_workspace",
                "operation_id": "export_workspace",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "workspace_id_request_body",
                ],
                "required": [
                    "workspace_id_request_body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "workspace_id_request_body": (WorkspaceIdRequestBody,),
                },
                "attribute_map": {},
                "location_map": {
                    "workspace_id_request_body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/x-gzip"], "content_type": ["application/json"]},
            api_client=api_client,
        )
        self.import_archive_endpoint = _Endpoint(
            settings={
                "response_type": (ImportRead,),
                "auth": [],
                "endpoint_path": "/v1/deployment/import",
                "operation_id": "import_archive",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "body",
                ],
                "required": [
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body": (file_type,),
                },
                "attribute_map": {},
                "location_map": {
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/x-gzip"]},
            api_client=api_client,
        )
        self.import_into_workspace_endpoint = _Endpoint(
            settings={
                "response_type": (ImportRead,),
                "auth": [],
                "endpoint_path": "/v1/deployment/import_into_workspace",
                "operation_id": "import_into_workspace",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "import_request_body",
                ],
                "required": [
                    "import_request_body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "import_request_body": (ImportRequestBody,),
                },
                "attribute_map": {},
                "location_map": {
                    "import_request_body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )
        self.upload_archive_resource_endpoint = _Endpoint(
            settings={
                "response_type": (UploadRead,),
                "auth": [],
                "endpoint_path": "/v1/deployment/upload_archive_resource",
                "operation_id": "upload_archive_resource",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "body",
                ],
                "required": [
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body": (file_type,),
                },
                "attribute_map": {},
                "location_map": {
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/x-gzip"]},
            api_client=api_client,
        )

    def export_archive(self, **kwargs):
        """Export Airbyte Configuration and Data Archive  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.export_archive(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            file_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        return self.export_archive_endpoint.call_with_http_info(**kwargs)

    def export_workspace(self, workspace_id_request_body, **kwargs):
        """Export Airbyte Workspace Configuration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.export_workspace(workspace_id_request_body, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_id_request_body (WorkspaceIdRequestBody):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            file_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["workspace_id_request_body"] = workspace_id_request_body
        return self.export_workspace_endpoint.call_with_http_info(**kwargs)

    def import_archive(self, body, **kwargs):
        """Import Airbyte Configuration and Data Archive  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.import_archive(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (file_type):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ImportRead
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["body"] = body
        return self.import_archive_endpoint.call_with_http_info(**kwargs)

    def import_into_workspace(self, import_request_body, **kwargs):
        """Import Airbyte Configuration into Workspace (this operation might change ids of imported configurations). Note, in order to use this api endpoint, you might need to upload a temporary archive resource with 'deployment/upload_archive_resource' first   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.import_into_workspace(import_request_body, async_req=True)
        >>> result = thread.get()

        Args:
            import_request_body (ImportRequestBody):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ImportRead
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["import_request_body"] = import_request_body
        return self.import_into_workspace_endpoint.call_with_http_info(**kwargs)

    def upload_archive_resource(self, body, **kwargs):
        """Upload a GZIP archive tarball and stage it in the server's cache as a temporary resource  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_archive_resource(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (file_type):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UploadRead
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["body"] = body
        return self.upload_archive_resource_endpoint.call_with_http_info(**kwargs)
