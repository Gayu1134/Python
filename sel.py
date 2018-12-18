#find . -name "*.pyc" -exec rm -f {} \;
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.zippyops.com")
