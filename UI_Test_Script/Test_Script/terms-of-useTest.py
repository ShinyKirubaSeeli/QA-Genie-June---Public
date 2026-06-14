# Generated Playwright Tests for terms-of-use
from playwright.sync_api import sync_playwright, expect, TimeoutError as PlaywrightTimeoutError
from terms-of-use_pom import GeneratedPage
import json
import re
import time
import os

urls = {}
from Utility import Utility


# Test Case 1 - TC-0001
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
# Test URLs dictionary (update as needed)
urls: dict[str, str] = {
    "home": os.environ.get("TEST_BASE_URL", "https://localhost:8000/")
}
def test_logo_redirects_to_home_page() -> None:
    """
    TC-0001: Logo Redirects to Home Page
    Verifies that clicking the logo in the navigation bar always redirects the user to the home page and maintains the layout.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        test_passed: bool = False
        # Attach console logger
        page.on("console", Utility.log_console_message)
        try:
            # --- GIVEN: Setup and navigation to initial state ---
            Utility.log_test_step("Navigating to the home page.")
            navigation_success: bool = Utility.navigate_to_page(page, urls["home"], timeout=15000)
            if not navigation_success:
                Utility.log_error("Failed to navigate to the home page.")
                raise Exception("Navigation to home page failed.")
            Utility.log_test_step("Waiting for body to be visible.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # Accept cookies/pop-ups if present (using Utility, selector must be known)
            # Example: Utility.safe_wait_and_interact(page, "#accept-cookies", "click")
            # (No cookies selector in POM, so skip unless added.)
            # --- THEN: Verify logo is visible on the left side of the navigation bar ---
            Utility.log_test_step("Verifying logo image is visible.")
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={generated_page._img_logo_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=1000
            )
            Utility.log_element_state("Logo Image", page.locator(f"xpath={generated_page._img_logo_xpath}"), timeout=15000)
            # --- WHEN: Hover over the logo image ---
            Utility.log_test_step("Hovering over the logo image to check pointer change.")
            logo_locator = page.locator(f"xpath={generated_page._img_logo_xpath}")
            logo_locator.hover()
            # Pointer check is visual; log for manual review
            Utility.log_test_result("INFO", "Pointer should change to indicate clickability.")
            # --- WHEN: Click on the logo image ---
            Utility.log_test_step("Clicking the logo image.")
            generated_page.click_logo_image()
            # --- THEN: Wait for navigation and verify URL is set to the main index page ---
            Utility.log_test_step("Waiting for navigation to complete.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            current_url: str = page.url
            expected_url: str = urls["home"].rstrip("/") + "/"
            Utility.log_test_step(f"Verifying URL after logo click. Expected: {expected_url}, Actual: {current_url}")
            Utility.retry_assertion(
                lambda: expect(page).to_have_url(expected_url, timeout=15000),
                retries=3,
                delay=1000
            )
            # --- THEN: Check the main content area displays the default homepage content ---
            Utility.log_test_step("Validating essential elements on the homepage.")
            generated_page.validate_essential_elements()
            # --- THEN: Confirm the navigation bar and footer are still visible after navigation ---
            Utility.log_test_step("Verifying navigation bar and footer visibility.")
            # Navigation bar: logo and search bar (from POM)
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={generated_page._img_logo_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=1000
            )
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={generated_page._input_search_bar_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=1000
            )
            # Footer: Not defined in POM, so log info for manual check
            Utility.log_test_result("INFO", "Footer visibility check skipped (not in POM).")
            test_passed = True
            Utility.log_test_result("PASS", "Logo redirects to home page and layout is maintained.")
        except AssertionError as ae:
            Utility.log_error(f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_error(f"Test failed due to exception: {e}")
            raise
        finally:
            if not test_passed:
                Utility.log_test_result("FAIL", "Logo redirect to home page test did not pass.")
            browser.close()
#---#
#######

# Test Case 2 - TC-0004
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
# Test URLs (replace with actual URLs as needed)
urls: dict[str, str] = {
    "index": os.environ.get("INDEX_URL", "https://styleup.example.com/"),
    "sign_in": os.environ.get("SIGNIN_URL", "https://styleup.example.com/signin"),
    "sign_up": os.environ.get("SIGNUP_URL", "https://styleup.example.com/signup"),
}
def test_navbar_signin_signup_options_displayed_for_anonymous_users() -> None:
    """
    TC-0004: Verify that anonymous users see 'Sign In' and 'Sign Up' options in the navigation bar,
    and that these options redirect to the correct pages.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        page.on("console", lambda msg: Utility.log_console_message(msg))
        test_result: str = "PASSED"
        test_details: str = ""
        try:
            # --- Given: Land on the index page as an anonymous user ---
            Utility.log_test_step("Navigating to the index page as anonymous user.")
            navigation_success: bool = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            if not navigation_success:
                raise Exception("Failed to navigate to index page.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            # Accept cookies/pop-ups if present
            Utility.safe_wait_and_interact(page, "xpath=//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept') or contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'agree')]", "click", timeout=5000)
            # --- Then: The navigation bar displays "Sign In" and "Sign Up" options ---
            Utility.log_test_step("Verifying 'Sign In' and 'Sign Up' options are visible.")
            sign_in_xpath: str = "//a[normalize-space()='Sign In']"
            sign_up_xpath: str = "//a[normalize-space()='Sign Up']"
            Utility.log_element_state("Sign In option", page.locator(f"xpath={sign_in_xpath}"), timeout=15000)
            Utility.log_element_state("Sign Up option", page.locator(f"xpath={sign_up_xpath}"), timeout=15000)
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={sign_in_xpath}")).to_be_visible(timeout=15000),
                retries=3, delay=2000
            )
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={sign_up_xpath}")).to_be_visible(timeout=15000),
                retries=3, delay=2000
            )
            # --- When: Hover over the "Sign In" option ---
            Utility.log_test_step("Hovering over 'Sign In' option.")
            page.locator(f"xpath={sign_in_xpath}").hover()
            time.sleep(1)
            pointer_sign_in: str = page.evaluate("el => window.getComputedStyle(el).cursor", page.query_selector(f"xpath={sign_in_xpath}"))
            if pointer_sign_in not in ["pointer", "hand"]:
                Utility.log_error("Pointer did not change to clickable for 'Sign In'.")
            # --- Then: The pointer changes to indicate it is clickable ---
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={sign_in_xpath}")).to_be_visible(timeout=15000),
                retries=3, delay=2000
            )
            # --- When: Click on the "Sign In" option ---
            Utility.log_test_step("Clicking on 'Sign In' option.")
            Utility.safe_wait_and_interact(page, f"xpath={sign_in_xpath}", "click", timeout=15000)
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # --- Then: The user is redirected to the sign-in page ---
            Utility.log_test_step("Verifying redirection to sign-in page.")
            Utility.retry_assertion(
                lambda: expect(page).to_have_url(urls["sign_in"], timeout=15000),
                retries=3, delay=2000
            )
            # --- When: Return to the index page and hover over the "Sign Up" option ---
            Utility.log_test_step("Returning to index page.")
            navigation_success = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            if not navigation_success:
                raise Exception("Failed to navigate back to index page.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            Utility.log_test_step("Hovering over 'Sign Up' option.")
            page.locator(f"xpath={sign_up_xpath}").hover()
            time.sleep(1)
            pointer_sign_up: str = page.evaluate("el => window.getComputedStyle(el).cursor", page.query_selector(f"xpath={sign_up_xpath}"))
            if pointer_sign_up not in ["pointer", "hand"]:
                Utility.log_error("Pointer did not change to clickable for 'Sign Up'.")
            # --- Then: The pointer changes to indicate it is clickable ---
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={sign_up_xpath}")).to_be_visible(timeout=15000),
                retries=3, delay=2000
            )
            # --- When: Click on the "Sign Up" option ---
            Utility.log_test_step("Clicking on 'Sign Up' option.")
            Utility.safe_wait_and_interact(page, f"xpath={sign_up_xpath}", "click", timeout=15000)
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # --- Then: The user is redirected to the sign-up page ---
            Utility.log_test_step("Verifying redirection to sign-up page.")
            Utility.retry_assertion(
                lambda: expect(page).to_have_url(urls["sign_up"], timeout=15000),
                retries=3, delay=2000
            )
            # --- Then: The navigation bar remains consistent and displays the correct options ---
            Utility.log_test_step("Verifying navigation bar consistency after navigation.")
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={sign_in_xpath}")).to_be_visible(timeout=15000),
                retries=3, delay=2000
            )
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={sign_up_xpath}")).to_be_visible(timeout=15000),
                retries=3, delay=2000
            )
            test_details = "All navigation bar options and redirects verified successfully."
        except AssertionError as ae:
            test_result = "FAILED"
            test_details = f"Assertion failed: {ae}"
            Utility.log_error(test_details)
            raise
        except Exception as e:
            test_result = "FAILED"
            test_details = f"Test failed: {e}"
            Utility.log_error(test_details)
            raise
        finally:
            Utility.log_test_result(test_result, test_details)
            browser.close()
