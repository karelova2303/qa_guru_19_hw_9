from pathlib import Path

from selene import browser, have, be, command


def test_form_demoqa(browser_options):
    browser.open('/automation-practice-form')

    # WHEN
    browser.element('#firstName').should(be.blank).type('Veronika')
    browser.element('#lastName').should(be.blank).type('Filatova')
    browser.element('#userEmail').should(be.blank).type('Veronika_Fila@mail.com')
    browser.all('[name="gender"]').element_by(have.value('Female')).element('..').click()
    browser.element('#userNumber').should(be.blank).type('9999872282')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('February')
    browser.element('.react-datepicker__year-select').type('1999')
    browser.element(f'.react-datepicker__day--0{21}:not(.react-datepicker__day--outside-month)').click()

    browser.element('#subjectsInput').perform(
        command.js.scroll_into_view).should(be.blank).type('Chemistry').press_enter()
    browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).click()

    browser.element('#uploadPicture').send_keys(
        str(Path(__file__).parent.parent.joinpath(f'resources/girafe.jpg').absolute()))

    browser.element('#currentAddress').should(be.blank).type('41 Eastern Avenue APT 243 San Francisco, 77338')

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Rajasthan')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Jaiselmer')).click()

    browser.element('#submit').click()

    # THEN
    browser.element('#example-modal-sizes-title-lg').should(
        have.exact_text('Thanks for submitting the form'))

    browser.element('.table').all('td').even.should(
        have.exact_texts('Veronika Filatova',
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
    )
