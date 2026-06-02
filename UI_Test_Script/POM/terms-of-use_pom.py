from playwright.sync_api import Page, Locator, expect, TimeoutError as PlaywrightTimeoutError

class GeneratedPage:
    """
    Page Object Model for the Styleup page.
    Encapsulates element XPaths and safe interaction methods.
    """

    def __init__(self, page: Page, timeout: int = 5000):
        """
        Initializes the GeneratedPage with the given Playwright Page and timeout.
        Stores XPath strings for interactable elements.
        """
        self._page = page
        self._timeout = timeout

        self._img_logo_xpath = "//img[@alt='logo']"
        self._input_search_bar_xpath = "//input[@id='search-bar']"

    def _safe_click(self, xpath: str):
        """
        Safely clicks an element specified by its XPath.
        Waits for visibility before clicking.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        locator.click()

    def _safe_fill(self, xpath: str, text: str):
        """
        Safely fills an input or textarea specified by its XPath.
        Waits for visibility and clears the field before filling.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        locator.fill("")
        locator.fill(text)

    def _safe_check(self, xpath: str):
        """
        Safely checks a checkbox or radio button specified by its XPath.
        Waits for visibility and checks only if not already checked.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        if not locator.is_checked():
            locator.check()

    def _safe_select(self, xpath: str, value: str):
        """
        Safely selects an option in a select element specified by its XPath.
        Waits for visibility before selecting.
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