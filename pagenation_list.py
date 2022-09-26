from selenium import webdriver
from selenium.webdriver.common.by import By
from cgitb import text
import json

link = 'https://www.amazon.com'
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)


search = browser.find_element(By.ID, 'twotabsearchtextbox')
search.send_keys('cars')

search_btn = browser.find_element(By.CSS_SELECTOR, '#nav-search-submit-text')
search_btn.click()

page_count = []

for i in range(1, 3):
    page = browser.find_element(By.CSS_SELECTOR, f'.s-pagination-item:nth-child({i})')
    page.click()
    res = browser.find_elements(By.CSS_SELECTOR, '.a-section>.sg-row')
    page_count.append(res)
    
amazon_list = []
for j in range(len(page_count)):
    for i in range(0, 5, 2):
        info_list = {}
        info_list['page'] = j + 1
        info_list['title'] = page_count[j][i].find_element(By.CSS_SELECTOR, '.s-list-col-right>.sg-col-inner>.a-spacing-top-small>.s-title-instructions-style>.s-line-clamp-2').text
        info_list['view'] = page_count[j][i].find_element(By.CSS_SELECTOR, '.s-list-col-right>.sg-col-inner>.a-spacing-top-small>.a-spacing-top-micro>.a-size-small>span:nth-child(2)').text
        info_list['summa'] = page_count[j][i].find_element(By.CSS_SELECTOR, '.s-list-col-right>.sg-col-inner>.a-spacing-top-small>.sg-row>.sg-col-4-of-20>.sg-col-inner>.s-price-instructions-style').text
        amazon_list.append(info_list)


browser.close()   
    
amazon = json.dumps(amazon_list)

amazon_file = open("amazon.json", "w")
amazon_file.write(amazon)
amazon_file.close()   
  
    










