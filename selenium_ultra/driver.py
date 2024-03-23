# custom implementation of Selenium webdriver
# author: https://github.com/Armen-Jean-Andreasian

from .custom_selenium import webdriver
from .custom_selenium.common import NoSuchDriverException
from .custom_selenium.common import NoSuchChromeExecutable
from .google_chrome_bin import DefaultGoogleChromeExePath
from .google_chrome_bin import DefaultChromedriverExePath
from .utils import FileSystem
from typing import Optional, Iterable, Any, Sequence


class Driver(webdriver.Chrome):
    def __init__(
            self,
            chrome_exe_filepath: Optional[str] = None,
            chromedriver_exe_filepath: Optional[str] = None,
            maximized_mode: bool = True,
            disable_controlled: bool = True,
            custom_option_arguments: tuple[str] | Iterable[str] = None,
            custom_option_experimental_arguments: tuple[tuple[str, Any]] = None

    ):
        """
        chrome_exe_filepath: filepath to Google Chrome executable [Optional]
        chromedriver_exe_filepath: filepath to chromedriver executable [Optional]
        maximized_mode: Browser window is maximized
        disable_controlled: Removes the message "is controlled by a software"
        custom_option_arguments: Iterable of driver option arguments
        custom_option_experimental_arguments: A sequence of sequence containing name value pairs. E.g. tuple[tuple[str, Any]]
        """

        # chrome.exe
        if chrome_exe_filepath is None:
            FileSystem.check_file_exists(
                path=DefaultGoogleChromeExePath().__str__(),
                name=DefaultGoogleChromeExePath().filename,
                err_to_raise=NoSuchChromeExecutable
            )
            chrome_exe_filepath = DefaultGoogleChromeExePath().__str__()

        # chromedriver.exe
        if chromedriver_exe_filepath is None:
            FileSystem.check_file_exists(
                path=DefaultChromedriverExePath().__str__(),
                name=DefaultChromedriverExePath().filename,
                err_to_raise=NoSuchDriverException
            )
            chromedriver_exe_filepath = DefaultChromedriverExePath().__str__()

        # initializations
        browser_service = webdriver.chrome.Service(executable_path=chromedriver_exe_filepath)
        browser_options = webdriver.ChromeOptions()

        # modifications
        if maximized_mode:
            browser_options.add_argument("start-maximized")

        if disable_controlled:
            browser_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            browser_options.add_experimental_option('useAutomationExtension', False)

        if custom_option_arguments:
            for option in custom_option_arguments:
                browser_options.add_argument(option)

        if custom_option_experimental_arguments:
            for experimental_option_pair in custom_option_experimental_arguments:
                browser_options.add_experimental_option(experimental_option_pair[0], experimental_option_pair[1])

        browser_options.binary_location = chrome_exe_filepath

        # result
        super().__init__(options=browser_options, service=browser_service)
        self.selenium_version = "4.18.1"

    def __version__(self):
        return self.selenium_version
