from selene import browser, be, have, command

from demoqa_tests import resource
from demoqa_tests.data.users import User


class RegistrationPage():
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name="gender"]')
        self.number = browser.element('#userNumber')
        self.dateOfBirthInput = browser.element('#dateOfBirthInput')
        self.subject = browser.element('#subjectsInput')
        self.hobby = browser.all('.custom-checkbox')
        self.file = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.states_and_cities = browser.all('[id^=react-select][id*=option]')

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        self.first_name.should(be.blank).type(value)

    def fill_last_name(self, value):
        self.last_name.should(be.blank).type(value)

    def fill_email(self, value):
        self.email.should(be.blank).type(value)

    def select_gender(self, value):
        self.gender.element_by(have.value(value)).element('..').click()

    def fill_mobile_number(self, value):
        self.number.should(be.blank).type(value)

    def fill_date_of_birth(self, day, month, year):
        self.dateOfBirthInput.click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def select_subjects(self, value):
        self.subject.perform(
            command.js.scroll_into_view).should(be.blank).type(value).press_enter()

    def select_hobbies(self, value):
        self.hobby.element_by(have.exact_text(value)).click()

    def upload_picture(self, value):
        self.file.send_keys(resource.path_file(value))

    def fill_current_address(self, value):
        self.address.should(be.blank).type(value)

    def select_state(self, value):
        self.state.click()
        self.states_and_cities.element_by(have.exact_text(value)).click()

    def select_city(self, value):
        self.city.click()
        self.states_and_cities.element_by(have.exact_text(value)).click()

    def click_submit(self):
        browser.element('#submit').click()

    def fill_registration_form(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.user_email)
        self.select_gender(user.gender)
        self.fill_mobile_number(user.mobile)
        self.fill_date_of_birth(user.day, user.month, user.year)
        self.select_subjects(user.subject)
        self.select_hobbies(user.hobby)
        self.upload_picture(user.file)
        self.fill_current_address(user.address)
        self.select_state(user.state)
        self.select_city(user.city)
        self.click_submit()

    def should_title_submit_the_form(self, title):
        browser.element('#example-modal-sizes-title-lg').should(
            have.exact_text(title)
        )

    def should_registered_user_with(self, student: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{student.first_name} {student.last_name}',
                student.user_email,
                student.gender,
                student.mobile,
                f'{student.day} {student.month},{student.year}',
                student.subject,
                student.hobby,
                student.file,
                student.address,
                f'{student.state} {student.city}',
            )
        )
