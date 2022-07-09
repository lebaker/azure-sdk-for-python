# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._sip_routing_service_operations import build_get_sip_configuration_request, build_patch_sip_configuration_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class SIPRoutingServiceOperationsMixin:

    @distributed_trace_async
    async def get_sip_configuration(
        self,
        **kwargs: Any
    ) -> "_models.SipConfiguration":
        """Gets SIP configuration for resource.

        Gets SIP configuration for resource.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SipConfiguration, or the result of cls(response)
        :rtype: ~azure.communication.phonenumbers.siprouting.models.SipConfiguration
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SipConfiguration"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-05-01-preview")  # type: str

        
        request = build_get_sip_configuration_request(
            api_version=api_version,
            template_url=self.get_sip_configuration.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SipConfiguration', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_sip_configuration.metadata = {'url': "/sip"}  # type: ignore


    @distributed_trace_async
    async def patch_sip_configuration(
        self,
        body: Optional["_models.SipConfiguration"] = None,
        **kwargs: Any
    ) -> "_models.SipConfiguration":
        """Patches SIP configuration for resource.

        Patches SIP configuration for resource.

        :param body: Configuration patch. Default value is None.
        :type body: ~azure.communication.phonenumbers.siprouting.models.SipConfiguration
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SipConfiguration, or the result of cls(response)
        :rtype: ~azure.communication.phonenumbers.siprouting.models.SipConfiguration
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SipConfiguration"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-05-01-preview")  # type: str
        content_type = kwargs.pop('content_type', "application/merge-patch+json")  # type: Optional[str]

        if body is not None:
            _json = self._serialize.body(body, 'SipConfiguration')
        else:
            _json = None

        request = build_patch_sip_configuration_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.patch_sip_configuration.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SipConfiguration', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    patch_sip_configuration.metadata = {'url': "/sip"}  # type: ignore
