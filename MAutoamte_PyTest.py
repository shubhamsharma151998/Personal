# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_test(self):
    self.driver.get("https://webdriveruniversity.com/index.html")
    self.driver.set_window_size(1296, 688)
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, "#dropdown-checkboxes-radiobuttons h1").click()
    self.vars["win1920"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win1920"])
    dropdown = self.driver.find_element(By.ID, "dropdowm-menu-1")
    # dropdown = self.driver.find_element_by_id("dropdown_id")

    # Create a Select object to interact with the dropdown
    select = Select(dropdown)
    sel_value="python"
    # Select by visible text
    select.select_by_value(sel_value)
    assert dropdown.get_attribute("value") == sel_value

    self.driver.find_element(By.XPATH,"(//input[@type=\"checkbox\"])[1]").click()

    all_checkboxes = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")

    checked_checkboxes = [checkbox for checkbox in all_checkboxes if checkbox.is_selected()]
    unchecked_checkboxes = [checkbox for checkbox in all_checkboxes if not checkbox.is_selected()]

    print(f"Checked Checkboxes: {len(checked_checkboxes)}")
    print(f"Unchecked Checkboxes: {len(unchecked_checkboxes)}")

    self.driver.find_element(By.XPATH,"(//input[@type=\"radio\"])[1]").click()

    all_radios =self.driver.find_elements(By.XPATH, "//input[@type='radio']")

    checked_radios = [radio for radio in all_radios if radio.is_selected()]
    unchecked_radios = [radio for radio in all_radios if not radio.is_selected()]

    print(f"Checked Radios: {len(checked_radios)}")
    print(f"Unchecked Radios: {len(unchecked_radios)}")
  
