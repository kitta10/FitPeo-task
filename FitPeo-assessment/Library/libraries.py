from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

class Base:
      def __init__(self,driver):
          self.driver=driver
          self.actions=ActionChains(self.driver)

      def search_for_an_element(self, locator):
          element = self.driver.find_element(*locator)
          return element

      def get_text_of_an_element(self, locator):
        return self.search_for_an_element(locator).text

      def click_on_element(self, locator):
          element = self.search_for_an_element(locator)
          element.click()

      def send_text_to_an_element(self, locator, text):
          element = self.search_for_an_element(locator)
          self.actions.click(element).key_down(Keys.CONTROL).send_keys('a').send_keys(Keys.BACKSPACE).key_up(
              Keys.CONTROL).send_keys(text).perform()

      def right_click_on_an_element(self, locators):
          element = self.search_for_an_element(locators)
          self.actions.context_click(element).perform()

      def move_element_by_pixel(self, locator, x, y):
          element = self.search_for_an_element(locator)
          self.actions.click_and_hold(element).move_by_offset(x, y).perform()

      def scroll(self,locator):
          element = self.search_for_an_element(locator)
          self.actions.scroll_to_element(element).perform()

      def wait_for_visibility(self, locator, timeout):
          wait = WebDriverWait(self.driver, timeout)
          condition = visibility_of_element_located(locator)
          element = wait.until(condition)
          return element