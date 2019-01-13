from selenium import webdriver
browser = webdriver.Chrome()

# Get the page you'd like to open
browser.get("https://www.google.com")
search = browser.find_element_by_css_selector("input[name='q']")
