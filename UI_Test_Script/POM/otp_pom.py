from playwright.sync_api import Page, Locator, expect, TimeoutError as PlaywrightTimeoutError

class GeneratedPage:
    """
    Page Object Model for the Payment OTP page.
    """

    def __init__(self, page: Page, timeout: int = 5000):
        """
        Initializes the GeneratedPage with XPath locators for interactable elements.

        :param page: Playwright Page object.
        :param timeout: Timeout in milliseconds for element interactions.
        """
        self._page = page
        self._timeout = timeout

        self._input_otp_xpath = "//input[@id='otP']"
        self._btn_submit_xpath = "//button[@id='submit']"
        self._lnk_bag_xpath = "//a[normalize-space()='BAG']"
        self._lnk_address_xpath = "//a[normalize-space()='ADDRESS']"
        self._lnk_payment_xpath = "//a[normalize-space()='PAYMENT']"

    def _safe_click(self, xpath: str):
        """
        Safely clicks an element specified by its XPath.

        :param xpath: XPath string of the element to click.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        locator.click()

    def _safe_fill(self, xpath: str, text: str):
        """
        Safely fills an input field specified by its XPath.

        :param xpath: XPath string of the input element.
        :param text: Text to fill into the input.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        locator.clear()
        locator.fill(text)

    def _safe_check(self, xpath: str):
        """
        Safely checks a checkbox or radio button specified by its XPath.

        :param xpath: XPath string of the checkbox or radio element.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        if not locator.is_checked():
            locator.check()

    def _safe_select(self, xpath: str, value: str):
        """
        Safely selects an option from a select dropdown specified by its XPath.

        :param xpath: XPath string of the select element.
        :param value: Value attribute of the option to select.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        locator.select_option(value)

    def fill_otp_field(self, otp: str):
        """
        Fills the OTP input field.

        :param otp: OTP value to enter.
        """
        self._safe_fill(self._input_otp_xpath, otp)

    def click_submit_button(self):
        """
        Clicks the SUBMIT button.
        """
        self._safe_click(self._btn_submit_xpath)

    def click_bag_link(self):
        """
        Clicks the BAG navigation link.
        """
        self._safe_click(self._lnk_bag_xpath)

    def click_address_link(self):
        """
        Clicks the ADDRESS navigation link.
        """
        self._safe_click(self._lnk_address_xpath)

    def click_payment_link(self):
        """
        Clicks the PAYMENT navigation link.
        """
        self._safe_click(self._lnk_payment_xpath)

    def validate_essential_elements(self):
        """
        Validates that all essential elements are visible on the page.
        """
        locator = self._page.locator(f"xpath={self._input_otp_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._btn_submit_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._lnk_bag_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._lnk_address_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._lnk_payment_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)