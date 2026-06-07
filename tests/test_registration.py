from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromiun_page:Page):
        chromiun_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = chromiun_page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        user_input = chromiun_page.get_by_test_id('registration-form-username-input').locator('input')
        user_input.fill('username')

        password_input = chromiun_page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = chromiun_page.get_by_test_id('registration-page-registration-button')
        registration_button.click()


        dashboard_tittle = chromiun_page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard_tittle).to_be_visible()