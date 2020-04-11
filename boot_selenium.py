from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://yahoo.org/')
assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')
elem.send_keys('seleniumhq'+Keys.RETURN)

browser.quit()

