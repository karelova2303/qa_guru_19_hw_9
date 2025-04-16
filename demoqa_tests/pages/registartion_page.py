from selene import browser, be, have, command

from demoqa_tests import resource
from demoqa_tests.data.users import User


class RegistrationPage():

    def __init__(self):
        self.states_and_cities = browser.all('[id^=react-select][id*=option]')

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, first_name):
        browser.element('#firstName').should(be.blank).type(first_name)

    def fill_last_name(self, last_name):
        browser.element('#lastName').should(be.blank).type(last_name)

    def fill_email(self, email):
        browser.element('#userEmail').should(be.blank).type(email)

    def select_gender(self, gender):
        browser.all('[name="gender"]').element_by(have.value(gender)).element('..').click()

    def fill_mobile_number(self, number):
        browser.element('#userNumber').should(be.blank).type(number)

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def select_subjects(self, subject):
        browser.element('#subjectsInput').perform(
            command.js.scroll_into_view).should(be.blank).type(subject).press_enter()

    def select_hobbies(self, hobby):
        browser.all('.custom-checkbox').element_by(have.exact_text(hobby)).click()

    def upload_picture(self, file):
        browser.element('#uploadPicture').send_keys(resource.path_file(file))

    def fill_current_address(self, address):
        browser.element('#currentAddress').should(be.blank).type(address)

    def select_state(self, state):
        browser.element('#state').click()
        self.states_and_cities.element_by(have.exact_text(state)).click()

    def select_city(self, city):
        browser.element('#city').click()
        self.states_and_cities.element_by(have.exact_text(city)).click()

    def click_submit(self):
        browser.element('#submit').click()

    def should_title_submit_the_form(self, title):
        browser.element('#example-modal-sizes-title-lg').should(
            have.exact_text(title)
        )

    def should_registered_user_with(self, student: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{student.first_name} {student.last_name}',
                student.userEmail,
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
