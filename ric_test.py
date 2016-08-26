import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 


class RicTest(unittest.TestCase):
    
       def test_serach_firefox(self):
           d = webdriver.Firefox()
           d.maximize_window()
           d.get('https://www.aviva.co.uk/ric-tool/')
           d.implicitly_wait(15)
           self.assertIn('Aviva', d.title)
           e =  d.find_elements_by_tag_name('tspan')
           for i in e:
              if i.text == 'Your details':
                     i.click()
                     break
           d.implicitly_wait(15)
           d.find_element_by_id('male').click()
           d.find_element_by_id('id_you_date_of_birth_day').find_elements_by_tag_name('option')[15].click()
           d.find_element_by_id('id_you_date_of_birth_month').find_elements_by_tag_name('option')[1].click()
           d.find_element_by_id('id_you_date_of_birth_year').find_elements_by_tag_name('option')[3].click()
           d.find_element_by_name('continue').click()
           d.find_element_by_id('id_marital_status').find_elements_by_tag_name('option')[4].click()
           d.find_element_by_name('continue').click()
           d.find_element_by_id('id_postcode').send_keys('NR1 3NS')
           d.find_element_by_name('continue').click()
           d.find_element_by_id('id_you_smoke_1').click()
           d.find_element_by_name('continue').click()
           d.find_element_by_id('yes').click()
           #d.find_element_by_name('continue').click()
           d.find_element_by_id('id_aviva_non_protected_1').send_keys(12000)
           d.find_element_by_id('id_aviva_non_protected_2').send_keys(12000)
           d.find_element_by_name('continue').click()
           d.find_element_by_id('no').click()          
           slide = d.find_element_by_id('handle_id_tax_free_cash')
           width = slide.size['width']
           move =  webdriver.ActionChains(d)
           move.click_and_hold(slide).move_by_offset(55,0).release().perform()
           
           d.find_element_by_name('continue').click()
           time.sleep(15)
           ele = d.find_elements_by_tag_name('tspan')
           #ele =  WebDriverWait(d, 30).until(EC.element_to_be_clickable((By.TAG_NAME, 'tspan')))
           for i in ele:
              if i.text == 'Your health':
                     i.click()
                     break
           d.find_element_by_name('continue').click()
           
           d.find_element_by_name("you_height_imperial_feet").send_keys(6)
           d.find_element_by_name("you_height_imperial_inches").send_keys(2)
           d.find_element_by_name('continue').click()
           d.find_element_by_name("you_weight_imperial_stones").send_keys(15)
           d.find_element_by_name("you_weight_imperial_pounds").send_keys(9)
           d.find_element_by_name('continue').click()
           d.find_element_by_id('no').click()
           time.sleep(1)
           d.find_element_by_id('no').click()
           time.sleep(1)
           d.find_element_by_name('continue').click()
           
           time.sleep(15)
           ele = d.find_elements_by_tag_name('tspan')
           #ele =  WebDriverWait(d, 30).until(EC.element_to_be_clickable((By.TAG_NAME, 'tspan')))
           for i in ele:
              if i.text == 'Your dependants':
                     i.click()
                     break
           d.find_element_by_name('continue').click()
           d.find_element_by_id('no').click()
           time.sleep(1)
           d.find_element_by_name('continue').click()
         
           time.sleep(10)
           ele = d.find_elements_by_tag_name('tspan')
           #ele =  WebDriverWait(d, 30).until(EC.element_to_be_clickable((By.TAG_NAME, 'tspan')))
           for i in ele:
              if i.text == 'Your income':
                     i.click()
                     break
           d.find_element_by_id('id_escalation_1').click()
           d.find_element_by_name('continue').click()
           time.sleep(1)
           d.find_element_by_name('continue').click()
           d.find_element_by_id('advance').click()
           time.sleep(1)
           d.find_element_by_name('continue').click()
           time.sleep(10)
           ele = d.find_elements_by_tag_name('tspan')
           #ele =  WebDriverWait(d, 30).until(EC.element_to_be_clickable((By.TAG_NAME, 'tspan')))
           for i in ele:
              if i.text == 'Your guarantee':
                     i.click()
                     break
           time.sleep(2) 
           d.find_element_by_id('id_payment_guarantee_1').click()
           time.sleep(1)
           d.find_element_by_name('continue').click()
           
           time.sleep(5)
           
           
       def test_serach_chrome(self):
           chromedriver = "/usr/local/bin/chromedriver"
           os.environ["webdriver.chrome.driver"] = chromedriver
           d = webdriver.Chrome(chromedriver)
           d.maximize_window()
           d.get('https://www.aviva.co.uk/ric-tool/')
           d.implicitly_wait(15)
           self.assertIn('Aviva', d.title)
           time.sleep(15)
           e =  d.find_elements_by_tag_name('tspan')
           for i in e:
              if i.text == 'Your details':
                     i.click()
                     break
           d.implicitly_wait(15)
           d.find_element_by_id('male').click()
           d.find_element_by_id('id_you_date_of_birth_day').find_elements_by_tag_name('option')[15].click()
           d.find_element_by_id('id_you_date_of_birth_month').find_elements_by_tag_name('option')[1].click()
           d.find_element_by_id('id_you_date_of_birth_year').find_elements_by_tag_name('option')[3].click()
           d.find_element_by_name('continue').click()
           d.find_element_by_id('id_marital_status').find_elements_by_tag_name('option')[4].click()
           d.find_element_by_name('continue').click()
           d.find_element_by_id('id_postcode').send_keys('NR1 3NS')
           d.find_element_by_name('continue').click()
           d.find_element_by_id('id_you_smoke_1').click()
           d.find_element_by_name('continue').click()
           d.find_element_by_id('yes').click()
           #d.find_element_by_name('continue').click()
           d.find_element_by_id('id_aviva_non_protected_1').send_keys(12000)
           d.find_element_by_id('id_aviva_non_protected_2').send_keys(12000)
           d.find_element_by_name('continue').click()
           d.find_element_by_id('no').click()          
           slide = d.find_element_by_id('handle_id_tax_free_cash')
           width = slide.size['width']
           move =  webdriver.ActionChains(d)
           move.click_and_hold(slide).move_by_offset(55,0).release().perform()
           
           d.find_element_by_name('continue').click()
           time.sleep(15)
           ele = d.find_elements_by_tag_name('tspan')
           #ele =  WebDriverWait(d, 30).until(EC.element_to_be_clickable((By.TAG_NAME, 'tspan')))
           for i in ele:
              if i.text == 'Your health':
                     i.click()
                     break
           d.find_element_by_name('continue').click()
           
           d.find_element_by_name("you_height_imperial_feet").send_keys(6)
           d.find_element_by_name("you_height_imperial_inches").send_keys(2)
           d.find_element_by_name('continue').click()
           d.find_element_by_name("you_weight_imperial_stones").send_keys(15)
           d.find_element_by_name("you_weight_imperial_pounds").send_keys(9)
           d.find_element_by_name('continue').click()
           d.find_element_by_id('no').click()
           time.sleep(1)
           d.find_element_by_id('no').click()
           time.sleep(1)
           d.find_element_by_name('continue').click()
           
           time.sleep(15)
           ele = d.find_elements_by_tag_name('tspan')
           #ele =  WebDriverWait(d, 30).until(EC.element_to_be_clickable((By.TAG_NAME, 'tspan')))
           for i in ele:
              if i.text == 'Your dependants':
                     i.click()
                     break
           d.find_element_by_name('continue').click()
           d.find_element_by_id('no').click()
           time.sleep(1)
           d.find_element_by_name('continue').click()
         
           time.sleep(10)
           ele = d.find_elements_by_tag_name('tspan')
           #ele =  WebDriverWait(d, 30).until(EC.element_to_be_clickable((By.TAG_NAME, 'tspan')))
           for i in ele:
              if i.text == 'Your income':
                     i.click()
                     break
           d.find_element_by_id('id_escalation_1').click()
           d.find_element_by_name('continue').click()
           time.sleep(1)
           d.find_element_by_name('continue').click()
           d.find_element_by_id('advance').click()
           time.sleep(1)
           d.find_element_by_name('continue').click()
           time.sleep(10)
           ele = d.find_elements_by_tag_name('tspan')
           #ele =  WebDriverWait(d, 30).until(EC.element_to_be_clickable((By.TAG_NAME, 'tspan')))
           for i in ele:
              if i.text == 'Your guarantee':
                     i.click()
                     break
           time.sleep(2) 
           d.find_element_by_id('id_payment_guarantee_1').click()
           time.sleep(1)
           d.find_element_by_name('continue').click()
           
           time.sleep(5)
           
           
       
if __name__ == '__main__':
       unittest.main()