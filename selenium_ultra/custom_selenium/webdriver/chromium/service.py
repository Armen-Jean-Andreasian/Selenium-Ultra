import typing
from selenium_ultra.custom_selenium.types import SubprocessStdAlias
from selenium_ultra.custom_selenium.webdriver.common import service


class ChromiumService(service.Service):
    """A Service class that is responsible for the starting and stopping the
    WebDriver instance of the ChromiumDriver.

    :param executable_path: install path of the executable.
    :param port: Port for the service to run on, defaults to 0 where the operating system will decide.
    :param service_args: (Optional) List of args to be passed to the subprocess when launching the executable.
    :param log_output: (Optional) int representation of STDOUT/DEVNULL, any IO instance or String path to file.
    :param env: (Optional) Mapping of environment variables for the new process, defaults to `os.environ`.
    """

    def __init__(
        self,
        executable_path: str = None,
        port: int = 0,
        service_args: typing.Optional[typing.List[str]] = None,
        log_output: SubprocessStdAlias = None,
        env: typing.Optional[typing.Mapping[str, str]] = None,
        **kwargs,
    ) -> None:
        self.service_args = service_args or []

        if isinstance(log_output, str):
            self.service_args.append(f"--log-path={log_output}")
            self.log_output = None
        else:
            self.log_output = log_output

        super().__init__(
            executable_path=executable_path,
            port=port,
            env=env,
            log_output=self.log_output,
            **kwargs,
        )

    def command_line_args(self) -> typing.List[str]:
        return [f"--port={self.port}"] + self.service_args
