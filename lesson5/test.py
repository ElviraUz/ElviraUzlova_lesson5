import os
import pytest
from selene import browser, be, command, have


@pytest.fixture(scope="session")
def setup():
    browser.config.browser_name = "chrome"
    browser.config.window_height = '1024'
    browser.config.window_width = '1024'


def test_fill_and_send_form(setup):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#fixedban').perform(command.js.remove)
    browser.element('#firstName').should(be.blank).type('Arya')
    browser.element('#lastName').should(be.blank).type('Stark')
    browser.element('#userEmail').should(be.blank).type('aryastark@westeros.com')
    browser.element('[for="gender-radio-2"]').should(be.visible).click()
    browser.element('#userNumber').should(be.blank).type('0123456789')
    browser.execute_script("window.scrollBy(0, 500)")
    browser.element('#dateOfBirthInput').should(be.clickable).click()
    browser.element('.react-datepicker__month-select').should(be.clickable).click()
    browser.element('[value="11"]').should(be.clickable).click()
    browser.element('.react-datepicker__month-select').should(be.clickable).click()
    browser.element('#react-select-3-input').should(be.blank).type('Haryana').press_enter()
    browser.element('[value="1990"]').should(be.clickable).click()
    browser.element('div[class="react-datepicker__day react-datepicker__day--014"]').should(be.clickable).click()
    browser.element('[for="hobbies-checkbox-1"]').should(be.clickable).click()
    browser.element('#subjectsInput').should(be.blank).type('Ph').press_enter()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/kotik.jpg')
    browser.element("#currentAddress").should(be.blank).type('Winterfell')
    browser.element('#react-select-3-input').should(be.blank).type('Har').press_enter()
    browser.element('#react-select-4-input').should(be.blank).type('Ka').press_enter()
    browser.execute_script("window.scrollBy(200, 500)")
    browser.element('#submit').press_enter()

    # проверка

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('//tbody/tr[1]/td[2]').should(have.text('Arya Stark'))
    browser.element('//tbody/tr[2]/td[2]').should(have.text('aryastark@westeros.com'))
    browser.element('//tbody/tr[3]/td[2]').should(have.text('Female'))
    browser.element('//tbody/tr[4]/td[2]').should(have.text('0123456789'))
    browser.element('//tbody/tr[5]/td[2]').should(have.text('14 December,1990'))
    browser.element('//tbody/tr[6]/td[2]').should(have.text('Physics'))
    browser.element('//tbody/tr[7]/td[2]').should(have.text('Sports'))
    browser.element('//tbody/tr[8]/td[2]').should(have.text('kotik.jpg'))
    browser.element('//tbody/tr[9]/td[2]').should(have.text('Winterfell'))
    browser.element('//tbody/tr[10]/td[2]').should(have.text('Haryana Karnal'))
