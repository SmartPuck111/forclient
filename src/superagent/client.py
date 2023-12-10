# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import SuperagentEnvironment
from .resources.agent.client import AgentClient, AsyncAgentClient
from .resources.api_user.client import ApiUserClient, AsyncApiUserClient
from .resources.datasource.client import AsyncDatasourceClient, DatasourceClient
from .resources.llm.client import AsyncLlmClient, LlmClient
from .resources.tool.client import AsyncToolClient, ToolClient
from .resources.workflow.client import AsyncWorkflowClient, WorkflowClient


class Superagent:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: SuperagentEnvironment = SuperagentEnvironment.DEFAULT,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.agent = AgentClient(client_wrapper=self._client_wrapper)
        self.llm = LlmClient(client_wrapper=self._client_wrapper)
        self.api_user = ApiUserClient(client_wrapper=self._client_wrapper)
        self.datasource = DatasourceClient(client_wrapper=self._client_wrapper)
        self.tool = ToolClient(client_wrapper=self._client_wrapper)
        self.workflow = WorkflowClient(client_wrapper=self._client_wrapper)


class AsyncSuperagent:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: SuperagentEnvironment = SuperagentEnvironment.DEFAULT,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.agent = AsyncAgentClient(client_wrapper=self._client_wrapper)
        self.llm = AsyncLlmClient(client_wrapper=self._client_wrapper)
        self.api_user = AsyncApiUserClient(client_wrapper=self._client_wrapper)
        self.datasource = AsyncDatasourceClient(client_wrapper=self._client_wrapper)
        self.tool = AsyncToolClient(client_wrapper=self._client_wrapper)
        self.workflow = AsyncWorkflowClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: SuperagentEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
