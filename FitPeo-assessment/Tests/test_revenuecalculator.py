from time import sleep
from POM.revenuecalcpage import RevenueCalculatorPage

def test_run(driver):
    revenue = RevenueCalculatorPage(driver)
    sleep(2)
    revenue.click_on_revenue_calc_link()
    sleep(2)
    revenue.scroll_to_slider()
    sleep(2)
    revenue.send_text_to_text_box('560')
    assert revenue.check_slider_for_560()
    sleep(2)
    revenue.click_on_check_box_with_heading("CPT-99091")
    sleep(2)
    revenue.click_on_check_box_with_heading("CPT-99453")
    sleep(2)
    revenue.click_on_check_box_with_heading("CPT-99454")
    sleep(2)
    revenue.click_on_check_box_with_heading("CPT-99474")
    sleep(2)
    revenue.send_text_to_text_box('820')
    sleep(2)
    revenue.scroll_to_top()
    sleep(2)
    assert revenue.check_trr("$110700")
    sleep(3)



