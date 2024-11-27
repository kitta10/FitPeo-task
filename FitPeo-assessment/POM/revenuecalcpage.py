from FitPeo.POM.homepage import HomePage


class RevenueCalculatorPage(HomePage):
    text_box_locator = ("css selector", "input[type='number']")
    scroll_knob_locator = ("css selector", "input[type='range']")
    check_box_locator = "//p[text()='HEADING']/..//input"
    trr_locator = ("xpath", "//p[contains(text(), 'Recurring Reimbursement ')]/../p[2]")


    def scroll_to_slider(self):
        self.scroll(self.text_box_locator)

    def scroll_to_top(self):
        self.scroll(self.trr_locator)

    def move_knob_to_826(self):
        self.move_element_by_pixel(self.scroll_knob_locator, 94, 0)

    def move_knob_left_until(self, target):
        element = self.search_for_an_element(self.text_box_locator)
        while element.text != target:
            self.move_element_by_pixel(self.scroll_knob_locator, -1, 0)

    def click_on_check_box_with_heading(self, heading):
        xpath_value = self.check_box_locator.replace('HEADING', heading)
        locator = ("xpath", xpath_value)
        self.click_on_element(locator)

    def send_text_to_text_box(self, text):
        self.send_text_to_an_element(self.text_box_locator, text)

    def check_trr(self, text):
        return self.get_text_of_an_element(self.trr_locator) == text

    def check_slider_for_560(self):
        return self.search_for_an_element(self.scroll_knob_locator).get_attribute("value") == "560"