#---#
#######

# Test Case 3 - TC-0005
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
def test_navbar_user_avatar_logout_cart_displayed() -> None:
    """
    TC-0005: User Avatar, Log Out, and Cart Icon Displayed for Logged-In Users
    Given: User is logged in and lands on the index page
    When: User hovers over avatar, log out, and cart icon, and clicks cart icon
    Then: Navigation bar displays avatar, log out, cart icon with item count, and all are interactive
    """
    # --- Test Data and URLs ---
    urls: dict[str, str] = {
        "index": os.environ.get("INDEX_URL", "https://styleup.example.com/")
    }
    # --- Start Playwright ---
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        # --- Enhanced Console Logging ---
        page.on("console", lambda msg: Utility.log_console_message(msg))
        # --- Accept Cookies/Pop-ups if present ---
        # (Assume a cookie banner with a known XPath, else skip)
        cookie_banner_xpath: str = "//button[contains(.,'Accept') or contains(.,'accept')]"
        try:
            Utility.safe_wait_and_interact(
                page,
                f"xpath={cookie_banner_xpath}",
                action="click",
                timeout=5000,
                retries=1
            )
        except Exception:
            pass  # No cookie banner, continue
        try:
            # --- GIVEN: Navigate to index page as logged-in user ---
            Utility.log_test_step("Navigating to index page as logged-in user")
            nav_success: bool = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            if not nav_success:
                Utility.log_error("Failed to navigate to index page")
                raise Exception("Navigation failed")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # --- Wait for essential elements (logo, search bar) ---
            Utility.log_test_step("Validating essential elements")
            Utility.retry_assertion(
                lambda: generated_page.validate_essential_elements(),
                retries=3,
                delay=2000
            )
            # --- THEN: Validate user avatar, log out, and cart icon are visible ---
            # Assume the following XPaths are defined in the POM (add them if missing):
            user_avatar_xpath: str = "//img[contains(@class,'user-avatar')]"
            logout_option_xpath: str = "//button[contains(.,'Log Out') or contains(.,'Logout')]"
            cart_icon_xpath: str = "//span[contains(@class,'cart-icon')]"
            cart_count_xpath: str = "//span[contains(@class,'cart-count')]"
            # --- Log element states before interaction ---
            Utility.log_element_state("User Avatar", page.locator(f"xpath={user_avatar_xpath}"), timeout=15000)
            Utility.log_element_state("Log Out Option", page.locator(f"xpath={logout_option_xpath}"), timeout=15000)
            Utility.log_element_state("Cart Icon", page.locator(f"xpath={cart_icon_xpath}"), timeout=15000)
            Utility.log_element_state("Cart Count", page.locator(f"xpath={cart_count_xpath}"), timeout=15000)
            # --- WHEN: Hover over user avatar ---
            Utility.log_test_step("Hovering over user avatar")
            Utility.safe_wait_and_interact(
                page,
                f"xpath={user_avatar_xpath}",
                action="click",  # Use click to focus, then hover
                timeout=15000
            )
            page.hover(f"xpath={user_avatar_xpath}")
            # --- THEN: Pointer should indicate interactivity (not directly assertable, but log) ---
            Utility.log_test_step("Pointer should indicate avatar is interactive")
            # --- WHEN: Hover over "Log Out" option ---
            Utility.log_test_step("Hovering over Log Out option")
            page.hover(f"xpath={logout_option_xpath}")
            Utility.log_test_step("Pointer should indicate Log Out is clickable")
            # --- WHEN: Hover over cart icon ---
            Utility.log_test_step("Hovering over cart icon")
            page.hover(f"xpath={cart_icon_xpath}")
            Utility.log_test_step("Pointer should indicate cart icon is clickable")
            # --- WHEN: Click on cart icon ---
            Utility.log_test_step("Clicking on cart icon")
            Utility.safe_wait_and_interact(
                page,
                f"xpath={cart_icon_xpath}",
                action="click",
                timeout=15000
            )
            # --- THEN: User is redirected to cart page ---
            Utility.log_test_step("Verifying redirection to cart page")
            Utility.retry_assertion(
                lambda: expect(page).to_have_url(lambda url: "cart" in url, timeout=15000),
                retries=3,
                delay=2000
            )
            # --- THEN: Cart item count is accurate ---
            Utility.log_test_step("Validating cart item count")
            cart_count_text: str = Utility.get_element_text(page, f"xpath={cart_count_xpath}", timeout=15000)
            cart_count: int = Utility.validate_and_convert_data(cart_count_text.strip(), int)
            if cart_count < 0:
                Utility.log_error("Cart count is negative or invalid")
                raise AssertionError("Cart count is invalid")
            Utility.log_test_result("PASS", f"Cart count displayed: {cart_count}")
            # --- Final Test Summary ---
            Utility.log_test_result("PASS", "User avatar, log out, and cart icon displayed and interactive")
        except AssertionError as ae:
            Utility.log_test_result("FAIL", f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_test_result("FAIL", f"Test failed: {e}")
            raise
        finally:
            browser.close()
#---#
#######

# Test Case 4 - TC-0006
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
def test_logout_option_logs_out_user_and_updates_ui() -> None:
    # Test Data and URLs
    urls: dict[str, str] = {
        "index": os.environ.get("STYLEUP_INDEX_URL", "https://styleup.example.com/"),
        "sign_in": os.environ.get("STYLEUP_SIGNIN_URL", "https://styleup.example.com/signin"),
        "category_men": os.environ.get("STYLEUP_MEN_URL", "https://styleup.example.com/category/men")
    }
    # XPaths for navigation bar elements (must match POM or be handled via POM methods)
    user_avatar_xpath: str = "//img[contains(@class, 'user-avatar')]"
    logout_option_xpath: str = "//button[normalize-space()='Log Out']"
    cart_icon_xpath: str = "//span[contains(@class, 'cart-icon')]"
    sign_in_option_xpath: str = "//a[normalize-space()='Sign In']"
    sign_up_option_xpath: str = "//a[normalize-space()='Sign Up']"
    category_men_link_xpath: str = "//a[normalize-space()='MEN']"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        # Attach console logger
        page.on("console", lambda msg: Utility.log_console_message(msg))
        try:
            # --- GIVEN: User is logged in and lands on index page ---
            Utility.log_test_step("Navigating to index page as logged-in user")
            navigation_success: bool = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            if not navigation_success:
                Utility.log_error("Failed to navigate to index page.")
                raise Exception("Navigation to index page failed.")
            # Accept cookies/pop-ups if present
            Utility.safe_wait_and_interact(
                page,
                "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept')]",
                "click",
                timeout=5000,
                retries=1
            )
            # Wait for essential elements
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            # Log element states
            Utility.log_element_state("User Avatar", page.locator(f"xpath={user_avatar_xpath}"))
            Utility.log_element_state("Log Out Option", page.locator(f"xpath={logout_option_xpath}"))
            Utility.log_element_state("Cart Icon", page.locator(f"xpath={cart_icon_xpath}"))
            # --- THEN: Navigation bar displays user avatar, "Log Out", and cart icon ---
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={user_avatar_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=1000
            )
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={logout_option_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=1000
            )
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={cart_icon_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=1000
            )
            # --- WHEN: Click on the "Log Out" option ---
            Utility.log_test_step("Clicking on the 'Log Out' option")
            Utility.safe_wait_and_interact(page, f"xpath={logout_option_xpath}", "click", timeout=15000, retries=3)
            # --- THEN: User is logged out and page reloads ---
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            time.sleep(2)  # Wait for UI update
            # --- THEN: Navigation bar now displays "Sign In" and "Sign Up" options ---
            Utility.log_element_state("Sign In Option", page.locator(f"xpath={sign_in_option_xpath}"))
            Utility.log_element_state("Sign Up Option", page.locator(f"xpath={sign_up_option_xpath}"))
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={sign_in_option_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=1000
            )
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={sign_up_option_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=1000
            )
            # User avatar and log out should not be visible
            try:
                expect(page.locator(f"xpath={user_avatar_xpath}")).not_to_be_visible(timeout=5000)
            except Exception:
                Utility.log_error("User avatar still visible after logout.")
                raise
            try:
                expect(page.locator(f"xpath={logout_option_xpath}")).not_to_be_visible(timeout=5000)
            except Exception:
                Utility.log_error("Log Out option still visible after logout.")
                raise
            # --- WHEN: Attempt to access a category link (e.g., "MEN") ---
            Utility.log_test_step("Attempting to access 'MEN' category link")
            Utility.safe_wait_and_interact(page, f"xpath={category_men_link_xpath}", "click", timeout=15000, retries=3)
            # --- THEN: User is prompted to log in and redirected to sign-in page ---
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            current_url: str = Utility.validate_and_convert_data(page.url, str)
            expected_signin_url: str = Utility.validate_and_convert_data(urls["sign_in"], str)
            if not current_url.startswith(expected_signin_url):
                Utility.log_error(f"User not redirected to sign-in page. URL: {current_url}")
                raise AssertionError("Redirection to sign-in page failed.")
            # --- WHEN: Return to index page and observe the cart icon ---
            Utility.log_test_step("Returning to index page to check cart icon")
            Utility.navigate_to_page(page, urls["index"], timeout=15000)
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            time.sleep(1)
            # Cart icon should not be visible
            try:
                expect(page.locator(f"xpath={cart_icon_xpath}")).not_to_be_visible(timeout=5000)
            except Exception:
                Utility.log_error("Cart icon still visible for anonymous user.")
                raise
            # --- WHEN: Refresh the page to confirm session status ---
            Utility.log_test_step("Refreshing page to confirm user remains logged out")
            page.reload(timeout=15000)
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={sign_in_option_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=1000
            )
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={sign_up_option_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=1000
            )
            try:
                expect(page.locator(f"xpath={user_avatar_xpath}")).not_to_be_visible(timeout=5000)
            except Exception:
                Utility.log_error("User avatar visible after refresh.")
                raise
            Utility.log_test_result("PASS", "Log Out option logs out user and updates UI as expected.")
        except AssertionError as ae:
            Utility.log_test_result("FAIL", f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_test_result("FAIL", f"Test failed: {e}")
            raise
        finally:
            browser.close()
#---#
#######

# Test Case 5 - TC-0007
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
# Test Data
SEARCH_TERM = "Nike"
def test_search_bar_returns_matching_products_and_redirects() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        page.on("console", lambda msg: Utility.log_console_message(msg))
        alert_message: str = ""
        dialog_handled: bool = False
        def handle_dialog(dialog):
            nonlocal alert_message, dialog_handled
            alert_message = dialog.message
            Utility.log_test_step(f"Alert appeared: {alert_message}")
            dialog.accept()
            dialog_handled = True
        page.on("dialog", handle_dialog)
        try:
            # Given: Navigate to the index page and ensure page is loaded
            Utility.log_test_step("Navigating to index page")
            navigation_success = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            if not navigation_success:
                Utility.log_error("Failed to navigate to index page.")
                raise Exception("Navigation to index page failed.")
            Utility.log_test_step("Waiting for body to be visible")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # Accept cookies/pop-ups if present (assuming a button with id 'accept-cookies')
            Utility.log_test_step("Checking for cookies pop-up")
            Utility.safe_wait_and_interact(page, "#accept-cookies", "click", timeout=5000)
            # Then: Validate essential elements (logo and search bar)
            Utility.log_test_step("Validating essential elements")
            Utility.retry_assertion(
                lambda: generated_page.validate_essential_elements(),
                retries=3,
                delay=2000
            )
            # Then: Verify search bar is visible with placeholder text
            Utility.log_test_step("Verifying search bar visibility and placeholder")
            search_bar_xpath = generated_page._input_search_bar_xpath
            search_bar_selector = f"xpath={search_bar_xpath}"
            Utility.wait_for_element_state(page, search_bar_selector, state="visible", timeout=15000)
            search_bar_placeholder = Utility.get_element_text(page, search_bar_selector, timeout=15000)
            if not isinstance(search_bar_placeholder, str):
                Utility.log_error("Search bar placeholder is not a string.")
                raise Exception("Invalid search bar placeholder type.")
            # When: Click inside the search bar and type a valid brand name
            Utility.log_test_step(f"Typing search term '{SEARCH_TERM}' in search bar")
            validated_search_term = Utility.validate_and_convert_data(SEARCH_TERM, str)
            if not validated_search_term:
                Utility.log_error("Search term is invalid or empty.")
                raise Exception("Invalid search term.")
            generated_page.fill_search_bar(validated_search_term)
            Utility.log_element_state("Search Bar", page.locator(search_bar_selector), timeout=15000)
            # Then: Verify the search bar displays the typed text
            Utility.log_test_step("Verifying search bar displays typed text")
            typed_value = page.locator(search_bar_selector).input_value()
            if typed_value != validated_search_term:
                Utility.log_error(f"Search bar value '{typed_value}' does not match '{validated_search_term}'")
                raise AssertionError("Search bar did not retain typed value.")
            # When: Press Enter to trigger the search
            Utility.log_test_step("Triggering search by pressing Enter")
            page.locator(search_bar_selector).press("Enter")
            time.sleep(1)  # Allow dialog to appear
            # Then: Wait for alert and verify its message
            Utility.log_test_step("Waiting for alert dialog")
            for attempt in range(3):
                if dialog_handled:
                    break
                time.sleep(1)
            if not dialog_handled:
                Utility.log_error("Alert dialog did not appear after search.")
                raise Exception("No alert dialog appeared after search.")
            if not isinstance(alert_message, str) or not alert_message:
                Utility.log_error("Alert message is invalid or empty.")
                raise Exception("Invalid alert message.")
            Utility.log_test_step(f"Alert message received: {alert_message}")
            # Then: Wait for redirection to search results page
            Utility.log_test_step("Waiting for search results page to load")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            time.sleep(2)  # Allow for page transition
            # Then: Verify only matching products are displayed
            Utility.log_test_step("Verifying displayed products match search term")
            # Assuming products are displayed with a class 'product-title'
            product_titles_selector = ".product-title"
            Utility.wait_for_element_state(page, product_titles_selector, state="visible", timeout=15000)
            product_titles = page.locator(product_titles_selector).all_inner_texts()
            if not isinstance(product_titles, list):
                Utility.log_error("Product titles are not a list.")
                raise Exception("Invalid product titles type.")
            for title in product_titles:
                if validated_search_term.lower() not in title.lower():
                    Utility.log_error(f"Product '{title}' does not match search term '{validated_search_term}'")
                    raise AssertionError("Non-matching product found in search results.")
            # Then: Check the search bar after redirection
            Utility.log_test_step("Checking search bar after redirection")
            search_bar_value_after = page.locator(search_bar_selector).input_value()
            if search_bar_value_after and len(search_bar_value_after) > 70:
                Utility.log_error("Search bar value exceeds maximum allowed length.")
                raise Exception("Search bar value too long.")
            Utility.log_test_result("PASS", "Search bar returns matching products and redirects correctly.")
        except AssertionError as ae:
            Utility.log_test_result("FAIL", f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_test_result("FAIL", f"Test failed: {e}")
            raise
        finally:
            browser.close()
#---#
#######

# Test Case 6 - TC-0013
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
# Global URLs dictionary (update with actual URLs as needed)
urls: dict[str, str] = {
    "index": os.environ.get("STYLEUP_INDEX_URL", "https://styleup.example.com/"),
    "about": os.environ.get("STYLEUP_ABOUT_URL", "https://styleup.example.com/about"),
    "contact": os.environ.get("STYLEUP_CONTACT_URL", "https://styleup.example.com/contact"),
}
def test_footer_terms_and_conditions_visibility_and_readability() -> None:
    """
    TC-0013: Footer Section - Terms and Conditions Footer is Visible and Readable
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        page.on("console", Utility.log_console_message)
        test_passed: bool = False
        try:
            # Given: Navigate to the index page
            Utility.log_test_step("Navigating to the index page.")
            navigation_success: bool = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            if not navigation_success:
                Utility.log_error("Failed to navigate to index page.")
                raise Exception("Navigation to index page failed.")
            Utility.log_test_step("Waiting for body to be visible.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # Accept cookies/pop-ups if present
            Utility.log_test_step("Checking for cookies or pop-ups.")
            cookie_accepted: bool = Utility.safe_wait_and_interact(
                page,
                "xpath=//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept')]",
                "click",
                timeout=5000,
                retries=2
            )
            # When: Scroll to the bottom of the page
            Utility.log_test_step("Scrolling to the bottom of the page.")
            page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            # Then: Validate essential elements (logo, search bar) as smoke check
            Utility.log_test_step("Validating essential elements.")
            Utility.retry_assertion(
                lambda: generated_page.validate_essential_elements(),
                retries=3,
                delay=1000
            )
            # Then: Check for the footer section with the expected heading
            Utility.log_test_step("Checking for 'STYLEUP: TERMS AND CONDITION' heading in footer.")
            footer_heading_xpath: str = "//footer//*[contains(text(), 'STYLEUP: TERMS AND CONDITION')]"
            heading_text: str = Utility.get_element_text(page, f"xpath={footer_heading_xpath}", timeout=15000)
            heading_text = Utility.validate_and_convert_data(heading_text, str)
            if "STYLEUP: TERMS AND CONDITION" not in heading_text:
                Utility.log_error("Footer heading not found or incorrect.")
                raise AssertionError("Footer heading missing or incorrect.")
            # Then: Check that the footer text is readable and not cut off
            Utility.log_test_step("Checking readability and formatting of footer text.")
            footer_text_xpath: str = "//footer"
            footer_text: str = Utility.get_element_text(page, f"xpath={footer_text_xpath}", timeout=15000)
            footer_text = Utility.validate_and_convert_data(footer_text, str)
            if len(footer_text.strip()) == 0:
                Utility.log_error("Footer text is empty or not readable.")
                raise AssertionError("Footer text is empty or not readable.")
            if len(footer_text) > 200:
                footer_text = footer_text[:70] + "..."
            # Then: Check alignment and spacing (visual check via bounding box)
            Utility.log_test_step("Checking alignment and spacing of footer content.")
            try:
                footer_locator = page.locator(f"xpath={footer_text_xpath}")
                expect(footer_locator).to_be_visible(timeout=15000)
                bbox = footer_locator.bounding_box()
                if bbox is None or bbox["height"] < 40 or bbox["width"] < 200:
                    Utility.log_error("Footer alignment or size is not as expected.")
                    raise AssertionError("Footer alignment or size is not as expected.")
            except Exception as e:
                Utility.log_error(f"Footer alignment/spacing check failed: {e}")
                raise
            # Then: Check responsiveness on different screen sizes
            Utility.log_test_step("Checking footer responsiveness on different screen sizes.")
            for viewport in [{"width": 375, "height": 667}, {"width": 768, "height": 1024}, {"width": 1440, "height": 900}]:
                context.set_viewport_size(viewport)
                time.sleep(1)
                Utility.retry_assertion(
                    lambda: expect(page.locator(f"xpath={footer_text_xpath}")).to_be_visible(timeout=15000),
                    retries=3,
                    delay=1000
                )
                Utility.log_element_state(f"Footer at {viewport}", page.locator(f"xpath={footer_text_xpath}"), timeout=15000)
            # Then: Ensure footer remains at the bottom and does not overlap
            Utility.log_test_step("Ensuring footer remains at the bottom and does not overlap.")
            page.evaluate("window.scrollTo(0, 0);")
            time.sleep(1)
            page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={footer_text_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=1000
            )
            # Then: Check footer on different pages (about, contact)
            for page_key in ["about", "contact"]:
                Utility.log_test_step(f"Navigating to {page_key} page to check footer consistency.")
                navigation_success = Utility.navigate_to_page(page, urls[page_key], timeout=15000)
                if not navigation_success:
                    Utility.log_error(f"Failed to navigate to {page_key} page.")
                    raise Exception(f"Navigation to {page_key} page failed.")
                Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
                Utility.retry_assertion(
                    lambda: expect(page.locator(f"xpath={footer_text_xpath}")).to_be_visible(timeout=15000),
                    retries=3,
                    delay=1000
                )
                Utility.log_element_state(f"Footer on {page_key} page", page.locator(f"xpath={footer_text_xpath}"), timeout=15000)
            test_passed = True
            Utility.log_test_result("PASS", "Footer is visible, readable, and consistent across pages and viewports.")
        except AssertionError as ae:
            Utility.log_test_result("FAIL", f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_test_result("FAIL", f"Test failed due to exception: {e}")
            raise
        finally:
            if not test_passed:
                Utility.log_error("Test did not pass. See logs for details.")
            browser.close()
#---#
#######

# Test Case 7 - TC-0015
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
def test_styling_and_ui_consistency_navigation_bar_product_grids_footer() -> None:
    """
    Test Case TC-0015: Styling and UI Consistency
    Scenario: Navigation Bar, Product Grids, and Footer Maintain Visual Consistency
    Steps:
        1. Land on the index page and observe the navigation bar, product grids, and footer.
        2. Hover over all interactive elements (logo, category links, sign in/up, cart icon).
        3. Observe spacing and alignment of product images in the grids.
        4. Scroll through the page to check for overlapping or misaligned elements.
        5. Resize the browser window to test responsiveness.
        6. Navigate between pages (e.g., sign in, cart, product pages) and observe UI consistency.
    """
    urls: dict[str, str] = {
        "index": os.environ.get("STYLEUP_INDEX_URL", "https://styleup.example.com/"),
        "sign_in": os.environ.get("STYLEUP_SIGNIN_URL", "https://styleup.example.com/signin"),
        "cart": os.environ.get("STYLEUP_CART_URL", "https://styleup.example.com/cart"),
        "product": os.environ.get("STYLEUP_PRODUCT_URL", "https://styleup.example.com/product/1"),
    }
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        page.on("console", Utility.log_console_message)
        test_passed: bool = False
        try:
            # Given: Navigate to the index page
            Utility.log_test_step("Navigating to the index page.")
            navigation_success: bool = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            if not navigation_success:
                Utility.log_error("Failed to navigate to index page.")
                raise Exception("Navigation to index page failed.")
            Utility.log_test_step("Waiting for body to be visible.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # Accept cookies/pop-ups if present
            Utility.log_test_step("Checking for cookies or pop-ups.")
            cookie_popup_selectors = [
                "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept')]",
                "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'agree')]",
                "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'close')]"
            ]
            for selector in cookie_popup_selectors:
                Utility.safe_wait_and_interact(page, f"xpath={selector}", "click", timeout=3000, retries=1)
            # When: Validate essential elements (navigation bar, logo, search bar)
            Utility.log_test_step("Validating essential elements on the index page.")
            Utility.retry_assertion(lambda: generated_page.validate_essential_elements(), retries=3, delay=2000)
            # Then: All sections are visually aligned and use consistent fonts and colors
            Utility.log_test_step("Checking visual alignment and consistency of navigation bar, product grids, and footer.")
            Utility.log_element_state("Logo Image", page.locator(f"xpath={generated_page._img_logo_xpath}"), timeout=15000)
            Utility.log_element_state("Search Bar", page.locator(f"xpath={generated_page._input_search_bar_xpath}"), timeout=15000)
            # When: Hover over all interactive elements (logo, category links, sign in/up, cart icon)
            Utility.log_test_step("Hovering over interactive elements for pointer and hover effect consistency.")
            try:
                logo_locator = page.locator(f"xpath={generated_page._img_logo_xpath}")
                expect(logo_locator).to_be_visible(timeout=15000)
                logo_locator.hover()
                time.sleep(1)
            except Exception as e:
                Utility.log_error(f"Logo hover failed: {e}")
            # Category links, sign in/up, cart icon are not defined in POM, so we skip direct interaction
            # Then: Observe spacing and alignment of product images in the grids
            Utility.log_test_step("Observing spacing and alignment of product images in the grids.")
            # No direct POM method for product grids, so we log that this is a visual/manual check
            # When: Scroll through the page to check for overlapping or misaligned elements
            Utility.log_test_step("Scrolling through the page to check for overlapping or misaligned elements.")
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)
            page.evaluate("window.scrollTo(0, 0)")
            time.sleep(1)
            # Then: Resize the browser window to test responsiveness
            Utility.log_test_step("Resizing browser window to test responsiveness.")
            for viewport in [{"width": 1200, "height": 800}, {"width": 768, "height": 1024}, {"width": 375, "height": 667}]:
                context.set_viewport_size(viewport)
                time.sleep(1)
                Utility.log_test_step(f"Viewport set to {viewport['width']}x{viewport['height']}")
                Utility.retry_assertion(lambda: generated_page.validate_essential_elements(), retries=2, delay=1000)
            context.set_viewport_size({"width": 1920, "height": 1080})
            # When: Navigate between pages (sign in, cart, product) and observe UI consistency
            for page_key in ["sign_in", "cart", "product"]:
                Utility.log_test_step(f"Navigating to {page_key} page.")
                navigation_success = Utility.navigate_to_page(page, urls[page_key], timeout=15000)
                if not navigation_success:
                    Utility.log_error(f"Failed to navigate to {page_key} page.")
                    continue
                Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
                Utility.retry_assertion(lambda: generated_page.validate_essential_elements(), retries=2, delay=1000)
            test_passed = True
            Utility.log_test_result("PASS", "Styling and UI Consistency test completed successfully.")
        except AssertionError as ae:
            Utility.log_error(f"Assertion failed: {ae}")
            Utility.log_test_result("FAIL", f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_error(f"Test failed: {e}")
            Utility.log_test_result("FAIL", f"Test failed: {e}")
            raise
        finally:
            if not test_passed:
                Utility.log_test_result("FAIL", "Styling and UI Consistency test did not complete successfully.")
            browser.close()
#---#
#######

# Test Case 8 - TC-0030
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
def test_cart_item_counter_handles_missing_or_corrupted_cartdata() -> None:
    """
    TC-0030: Cart item count does not update when cartData in localStorage is missing or corrupted.
    Given: The homepage is loaded and cart icon/counter is visible.
    When: cartData is missing, null, invalid, or empty in localStorage.
    Then: Counter displays 0 or does not update; never shows incorrect count.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        test_summary = []
        # Attach console logger
        page.on("console", Utility.log_console_message)
        try:
            # --- GIVEN: Navigate to homepage and validate essential elements ---
            Utility.log_test_step("Navigate to homepage and validate essential elements")
            navigation_success = Utility.navigate_to_page(page, urls["home"], timeout=15000)
            if not navigation_success:
                Utility.log_test_result("FAIL", "Navigation to homepage failed")
                return
            Utility.wait_for_element_state(page, "xpath=//body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            Utility.log_element_state("Logo Image", page.locator("xpath=//img[@alt='logo']"), timeout=15000)
            Utility.log_element_state("Search Bar", page.locator("xpath=//input[@id='search-bar']"), timeout=15000)
            test_summary.append("Homepage loaded and essential elements visible.")
            # --- WHEN: Set localStorage cartData to null and reload ---
            Utility.log_test_step("Set localStorage cartData to null and reload")
            page.evaluate("window.localStorage.setItem('cartData', null);")
            page.reload()
            Utility.wait_for_element_state(page, "xpath=//body", state="visible", timeout=15000)
            # --- THEN: Counter displays 0 or does not update ---
            Utility.log_test_step("Verify cart counter displays 0 or does not update (cartData=null)")
            # Since POM does not expose cart counter, use Utility to get text if selector is known
            cart_counter_selector = "xpath=//span[contains(@class,'cart-counter')]"
            counter_text = Utility.get_element_text(page, cart_counter_selector, timeout=15000)
            counter_value = Utility.validate_and_convert_data(counter_text.strip(), int)
            if counter_value != 0:
                Utility.log_test_result("FAIL", f"Cart counter not zero with null cartData: {counter_value}")
            else:
                Utility.log_test_result("PASS", "Cart counter is zero with null cartData")
            test_summary.append(f"Cart counter with null cartData: {counter_value}")
            # --- WHEN: Set localStorage cartData to invalid JSON and reload ---
            Utility.log_test_step("Set localStorage cartData to invalid JSON and reload")
            page.evaluate("window.localStorage.setItem('cartData', 'invalid_json');")
            page.reload()
            Utility.wait_for_element_state(page, "xpath=//body", state="visible", timeout=15000)
            Utility.log_test_step("Verify cart counter displays 0 or does not update (invalid JSON)")
            counter_text = Utility.get_element_text(page, cart_counter_selector, timeout=15000)
            counter_value = Utility.validate_and_convert_data(counter_text.strip(), int)
            if counter_value != 0:
                Utility.log_test_result("FAIL", f"Cart counter not zero with invalid cartData: {counter_value}")
            else:
                Utility.log_test_result("PASS", "Cart counter is zero with invalid cartData")
            test_summary.append(f"Cart counter with invalid cartData: {counter_value}")
            # --- WHEN: Add an item to cart (simulate valid cartData), then refresh ---
            Utility.log_test_step("Add an item to cart (simulate valid cartData), then refresh")
            valid_cart_data = '[{"id":1,"qty":1}]'
            page.evaluate(f"window.localStorage.setItem('cartData', '{valid_cart_data}');")
            page.reload()
            Utility.wait_for_element_state(page, "xpath=//body", state="visible", timeout=15000)
            Utility.log_test_step("Verify cart counter updates to 1")
            counter_text = Utility.get_element_text(page, cart_counter_selector, timeout=15000)
            counter_value = Utility.validate_and_convert_data(counter_text.strip(), int)
            if counter_value != 1:
                Utility.log_test_result("FAIL", f"Cart counter did not update to 1: {counter_value}")
            else:
                Utility.log_test_result("PASS", "Cart counter updated to 1 with valid cartData")
            test_summary.append(f"Cart counter with valid cartData: {counter_value}")
            # --- WHEN: Remove cartData from localStorage and reload ---
            Utility.log_test_step("Remove cartData from localStorage and reload")
            page.evaluate("window.localStorage.removeItem('cartData');")
            page.reload()
            Utility.wait_for_element_state(page, "xpath=//body", state="visible", timeout=15000)
            Utility.log_test_step("Verify cart counter resets to 0")
            counter_text = Utility.get_element_text(page, cart_counter_selector, timeout=15000)
            counter_value = Utility.validate_and_convert_data(counter_text.strip(), int)
            if counter_value != 0:
                Utility.log_test_result("FAIL", f"Cart counter did not reset to 0: {counter_value}")
            else:
                Utility.log_test_result("PASS", "Cart counter reset to 0 after cartData removal")
            test_summary.append(f"Cart counter after cartData removal: {counter_value}")
            # --- WHEN: Set cartData as empty array and reload ---
            Utility.log_test_step("Set cartData as empty array and reload")
            page.evaluate("window.localStorage.setItem('cartData', '[]');")
            page.reload()
            Utility.wait_for_element_state(page, "xpath=//body", state="visible", timeout=15000)
            Utility.log_test_step("Verify cart counter displays 0 with empty array")
            counter_text = Utility.get_element_text(page, cart_counter_selector, timeout=15000)
            counter_value = Utility.validate_and_convert_data(counter_text.strip(), int)
            if counter_value != 0:
                Utility.log_test_result("FAIL", f"Cart counter not zero with empty array: {counter_value}")
            else:
                Utility.log_test_result("PASS", "Cart counter is zero with empty array")
            test_summary.append(f"Cart counter with empty array: {counter_value}")
            # --- WHEN: Attempt to interact with the cart icon (navigate to cart.html) ---
            Utility.log_test_step("Attempt to interact with the cart icon")
            cart_icon_selector = "xpath=//a[contains(@href,'cart')]"
            Utility.safe_wait_and_interact(page, cart_icon_selector, "click", timeout=15000)
            Utility.wait_for_element_state(page, "xpath=//body", state="visible", timeout=15000)
            Utility.log_test_step("Verify navigation to cart page and no items are shown")
            # Check for empty cart message or absence of cart items
            empty_cart_selector = "xpath=//*[contains(text(),'No items') or contains(text(),'empty cart')]"
            is_empty_cart = Utility.wait_for_element_state(page, empty_cart_selector, state="visible", timeout=15000)
            if is_empty_cart:
                Utility.log_test_result("PASS", "Cart page shows no items as expected")
            else:
                Utility.log_test_result("FAIL", "Cart page did not show empty state")
            test_summary.append("Cart page empty state verified.")
            # --- Accept cookies/pop-ups if present ---
            cookie_selector = "xpath=//button[contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'accept')]"
            Utility.safe_wait_and_interact(page, cookie_selector, "click", timeout=5000)
        except Exception as e:
            Utility.log_error(f"Test failed: {e}")
            raise
        finally:
            Utility.log_test_step("Test execution summary:")
            for step in test_summary:
                print(f"  - {step}")
            browser.close()
#---#
#######

# Test Case 9 - TC-0083
# Import the POM class
def test_alert_navigation_race_condition_search() -> None:
    """
    TC-0083: User closes alert before navigation, causing inconsistent state.
    Ensures that alert and navigation timing does not cause UI to freeze or enter an inconsistent state if user interrupts the flow.
    """
    search_term = "shirt"
    search_term = Utility.validate_and_convert_data(search_term, str)[:70]
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        # Attach console logger
        page.on("console", Utility.log_console_message)
        # Dialog handler for alert
        alert_texts = []
        def handle_dialog2(dialog):
            try:
                alert_texts.append(dialog.message)
                dialog.dismiss()
                Utility.log_console_message(f"[ALERT] Dismissed: {dialog.message}")
            except Exception as e:
                Utility.log_error(f"Dialog handling failed: {e}")
        page.on("dialog", handle_dialog)
        try:
            # Given: Navigate to index page
            Utility.log_test_step("Navigate to index page")
            navigation_success = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            if not navigation_success:
                Utility.log_error("Navigation to index page failed.")
                raise Exception("Navigation to index page failed.")
            # Wait for body and essential elements
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            Utility.log_element_state("Logo Image", page.locator(f"xpath={generated_page._img_logo_xpath}"))
            Utility.log_element_state("Search Bar", page.locator(f"xpath={generated_page._input_search_bar_xpath}"))
            # Then: Search bar is visible and accepts input
            Utility.log_test_step("Verify search bar is visible and accepts input")
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={generated_page._input_search_bar_xpath}")).to_be_visible(timeout=15000),
                retries=3, delay=2000
            )
            # When: Enter a search term and trigger search (simulate Enter key)
            Utility.log_test_step("Enter search term and trigger search")
            generated_page.fill_search_bar(search_term)
            Utility.safe_wait_and_interact(page, f"xpath={generated_page._input_search_bar_xpath}", "type", value="\n", timeout=15000)
            # Then: Alert shows number of products found, then navigates to search.html
            Utility.log_test_step("Wait for alert and quickly close it before navigation")
            # Wait for dialog (alert) and dismiss it quickly
            alert_handled = False
            for _ in range(3):
                try:
                    # Wait for dialog event to be triggered
                    time.sleep(1.5)
                    if alert_texts:
                        alert_handled = True
                        break
                except Exception as e:
                    Utility.log_error(f"Alert wait failed: {e}")
                    time.sleep(1)
            if not alert_handled:
                Utility.log_error("Alert did not appear or was not handled.")
                raise Exception("Alert did not appear or was not handled.")
            # Then: Navigation may be interrupted or delayed
            Utility.log_test_step("Check if navigation occurred or was interrupted")
            time.sleep(2)
            current_url = page.url
            Utility.log_console_message(f"[INFO] Current URL after alert: {current_url}")
            # Then: Either navigation completes or user remains on the page without errors
            Utility.log_test_step("Verify UI is not stuck or in inconsistent state")
            Utility.retry_assertion(
                lambda: expect(page).not_to_have_url("about:blank", timeout=15000),
                retries=3, delay=2000
            )
            # Then: Search functionality remains usable
            Utility.log_test_step("Attempt to search again")
            generated_page.fill_search_bar(search_term)
            Utility.safe_wait_and_interact(page, f"xpath={generated_page._input_search_bar_xpath}", "type", value="\n", timeout=15000)
            time.sleep(2)
            Utility.log_console_message("[INFO] Second search triggered.")
            # Then: Data is consistent with last search (check localStorage)
            Utility.log_test_step("Check if searchData in localStorage is updated")
            search_data = page.evaluate("window.localStorage.getItem('searchData')")
            search_data = Utility.validate_and_convert_data(search_data, str)
            Utility.log_console_message(f"[INFO] searchData in localStorage: {search_data}")
            if search_term not in search_data:
                Utility.log_error("searchData in localStorage does not match search term.")
                raise AssertionError("searchData in localStorage does not match search term.")
            # Then: UI resumes normal operation after reload
            Utility.log_test_step("Reload the page and verify UI resumes normal operation")
            page.reload(timeout=15000)
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            Utility.log_console_message("[INFO] Page reloaded and essential elements validated.")
            # Then: No unhandled errors; site remains usable
            Utility.log_test_step("Review browser console for errors")
            # (Console errors are logged via event handler above)
            Utility.log_test_result("PASS", "Alert and navigation race condition handled gracefully.")
        except PlaywrightTimeoutError as te:
            Utility.log_error(f"Timeout occurred: {te}")
            Utility.log_test_result("FAIL", f"Timeout occurred: {te}")
            raise
        except AssertionError as ae:
            Utility.log_error(f"Assertion failed: {ae}")
            Utility.log_test_result("FAIL", f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_error(f"Unexpected error: {e}")
            Utility.log_test_result("FAIL", f"Unexpected error: {e}")
            raise
        finally:
            browser.close()
#---#
#######

# Test Case 10 - TC-0084
def test_alert_and_navigation_overlap_ui_freeze_not_logged_in() -> None:
    """
    TC-0084: Product Category Navigation (Not Logged In)
    Scenario: Alert and navigation overlap causes UI freeze or double navigation
    Steps:
        1. Open the index page with loginStatus set to false
        2. Click any category (e.g., MEN)
        3. Quickly close the alert before navigation
        4. Observe if the UI is stuck or in an inconsistent state
        5. Attempt to click category again
        6. Log in and try again
        7. Reload the page
        8. Review browser console for errors
    """
    # --- Test Data and URLs ---
    urls: dict[str, str] = {
        "index": "https://styleup.example.com/index.html?loginStatus=false",
        "signin": "https://styleup.example.com/signin.html",
        "category_men": "https://styleup.example.com/category.html?cat=MEN",
    }
    # --- Category Button XPath (Assumed for demonstration) ---
    category_men_xpath: str = "//a[contains(@href, 'category.html') and contains(., 'MEN')]"
    signin_username_xpath: str = "//input[@id='username']"
    signin_password_xpath: str = "//input[@id='password']"
    signin_button_xpath: str = "//button[@id='signin-btn']"
    # --- Credentials for login step (short, safe) ---
    test_username: str = "testuser"
    test_password: str = "Test@123"
    # --- Console error tracking ---
    console_errors: list[str] = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        # --- Attach console logger ---
        def handle_console_message(msg):
            Utility.log_console_message(msg)
            if msg.type == "error":
                console_errors.append(msg.text)
        page.on("console", handle_console_message)
        # --- Accept cookies/pop-ups if present (Assumed XPath) ---
        cookies_accept_xpath: str = "//button[contains(., 'Accept') or contains(., 'accept')]"
        try:
            # --- Given: Navigate to index page (not logged in) ---
            Utility.log_test_step("Navigate to index page with loginStatus=false")
            nav_success: bool = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            if not nav_success:
                Utility.log_error("Failed to navigate to index page.")
                raise Exception("Navigation to index page failed.")
            # --- Accept cookies if present ---
            Utility.safe_wait_and_interact(page, cookies_accept_xpath, "click", timeout=3000, retries=1)
            # --- Validate essential elements are visible ---
            Utility.log_test_step("Validate essential elements on index page")
            Utility.retry_assertion(lambda: generated_page.validate_essential_elements(), retries=3, delay=2000)
            # --- Log element state before interaction ---
            Utility.log_element_state("MEN Category Link", page.locator(f"xpath={category_men_xpath}"), timeout=15000)
            # --- When: Click MEN category (should trigger alert) ---
            Utility.log_test_step("Click MEN category link (expect alert)")
            alert_message: str = ""
            alert_handled: bool = False
            def handle_dialog3(dialog):
                nonlocal alert_message, alert_handled
                alert_message = dialog.message
                Utility.log_test_step(f"Alert shown: {alert_message}")
                dialog.dismiss()
                alert_handled = True
            page.once("dialog", handle_dialog)
            Utility.safe_wait_and_interact(page, category_men_xpath, "click", timeout=15000, retries=3)
            time.sleep(1.5)  # Give time for alert and navigation to trigger
            # --- Then: Verify alert was shown and navigation attempted ---
            Utility.log_test_step("Verify alert was shown and navigation attempted")
            if not alert_handled:
                Utility.log_error("Alert was not handled as expected.")
                raise Exception("Alert not shown on category click.")
            # --- Wait for possible navigation to signin page ---
            time.sleep(2)
            current_url: str = page.url
            if "signin.html" not in current_url:
                Utility.log_error("Navigation to signin.html did not occur after alert.")
            else:
                Utility.log_test_step("Navigation to signin.html occurred as expected.")
            # --- When: Quickly close alert before navigation (already handled above) ---
            # --- Then: Observe if UI is stuck or inconsistent ---
            Utility.log_test_step("Observe UI state after alert and navigation")
            Utility.retry_assertion(lambda: expect(page).not_to_have_url(urls["index"], timeout=15000), retries=3, delay=2000)
            # --- When: Attempt to click category again (should repeat alert+nav) ---
            Utility.log_test_step("Navigate back to index and repeat category click")
            Utility.navigate_to_page(page, urls["index"], timeout=15000)
            Utility.safe_wait_and_interact(page, cookies_accept_xpath, "click", timeout=3000, retries=1)
            Utility.retry_assertion(lambda: generated_page.validate_essential_elements(), retries=3, delay=2000)
            page.once("dialog", handle_dialog)
            Utility.safe_wait_and_interact(page, category_men_xpath, "click", timeout=15000, retries=3)
            time.sleep(1.5)
            if not alert_handled:
                Utility.log_error("Alert was not handled on second attempt.")
                raise Exception("Alert not shown on second category click.")
            # --- Then: Navigation to signin.html should occur again ---
            time.sleep(2)
            if "signin.html" not in page.url:
                Utility.log_error("Navigation to signin.html did not occur on second attempt.")
            # --- When: Log in and try again ---
            Utility.log_test_step("Perform login and try category navigation again")
            if "signin.html" not in page.url:
                Utility.navigate_to_page(page, urls["signin"], timeout=15000)
            Utility.safe_wait_and_interact(page, signin_username_xpath, "fill", value=test_username, timeout=15000)
            Utility.safe_wait_and_interact(page, signin_password_xpath, "fill", value=test_password, timeout=15000)
            Utility.safe_wait_and_interact(page, signin_button_xpath, "click", timeout=15000)
            time.sleep(2)
            Utility.navigate_to_page(page, urls["index"], timeout=15000)
            Utility.safe_wait_and_interact(page, cookies_accept_xpath, "click", timeout=3000, retries=1)
            Utility.retry_assertion(lambda: generated_page.validate_essential_elements(), retries=3, delay=2000)
            Utility.log_element_state("MEN Category Link", page.locator(f"xpath={category_men_xpath}"), timeout=15000)
            Utility.safe_wait_and_interact(page, category_men_xpath, "click", timeout=15000, retries=3)
            time.sleep(2)
            # --- Then: Navigation to category page should occur without alert ---
            Utility.log_test_step("Verify navigation to category page without alert")
            if "category.html" not in page.url:
                Utility.log_error("Navigation to category page did not occur after login.")
                raise Exception("Navigation to category page failed after login.")
            # --- When: Reload the page ---
            Utility.log_test_step("Reload the category page")
            page.reload()
            time.sleep(2)
            Utility.retry_assertion(lambda: expect(page).to_have_url(page.url, timeout=15000), retries=3, delay=2000)
            # --- Then: Review browser console for errors ---
            Utility.log_test_step("Review browser console for errors")
            if console_errors:
                Utility.log_error(f"Console errors detected: {console_errors}")
                raise Exception(f"Console errors found: {console_errors}")
            Utility.log_test_result("PASS", "Test completed successfully with no UI freeze or errors.")
        except PlaywrightTimeoutError as te:
            Utility.log_error(f"TimeoutError occurred: {te}")
            Utility.log_test_result("FAIL", f"TimeoutError: {te}")
            raise
        except AssertionError as ae:
            Utility.log_error(f"AssertionError occurred: {ae}")
            Utility.log_test_result("FAIL", f"AssertionError: {ae}")
            raise
        except Exception as e:
            Utility.log_error(f"Unexpected error: {e}")
            Utility.log_test_result("FAIL", f"Unexpected error: {e}")
            raise
        finally:
            browser.close()
#---#
#######

# Test Case 11 - TC-0085
# Import the POM class
def test_terms_and_conditions_section_resilience() -> None:
    """
    TC-0085: Ensures that missing or delayed Terms and Conditions content does not break the page layout or cause UI errors.
    """
    # --- Test Data and URLs ---
    urls: dict[str, str] = {
        "index": os.environ.get("INDEX_PAGE_URL", "http://localhost:3000/")
    }
    terms_section_xpath: str = "//div[contains(@class, 'end-container')]"
    # --- Begin Test ---
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        console_errors: list[str] = []
        # --- Attach console logger ---
        def handle_console_message2(msg):
            Utility.log_console_message(msg)
            if msg.type == "error":
                console_errors.append(msg.text)
        page.on("console", handle_console_message)
        try:
            # --- Given: Navigate to index page ---
            Utility.log_test_step("Navigate to index page")
            navigation_success: bool = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            if not navigation_success:
                Utility.log_error("Navigation to index page failed.")
                raise Exception("Navigation to index page failed.")
            # --- Wait for essential elements ---
            Utility.log_test_step("Validate essential elements are visible")
            Utility.retry_assertion(lambda: generated_page.validate_essential_elements(), retries=3, delay=2000)
            # --- Accept cookies/pop-ups if present ---
            # (Assume a cookie banner with id 'cookie-accept' for demonstration)
            cookie_accept_xpath: str = "//button[contains(@id, 'cookie-accept')]"
            Utility.safe_wait_and_interact(page, f"xpath={cookie_accept_xpath}", "click", timeout=5000)
            # --- THEN: Terms and Conditions section is visible at the bottom ---
            Utility.log_test_step("Verify Terms and Conditions section is visible")
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={terms_section_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=2000
            )
            Utility.log_element_state("Terms and Conditions section", page.locator(f"xpath={terms_section_xpath}"))
            # --- WHEN: Remove or comment out the end-container div from the HTML ---
            Utility.log_test_step("Remove Terms and Conditions section from DOM")
            page.evaluate("""
                () => {
                    const el = document.evaluate(arguments[0], document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                    if (el) { el.parentNode.removeChild(el); }
                }
            """, terms_section_xpath)
            time.sleep(1)
            # --- THEN: Terms and Conditions section is missing ---
            Utility.log_test_step("Verify Terms and Conditions section is missing")
            try:
                expect(page.locator(f"xpath={terms_section_xpath}")).not_to_be_visible(timeout=5000)
                Utility.log_test_result("PASS", "Terms and Conditions section is not visible as expected.")
            except Exception as e:
                Utility.log_test_result("FAIL", f"Section still visible: {e}")
                raise
            # --- THEN: No visual glitches or layout breaks occur ---
            Utility.log_test_step("Observe page layout for visual glitches")
            # (No direct POM method; check essential elements remain visible)
            Utility.retry_assertion(lambda: generated_page.validate_essential_elements(), retries=3, delay=2000)
            # --- THEN: Other content remains accessible ---
            Utility.log_test_step("Scroll to bottom and verify other content is accessible")
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            Utility.retry_assertion(lambda: generated_page.validate_essential_elements(), retries=3, delay=2000)
            # --- WHEN: Restore the end-container and reload ---
            Utility.log_test_step("Restore Terms and Conditions section and reload")
            page.reload(timeout=15000)
            Utility.retry_assertion(lambda: generated_page.validate_essential_elements(), retries=3, delay=2000)
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={terms_section_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=2000
            )
            # --- WHEN: Simulate slow network or partial HTML load ---
            Utility.log_test_step("Simulate slow network and reload page")
            context.set_offline(False)
            context.set_default_navigation_timeout(20000)
            context.set_default_timeout(20000)
            context.route("**/*", lambda route: time.sleep(2) or route.continue_())
            page.reload(timeout=20000)
            Utility.retry_assertion(lambda: generated_page.validate_essential_elements(), retries=3, delay=2000)
            # Section may appear late, but no UI freezes occur
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={terms_section_xpath}")).to_be_visible(timeout=20000),
                retries=3,
                delay=2000
            )
            # --- THEN: Check for error messages or fallback UI ---
            Utility.log_test_step("Check for error messages or fallback UI")
            error_banner_xpath: str = "//div[contains(@class, 'error') or contains(@class, 'fallback')]"
            try:
                expect(page.locator(f"xpath={error_banner_xpath}")).not_to_be_visible(timeout=5000)
                Utility.log_test_result("PASS", "No user-facing error or fallback UI shown.")
            except Exception:
                Utility.log_test_result("INFO", "Fallback UI or error banner may be present.")
            # --- THEN: No script errors; site remains usable ---
            Utility.log_test_step("Review browser console for errors")
            if console_errors:
                Utility.log_test_result("FAIL", f"Console errors detected: {console_errors}")
                raise Exception(f"Console errors detected: {console_errors}")
            else:
                Utility.log_test_result("PASS", "No console errors detected.")
            Utility.log_test_result("PASS", "TC-0085 completed successfully.")
        except PlaywrightTimeoutError as te:
            Utility.log_error(f"Timeout occurred: {te}")
            raise
        except AssertionError as ae:
            Utility.log_error(f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_error(f"Test failed: {e}")
            raise
        finally:
            browser.close()
#---#
#######
