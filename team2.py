import time
import selenium
import matplotlib.pyplot as plt
import matplotlib
from selenium import webdriver


URL = 'http://www.index.go.kr/unify/idx-info.do?idxCd=4205'

driver = webdriver.Chrome(executable_path='C:/Users/pp/Anaconda3/chromedriver.exe')

driver.get(url=URL)
startup_table=driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div[3]/div[2]/div[2]")
startup_table_thead=startup_table.find_element_by_xpath('//*[@id="t_Table_420501"]/thead')

year=[]
for startup_table_thead_tr in startup_table_thead.find_elements_by_css_selector('tr') :
    startup_table_thead_tr_td_list=startup_table_thead_tr.find_elements_by_tag_name("th")
    for startup_table_thead_tr_td in startup_table_thead_tr_td_list :
        year.append(startup_table_thead_tr_td.text)
    print("")
nyear=year[1:14]
print(nyear)

startup_table_tbody=startup_table.find_element_by_xpath('//*[@id="t_Table_420501"]/tbody')

title=[]
for startup_table_tbody_tr in startup_table_tbody.find_elements_by_css_selector('tr') :
    startup_table_tbody_tr_td_list = startup_table_tbody_tr.find_elements_by_tag_name("th")
    for startup_table_tbody_tr_td in startup_table_tbody_tr_td_list :
        title.append(startup_table_tbody_tr_td.text)
    print("")
title1=title[0]
title2=title[1]
print(title1)
print(title2)

text=[]
for startup_table_tbody_tr in startup_table_tbody.find_elements_by_css_selector('tr') :
    startup_table_tbody_tr_td_list=startup_table_tbody_tr.find_elements_by_tag_name("td")
    for startup_table_tbody_tr_td in startup_table_tbody_tr_td_list :
        text.append(startup_table_tbody_tr_td.text)
    print("")

con=text[0:13]
con=[i.replace(',','') for i in con]
con=[int(i) for i in con]
est=text[13:26]
est=[i.replace('.','') for i in est]
est=[int(i) for i in est]
est=[float(i)/10 for i in est]
print(con)
print(est)
time.sleep(3)

matplotlib.rcParams['axes.unicode_minus']=False
plt.rc('font',family='Malgun Gothic')

plt.suptitle('연도별 총활동기업수와 창업률')
x=nyear
plt.plot(x,con,color='mediumturquoise')
plt.plot(x,est,color='mediumpurple')
plt.xlabel('년도')
plt.legend([title1,title2])
plt.show()

driver.close()