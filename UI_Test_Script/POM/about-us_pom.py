from playwright.sync_api import Page, Locator, expect, TimeoutError as PlaywrightTimeoutError

class GeneratedPage:
    """
    Page Object Model for the Styleup page.
    Encapsulates element locators and safe interaction methods.
    """

    def __init__(self, page: Page, timeout: int = 5000):
        """
        Initializes the GeneratedPage with XPath locators for interactable elements.

        :param page: Playwright Page object
        :param timeout: Timeout in milliseconds for element interactions
        """
        self._page = page
        self._timeout = timeout

        self._img_logo_xpath = "//img[@alt='logo']"
        self._input_search_bar_xpath = "//input[@id='search-bar']"

    def _safe_click(self, xpath: str):
        """
        Safely clicks an element specified by its XPath.

        :param xpath: XPath string of the element to click
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        locator.click()

    def _safe_fill(self, xpath: str, text: str):
        """
        Safely fills an input field specified by its XPath.

        :param xpath: XPath string of the input element
        :param text: Text to fill into the input
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        locator.clear()
        locator.fill(text)

    def _safe_check(self, xpath: str):
        """
        Safely checks a checkbox or radio button specified by its XPath.

        :param xpath: XPath string of the checkbox or radio element
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        if not locator.is_checked():
            locator.check()

    def _safe_select(self, xpath: str, value: str):
        """
        Safely selects an option in a select dropdown specified by its XPath.

        :param xpath: XPath string of the select element
        :param value: Value attribute of the option to select
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        locator.select_option(value)

    def click_logo_image(self):
        """
        Clicks the logo image.
        """
        self._safe_click(self._img_logo_xpath)

    def fill_search_bar(self, text: str):
        """
        Fills the search bar input with the provided text.

        :param text: Text to enter into the search bar
        """
        self._safe_fill(self._input_search_bar_xpath, text)

    def validate_essential_elements(self):
        """
        Validates that essential elements are visible on the page.
        """
        locator = self._page.locator(f"xpath={self._img_logo_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._input_search_bar_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)