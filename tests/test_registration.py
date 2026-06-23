import pytest

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize(
    "email, username, password",
    [
        ("test123@example.com", "test_user_123", "Test123!")
    ]
)
def test_successful_registration(
        registration_page: RegistrationPage,
        dashboard_page: DashboardPage,
        email: str,
        username:str,
        password: str
):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.fill_registration_form(email=email, username=username, password=password)
        registration_page.click_registration_button()
        dashboard_page.check_dashboard_title_visible()






        # chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        #
        # email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
        # email_input.fill('user.name@gmail.com')
        #
        # user_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
        # user_input.fill('username')
        #
        # password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
        # password_input.fill('password')
        #
        # registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
        # registration_button.click()
        #
        #
        # dashboard_tittle = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
        # expect(dashboard_tittle).to_be_visible()