from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://techstepacademy.com/training-ground")

input2_css_locator = "input[id='ipt2']"
button4_xpath_locator = "//button[@id='b4']"

# Assign elements
input2 = browser.find_element_by_css_selector(input2_css_locator)
button4 = browser.find_element_by_xpath(button4_xpath_locator)

# Manipulate elements
input2.send_keys("Test text")
button4 .click
browser.quit()
