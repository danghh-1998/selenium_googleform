from selenium import webdriver
from faker import Faker
from faker.providers import BaseProvider
import random


class Form:
    class OtherGendersProvider(BaseProvider):
        def other_genders(self):
            lgbt_types = ['Lesbian', 'Bisexual', 'Pansexual', 'Gay', 'Asexual', 'Allosexual', 'Heterosexual',
                          'Homosexual', 'Monosexual', 'Polysexual', 'Queer']
            return random.choice(lgbt_types)

    def __init__(self, url):
        option = webdriver.ChromeOptions()
        option.add_argument('-incognito')
        option.headless = True
        self.browser = webdriver.Chrome(executable_path='../resources/chromedriver', options=option)
        self.browser.get(url)

        faker = Faker()
        faker.add_provider(self.OtherGendersProvider)
        self.gender = faker.random_int(0, 2)
        self.age = faker.random_int(0, 100)
        self.email = faker.email()
        if self.gender == 0:
            self.name = faker.name_male()
        elif self.gender == 1:
            self.name = faker.name_female()
        else:
            self.name = faker.name()
            self.other = faker.other_genders()

    def fill_form(self):
        name_input, age_input, email_input = self.browser.find_elements_by_class_name(
            'quantumWizTextinputPaperinputInput')
        other_input = self.browser.find_element_by_class_name('quantumWizTextinputSimpleinputInput')
        male_radio, female_radio, other_radio = self.browser.find_elements_by_class_name(
            'docssharedWizToggleLabeledLabelWrapper')
        submit_button = self.browser.find_element_by_class_name('appsMaterialWizButtonPaperbuttonContent')
        name_input.send_keys(self.name)
        age_input.send_keys(self.age)
        email_input.send_keys(self.email)
        if self.gender == 0:
            male_radio.click()
        elif self.gender == 1:
            female_radio.click()
        else:
            other_radio.click()
            other_input.send_keys(self.other)
        print(self)
        submit_button.click()
        self.browser.close()

    def __str__(self):
        gender_part = f'{self.other}' if self.gender == 2 else f'{"Male" if self.gender == 0 else "Female"}'
        return f'Name: {self.name}, Age: {self.age}, Email: {self.email}, gender: {gender_part}'


def main():
    for _ in range(1000):
        Form(
            url='https://docs.google.com/forms/d/e/1FAIpQLSfMWIja0X-OQtNtwdX5rYBZyJQXN8AgyBWLnoE_TeWFBcPkTg/viewform').fill_form()


if __name__ == '__main__':
    main()
