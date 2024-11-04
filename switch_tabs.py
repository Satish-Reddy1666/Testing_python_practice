import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/satis/Downloads/drivers/chromedriver-win64/chromedriver.exe")
driver.maximize_window()
driver.get('https://www.selenium.dev/')
driver.switch_to.new_window()
driver.get('https://playwright.dev/')
no_of_tabs = len(driver.window_handles)  #here we are counting the no of tabs are present.
print(no_of_tabs)
tab_values= driver.window_handles  #here we are calling the value of the tabs.
print(tab_values)
current_win_han = driver.current_window_handle # here we are calling the currebt value of the tab.
print(current_win_han)
driver.find_element(By.CSS_SELECTOR, ".getStarted_Sjon").click()
time.sleep(2)

first_tab = driver.window_handles[0]
if current_win_han != first_tab:      # this logic is to fing the current tab and if it is not in 1 tabs by using the current tabs variable it swith to the 1 tab
    driver.switch_to.window(first_tab)
time.sleep(2)
driver.find_element(By.XPATH, "//span[normalize-space()='Downloads']").click()

driver.quit()










