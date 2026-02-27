from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('username@gmail.com')

    user_input = page.get_by_test_id('registration-form-username-input').locator('input')
    user_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path='browser-state2.json')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state2.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    text_courses = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(text_courses).to_have_text("Courses")

    icon_there = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_there).to_be_visible()

    text_there = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(text_there).to_have_text('There is no results')

    description_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(description_text).to_have_text('Results from the load test pipeline will be displayed here')

    page.wait_for_timeout(10000)
