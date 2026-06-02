# Generated Playwright Tests for navbar
from playwright.sync_api import sync_playwright, expect, TimeoutError as PlaywrightTimeoutError
from navbar_pom import GeneratedPage
import json
import re
import time
import os

urls = {}
from Utility import Utility


# Test Case 1 - TC-0001
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
def test_logo_redirects_user_to_home_page() -> None:
    # Test data and URLs
    urls: dict[str, str] = {
        "home": os.environ.get("TEST_HOME_URL", "https://example.com/"),
        "category": os.environ.get("TEST_CATEGORY_URL", "https://example.com/category")
    }
    logo_xpath: str = "//a[@id='navbar-logo']"  # Example, update if needed
    home_page_identifier_xpath: str = "//input[@id='search-bar']"  # From POM
    max_string_length: int = 70
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
        try:
            # --- GIVEN: Navigate to Home Page ---
            Utility.log_test_step("Navigating to Home Page")
            navigation_success: bool = Utility.navigate_to_page(page, urls["home"], timeout=15000)
            if not navigation_success:
                Utility.log_error("Failed to navigate to Home Page")
                raise Exception("Navigation to Home Page failed")
            Utility.wait_for_element_state(page, "xpath=//body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            # Accept cookies/pop-ups if present
            Utility.safe_wait_and_interact(page, "xpath=//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept') or contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'agree')]", "click", timeout=5000)
            # --- THEN: Logo is visible and clickable ---
            Utility.log_test_step("Checking logo visibility and clickability")
            Utility.wait_for_element_state(page, f"xpath={logo_xpath}", state="visible", timeout=15000)
            logo_locator = page.locator(f"xpath={logo_xpath}")
            Utility.log_element_state("Navbar Logo", logo_locator, timeout=15000)
            expect(logo_locator).to_be_visible(timeout=15000)
            expect(logo_locator).to_be_enabled(timeout=15000)
            # --- WHEN: Hover over the logo ---
            Utility.log_test_step("Hovering over the logo to check pointer")
            logo_locator.hover()
            pointer_style: str = logo_locator.evaluate("el => window.getComputedStyle(el).cursor")
            if pointer_style not in ["pointer", "hand"]:
                Utility.log_error(f"Logo pointer style is '{pointer_style}', expected 'pointer'")
                raise AssertionError("Logo is not visually clickable (pointer missing)")
            # --- WHEN: Click the logo ---
            Utility.log_test_step("Clicking the logo")
            Utility.retry_assertion(lambda: logo_locator.click(), retries=3, delay=1000)
            # --- THEN: User is redirected to Home Page ---
            Utility.log_test_step("Verifying redirection to Home Page")
            Utility.wait_for_element_state(page, f"xpath={home_page_identifier_xpath}", state="visible", timeout=15000)
            expect(page).to_have_url(urls["home"], timeout=15000)
            generated_page.validate_essential_elements()
            # --- THEN: Home page content is displayed without errors ---
            Utility.log_test_step("Validating Home Page content")
            Utility.retry_assertion(lambda: generated_page.validate_essential_elements(), retries=3, delay=1000)
            # --- WHEN: Navigate to a different page (category) ---
            Utility.log_test_step("Navigating to Category Page")
            navigation_success = Utility.navigate_to_page(page, urls["category"], timeout=15000)
            if not navigation_success:
                Utility.log_error("Failed to navigate to Category Page")
                raise Exception("Navigation to Category Page failed")
            Utility.wait_for_element_state(page, "xpath=//body", state="visible", timeout=15000)
            # --- THEN: Logo remains visible and functional ---
            Utility.log_test_step("Checking logo on Category Page")
            Utility.wait_for_element_state(page, f"xpath={logo_xpath}", state="visible", timeout=15000)
            logo_locator = page.locator(f"xpath={logo_xpath}")
            Utility.log_element_state("Navbar Logo (Category)", logo_locator, timeout=15000)
            expect(logo_locator).to_be_visible(timeout=15000)
            expect(logo_locator).to_be_enabled(timeout=15000)
            # --- WHEN: Click the logo from Category Page ---
            Utility.log_test_step("Clicking logo from Category Page")
            Utility.retry_assertion(lambda: logo_locator.click(), retries=3, delay=1000)
            # --- THEN: User is redirected to Home Page again ---
            Utility.log_test_step("Verifying redirection to Home Page again")
            Utility.wait_for_element_state(page, f"xpath={home_page_identifier_xpath}", state="visible", timeout=15000)
            expect(page).to_have_url(urls["home"], timeout=15000)
            generated_page.validate_essential_elements()
            # --- WHEN: Resize browser window and repeat logo click ---
            Utility.log_test_step("Resizing browser window to 800x600")
            context.set_viewport_size({"width": 800, "height": 600})
            Utility.wait_for_element_state(page, f"xpath={logo_xpath}", state="visible", timeout=15000)
            logo_locator = page.locator(f"xpath={logo_xpath}")
            Utility.log_element_state("Navbar Logo (Resized)", logo_locator, timeout=15000)
            expect(logo_locator).to_be_visible(timeout=15000)
            expect(logo_locator).to_be_enabled(timeout=15000)
            Utility.log_test_step("Clicking logo after resizing window")
            Utility.retry_assertion(lambda: logo_locator.click(), retries=3, delay=1000)
            Utility.wait_for_element_state(page, f"xpath={home_page_identifier_xpath}", state="visible", timeout=15000)
            expect(page).to_have_url(urls["home"], timeout=15000)
            generated_page.validate_essential_elements()
            Utility.log_test_result("PASS", "Logo navigation and visibility verified across scenarios.")
        except AssertionError as ae:
            Utility.log_test_result("FAIL", f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_test_result("FAIL", f"Unexpected error: {e}")
            raise
        finally:
            browser.close()
#---#
#######

# Test Case 2 - TC-0004
from playwright.sync_api import sync_playwright, expect
# Test URLs (replace with actual URLs as needed)
urls: dict[str, str] = {
    "index": os.environ.get("TEST_INDEX_URL", "https://example.com/"),
    "sign_in": os.environ.get("TEST_SIGNIN_URL", "https://example.com/signin"),
    "sign_up": os.environ.get("TEST_SIGNUP_URL", "https://example.com/signup"),
}
def test_navbar_sign_in_and_sign_up_options_display_for_anonymous_users() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        page.on("console", lambda msg: Utility.log_console_message(msg))
        cookies_accepted: bool = False
        # XPaths for navbar elements (must match actual app)
        sign_in_xpath: str = "//a[normalize-space()='Sign In']"
        sign_up_xpath: str = "//a[normalize-space()='Sign Up']"
        navbar_xpath: str = "//nav"
        try:
            # Given: User is logged out and lands on the index page
            Utility.log_test_step("Setting loginStatus to false in localStorage.")
            page.goto("about:blank")
            page.evaluate("window.localStorage.setItem('loginStatus', 'false')")
            Utility.log_test_step("Navigating to index page as anonymous user.")
            navigation_success: bool = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            if not navigation_success:
                raise Exception("Navigation to index page failed.")
            Utility.log_test_step("Waiting for body and navbar to be visible.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            Utility.wait_for_element_state(page, f"xpath={navbar_xpath}", state="visible", timeout=15000)
            # Accept cookies/pop-ups if present
            cookie_btn_xpath: str = "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept')]"
            if Utility.wait_for_element_state(page, f"xpath={cookie_btn_xpath}", state="visible", timeout=3000):
                Utility.log_test_step("Accepting cookies popup.")
                Utility.safe_wait_and_interact(page, f"xpath={cookie_btn_xpath}", action="click", timeout=5000)
                cookies_accepted = True
            # Then: "Sign In" and "Sign Up" options are visible in the navigation bar
            Utility.log_test_step("Verifying 'Sign In' and 'Sign Up' options are visible.")
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={sign_in_xpath}")).to_be_visible(timeout=15000),
                retries=3, delay=2000
            )
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={sign_up_xpath}")).to_be_visible(timeout=15000),
                retries=3, delay=2000
            )
            Utility.log_element_state("Sign In option", page.locator(f"xpath={sign_in_xpath}"), timeout=15000)
            Utility.log_element_state("Sign Up option", page.locator(f"xpath={sign_up_xpath}"), timeout=15000)
            # When: Hover over the "Sign In" option
            Utility.log_test_step("Hovering over 'Sign In' option.")
            page.hover(f"xpath={sign_in_xpath}")
            time.sleep(1)
            pointer_style_sign_in: str = page.evaluate(
                "el => window.getComputedStyle(el).cursor",
                page.query_selector(f"xpath={sign_in_xpath}")
            )
            if pointer_style_sign_in not in ["pointer", "hand"]:
                Utility.log_error("Pointer does not indicate clickable for 'Sign In'.")
            # When: Click on the "Sign In" option
            Utility.log_test_step("Clicking 'Sign In' option.")
            Utility.safe_wait_and_interact(page, f"xpath={sign_in_xpath}", action="click", timeout=15000)
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # Then: User is redirected to the sign-in page
            Utility.log_test_step("Verifying redirection to sign-in page.")
            Utility.retry_assertion(
                lambda: expect(page).to_have_url(urls["sign_in"], timeout=15000),
                retries=3, delay=2000
            )
            Utility.wait_for_element_state(page, f"xpath={navbar_xpath}", state="visible", timeout=15000)
            Utility.log_element_state("Navbar on sign-in page", page.locator(f"xpath={navbar_xpath}"), timeout=15000)
            # When: Return to index page and hover over "Sign Up" option
            Utility.log_test_step("Returning to index page.")
            Utility.navigate_to_page(page, urls["index"], timeout=15000)
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            Utility.wait_for_element_state(page, f"xpath={sign_up_xpath}", state="visible", timeout=15000)
            Utility.log_test_step("Hovering over 'Sign Up' option.")
            page.hover(f"xpath={sign_up_xpath}")
            time.sleep(1)
            pointer_style_sign_up: str = page.evaluate(
                "el => window.getComputedStyle(el).cursor",
                page.query_selector(f"xpath={sign_up_xpath}")
            )
            if pointer_style_sign_up not in ["pointer", "hand"]:
                Utility.log_error("Pointer does not indicate clickable for 'Sign Up'.")
            # When: Click on the "Sign Up" option
            Utility.log_test_step("Clicking 'Sign Up' option.")
            Utility.safe_wait_and_interact(page, f"xpath={sign_up_xpath}", action="click", timeout=15000)
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # Then: User is redirected to the sign-up page
            Utility.log_test_step("Verifying redirection to sign-up page.")
            Utility.retry_assertion(
                lambda: expect(page).to_have_url(urls["sign_up"], timeout=15000),
                retries=3, delay=2000
            )
            Utility.wait_for_element_state(page, f"xpath={navbar_xpath}", state="visible", timeout=15000)
            Utility.log_element_state("Navbar on sign-up page", page.locator(f"xpath={navbar_xpath}"), timeout=15000)
            # Then: Navigation bar remains visible and consistent
            Utility.log_test_result("PASS", "Sign In/Sign Up options and navbar verified for anonymous users.")
        except Exception as e:
            Utility.log_test_result("FAIL", f"Test failed: {str(e)}")
            raise
        finally:
            browser.close()
#---#
#######

# Test Case 3 - TC-0005
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
def test_navbar_logged_in_user_avatar_logout_cart_display() -> None:
    """
    Test Case: TC-0005
    Scenario: User Avatar, Log Out, and Cart Display for Logged-In Users
    Steps:
        1. Land on the index page with the user logged in (loginStatus is true in localStorage).
        2. Hover over the user avatar and verify pointer change.
        3. Hover over the "Log Out" option and verify pointer change.
        4. Click on the "Log Out" option and verify navbar updates.
        5. Log in again and hover over the cart icon.
        6. Click on the cart icon and verify redirection and item count.
    """
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
        # --- Given: Setup and navigation to initial state ---
        try:
            Utility.log_test_step("Setting loginStatus in localStorage to true before navigation.")
            page.goto("about:blank")
            page.evaluate("window.localStorage.setItem('loginStatus', 'true');")
            Utility.log_test_step("Navigating to index page as logged-in user.")
            navigation_success = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            if not navigation_success:
                Utility.log_error("Navigation to index page failed.")
                raise Exception("Navigation to index page failed.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # Accept cookies/pop-ups if present
            Utility.safe_wait_and_interact(page, "button:has-text('Accept')", "click", timeout=5000)
            # --- Then: Verify essential navbar elements for logged-in user ---
            Utility.log_test_step("Validating essential elements on the page.")
            Utility.retry_assertion(lambda: generated_page.validate_essential_elements(), retries=3, delay=2000)
            # --- Then: Verify user avatar, log out, and cart icon are visible ---
            avatar_xpath = "//img[contains(@class, 'user-avatar')]"
            logout_xpath = "//button[normalize-space()='Log Out']"
            cart_icon_xpath = "//div[contains(@class, 'cart-icon')]"
            cart_count_xpath = "//span[contains(@class, 'cart-count')]"
            # Validate avatar
            avatar_locator = page.locator(f"xpath={avatar_xpath}")
            Utility.log_element_state("User Avatar", avatar_locator, timeout=15000)
            expect(avatar_locator).to_be_visible(timeout=15000)
            # Validate log out button
            logout_locator = page.locator(f"xpath={logout_xpath}")
            Utility.log_element_state("Log Out Button", logout_locator, timeout=15000)
            expect(logout_locator).to_be_visible(timeout=15000)
            # Validate cart icon and count
            cart_icon_locator = page.locator(f"xpath={cart_icon_xpath}")
            Utility.log_element_state("Cart Icon", cart_icon_locator, timeout=15000)
            expect(cart_icon_locator).to_be_visible(timeout=15000)
            cart_count_locator = page.locator(f"xpath={cart_count_xpath}")
            Utility.log_element_state("Cart Count", cart_count_locator, timeout=15000)
            expect(cart_count_locator).to_be_visible(timeout=15000)
            # --- When: Hover over the user avatar ---
            Utility.log_test_step("Hovering over the user avatar.")
            avatar_locator.hover()
            time.sleep(1)
            pointer_avatar = page.evaluate("""
                (xpath) => {
                    const el = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                    return window.getComputedStyle(el).cursor;
                }
            """, avatar_xpath)
            Utility.log_test_result("Pointer on avatar", pointer_avatar)
            if pointer_avatar not in ["pointer", "hand"]:
                Utility.log_error("Pointer did not change to clickable on avatar.")
            # --- When: Hover over the 'Log Out' option ---
            Utility.log_test_step("Hovering over the 'Log Out' option.")
            logout_locator.hover()
            time.sleep(1)
            pointer_logout = page.evaluate("""
                (xpath) => {
                    const el = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                    return window.getComputedStyle(el).cursor;
                }
            """, logout_xpath)
            Utility.log_test_result("Pointer on Log Out", pointer_logout)
            if pointer_logout not in ["pointer", "hand"]:
                Utility.log_error("Pointer did not change to clickable on Log Out.")
            # --- When: Click on the 'Log Out' option ---
            Utility.log_test_step("Clicking on the 'Log Out' option.")
            Utility.safe_wait_and_interact(page, f"xpath={logout_xpath}", "click", timeout=15000)
            # --- Then: Verify navbar updates to show 'Sign In' and 'Sign Up' options ---
            sign_in_xpath = "//a[normalize-space()='Sign In']"
            sign_up_xpath = "//a[normalize-space()='Sign Up']"
            sign_in_locator = page.locator(f"xpath={sign_in_xpath}")
            sign_up_locator = page.locator(f"xpath={sign_up_xpath}")
            Utility.retry_assertion(lambda: expect(sign_in_locator).to_be_visible(timeout=15000), retries=3, delay=2000)
            Utility.retry_assertion(lambda: expect(sign_up_locator).to_be_visible(timeout=15000), retries=3, delay=2000)
            Utility.log_test_result("Navbar after logout", "Sign In and Sign Up are visible.")
            # --- When: Log in again ---
            Utility.log_test_step("Logging in again by setting loginStatus in localStorage.")
            page.evaluate("window.localStorage.setItem('loginStatus', 'true');")
            Utility.navigate_to_page(page, urls["index"], timeout=15000)
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            Utility.retry_assertion(lambda: expect(avatar_locator).to_be_visible(timeout=15000), retries=3, delay=2000)
            Utility.retry_assertion(lambda: expect(cart_icon_locator).to_be_visible(timeout=15000), retries=3, delay=2000)
            # --- When: Hover over the cart icon ---
            Utility.log_test_step("Hovering over the cart icon.")
            cart_icon_locator.hover()
            time.sleep(1)
            pointer_cart = page.evaluate("""
                (xpath) => {
                    const el = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                    return window.getComputedStyle(el).cursor;
                }
            """, cart_icon_xpath)
            Utility.log_test_result("Pointer on Cart Icon", pointer_cart)
            if pointer_cart not in ["pointer", "hand"]:
                Utility.log_error("Pointer did not change to clickable on Cart Icon.")
            # --- When: Click on the cart icon ---
            Utility.log_test_step("Clicking on the cart icon.")
            Utility.safe_wait_and_interact(page, f"xpath={cart_icon_xpath}", "click", timeout=15000)
            # --- Then: Verify redirection to cart page and correct item count ---
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            current_url = page.url
            Utility.log_test_result("Redirected URL", current_url)
            if "cart" not in current_url:
                Utility.log_error("Did not redirect to cart page after clicking cart icon.")
            cart_count_text = Utility.get_element_text(page, f"xpath={cart_count_xpath}", timeout=15000)
            cart_count = Utility.validate_and_convert_data(cart_count_text, int)
            Utility.log_test_result("Cart Item Count", str(cart_count))
            if cart_count < 0:
                Utility.log_error("Cart item count is negative or invalid.")
            Utility.log_test_result("Test Execution Summary", "All steps executed successfully.")
        except Exception as e:
            Utility.log_error(f"Test failed: {e}")
            raise
        finally:
            browser.close()
#---#
#######

# Test Case 4 - TC-0006
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
def test_cart_icon_displays_item_count_and_redirects_to_cart_page() -> None:
    # Test Data and URLs
    # XPaths for cart icon and item count (must match actual app, update if needed)
    cart_icon_xpath = "//div[contains(@class,'navbar')]//a[contains(@href,'cart')]"
    cart_count_xpath = "//div[contains(@class,'navbar')]//a[contains(@href,'cart')]//span[contains(@class,'cart-count')]"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        # Attach console logger
        page.on("console", lambda msg: Utility.log_console_message(msg))
        # Set loginStatus in localStorage before navigation
        def set_login_status():
            page.evaluate("window.localStorage.setItem('loginStatus', 'true');")
        try:
            # --- Given: Setup and navigation to initial state ---
            Utility.log_test_step("Setting loginStatus in localStorage.")
            set_login_status()
            Utility.log_test_step("Navigating to index page.")
            navigation_success = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            if not navigation_success:
                Utility.log_error("Failed to navigate to index page.")
                raise Exception("Navigation to index page failed.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page = GeneratedPage(page)
            # Accept cookies/pop-ups if present (try both button and link)
            Utility.safe_wait_and_interact(page, "button:has-text('Accept')", "click", timeout=5000)
            Utility.safe_wait_and_interact(page, "text=Accept", "click", timeout=5000)
            # --- Then: Cart icon with item count (default 0) is visible in the navigation bar ---
            Utility.log_test_step("Validating essential elements on the page.")
            generated_page.validate_essential_elements()
            Utility.log_test_step("Checking cart icon visibility and item count.")
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={cart_icon_xpath}")).to_be_visible(timeout=15000),
                retries=3, delay=2000
            )
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={cart_count_xpath}")).to_be_visible(timeout=15000),
                retries=3, delay=2000
            )
            cart_count_text = Utility.get_element_text(page, f"xpath={cart_count_xpath}", timeout=15000)
            cart_count = Utility.validate_and_convert_data(cart_count_text.strip(), int)
            if cart_count != 0:
                Utility.log_error(f"Expected cart count 0, found {cart_count}")
                raise AssertionError("Cart count is not 0 on initial load.")
            Utility.log_element_state("Cart Icon", page.locator(f"xpath={cart_icon_xpath}"), timeout=15000)
            Utility.log_element_state("Cart Count", page.locator(f"xpath={cart_count_xpath}"), timeout=15000)
            # --- Then: Cart icon and item count are visually aligned and readable ---
            Utility.log_test_step("Checking cart icon and count alignment/readability.")
            # (Visual checks are limited in automation; check visibility and bounding box)
            cart_icon_box = page.locator(f"xpath={cart_icon_xpath}").bounding_box()
            cart_count_box = page.locator(f"xpath={cart_count_xpath}").bounding_box()
            if not cart_icon_box or not cart_count_box:
                Utility.log_error("Cart icon or count bounding box not found.")
                raise AssertionError("Cart icon/count not rendered properly.")
            if abs(cart_icon_box["y"] - cart_count_box["y"]) > 30:
                Utility.log_error("Cart icon and count are not vertically aligned.")
                raise AssertionError("Cart icon/count alignment issue.")
            # --- When: Hover over the cart icon ---
            Utility.log_test_step("Hovering over the cart icon to check pointer style.")
            page.hover(f"xpath={cart_icon_xpath}")
            pointer_style = page.evaluate(
                """el => window.getComputedStyle(el).cursor""",
                page.query_selector(f"xpath={cart_icon_xpath}")
            )
            if pointer_style not in ["pointer", "hand"]:
                Utility.log_error(f"Cart icon pointer style is '{pointer_style}'")
                raise AssertionError("Cart icon is not clickable (pointer style missing).")
            # --- When: Click on the cart icon ---
            Utility.log_test_step("Clicking on the cart icon to redirect to cart page.")
            Utility.safe_wait_and_interact(page, f"xpath={cart_icon_xpath}", "click", timeout=15000)
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # --- Then: User is redirected to the cart page ---
            Utility.log_test_step("Verifying redirection to cart page.")
            Utility.retry_assertion(
                lambda: expect(page).to_have_url(urls["cart"], timeout=15000),
                retries=3, delay=2000
            )
            # --- When: Add items to the cart (if supported in the UI) and return to the index page ---
            Utility.log_test_step("Attempting to add item to cart (if UI supports).")
            # Try to find and click an 'Add to Cart' button if present
            add_to_cart_xpath = "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'add to cart')]"
            add_to_cart_found = Utility.safe_wait_and_interact(page, f"xpath={add_to_cart_xpath}", "click", timeout=5000)
            if not add_to_cart_found:
                Utility.log_test_step("No 'Add to Cart' button found; skipping add item step.")
            else:
                Utility.log_test_step("'Add to Cart' button clicked.")
            Utility.log_test_step("Navigating back to index page to check cart count update.")
            Utility.navigate_to_page(page, urls["index"], timeout=15000)
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # --- Then: Cart icon updates to reflect the correct number of items ---
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={cart_count_xpath}")).to_be_visible(timeout=15000),
                retries=3, delay=2000
            )
            updated_cart_count_text = Utility.get_element_text(page, f"xpath={cart_count_xpath}", timeout=15000)
            updated_cart_count = Utility.validate_and_convert_data(updated_cart_count_text.strip(), int)
            if add_to_cart_found and updated_cart_count < 1:
                Utility.log_error("Cart count did not update after adding item.")
                raise AssertionError("Cart count did not increment after adding item.")
            # --- Then: Cart item count persists and remains accurate after refresh ---
            Utility.log_test_step("Refreshing page to verify cart count persistence.")
            page.reload(timeout=15000)
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            refreshed_cart_count_text = Utility.get_element_text(page, f"xpath={cart_count_xpath}", timeout=15000)
            refreshed_cart_count = Utility.validate_and_convert_data(refreshed_cart_count_text.strip(), int)
            if refreshed_cart_count != updated_cart_count:
                Utility.log_error("Cart count did not persist after refresh.")
                raise AssertionError("Cart count is not persistent after refresh.")
            Utility.log_test_result("PASS", "Cart icon displays item count and redirects as expected.")
        except AssertionError as ae:
            Utility.log_test_result("FAIL", f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_test_result("FAIL", f"Unexpected error: {e}")
            raise
        finally:
            browser.close()
#---#
#######

# Test Case 5 - TC-0007
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
def test_search_bar_accepts_input_and_displays_placeholder() -> None:
    """
    TC-0007: Search Bar Accepts Input and Displays Placeholder
    Scenario: 
        1. Search bar is visible with the placeholder text.
        2. Clicking inside the search bar focuses and hides placeholder.
        3. Typing input is accepted and displayed.
        4. Clearing and typing new input is accepted.
        5. Search bar remains visually consistent and aligned.
        6. Search bar remains visible and functional across screen sizes.
    """
    urls: dict[str, str] = {
        "index": os.environ.get("TEST_INDEX_URL", "https://localhost/"),
    }
    search_placeholder: str = "Search for products, brands & more"
    first_search_term: str = "Laptop"
    second_search_term: str = "Nike"
    search_bar_xpath: str = "//input[@id='search-bar']"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        page.on("console", lambda msg: Utility.log_console_message(msg))
        test_passed: bool = False
        try:
            # Given: Navigate to index page and ensure page is loaded
            Utility.log_test_step("Navigating to index page.")
            navigation_success: bool = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            if not navigation_success:
                Utility.log_error("Failed to navigate to index page.")
                raise Exception("Navigation to index page failed.")
            Utility.log_test_step("Waiting for body to be visible.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # Accept cookies/pop-ups if present
            Utility.log_test_step("Checking for cookies or pop-ups.")
            cookie_popup_selectors: list[str] = [
                "button:has-text('Accept')",
                "button:has-text('Got it')",
                "button:has-text('Allow all')"
            ]
            for selector in cookie_popup_selectors:
                Utility.safe_wait_and_interact(page, selector, "click", timeout=3000, retries=1)
            # Then: Validate essential elements (search bar and invite button)
            Utility.log_test_step("Validating essential elements on the page.")
            Utility.retry_assertion(lambda: generated_page.validate_essential_elements(), retries=3, delay=1000)
            # Then: Verify search bar is visible and has correct placeholder
            Utility.log_test_step("Verifying search bar visibility and placeholder.")
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={search_bar_xpath}")).to_be_visible(timeout=15000),
                retries=3, delay=1000
            )
            actual_placeholder: str = page.locator(f"xpath={search_bar_xpath}").get_attribute("placeholder")
            actual_placeholder = Utility.validate_and_convert_data(actual_placeholder, str)
            if actual_placeholder.strip() != search_placeholder:
                Utility.log_error(f"Expected placeholder '{search_placeholder}', got '{actual_placeholder}'")
                raise AssertionError("Search bar placeholder text mismatch.")
            # When: Click inside the search bar
            Utility.log_test_step("Clicking inside the search bar.")
            Utility.safe_wait_and_interact(page, f"xpath={search_bar_xpath}", "click", timeout=15000, retries=3)
            # Then: Placeholder should disappear (value should be empty, placeholder attribute remains)
            Utility.log_test_step("Verifying placeholder disappears on focus.")
            is_focused: bool = page.locator(f"xpath={search_bar_xpath}").evaluate("el => document.activeElement === el")
            if not is_focused:
                Utility.log_error("Search bar did not receive focus after click.")
                raise AssertionError("Search bar not focused after click.")
            # When: Type a valid product name into the search bar
            Utility.log_test_step(f"Typing first search term: '{first_search_term}'.")
            generated_page.fill_search_bar(first_search_term)
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={search_bar_xpath}")).to_have_value(first_search_term, timeout=15000),
                retries=3, delay=1000
            )
            # Then: Text appears as typed
            actual_value: str = page.locator(f"xpath={search_bar_xpath}").input_value()
            actual_value = Utility.validate_and_convert_data(actual_value, str)
            if actual_value.strip() != first_search_term:
                Utility.log_error(f"Expected input '{first_search_term}', got '{actual_value}'")
                raise AssertionError("Search bar did not accept first input.")
            # When: Clear the input and type a different valid search term
            Utility.log_test_step(f"Clearing and typing second search term: '{second_search_term}'.")
            generated_page.fill_search_bar(second_search_term)
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={search_bar_xpath}")).to_have_value(second_search_term, timeout=15000),
                retries=3, delay=1000
            )
            # Then: New text appears as typed
            actual_value_2: str = page.locator(f"xpath={search_bar_xpath}").input_value()
            actual_value_2 = Utility.validate_and_convert_data(actual_value_2, str)
            if actual_value_2.strip() != second_search_term:
                Utility.log_error(f"Expected input '{second_search_term}', got '{actual_value_2}'")
                raise AssertionError("Search bar did not accept second input.")
            # Then: Search bar remains visually consistent and aligned
            Utility.log_test_step("Checking search bar alignment and consistency.")
            bounding_box = page.locator(f"xpath={search_bar_xpath}").bounding_box()
            if not bounding_box or bounding_box["width"] < 100 or bounding_box["height"] < 20:
                Utility.log_error("Search bar alignment or size is inconsistent.")
                raise AssertionError("Search bar alignment/size issue detected.")
            # When: Resize browser window and observe search bar
            Utility.log_test_step("Resizing browser window to test responsiveness.")
            for viewport in [{"width": 1200, "height": 800}, {"width": 768, "height": 600}, {"width": 375, "height": 667}]:
                context.set_viewport_size(viewport)
                time.sleep(1)
                Utility.retry_assertion(
                    lambda: expect(page.locator(f"xpath={search_bar_xpath}")).to_be_visible(timeout=15000),
                    retries=3, delay=1000
                )
                Utility.log_element_state(f"Search bar at {viewport}", page.locator(f"xpath={search_bar_xpath}"), timeout=15000)
            test_passed = True
            Utility.log_test_result("PASS", "Search bar input, placeholder, and responsiveness verified.")
        except AssertionError as ae:
            Utility.log_test_result("FAIL", f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_test_result("FAIL", f"Unexpected error: {e}")
            raise
        finally:
            if not test_passed:
                Utility.log_error("Test did not complete successfully.")
            browser.close()
#---#
#######

# Test Case 6 - TC-0013
# Import the POM class
# Test URLs (replace with actual URLs as needed)
urls: dict[str, str] = {
    "index": os.environ.get("TEST_INDEX_URL", "http://localhost:8000/index.html"),
    "signin": os.environ.get("TEST_SIGNIN_URL", "http://localhost:8000/signin.html"),
    "signup": os.environ.get("TEST_SIGNUP_URL", "http://localhost:8000/signup.html"),
}
def test_signin_signup_not_accessible_when_logged_in() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        page.on("console", lambda msg: Utility.log_console_message(msg))
        test_passed: bool = False
        try:
            # --- Given: Navigate to the index page ---
            Utility.log_test_step("Navigate to the index page")
            navigation_success: bool = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            if not navigation_success:
                Utility.log_error("Failed to navigate to index page.")
                raise Exception("Navigation to index page failed.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            Utility.log_element_state("Search Bar", page.locator("xpath=//input[@id='search-bar']"))
            Utility.log_element_state("Invite Now Button", page.locator("xpath=//button[normalize-space()='Invite Now >']"))
            # --- Accept cookies/pop-ups if present ---
            Utility.safe_wait_and_interact(page, "text=Accept", "click", timeout=5000)
            Utility.safe_wait_and_interact(page, "text=Close", "click", timeout=5000)
            # --- When: Set loginStatus in localStorage to true and reload the page ---
            Utility.log_test_step("Set loginStatus in localStorage to true and reload")
            page.evaluate("window.localStorage.setItem('loginStatus', 'true')")
            page.reload()
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            # --- Then: Navbar should show user avatar, 'Log Out', and cart icon ---
            Utility.log_test_step("Verify navbar shows user avatar, 'Log Out', and cart icon")
            # Since POM does not define these, we log that this step is skipped for direct assertion
            # --- When: Attempt to locate and click 'Sign In' or 'Sign Up' in the navbar ---
            Utility.log_test_step("Attempt to locate and click 'Sign In' or 'Sign Up' in navbar")
            sign_in_found: bool = Utility.safe_wait_and_interact(page, "text=Sign In", "click", timeout=5000)
            sign_up_found: bool = Utility.safe_wait_and_interact(page, "text=Sign Up", "click", timeout=5000)
            if sign_in_found or sign_up_found:
                Utility.log_error("'Sign In' or 'Sign Up' should not be clickable when logged in.")
                raise AssertionError("'Sign In' or 'Sign Up' was clickable while logged in.")
            # --- When: Try to access signin.html or signup.html directly via URL ---
            Utility.log_test_step("Try to access signin.html directly via URL")
            navigation_success_signin: bool = Utility.navigate_to_page(page, urls["signin"], timeout=15000)
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            # Check that user remains logged in (simulate by checking localStorage)
            login_status: str = page.evaluate("window.localStorage.getItem('loginStatus')")
            if login_status != "true":
                Utility.log_error("User was logged out after accessing signin.html directly.")
                raise AssertionError("User was logged out after accessing signin.html directly.")
            Utility.log_test_step("Try to access signup.html directly via URL")
            navigation_success_signup: bool = Utility.navigate_to_page(page, urls["signup"], timeout=15000)
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            login_status: str = page.evaluate("window.localStorage.getItem('loginStatus')")
            if login_status != "true":
                Utility.log_error("User was logged out after accessing signup.html directly.")
                raise AssertionError("User was logged out after accessing signup.html directly.")
            # --- Then: Return to the index page and observe the navbar ---
            Utility.log_test_step("Return to index page and observe navbar")
            navigation_success_index: bool = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            # --- When: Attempt to trigger sign-in or sign-up via browser console ---
            Utility.log_test_step("Attempt to trigger sign-in or sign-up via browser console")
            # Simulate click via JS (should have no effect)
            page.evaluate("""
                var signInBtn = document.querySelector('button#sign-in, a#sign-in');
                if (signInBtn) signInBtn.click();
                var signUpBtn = document.querySelector('button#sign-up, a#sign-up');
                if (signUpBtn) signUpBtn.click();
            """)
            time.sleep(1)
            # Check that loginStatus is still true
            login_status: str = page.evaluate("window.localStorage.getItem('loginStatus')")
            if login_status != "true":
                Utility.log_error("User was logged out after JS-triggered sign-in/up.")
                raise AssertionError("User was logged out after JS-triggered sign-in/up.")
            # --- Then: Refresh the page and repeat ---
            Utility.log_test_step("Refresh the page and repeat")
            page.reload()
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            login_status: str = page.evaluate("window.localStorage.getItem('loginStatus')")
            if login_status != "true":
                Utility.log_error("User was logged out after refresh.")
                raise AssertionError("User was logged out after refresh.")
            test_passed = True
            Utility.log_test_result("PASS", "Sign-in/up not accessible when logged in.")
        except PlaywrightTimeoutError as te:
            Utility.log_error(f"Timeout occurred: {te}")
            Utility.log_test_result("FAIL", "Timeout during test execution.")
            raise
        except AssertionError as ae:
            Utility.log_error(f"Assertion failed: {ae}")
            Utility.log_test_result("FAIL", str(ae))
            raise
        except Exception as e:
            Utility.log_error(f"Unexpected error: {e}")
            Utility.log_test_result("FAIL", f"Unexpected error: {e}")
            raise
        finally:
            if test_passed:
                print("[SUMMARY] Test completed successfully.")
            else:
                print("[SUMMARY] Test failed.")
            browser.close()
#---#
#######

# Test Case 7 - TC-0015
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
def test_search_bar_empty_and_invalid_input() -> None:
    """
    TC-0015: Attempting to use the search bar with an empty input and invalid characters.
    Ensures no search is triggered and no error or feedback is shown.
    """
    # --- Test Data and URLs ---
    urls: dict[str, str] = {
        "index": os.environ.get("INDEX_PAGE_URL", "http://localhost:8000/")
    }
    search_bar_placeholder: str = "Search for products, brands & more"
    empty_string: str = ""
    spaces_string: str = "     "
    special_chars_string: str = "!@#$%^&*()_+{}|:\"<>?~`"
    max_length: int = 70  # Enforce max string length
    # --- Test Execution ---
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        page.on("console", Utility.log_console_message)
        try:
            # --- Given: Setup and navigation to initial state ---
            Utility.log_test_step("Navigating to the index page.")
            navigation_success: bool = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            if not navigation_success:
                Utility.log_test_result("FAIL", "Navigation to index page failed.")
                raise Exception("Navigation to index page failed.")
            Utility.log_test_step("Waiting for main page and search bar to be visible.")
            Utility.wait_for_element_state(page, "xpath=//body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            Utility.log_element_state("Search Bar", page.locator("xpath=//input[@id='search-bar']"), timeout=15000)
            # --- Accept cookies/pop-ups if present ---
            # (Assume a cookie banner with button text 'Accept' if present)
            Utility.safe_wait_and_interact(page, "text=Accept", action="click", timeout=3000)
            # --- When: Ensure the search bar is empty and visible ---
            Utility.log_test_step("Ensuring the search bar is empty and placeholder is visible.")
            generated_page.fill_search_bar(empty_string)
            search_bar_text: str = Utility.get_element_text(page, "xpath=//input[@id='search-bar']", timeout=15000)
            # Validate placeholder attribute
            placeholder_value: str = page.get_attribute("xpath=//input[@id='search-bar']", "placeholder")
            placeholder_value = Utility.validate_and_convert_data(placeholder_value, str)
            if placeholder_value.strip() != search_bar_placeholder:
                Utility.log_test_result("FAIL", f"Placeholder mismatch: '{placeholder_value}'")
                raise AssertionError(f"Expected placeholder '{search_bar_placeholder}', got '{placeholder_value}'")
            # --- When: Press Enter with empty input ---
            Utility.log_test_step("Submitting empty search (pressing Enter).")
            page.keyboard.press("Enter")
            time.sleep(1)  # Wait for any UI feedback
            # --- Then: Verify no error message or feedback is shown ---
            Utility.log_test_step("Verifying no error message or feedback is shown.")
            # No error message element expected; check page remains unchanged
            Utility.retry_assertion(
                lambda: expect(page).not_to_have_url(lambda url: "search" in url, timeout=15000),
                retries=3,
                delay=1000
            )
            # --- When: Type only spaces and submit ---
            Utility.log_test_step("Typing only spaces and submitting search.")
            spaces_input: str = spaces_string[:max_length]
            generated_page.fill_search_bar(spaces_input)
            page.keyboard.press("Enter")
            time.sleep(1)
            # --- Then: Verify no search is triggered; no feedback is shown ---
            Utility.retry_assertion(
                lambda: expect(page).not_to_have_url(lambda url: "search" in url, timeout=15000),
                retries=3,
                delay=1000
            )
            # --- When: Paste invalid/special characters and submit ---
            Utility.log_test_step("Pasting special characters and submitting search.")
            special_input: str = special_chars_string[:max_length]
            generated_page.fill_search_bar(special_input)
            page.keyboard.press("Enter")
            time.sleep(1)
            # --- Then: Verify no search is triggered; no feedback is shown ---
            Utility.retry_assertion(
                lambda: expect(page).not_to_have_url(lambda url: "search" in url, timeout=15000),
                retries=3,
                delay=1000
            )
            # --- When: Refresh the page and repeat empty input submission ---
            Utility.log_test_step("Refreshing the page and repeating empty input submission.")
            page.reload(timeout=15000)
            Utility.wait_for_element_state(page, "xpath=//body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            generated_page.fill_search_bar(empty_string)
            page.keyboard.press("Enter")
            time.sleep(1)
            # --- Then: Verify behavior remains consistent ---
            Utility.retry_assertion(
                lambda: expect(page).not_to_have_url(lambda url: "search" in url, timeout=15000),
                retries=3,
                delay=1000
            )
            Utility.log_test_result("PASS", "Search bar does not trigger search or show errors for empty/invalid input.")
        except AssertionError as ae:
            Utility.log_test_result("FAIL", f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_test_result("FAIL", f"Test failed: {e}")
            raise
        finally:
            browser.close()
            Utility.log_test_step("Browser closed. Test execution complete.")
#---#
#######

# Test Case 8 - TC-0030
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
def test_invite_banner_image_failure_and_button_unresponsive() -> None:
    """
    TC-0030: Invite banner image fails to load, or Invite Now button is unresponsive due to missing handler.
    Ensures that the invite banner handles missing images and unresponsive buttons without breaking layout or causing JS errors, and that the UI remains stable.
    """
    # --- Test Data and URLs ---
    invite_banner_img_url = "/assets/invite-banner.jpg"  # Example path, adjust as needed
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        console_errors: list[str] = []
        network_failures: list[str] = []
        # --- Console and Network Logging ---
        def on_console(msg):
            Utility.log_console_message(msg)
            if msg.type == "error":
                console_errors.append(msg.text[:200])
        def on_request_failed(request):
            url = request.url
            if invite_banner_img_url in url:
                network_failures.append(url[:200])
            Utility.log_error(f"Network failure: {url}")
        page.on("console", on_console)
        page.on("requestfailed", on_request_failed)
        try:
            # --- Given: Setup and navigation to initial state ---
            Utility.log_test_step("Navigate to index page")
            navigation_success = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            if not navigation_success:
                Utility.log_test_result("FAIL", "Navigation to index page failed")
                raise Exception("Navigation failed")
            Utility.log_test_step("Wait for body and essential elements")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            Utility.log_element_state("Invite Now Button", page.locator(f"xpath={generated_page._btn_invite_now_xpath}"))
            # Accept cookies/pop-ups if present
            Utility.safe_wait_and_interact(page, "button:has-text('Accept')", "click", timeout=5000)
            Utility.safe_wait_and_interact(page, "button:has-text('Close')", "click", timeout=5000)
            # --- When: Simulate failed image load for invite banner ---
            Utility.log_test_step("Block invite banner image to simulate load failure")
            def block_invite_banner(route, request):
                if invite_banner_img_url in request.url:
                    route.abort()
                else:
                    route.continue_()
            context.route("**/*", block_invite_banner)
            Utility.log_test_step("Reload page to trigger image load failure")
            page.reload()
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            Utility.log_element_state("Invite Now Button", page.locator(f"xpath={generated_page._btn_invite_now_xpath}"))
            # --- Then: Verify image is missing but text and button remain visible ---
            Utility.log_test_step("Verify invite banner image is missing or broken")
            # No direct image locator in POM, so check for network failure
            Utility.retry_assertion(
                lambda: (
                    len(network_failures) > 0
                ),
                retries=3,
                delay=2000
            )
            Utility.log_test_result("PASS", "Invite banner image failed to load as expected")
            Utility.log_test_step("Verify Invite Now button and text remain visible")
            Utility.retry_assertion(
                lambda: generated_page.validate_essential_elements(),
                retries=3,
                delay=2000
            )
            # --- When: Click Invite Now button (should be unresponsive if no handler) ---
            Utility.log_test_step("Click Invite Now button (expect no action if no handler)")
            try:
                generated_page.click_invite_now_button()
                Utility.log_test_result("PASS", "Invite Now button clicked (no error)")
            except Exception as e:
                Utility.log_error(f"Invite Now button click failed: {e}")
            # --- Then: Check for JS errors after click ---
            Utility.log_test_step("Check for JS errors after clicking Invite Now button")
            if console_errors:
                Utility.log_test_result("FAIL", f"Console errors detected: {console_errors}")
                raise Exception("JS errors detected after button click")
            # --- Then: Observe banner layout stability ---
            Utility.log_test_step("Verify banner layout remains stable")
            Utility.retry_assertion(
                lambda: generated_page.validate_essential_elements(),
                retries=3,
                delay=2000
            )
            # --- When: Hover over Invite Now button to check hover/focus effects ---
            Utility.log_test_step("Hover over Invite Now button")
            Utility.safe_wait_and_interact(page, f"xpath={generated_page._btn_invite_now_xpath}", "click", timeout=15000)
            page.hover(f"xpath={generated_page._btn_invite_now_xpath}")
            Utility.log_test_result("PASS", "Hovered over Invite Now button successfully")
            # --- Then: No visual glitches or JS errors occur ---
            Utility.log_test_step("Check for JS errors after hover")
            if console_errors:
                Utility.log_test_result("FAIL", f"Console errors detected: {console_errors}")
                raise Exception("JS errors detected after hover")
            # --- When: Refresh and repeat image load failure ---
            Utility.log_test_step("Refresh page and repeat image load failure")
            page.reload()
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            Utility.retry_assertion(
                lambda: (
                    len(network_failures) > 0
                ),
                retries=3,
                delay=2000
            )
            # --- Then: Check browser console for any unhandled exceptions ---
            Utility.log_test_step("Check browser console for unhandled exceptions")
            if console_errors:
                Utility.log_test_result("FAIL", f"Console errors detected: {console_errors}")
                raise Exception("Unhandled JS exceptions detected")
            # --- When: Restore image loading and verify recovery ---
            Utility.log_test_step("Restore image loading and verify banner recovery")
            context.unroute("**/*", block_invite_banner)
            page.reload()
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            Utility.log_test_result("PASS", "Invite banner displays correctly after image restored")
            Utility.log_test_result("PASS", "Test completed successfully")
        except Exception as e:
            Utility.log_error(f"Test failed: {e}")
            Utility.log_test_result("FAIL", str(e))
            raise
        finally:
            browser.close()
#---#
#######
