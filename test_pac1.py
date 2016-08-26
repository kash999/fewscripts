from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re


class TestPac1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.aviva.co.uk"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_pac1(self):
        driver = self.driver
        driver.get(self.base_url + "/pac/")
        driver.find_element_by_id("male").click()
        driver.find_element_by_id("id_detail-you_gender_0").click()
        Select(driver.find_element_by_id("id_detail-you_date_of_birth_day")).select_by_visible_text("3")
        Select(driver.find_element_by_id("id_detail-you_date_of_birth_month")).select_by_visible_text("February")
        Select(driver.find_element_by_id("id_detail-you_date_of_birth_year")).select_by_visible_text("1958")
        Select(driver.find_element_by_id("id_detail-marital_status")).select_by_visible_text("Single")
        driver.find_element_by_id("id_detail-postcode").clear()
        driver.find_element_by_id("id_detail-postcode").send_keys("NR1 3NS")
        driver.find_element_by_id("id_detail-funds_1").clear()
        driver.find_element_by_id("id_detail-funds_1").send_keys("120000")
        driver.find_element_by_id("id_detail-aviva_fund_0").click()
        driver.find_element_by_css_selector("input.button.yellow").click()
        driver.find_element_by_id("id_health-you_height_units_0").click()
        driver.find_element_by_id("id_health-you_height_imperial_feet").clear()
        driver.find_element_by_id("id_health-you_height_imperial_feet").send_keys("6")
        driver.find_element_by_id("id_health-you_weight_units_0").click()
        driver.find_element_by_id("id_health-you_weight_imperial_stones").clear()
        driver.find_element_by_id("id_health-you_weight_imperial_stones").send_keys("15")
        driver.find_element_by_id("id_health-you_smoke_0").click()
        driver.find_element_by_id("id_health-you_other_conditions_0").click()
        driver.find_element_by_id("id_health-you_other_conditions_1").click()
        driver.find_element_by_id("id_health-you_other_conditions_2").click()
        driver.find_element_by_css_selector("input.button.yellow").click()
        driver.find_element_by_id("id_blood-you_hp_diagnose_month").clear()
        driver.find_element_by_id("id_blood-you_hp_diagnose_month").send_keys("12")
        driver.find_element_by_id("id_blood-you_hp_diagnose_year").clear()
        driver.find_element_by_id("id_blood-you_hp_diagnose_year").send_keys("2004")
        driver.find_element_by_id("id_blood-you_hp_take_meds_0").click()
        Select(driver.find_element_by_id("id_blood-you_hp_med_name_0")).select_by_visible_text("Abacavir")
        driver.find_element_by_name("add_meds").click()
        Select(driver.find_element_by_id("id_blood-you_hp_med_name_1")).select_by_visible_text("Accolate")
        driver.find_element_by_css_selector("input.button.yellow").click()
        driver.find_element_by_id("id_cholesterol-you_ch_diagnose_month").clear()
        driver.find_element_by_id("id_cholesterol-you_ch_diagnose_month").send_keys("02")
        driver.find_element_by_id("id_cholesterol-you_ch_diagnose_year").clear()
        driver.find_element_by_id("id_cholesterol-you_ch_diagnose_year").send_keys("2002")
        driver.find_element_by_id("id_cholesterol-you_ch_take_med_0").click()
        Select(driver.find_element_by_id("id_cholesterol-you_ch_med_name_0")).select_by_visible_text("Acea Gel")
        driver.find_element_by_name("add_meds").click()
        Select(driver.find_element_by_id("id_cholesterol-you_ch_med_name_1")).select_by_visible_text("Airomir")
        driver.find_element_by_css_selector("input.button.yellow").click()
        driver.find_element_by_id("id_diabetes-you_dia_diagnose_month").clear()
        driver.find_element_by_id("id_diabetes-you_dia_diagnose_month").send_keys("04")
        driver.find_element_by_id("id_diabetes-you_dia_diagnose_year").clear()
        driver.find_element_by_id("id_diabetes-you_dia_diagnose_year").send_keys("2004")
        driver.find_element_by_id("id_diabetes-you_dia_hospitalized_0").click()
        driver.find_element_by_id("id_diabetes-you_dia_control_1").click()
        Select(driver.find_element_by_id("id_diabetes-you_dia_med_name_0")).select_by_visible_text("Adizem- XL")
        driver.find_element_by_id("id_diabetes-you_dia_med_dose_0").clear()
        driver.find_element_by_id("id_diabetes-you_dia_med_dose_0").send_keys("1")
        Select(driver.find_element_by_id("id_diabetes-you_dia_med_dose_unit_0")).select_by_visible_text("Milligram")
        driver.find_element_by_id("id_diabetes-you_dia_med_amount_0").clear()
        driver.find_element_by_id("id_diabetes-you_dia_med_amount_0").send_keys("1")
        Select(driver.find_element_by_id("id_diabetes-you_dia_med_time_period_0")).select_by_visible_text("Day")
        driver.find_element_by_id("id_diabetes-you_dia_other_others_0").click()
        driver.find_element_by_id("id_diabetes-you_dia_other_others_1").click()
        driver.find_element_by_id("id_diabetes-you_dia_other_others_2").click()
        driver.find_element_by_id("id_diabetes-you_dia_other_others_3").click()
        driver.find_element_by_id("id_diabetes-you_dia_other_others_4").click()
        driver.find_element_by_css_selector("input.button.yellow").click()
        driver.find_element_by_id("id_pdependent-provide_for_dependant_nonprotected_1").click()
        driver.find_element_by_css_selector("input.button.yellow").click()
        driver.find_element_by_id("id_taxfree-tax_free_cash").clear()
        driver.find_element_by_id("id_taxfree-tax_free_cash").send_keys("12")
        driver.find_element_by_css_selector("input.button.yellow").click()
        driver.find_element_by_css_selector("li > label").click()
        driver.find_element_by_id("id_payfreq-payment_frequency_0").click()
        driver.find_element_by_css_selector("input.button.yellow").click()
        driver.find_element_by_id("advance").click()
        driver.find_element_by_id("id_payadv-payment_advance_0").click()
        driver.find_element_by_css_selector("input.button.yellow").click()
        driver.find_element_by_xpath("//div[@id='main']/form/fieldset/div/div/ul/li[2]/label").click()
        driver.find_element_by_css_selector("input.button.yellow").click()
        driver.find_element_by_id("id_paygua-payment_guarantee_0").click()
        driver.find_element_by_css_selector("input.button.yellow").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
