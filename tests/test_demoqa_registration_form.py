from model.pages.registartion_page import RegistrationPage


def test_registartion_form(browser_options):
    registration_page = RegistrationPage()

    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Veronika')
    registration_page.fill_last_name('Filatova')
    registration_page.fill_email('Veronika_Fila@mail.com')
    registration_page.select_gender('Female')
    registration_page.fill_mobile_number('9999872282')
    registration_page.fill_date_of_birth('21', 'February', '1999')
    registration_page.select_subjects('Chemistry')
    registration_page.select_hobbies('Reading')
    registration_page.upload_picture('girafe.jpg')
    registration_page.fill_current_address('41 Eastern Avenue APT 243 San Francisco, 77338')
    registration_page.select_state('Rajasthan')
    registration_page.select_city('Jaiselmer')
    registration_page.click_submit()

    # THEN
    registration_page.should_title_submit_the_form(
        'Thanks for submitting the form')

    registration_page.should_registered_user_with(
        'Veronika Filatova',
        'Veronika_Fila@mail.com',
        'Female',
        '9999872282',
        '21 February,1999',
        'Chemistry',
        'Reading',
        'girafe.jpg',
        '41 Eastern Avenue APT 243 San Francisco, 77338',
        'Rajasthan Jaiselmer',
    )
