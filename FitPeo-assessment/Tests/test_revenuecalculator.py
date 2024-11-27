from POM.revenuecalcpage import RevenueCalculatorPage

def test_run(driver):
    revenue = RevenueCalculatorPage(driver)
    revenue.click_on_revenue_calc_link()
    revenue.scroll_to_slider()
    revenue.move_knob_to_value("820")
    assert revenue.compare_knob_with_textbox()
    revenue.send_text_to_text_box('560')
    assert revenue.check_slider_for_560()
    revenue.click_on_check_box_with_heading("CPT-99091")
    revenue.click_on_check_box_with_heading("CPT-99453")
    revenue.click_on_check_box_with_heading("CPT-99454")
    revenue.click_on_check_box_with_heading("CPT-99474")
    revenue.send_text_to_text_box('820')
    revenue.scroll_to_top()
    assert revenue.check_trr("$110700")



