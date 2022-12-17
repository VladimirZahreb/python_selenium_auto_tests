import random
import time
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage
# import time
# from pages.base_page import BasePage
# from locators.elements_page_locators import TextBoxPageLocators

# # def test(driver):
#     page = BasePage(driver, 'https://rozetka.com.ua/ua/')
#     page.open()
#     time.sleep(3)

class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            # input_data = text_box_page.fill_all_fields()
            # output_date = text_box_page.check_filled_form()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            # time.sleep(10)
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            # time.sleep(10)

            # print(output_name, output_email, current_address, permanent_address)
            # print(text_box_page.check_filled_form())
            # print(output_name)
            # print(output_email)
            # print(output_current_address)
            # print(output_permanent_address)
            # """Більше читабельно"""
            assert full_name == output_name, "the full_name does not math"
            assert email == output_email, "the email does not math"
            assert current_address == output_current_address, "the current_address does not math"
            assert permanent_address == output_permanent_address, "the permanent_address does not math"
            # """Менше читабельно"""
            # assert input_data == output_date

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            # time.sleep(5)
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page = get_output_result()
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result, 'checkboxes have not been selected'


    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == "No", "'No' have not been selected"


    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            # time.sleep(5)
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result


        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            # print(key_word)
            # print(table_result)
            assert key_word in table_result, "the person was not found in the table"


        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person()
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            print(age)
            print(row)
            assert age in row, "the person card has not been chanched"

        def test_web_table_delete_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person()
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found"

        def test_web_table_change_cound_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], "The number of rows has not been changed or has changed incorrectly"



