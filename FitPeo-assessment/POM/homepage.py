from Library.libraries import Base


class HomePage(Base):
    providers_link_locator = ("xpath", "//a[@href='/providers']")
    chronic_care_link_locator = ("xpath", "//a[@href='/chronic-care']")
    medical_kit_link_locator = ("xpath", "//a[@href='/medical-kit']")
    cpt_code_link_locator = ("xpath", "//a[@href='/cpt-codes']")
    revenue_calc_link_locator = ("xpath", "//a[@href='/revenue-calculator']")

    def click_on_providers_link(self):
        self.click_on_element(self.providers_link_locator)

    def click_on_chronic_care_link(self):
        self.click_on_element(self.chronic_care_link_locator)

    def click_on_medical_kit_link(self):
        self.click_on_element(self.medical_kit_link_locator)

    def click_on_cpt_code_link(self):
        self.click_on_element(self.cpt_code_link_locator)

    def click_on_revenue_calc_link(self):
        self.click_on_element(self.revenue_calc_link_locator)

