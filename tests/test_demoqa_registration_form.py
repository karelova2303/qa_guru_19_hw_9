from demoqa_tests.data.users import User
from demoqa_tests.pages.registartion_page import RegistrationPage


def test_registartion_form(browser_options):
    registration_page = RegistrationPage()

    student_filatova = User('Veronika', 'Filatova',
                            'Veronika_Fila@mail.com',
                            'Female', '9999872282',
                            '21', 'May', '1996',
                            'Chemistry', 'Reading',
                            'girafe.jpg',
                            '41 Eastern Avenue APT 243 San Francisco, 77338',
                            'Rajasthan',
                            'Jaiselmer'
                            )

    registration_page.open()

    # WHEN
    registration_page.fill_registration_form(student_filatova)

    # THEN
    registration_page.should_title_submit_the_form(
        'Thanks for submitting the form')

    registration_page.should_registered_user_with(student_filatova)
