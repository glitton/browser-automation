from selenium import webdriver
browser = webdriver.Chrome()

# Get the page you'd like to open
browser.get("https://www.google.com")
# Find the css for the search bar
search = browser.find_element_by_css_selector("input[name='q']")
# Input the search term
search.send_keys("python automation with selenium")
# Press Google Search key
search_btn = browser.find_element_by_css_selector("input[name='btnK']")
search_btn.click()
