from playwright.sync_api import expect

def test_empty_courses_list2(chromium_page_with_state):
    page = chromium_page_with_state

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    text_courses = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(text_courses).to_have_text("Courses")

    icon_there = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_there).to_be_visible()

    text_there = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(text_there).to_have_text('There is no results')

    description_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(description_text).to_have_text('Results from the load test pipeline will be displayed here')
