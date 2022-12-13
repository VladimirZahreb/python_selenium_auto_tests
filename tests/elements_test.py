# import time
from pages.elements_page import TextBoxPage, CheckBoxPage
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
            # check_box_page.open_full_list()
            # check_box_page.click_random_checkbox()
            # # time.sleep(5)
            # input_checkbox = check_box_page.get_checked_checkboxes()
            # output_result = check_box_page = get_output_result()
            # print(input_checkbox)
            # print(output_result)
            # assert input_checkbox == output_result

