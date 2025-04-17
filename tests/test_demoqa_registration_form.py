from demoqa_tests.data.users import student_filatova
from demoqa_tests.pages.registartion_page import RegistrationPage


def test_registartion_form(browser_options):
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.fill_registration_form(student_filatova)
    registration_page.should_title_registered_the_form()
    registration_page.should_registered_user_with(student_filatova)
