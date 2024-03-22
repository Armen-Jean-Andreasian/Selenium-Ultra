from selenium_ultra.custom_selenium.webdriver.chromium import ChromiumDriver
from selenium_ultra.custom_selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from .options import Options
from .service import Service


class WebDriver(ChromiumDriver):
    """Controls the ChromeDriver and allows you to drive the browser."""

    def __init__(
        self,
        options: Options = None,
        service: Service = None,
        keep_alive: bool = True,
    ) -> None:
        """Creates a new instance of the chrome driver. Starts the service and
        then creates new instance of chrome driver.

        :Args:
         - options - this takes an instance of ChromeOptions
         - service - Service object for handling the browser driver if you need to pass extra details
         - keep_alive - Whether to configure ChromeRemoteConnection to use HTTP keep-alive.
        """
        service = service if service else Service()
        options = options if options else Options()

        super().__init__(
            browser_name=DesiredCapabilities.CHROME["browserName"],
            vendor_prefix="goog",
            options=options,
            service=service,
            keep_alive=keep_alive,
        )
