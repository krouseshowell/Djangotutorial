from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

#does this open as a django site
assert 'Django' in browser.title
