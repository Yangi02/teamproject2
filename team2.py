import time
import selenium
from selenium import webdriver

URL = 'http://www.index.go.kr/unify/idx-info.do?idxCd=4205'

driver = webdriver.Chrome(executable_path='C:/Anaconda3/chromedriver.exe')

driver.get(url=URL)
startup_table=driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div[3]/div[2]/div[2]")
startup_table_thead=startup_table.find_element_by_xpath('//*[@id="t_Table_420501"]/thead')

for startup_table_thead_tr in startup_table_thead.find_elements_by_css_selector('tr') :
    startup_table_thead_tr_td_list=startup_table_thead_tr.find_elements_by_tag_name("th")
    for startup_table_thead_tr_td in startup_table_thead_tr_td_list :
        print("\t",startup_table_thead_tr_td.text, end="\t \t")
    print("")
