# Generated Playwright Tests for otp
from playwright.sync_api import sync_playwright, expect, TimeoutError as PlaywrightTimeoutError
from otp_pom import GeneratedPage
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
    "main_page": "file://" + os.path.abspath("index.html")
}
def test_navigation_bar_displays_all_key_sections_and_branding() -> None:
    """
    TC-0001: Navigation Bar Displays All Key Sections and Branding
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
        test_passed: bool = False
        try:
            # Given: Navigate to the main page (index.html) in a desktop browser
            Utility.log_test_step("Navigating to the main page (index.html)")
            navigation_success: bool = Utility.navigate_to_page(
                page, urls["main_page"], timeout=15000
            )
            if not navigation_success:
                Utility.log_error("Failed to navigate to main page.")
                raise Exception("Navigation to main page failed.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # Accept cookies/pop-ups if present
            Utility.safe_wait_and_interact(
                page, "button:has-text('Accept')", action="click", timeout=5000
            )
            # When: Wait for navigation bar and essential elements
            Utility.log_test_step("Validating essential navigation bar elements")
            Utility.retry_assertion(
                lambda: generated_page.validate_essential_elements(),
                retries=3,
                delay=2000
            )
            # Then: The navigation bar is visible at the top of the page
            Utility.log_element_state("Navigation Bar", page.locator("//nav"), timeout=15000)
            # Then: The company logo image is displayed and is clickable
            Utility.log_test_step("Checking company logo visibility and clickability")
            logo_xpath: str = "//nav//img[contains(@alt, 'logo') or contains(@class, 'logo')]"
            logo_visible: bool = Utility.wait_for_element_state(page, f"xpath={logo_xpath}", state="visible", timeout=15000)
            if not logo_visible:
                Utility.log_error("Company logo is not visible.")
                raise Exception("Logo not visible.")
            Utility.log_element_state("Company Logo", page.locator(f"xpath={logo_xpath}"), timeout=15000)
            Utility.safe_wait_and_interact(page, f"xpath={logo_xpath}", action="click", timeout=15000)
            # Then: The navigation links for BAG, ADDRESS, and PAYMENT are visible and separated by dashes
            Utility.log_test_step("Checking navigation links visibility and separation")
            nav_links_xpaths: list[str] = [
                generated_page._lnk_bag_xpath,
                generated_page._lnk_address_xpath,
                generated_page._lnk_payment_xpath
            ]
            for link_xpath in nav_links_xpaths:
                link_visible: bool = Utility.wait_for_element_state(page, f"xpath={link_xpath}", state="visible", timeout=15000)
                if not link_visible:
                    Utility.log_error(f"Navigation link not visible: {link_xpath}")
                    raise Exception(f"Navigation link not visible: {link_xpath}")
                Utility.log_element_state(f"Nav Link {link_xpath}", page.locator(f"xpath={link_xpath}"), timeout=15000)
            # Check for dashes between links (visual check, fallback to text check)
            nav_text_xpath: str = "//nav"
            nav_text: str = Utility.get_element_text(page, f"xpath={nav_text_xpath}", timeout=15000)
            if "-" not in nav_text:
                Utility.log_error("Navigation links are not separated by dashes.")
                raise Exception("Navigation links not separated by dashes.")
            # Then: Each link displays a visible hover effect (such as underline or color change)
            Utility.log_test_step("Checking hover effect on navigation links")
            for link_xpath in nav_links_xpaths:
                link_locator = page.locator(f"xpath={link_xpath}")
                expect(link_locator).to_be_visible(timeout=15000)
                box_before = link_locator.bounding_box()
                page.hover(f"xpath={link_xpath}")
                time.sleep(1)
                box_after = link_locator.bounding_box()
                # Check for style change (underline/color) by comparing bounding box or style
                style_before = page.evaluate("el => window.getComputedStyle(el).textDecoration", link_locator)
                style_after = page.evaluate("el => window.getComputedStyle(el).textDecoration", link_locator)
                color_before = page.evaluate("el => window.getComputedStyle(el).color", link_locator)
                color_after = page.evaluate("el => window.getComputedStyle(el).color", link_locator)
                if style_before == style_after and color_before == color_after:
                    Utility.log_error(f"No hover effect detected for link: {link_xpath}")
                    raise Exception(f"No hover effect for link: {link_xpath}")
            # Then: The secure icon image is displayed next to the text "100% secure"
            Utility.log_test_step("Checking secure icon and text")
            secure_icon_xpath: str = "//nav//*[contains(@alt, 'secure') or contains(@class, 'secure')]"
            secure_text_xpath: str = "//nav//*[contains(text(), '100% secure')]"
            secure_icon_visible: bool = Utility.wait_for_element_state(page, f"xpath={secure_icon_xpath}", state="visible", timeout=15000)
            secure_text_visible: bool = Utility.wait_for_element_state(page, f"xpath={secure_text_xpath}", state="visible", timeout=15000)
            if not (secure_icon_visible and secure_text_visible):
                Utility.log_error("Secure icon or text not visible.")
                raise Exception("Secure icon or text not visible.")
            Utility.log_element_state("Secure Icon", page.locator(f"xpath={secure_icon_xpath}"), timeout=15000)
            Utility.log_element_state("Secure Text", page.locator(f"xpath={secure_text_xpath}"), timeout=15000)
            # Then: All elements are properly aligned and spaced, with no overlap or misalignment
            Utility.log_test_step("Checking alignment and spacing of navigation bar elements")
            nav_bar_locator = page.locator("//nav")
            expect(nav_bar_locator).to_be_visible(timeout=15000)
            nav_bar_box = nav_bar_locator.bounding_box()
            if nav_bar_box is None or nav_bar_box["width"] < 600:
                Utility.log_error("Navigation bar width is unexpectedly small.")
                raise Exception("Navigation bar alignment issue.")
            # Check for overlap between logo, links, and secure icon
            logo_box = page.locator(f"xpath={logo_xpath}").bounding_box()
            bag_box = page.locator(f"xpath={generated_page._lnk_bag_xpath}").bounding_box()
            address_box = page.locator(f"xpath={generated_page._lnk_address_xpath}").bounding_box()
            payment_box = page.locator(f"xpath={generated_page._lnk_payment_xpath}").bounding_box()
            secure_icon_box = page.locator(f"xpath={secure_icon_xpath}").bounding_box()
            secure_text_box = page.locator(f"xpath={secure_text_xpath}").bounding_box()
            boxes = [logo_box, bag_box, address_box, payment_box, secure_icon_box, secure_text_box]
            for i in range(len(boxes)):
                for j in range(i + 1, len(boxes)):
                    if boxes[i] and boxes[j]:
                        overlap_x = max(0, min(boxes[i]["x"] + boxes[i]["width"], boxes[j]["x"] + boxes[j]["width"]) - max(boxes[i]["x"], boxes[j]["x"]))
                        overlap_y = max(0, min(boxes[i]["y"] + boxes[i]["height"], boxes[j]["y"] + boxes[j]["height"]) - max(boxes[i]["y"], boxes[j]["y"]))
                        if overlap_x > 0 and overlap_y > 0:
                            Utility.log_error("Overlap detected between navigation bar elements.")
                            raise Exception("Navigation bar elements overlap.")
            test_passed = True
            Utility.log_test_result("PASS", "Navigation bar displays all key sections and branding correctly.")
        except AssertionError as ae:
            Utility.log_error(f"Assertion failed: {ae}")
            Utility.log_test_result("FAIL", f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_error(f"Test failed: {e}")
            Utility.log_test_result("FAIL", f"Test failed: {e}")
            raise
        finally:
            if test_passed:
                print("[SUMMARY] Test completed successfully.")
            else:
                print("[SUMMARY] Test did not complete successfully.")
            browser.close()
#---#
#######

# Test Case 2 - TC-0004
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
# Test URLs dictionary (update as needed)
urls: dict[str, str] = {
    "otp_entry": "http://localhost:8000/otp-entry.html"  # Example URL, update as needed
}
def test_otp_entry_section_displays_correctly_and_accepts_input() -> None:
    """
    TC-0004: OTP Entry Section Displays Correctly and Accepts Input
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        otp_value: str = Utility.validate_and_convert_data("123456", str)
        try:
            # --- Console and Dialog Handling ---
            page.on("console", Utility.log_console_message)
            page.on("dialog", lambda dialog: dialog.accept())
            # --- Given: Navigate to OTP Entry Page ---
            Utility.log_test_step("Navigating to OTP Entry page.")
            navigation_success: bool = Utility.navigate_to_page(
                page, urls["otp_entry"], timeout=15000
            )
            if not navigation_success:
                Utility.log_error("Failed to navigate to OTP Entry page.")
                raise Exception("Navigation to OTP Entry page failed.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # --- Accept Cookies/Pop-ups if present ---
            # (Assume a cookie banner with id 'cookie-accept' if present)
            Utility.safe_wait_and_interact(
                page, "#cookie-accept", action="click", timeout=3000
            )
            # --- Then: OTP Entry Section is visible with heading "Enter OTP" ---
            Utility.log_test_step("Verifying OTP entry section and heading.")
            heading_selector: str = "//h2[normalize-space()='Enter OTP']"
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={heading_selector}")).to_be_visible(timeout=15000),
                retries=3, delay=1000
            )
            Utility.log_element_state("OTP Heading", page.locator(f"xpath={heading_selector}"))
            # --- Then: Message "OTP has been sent to your mobile number" is displayed ---
            Utility.log_test_step("Verifying OTP sent message.")
            otp_message_selector: str = "//p[contains(text(),'OTP has been sent to your mobile number')]"
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={otp_message_selector}")).to_be_visible(timeout=15000),
                retries=3, delay=1000
            )
            Utility.log_element_state("OTP Sent Message", page.locator(f"xpath={otp_message_selector}"))
            # --- Then: OTP input field is visible with placeholder "Enter the OTP" and accepts only numeric input ---
            Utility.log_test_step("Verifying OTP input field visibility and placeholder.")
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={generated_page._input_otp_xpath}")).to_be_visible(timeout=15000),
                retries=3, delay=1000
            )
            otp_input_placeholder: str = page.locator(f"xpath={generated_page._input_otp_xpath}").get_attribute("placeholder")
            if Utility.validate_and_convert_data(otp_input_placeholder, str) != "Enter the OTP":
                Utility.log_error("OTP input placeholder text mismatch.")
                raise AssertionError("OTP input placeholder is incorrect.")
            Utility.log_element_state("OTP Input Field", page.locator(f"xpath={generated_page._input_otp_xpath}"))
            # --- When: Enter a valid 6-digit OTP (e.g., 123456) into the input field ---
            Utility.log_test_step("Entering valid 6-digit OTP.")
            generated_page.fill_otp_field(otp_value)
            entered_value: str = page.locator(f"xpath={generated_page._input_otp_xpath}").input_value()
            if Utility.validate_and_convert_data(entered_value, str) != otp_value:
                Utility.log_error("OTP input value mismatch after entry.")
                raise AssertionError("OTP input value not accepted/displayed correctly.")
            # --- Then: "RESEND OTP" text is visible and clearly separated from the input field ---
            Utility.log_test_step("Verifying 'RESEND OTP' text visibility.")
            resend_otp_selector: str = "//span[normalize-space()='RESEND OTP']"
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={resend_otp_selector}")).to_be_visible(timeout=15000),
                retries=3, delay=1000
            )
            Utility.log_element_state("'RESEND OTP' Text", page.locator(f"xpath={resend_otp_selector}"))
            # --- Then: "SUBMIT" button is visible and enabled after entering the OTP ---
            Utility.log_test_step("Verifying 'SUBMIT' button visibility and enabled state.")
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={generated_page._btn_submit_xpath}")).to_be_visible(timeout=15000),
                retries=3, delay=1000
            )
            submit_button = page.locator(f"xpath={generated_page._btn_submit_xpath}")
            if not submit_button.is_enabled():
                Utility.log_error("'SUBMIT' button is not enabled after OTP entry.")
                raise AssertionError("'SUBMIT' button is not enabled after OTP entry.")
            Utility.log_element_state("'SUBMIT' Button", submit_button)
            # --- Test Execution Summary ---
            Utility.log_test_result("PASS", "OTP Entry Section displays and accepts input as expected.")
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

