from demoqa_tests.data.users import User
from demoqa_tests.pages.registartion_page import RegistrationPage


def test_registartion_form(browser_options):
    registration_page = RegistrationPage()

    student_filatova = User('Veronika', 'Filatova',
                            'Veronika_Fila@mail.com',
                            'Female', '9999872282',
                            '21', 'February', '1999',
                            'Chemistry', 'Reading',
                            'girafe.jpg',
                            '41 Eastern Avenue APT 243 San Francisco, 77338',
                            'Rajasthan', 'Jaiselmer'
                            )

    registration_page.open()

    # WHEN
    registration_page.fill_first_name(student_filatova.first_name)
    registration_page.fill_last_name(student_filatova.last_name)
    registration_page.fill_email(student_filatova.userEmail)
    registration_page.select_gender(student_filatova.gender)
    registration_page.fill_mobile_number(student_filatova.mobile)
    registration_page.fill_date_of_birth(student_filatova.day,
                                         student_filatova.month,
                                         student_filatova.year)
    registration_page.select_subjects(student_filatova.subject)
    registration_page.select_hobbies(student_filatova.hobby)
    registration_page.upload_picture(student_filatova.file)
    registration_page.fill_current_address(student_filatova.address)
    registration_page.select_state(student_filatova.state)
    registration_page.select_city(student_filatova.city)
    registration_page.click_submit()

    # THEN
    registration_page.should_title_submit_the_form(
        'Thanks for submitting the form')

    registration_page.should_registered_user_with(student_filatova)