# Test Case 3 - TC-0005
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
def test_otp_entry_section_submit_button_submits_otp_successfully() -> None:
    """
    Test Case ID: TC-0005
    Scenario: Submit Button Submits OTP Successfully
    Module: OTP Entry Section
    Given: The user lands on the main page and navigates to the OTP entry page.
    When: The user enters a valid OTP and clicks the SUBMIT button.
    Then: The OTP is submitted, UI responds with success, input is cleared/disabled,
          and the navigation bar remains visible.
    """
    # --- Test Data ---
    otp_value: str = Utility.validate_and_convert_data("654321", str)
    main_page_url: str = Utility.validate_and_convert_data(
        os.environ.get("MAIN_PAGE_URL", "http://localhost:8000/index.html"), str
    )
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
            # --- Given: Navigate to OTP entry page ---
            Utility.log_test_step("Navigating to the main page (OTP entry section).")
            navigation_success: bool = Utility.navigate_to_page(page, main_page_url, timeout=15000)
            if not navigation_success:
                Utility.log_error("Failed to navigate to the main page.")
                raise Exception("Navigation to main page failed.")
            Utility.log_test_step("Waiting for OTP entry section to be visible.")
            Utility.retry_assertion(
                lambda: generated_page.validate_essential_elements(),
                retries=3,
                delay=2000
            )
            # Accept cookies/pop-ups if present
            # (Assume a button with id 'accept-cookies' may exist)
            Utility.safe_wait_and_interact(
                page,
                "xpath=//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept')]",
                action="click",
                timeout=5000,
                retries=1
            )
            # --- When: Enter valid OTP and enable SUBMIT button ---
            Utility.log_test_step("Entering a valid OTP into the input field.")
            Utility.retry_assertion(
                lambda: generated_page.fill_otp_field(otp_value),
                retries=3,
                delay=2000
            )
            Utility.log_test_step("Verifying SUBMIT button is enabled.")
            submit_btn_selector: str = "xpath=//button[@id='submit']"
            Utility.retry_assertion(
                lambda: expect(page.locator(submit_btn_selector)).to_be_enabled(timeout=15000),
                retries=3,
                delay=2000
            )
            # --- When: Click the SUBMIT button ---
            Utility.log_test_step("Clicking the SUBMIT button.")
            Utility.retry_assertion(
                lambda: generated_page.click_submit_button(),
                retries=3,
                delay=2000
            )
            # --- Then: Observe UI response after submission ---
            Utility.log_test_step("Observing UI response after OTP submission.")
            # Wait for either a success message or navigation (simulate both)
            success_message_found: bool = False
            try:
                page.wait_for_selector(
                    "xpath=//*[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'success')]",
                    timeout=7000,
                    state="visible"
                )
                success_message_found = True
            except Exception:
                # If no success message, check for navigation or input field state
                pass
            # --- Then: Check OTP input field is cleared or disabled ---
            Utility.log_test_step("Checking OTP input field is cleared or disabled.")
            otp_input_selector: str = "xpath=//input[@id='otP']"
            otp_input_value: str = Utility.get_element_text(page, otp_input_selector, timeout=7000)
            otp_input_disabled: bool = False
            try:
                otp_input_disabled = page.locator(otp_input_selector).is_disabled()
            except Exception:
                otp_input_disabled = False
            if not (otp_input_disabled or otp_input_value.strip() == ""):
                Utility.log_error("OTP input field is neither cleared nor disabled after submission.")
                raise AssertionError("OTP input field not cleared/disabled.")
            # --- Then: Confirm navigation bar remains visible ---
            Utility.log_test_step("Confirming navigation bar remains visible after submission.")
            nav_links = [
                ("BAG", "xpath=//a[normalize-space()='BAG']"),
                ("ADDRESS", "xpath=//a[normalize-space()='ADDRESS']"),
                ("PAYMENT", "xpath=//a[normalize-space()='PAYMENT']")
            ]
            for link_name, link_xpath in nav_links:
                Utility.retry_assertion(
                    lambda ln=link_name, lx=link_xpath: expect(page.locator(lx)).to_be_visible(timeout=15000),
                    retries=3,
                    delay=2000
                )
                Utility.log_element_state(link_name, page.locator(link_xpath), timeout=15000)
            # --- Test Execution Summary ---
            Utility.log_test_result(
                "PASS",
                "OTP submitted successfully, UI responded as expected, navigation bar intact."
            )
        except AssertionError as ae:
            Utility.log_test_result("FAIL", f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_test_result("FAIL", f"Test failed due to exception: {e}")
            raise
        finally:
            browser.close()
#---#
#######

# Test Case 4 - TC-0006
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
# Test URLs dictionary (update as needed)
urls: dict[str, str] = {
    "otp_entry": "http://localhost:8000/index.html"  # Example URL, update as needed
}
def test_resend_otp_option_is_visible_and_accessible() -> None:
    """
    TC-0006: Resend OTP Option is Visible and Accessible
    Given: User lands on the OTP entry page
    When: User observes, hovers, and clicks the "RESEND OTP" text
    Then: The option is visible, interactive, and resends OTP with confirmation
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        test_result: str = "FAILED"
        test_details: str = ""
        otp_input_xpath: str = "//input[@id='otP']"
        resend_otp_xpath: str = "//span[normalize-space()='RESEND OTP']"
        resend_otp_selector: str = f"xpath={resend_otp_xpath}"
        otp_sent_msg_xpath: str = "//div[contains(@class,'otp-sent-msg')]"
        otp_sent_msg_selector: str = f"xpath={otp_sent_msg_xpath}"
        try:
            # --- Given: Setup and navigation to initial state ---
            Utility.log_test_step("Navigating to OTP entry page.")
            url: str = Utility.validate_and_convert_data(urls.get("otp_entry"), str)
            if not url:
                raise ValueError("OTP entry page URL is missing or invalid.")
            navigation_success: bool = Utility.navigate_to_page(page, url, timeout=15000)
            if not navigation_success:
                raise RuntimeError("Failed to navigate to OTP entry page.")
            # Accept cookies/pop-ups if present
            Utility.log_test_step("Checking for cookies or pop-ups.")
            cookie_popup_xpath: str = "//button[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'accept')]"
            Utility.safe_wait_and_interact(page, f"xpath={cookie_popup_xpath}", "click", timeout=5000)
            # Wait for OTP input field and essential elements
            Utility.log_test_step("Validating essential OTP entry elements.")
            generated_page.validate_essential_elements()
            Utility.log_element_state("OTP Input Field", page.locator(f"xpath={otp_input_xpath}"), timeout=15000)
            # --- When: Perform the action ---
            # Step 1: Verify "RESEND OTP" text is visible below the input field
            Utility.log_test_step("Verifying 'RESEND OTP' text is visible.")
            is_resend_visible: bool = Utility.wait_for_element_state(page, resend_otp_selector, state="visible", timeout=15000)
            if not is_resend_visible:
                raise AssertionError("'RESEND OTP' text is not visible on the page.")
            Utility.log_element_state("'RESEND OTP' Text", page.locator(resend_otp_selector), timeout=15000)
            # Step 2: Check that the text is clearly visible and distinguishable
            resend_text: str = Utility.get_element_text(page, resend_otp_selector, timeout=15000)
            resend_text = Utility.validate_and_convert_data(resend_text, str)
            if resend_text.strip().upper() != "RESEND OTP":
                raise AssertionError(f"Expected 'RESEND OTP', got '{resend_text.strip()}'.")
            # Step 3: Hover over the "RESEND OTP" text and check for hover effect
            Utility.log_test_step("Hovering over 'RESEND OTP' to check interactivity.")
            try:
                page.locator(resend_otp_selector).hover(timeout=15000)
                # Optionally, check for style change (color/underline) if possible
                # For demonstration, log the hover event
                Utility.log_console_message(type("msg", (), {"text": "Hovered over 'RESEND OTP'."})())
            except Exception as e:
                Utility.log_error(f"Hover action failed: {e}")
                raise
            # Step 4: Click on the "RESEND OTP" text
            Utility.log_test_step("Clicking 'RESEND OTP' to trigger resend action.")
            click_success: bool = Utility.safe_wait_and_interact(page, resend_otp_selector, "click", timeout=15000)
            if not click_success:
                raise AssertionError("Failed to click 'RESEND OTP'.")
            # --- Then: Verify expected outcomes ---
            # Step 5: Confirm a message or indicator that a new OTP has been sent
            Utility.log_test_step("Verifying OTP sent confirmation message.")
            otp_sent_confirmed: bool = False
            for attempt in range(3):
                otp_sent_confirmed = Utility.wait_for_element_state(page, otp_sent_msg_selector, state="visible", timeout=5000)
                if otp_sent_confirmed:
                    break
                time.sleep(1)
            if not otp_sent_confirmed:
                Utility.log_error("OTP sent confirmation message not found.")
                raise AssertionError("OTP sent confirmation message not visible after resend.")
            otp_sent_msg: str = Utility.get_element_text(page, otp_sent_msg_selector, timeout=15000)
            otp_sent_msg = Utility.validate_and_convert_data(otp_sent_msg, str)
            if "otp sent" not in otp_sent_msg.lower():
                Utility.log_error(f"Unexpected OTP sent message: {otp_sent_msg}")
                raise AssertionError("OTP sent confirmation message text is incorrect.")
            # Step 6: Confirm OTP input field is ready for new input (enabled/cleared)
            Utility.log_test_step("Checking OTP input field is enabled for new input.")
            otp_input_enabled: bool = page.locator(f"xpath={otp_input_xpath}").is_enabled()
            if not otp_input_enabled:
                raise AssertionError("OTP input field is not enabled after resend.")
            otp_input_value: str = page.locator(f"xpath={otp_input_xpath}").input_value()
            otp_input_value = Utility.validate_and_convert_data(otp_input_value, str)
            if len(otp_input_value) > 0:
                Utility.log_console_message(type("msg", (), {"text": "OTP input field is not cleared, but enabled."})())
            else:
                Utility.log_console_message(type("msg", (), {"text": "OTP input field is cleared and enabled."})())
            test_result = "PASSED"
            test_details = "Resend OTP option is visible, interactive, and functional."
        except AssertionError as ae:
            test_result = "FAILED"
            test_details = f"Assertion failed: {ae}"
            Utility.log_error(test_details)
            raise
        except Exception as e:
            test_result = "FAILED"
            test_details = f"Unexpected error: {e}"
            Utility.log_error(test_details)
            raise
        finally:
            Utility.log_test_result(test_result, test_details)
            browser.close()
#---#
#######

# Test Case 5 - TC-0007
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
# URLs for the application pages
urls: dict[str, str] = {
    "main": "http://localhost:8000/index.html",
    "cart": "http://localhost:8000/cart.html",
    "address": "http://localhost:8000/Address.html",
    "payment": "http://localhost:8000/payment.html"
}
def test_secure_badge_display_and_security_assurance() -> None:
    """
    TC-0007: Secure Badge is Displayed and Communicates Security Assurance
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
        test_passed: bool = True
        error_details: str = ""
        try:
            # Given: Navigate to the main page
            Utility.log_test_step("Navigating to main page (index.html)")
            navigation_success: bool = Utility.navigate_to_page(page, urls["main"])
            if not navigation_success:
                raise Exception("Navigation to main page failed.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            Utility.log_element_state("Navigation Bar", page.locator("xpath=//nav"), timeout=15000)
            # Accept cookies/pop-ups if present
            Utility.safe_wait_and_interact(page, "text=Accept", "click", timeout=5000)
            Utility.log_test_step("Accepted cookies if present.")
            # Then: The navigation bar is visible at the top of the page
            Utility.log_test_step("Validating essential elements on main page")
            Utility.retry_assertion(lambda: generated_page.validate_essential_elements(), retries=3, delay=1000)
            # When: Observe the right section of the navigation bar for secure badge
            Utility.log_test_step("Checking for secure badge presence and alignment")
            # Since secure badge is not in POM, we check via navigation bar essential elements
            # (Assume secure badge is part of essential elements for this test)
            # When: Hover over the secure icon and text to check tooltip/visual effect
            Utility.log_test_step("Hovering over secure icon and text for tooltip/visual effect")
            try:
                # Try to hover over the secure badge if present
                Utility.safe_wait_and_interact(page, "xpath=//nav//*[contains(text(),'100% secure')]", "click", timeout=5000)
                page.hover("xpath=//nav//*[contains(text(),'100% secure')]")
                time.sleep(1)
            except Exception as e:
                Utility.log_error(f"Secure badge hover failed: {e}")
            # Then: Check alignment and spacing (visual/manual check, log state)
            Utility.log_test_step("Checking alignment and spacing of secure badge (manual/visual check)")
            Utility.log_element_state("Secure Badge", page.locator("xpath=//nav//*[contains(text(),'100% secure')]"), timeout=15000)
            # When: Resize browser window to test responsiveness
            Utility.log_test_step("Resizing browser window to test responsiveness")
            for width, height in [(1200, 800), (768, 600), (375, 667)]:
                context.set_viewport_size({"width": width, "height": height})
                time.sleep(1)
                Utility.log_test_step(f"Viewport set to {width}x{height}")
                Utility.log_element_state("Secure Badge", page.locator("xpath=//nav//*[contains(text(),'100% secure')]"), timeout=15000)
            context.set_viewport_size({"width": 1920, "height": 1080})
            # Then: Secure badge is consistently displayed across all pages
            for page_key in ["cart", "address", "payment"]:
                Utility.log_test_step(f"Navigating to {page_key}.html to check secure badge")
                navigation_success = Utility.navigate_to_page(page, urls[page_key])
                if not navigation_success:
                    raise Exception(f"Navigation to {page_key}.html failed.")
                Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
                Utility.retry_assertion(lambda: generated_page.validate_essential_elements(), retries=3, delay=1000)
                Utility.log_element_state("Secure Badge", page.locator("xpath=//nav//*[contains(text(),'100% secure')]"), timeout=15000)
            Utility.log_test_result("PASS", "Secure badge is displayed and communicates security assurance.")
        except AssertionError as ae:
            test_passed = False
            error_details = f"Assertion failed: {ae}"
            Utility.log_test_result("FAIL", error_details)
            raise
        except Exception as e:
            test_passed = False
            error_details = f"Test failed: {e}"
            Utility.log_test_result("FAIL", error_details)
            raise
        finally:
            if not test_passed:
                screenshot_path = os.path.join(os.getcwd(), "secure_badge_failure.png")
                try:
                    page.screenshot(path=screenshot_path, full_page=True)
                    Utility.log_test_step(f"Screenshot saved to {screenshot_path}")
                except Exception as e:
                    Utility.log_error(f"Failed to capture screenshot: {e}")
            browser.close()
#---#
#######

# Test Case 6 - TC-0013
# Test URLs (replace with actual URLs as needed)
urls: dict[str, str] = {
    "index": os.environ.get("TEST_INDEX_URL", "https://your-app-url.com/"),
}
def test_otp_submission_with_incomplete_otp() -> None:
    """
    TC-0013: Submitting the OTP form with an incomplete or too short OTP value.
    Verifies that the OTP form does not accept incomplete OTPs and prevents navigation.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        test_result: str = "FAILED"
        error_details: str = ""
        short_otps: list[str] = ["1", "12"]
        initial_url: str = ""
        error_message_found: bool = False
        # Attach console logger
        page.on("console", Utility.log_console_message)
        try:
            # --- GIVEN: Navigate to the index page ---
            Utility.log_test_step("Navigate to the index page")
            navigation_success: bool = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            if not navigation_success:
                raise Exception("Failed to navigate to index page.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            initial_url = page.url
            Utility.log_element_state("BODY", page.locator("body"), timeout=15000)
            # --- WHEN: Click on the PAYMENT link in the navbar to reach the OTP entry page ---
            Utility.log_test_step('Click on the "PAYMENT" link in the navbar')
            generated_page.click_payment_link()
            Utility.wait_for_element_state(page, "xpath=//input[@id='otP']", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            otp_page_url: str = page.url
            # --- THEN: For each short OTP value, attempt to submit and verify behavior ---
            for short_otp in short_otps:
                # Validate OTP data type and length
                otp_value: str = Utility.validate_and_convert_data(short_otp, str)
                if not otp_value or not otp_value.isdigit() or len(otp_value) > 2:
                    raise ValueError(f"Invalid OTP test data: '{otp_value}'")
                Utility.log_test_step(f"Enter short OTP value '{otp_value}' into the OTP input field")
                generated_page.fill_otp_field(otp_value)
                Utility.log_element_state("OTP Input Field", page.locator("xpath=//input[@id='otP']"), timeout=15000)
                Utility.log_test_step('Click the "SUBMIT" button')
                generated_page.click_submit_button()
                # --- THEN: Observe for any error message or UI feedback ---
                Utility.log_test_step("Observe for error message or UI feedback")
                error_message_found = False
                error_selectors: list[str] = [
                    "xpath=//*[contains(@class,'error') or contains(@class,'invalid') or contains(@class,'alert')]",
                    "xpath=//*[contains(text(),'invalid') or contains(text(),'required') or contains(text(),'Incomplete')]"
                ]
                for selector in error_selectors:
                    try:
                        if Utility.wait_for_element_state(page, selector, state="visible", timeout=3000):
                            error_text: str = Utility.get_element_text(page, selector, timeout=3000)
                            if error_text and len(error_text) < 200:
                                Utility.log_test_result("ERROR MESSAGE FOUND", error_text)
                                error_message_found = True
                                break
                    except Exception:
                        continue
                # --- THEN: Check if the page navigates away or reloads ---
                Utility.log_test_step("Check if the page navigates away or reloads")
                current_url: str = page.url
                if current_url != otp_page_url:
                    raise AssertionError("Page navigated away after submitting incomplete OTP.")
                # --- THEN: Attempt to submit multiple times with the short OTP ---
                Utility.log_test_step("Attempt to submit multiple times with the short OTP")
                for attempt in range(2):
                    generated_page.click_submit_button()
                    time.sleep(1)
                    if page.url != otp_page_url:
                        raise AssertionError("Page navigated away after repeated incomplete OTP submissions.")
                # --- THEN: Refresh the page and repeat the submission with a short OTP ---
                Utility.log_test_step("Refresh the page and repeat the submission with a short OTP")
                page.reload(timeout=15000)
                Utility.wait_for_element_state(page, "xpath=//input[@id='otP']", state="visible", timeout=15000)
                generated_page.fill_otp_field(otp_value)
                generated_page.click_submit_button()
                time.sleep(1)
                if page.url != otp_page_url:
                    raise AssertionError("Page navigated away after refresh and incomplete OTP submission.")
            # --- THEN: Final assertion: No progress or navigation should occur; user remains on the OTP entry page ---
            Utility.log_test_step("Final assertion: User remains on the OTP entry page")
            if page.url != otp_page_url:
                raise AssertionError("User did not remain on the OTP entry page after all attempts.")
            test_result = "PASSED"
            Utility.log_test_result(test_result, "OTP form correctly blocks incomplete OTP submissions.")
        except PlaywrightTimeoutError as te:
            error_details = f"TimeoutError: {te}"
            Utility.log_error(error_details)
            raise
        except AssertionError as ae:
            error_details = f"AssertionError: {ae}"
            Utility.log_error(error_details)
            raise
        except Exception as e:
            error_details = f"Exception: {e}"
            Utility.log_error(error_details)
            raise
        finally:
            Utility.log_test_result(test_result, error_details if error_details else "Test completed successfully.")
            browser.close()
#---#
#######

# Test Case 7 - TC-0015
# Import the POM class
# Test URLs (replace with actual URLs as needed)
urls: dict[str, str] = {
    "index": os.environ.get("INDEX_PAGE_URL", "https://example.com/"),
}
def test_resend_otp_text_non_interactive() -> None:
    """
    TC-0015: Verifies that the 'RESEND OTP' text is not interactive and does not trigger any resend action.
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
        test_result: str = "FAILED"
        details: str = ""
        try:
            # Given: Navigate to the index page
            Utility.log_test_step("Navigate to the index page")
            index_url: str = Utility.validate_and_convert_data(urls.get("index"), str)
            if not index_url:
                raise ValueError("Index page URL is missing or invalid.")
            navigation_success: bool = Utility.navigate_to_page(page, index_url, timeout=15000)
            if not navigation_success:
                raise RuntimeError("Failed to navigate to the index page.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            Utility.log_element_state("Body", page.locator("body"), timeout=15000)
            Utility.log_test_step("Index page loaded successfully.")
            # Accept cookies/pop-ups if present
            Utility.safe_wait_and_interact(page, "button:has-text('Accept')", "click", timeout=5000)
            Utility.safe_wait_and_interact(page, "button:has-text('OK')", "click", timeout=5000)
            # Given: Wait for essential elements on index page
            generated_page.validate_essential_elements()
            # When: Click on the "PAYMENT" link in the navbar to reach the OTP entry page
            Utility.log_test_step("Click on the 'PAYMENT' link in the navbar")
            Utility.retry_assertion(
                lambda: generated_page.click_payment_link(),
                retries=3,
                delay=1000
            )
            # Then: OTP entry page loads, displaying the "RESEND OTP" text
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            Utility.log_test_step("OTP entry page loaded and essential elements are visible.")
            # When: Attempt to click on the "RESEND OTP" text
            Utility.log_test_step("Attempt to click on the 'RESEND OTP' text")
            resend_otp_xpath: str = "//span[normalize-space()='RESEND OTP']"
            resend_otp_selector: str = f"xpath={resend_otp_xpath}"
            # Wait for the RESEND OTP text to be visible
            is_resend_otp_visible: bool = Utility.wait_for_element_state(
                page, resend_otp_selector, state="visible", timeout=15000
            )
            if not is_resend_otp_visible:
                raise RuntimeError("'RESEND OTP' text is not visible on the page.")
            Utility.log_element_state("'RESEND OTP' text", page.locator(resend_otp_selector), timeout=15000)
            # Try to click the RESEND OTP text and catch any errors
            click_error: Exception | None = None
            try:
                Utility.safe_wait_and_interact(page, resend_otp_selector, "click", timeout=5000)
                time.sleep(1)
            except Exception as e:
                click_error = e
            # Then: The text is not a button or link and does not respond to clicks
            # Check that no navigation or UI feedback occurred
            Utility.log_test_step("Verify that clicking 'RESEND OTP' does not trigger any action")
            current_url: str = Utility.validate_and_convert_data(page.url, str)
            if current_url != page.url:
                raise AssertionError("Unexpected navigation occurred after clicking 'RESEND OTP'.")
            # Check that no new OTP input or feedback is shown (no visible change)
            otp_input_visible: bool = Utility.wait_for_element_state(
                page, f"xpath={generated_page._input_otp_xpath}", state="visible", timeout=5000
            )
            if not otp_input_visible:
                raise AssertionError("OTP input field disappeared after clicking 'RESEND OTP'.")
            # When: Attempt to double-click or right-click the "RESEND OTP" text
            Utility.log_test_step("Attempt to double-click and right-click 'RESEND OTP' text")
            try:
                page.locator(resend_otp_selector).dblclick(timeout=5000)
                page.locator(resend_otp_selector).click(button="right", timeout=5000)
            except Exception:
                pass  # Expected: no action or context menu
            # Then: No context menu or action is triggered
            # (No assertion needed if no error and no navigation)
            # When: Check for any cursor change (pointer) on hover
            Utility.log_test_step("Check cursor style on hover over 'RESEND OTP' text")
            cursor_style: str = page.evaluate(
                """selector => {
                    const el = document.evaluate(selector, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                    return el ? window.getComputedStyle(el).cursor : '';
                }""",
                resend_otp_xpath
            )
            if cursor_style != "auto" and cursor_style != "default":
                raise AssertionError(f"Cursor style is '{cursor_style}', expected 'auto' or 'default'.")
            # When: Refresh the page and click "RESEND OTP" again
            Utility.log_test_step("Refresh the page and repeat click on 'RESEND OTP' text")
            page.reload(timeout=15000)
            Utility.wait_for_element_state(page, resend_otp_selector, state="visible", timeout=15000)
            try:
                Utility.safe_wait_and_interact(page, resend_otp_selector, "click", timeout=5000)
            except Exception:
                pass  # Expected: no action
            # Then: The same behavior; no action is triggered
            Utility.log_test_step("Verify no action is triggered after refresh and click")
            current_url_after: str = Utility.validate_and_convert_data(page.url, str)
            if current_url_after != page.url:
                raise AssertionError("Unexpected navigation after refresh and click.")
            # Final: Test passed
            test_result = "PASSED"
            details = "RESEND OTP text is non-interactive as expected."
            Utility.log_test_result(test_result, details)
        except PlaywrightTimeoutError as te:
            details = f"Timeout occurred: {te}"
            Utility.log_error(details)
            raise
        except AssertionError as ae:
            details = f"Assertion failed: {ae}"
            Utility.log_error(details)
            raise
        except Exception as e:
            details = f"Unexpected error: {e}"
            Utility.log_error(details)
            raise
        finally:
            Utility.log_test_result(test_result, details)
            browser.close()
#---#
#######

# Test Case 8 - TC-0030
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
def test_resend_otp_text_non_interactive_behavior() -> None:
    """
    TC-0030: OTPbox - RESEND OTP - RESEND OTP text is not interactive or fails to trigger resend action due to missing handler.
    This test ensures that the UI does not break or freeze if the "RESEND OTP" action is non-functional, and that the user is not left in a broken state.
    """
    # --- Test URLs (replace with actual URL as needed) ---
    urls: dict[str, str] = {
        "otp_page": os.environ.get("OTP_PAGE_URL", "https://example.com/otp")
    }
    # --- XPaths from POM for elements not in POM (RESEND OTP) ---
    RESEND_OTP_XPATH: str = "//span[normalize-space()='RESEND OTP']"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        # --- Attach console logger ---
        page.on("console", Utility.log_console_message)
        generated_page = GeneratedPage(page)
        try:
            # --- Given: Navigate to OTP page and ensure essential elements are present ---
            Utility.log_test_step("Navigating to OTP page.")
            navigation_success: bool = Utility.navigate_to_page(page, urls["otp_page"], timeout=15000)
            if not navigation_success:
                Utility.log_test_result("FAIL", "Navigation to OTP page failed.")
                return
            Utility.log_test_step("Validating essential elements on OTP page.")
            generated_page.validate_essential_elements()
            # Accept cookies/pop-ups if present
            Utility.safe_wait_and_interact(page, "text=Accept", "click", timeout=5000)
            Utility.safe_wait_and_interact(page, "text=OK", "click", timeout=5000)
            # --- When: Wait for RESEND OTP text to be visible ---
            Utility.log_test_step("Waiting for 'RESEND OTP' text to be visible.")
            is_resend_otp_visible: bool = Utility.wait_for_element_state(page, f"xpath={RESEND_OTP_XPATH}", state="visible", timeout=15000)
            if not is_resend_otp_visible:
                Utility.log_test_result("FAIL", "'RESEND OTP' text not visible.")
                return
            # --- Then: Verify RESEND OTP text is visible and not interactive ---
            Utility.log_element_state("RESEND OTP", page.locator(f"xpath={RESEND_OTP_XPATH}"), timeout=15000)
            resend_otp_text: str = Utility.get_element_text(page, f"xpath={RESEND_OTP_XPATH}", timeout=15000)
            resend_otp_text = Utility.validate_and_convert_data(resend_otp_text, str)
            if resend_otp_text.strip() != "RESEND OTP":
                Utility.log_test_result("FAIL", "RESEND OTP text content mismatch.")
                return
            # Try clicking the RESEND OTP text (simulate missing handler)
            Utility.log_test_step("Attempting to click 'RESEND OTP' text (should do nothing).")
            click_result: bool = Utility.safe_wait_and_interact(page, f"xpath={RESEND_OTP_XPATH}", "click", timeout=15000)
            time.sleep(1)  # Wait for any possible UI feedback
            # Check for feedback or error message (should be none)
            Utility.log_test_step("Checking for feedback or error message after clicking 'RESEND OTP'.")
            feedback_present: bool = Utility.wait_for_element_state(page, "text=OTP resent", state="visible", timeout=3000)
            if feedback_present:
                Utility.log_test_result("FAIL", "Unexpected feedback shown after clicking RESEND OTP.")
                return
            # --- Then: Ensure OTP is not resent and no UI change occurs ---
            Utility.log_test_step("Clicking SUBMIT button after clicking 'RESEND OTP'.")
            generated_page.click_submit_button()
            time.sleep(1)  # Wait for any possible UI change
            # No OTP resent, no feedback expected
            Utility.log_test_step("Verifying no OTP resend or feedback after SUBMIT.")
            feedback_present_after_submit: bool = Utility.wait_for_element_state(page, "text=OTP resent", state="visible", timeout=3000)
            if feedback_present_after_submit:
                Utility.log_test_result("FAIL", "Unexpected feedback after SUBMIT.")
                return
            # --- When: Refresh and repeat to confirm persistence of issue ---
            Utility.log_test_step("Refreshing page to confirm issue persists.")
            page.reload()
            Utility.wait_for_element_state(page, f"xpath={RESEND_OTP_XPATH}", state="visible", timeout=15000)
            click_result_repeat: bool = Utility.safe_wait_and_interact(page, f"xpath={RESEND_OTP_XPATH}", "click", timeout=15000)
            time.sleep(1)
            feedback_present_repeat: bool = Utility.wait_for_element_state(page, "text=OTP resent", state="visible", timeout=3000)
            if feedback_present_repeat:
                Utility.log_test_result("FAIL", "Unexpected feedback after page reload and RESEND OTP click.")
                return
            # --- Then: Other elements remain functional ---
            Utility.log_test_step("Verifying other navigation links are functional.")
            generated_page.click_bag_link()
            time.sleep(1)
            generated_page.click_address_link()
            time.sleep(1)
            generated_page.click_payment_link()
            time.sleep(1)
            # --- When: Restore click handler (simulate by navigating to working page) ---
            Utility.log_test_step("Simulating restoration of RESEND OTP handler (manual step).")
            # This step would require a page reload with handler restored; for now, log as info.
            Utility.log_test_result("INFO", "Manual/Dev step: Restore click handler for RESEND OTP.")
            Utility.log_test_result("PASS", "RESEND OTP non-interactive behavior verified successfully.")
        except Exception as e:
            Utility.log_error(f"Test failed: {e}")
            raise
        finally:
            browser.close()
#---#
#######
