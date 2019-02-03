import os
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

# launch Chrome Headless browser
# options = Options()
# options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options = options)

start_url = "https://www.motivation-up.com/whats/16type.html"

def scrape_4096patterns():
    options1 = range(1, 3)
    options2 = range(1, 3)
    options3 = range(1, 3)
    options4 = range(1, 3)
    options5 = range(1, 3)
    options6 = range(1, 3)
    options7 = range(1, 3)
    options8 = range(1, 3)
    options9 = range(1, 3)
    options10 = range(1, 3)
    options11 = range(1, 3)
    options12 = range(1, 3)
    combinations = [(option1, option2, option3, option4, option5, option6, option7, option8, option9, option10, option11, option12)
    for option1 in options1
    for option2 in options2
    for option3 in options3
    for option4 in options4
    for option5 in options5
    for option6 in options6
    for option7 in options7
    for option8 in options8
    for option9 in options9
    for option10 in options10
    for option11 in options11
    for option12 in options12]
    
    num = 1
    df = pd.DataFrame(columns=['type', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12'])

    browser = webdriver.Chrome()
    # 2^12パターンアクセスする
    for option1, option2, option3, option4, option5, option6, option7, option8, option9, option10, option11, option12 in combinations:
        browser.get(start_url)
        print(str(num))
        time.sleep(1)
        element1 = '//*[@id="form1"]/p[1]/label[' + str(option1) + ']/input'
        element2 = '//*[@id="form1"]/p[2]/label[' + str(option2) + ']/input'
        element3 = '//*[@id="form1"]/p[3]/label[' + str(option3) + ']/input'
        element4 = '//*[@id="form1"]/p[4]/label[' + str(option4) + ']/input'
        element5 = '//*[@id="form1"]/p[5]/label[' + str(option5) + ']/input'
        element6 = '//*[@id="form1"]/p[6]/label[' + str(option6) + ']/input'
        element7 = '//*[@id="form1"]/p[7]/label[' + str(option7) + ']/input'
        element8 = '//*[@id="form1"]/p[8]/label[' + str(option8) + ']/input'
        element9 = '//*[@id="form1"]/p[9]/label[' + str(option9) + ']/input'
        element10 = '//*[@id="form1"]/p[10]/label[' + str(option10) + ']/input'
        element11 = '//*[@id="form1"]/p[11]/label[' + str(option11) + ']/input'
        element12 = '//*[@id="form1"]/p[12]/label[' + str(option12) + ']/input'
        btn1 = browser.find_element_by_xpath(element1)
        btn2 = browser.find_element_by_xpath(element2)
        btn3 = browser.find_element_by_xpath(element3)
        btn4 = browser.find_element_by_xpath(element4)
        btn5 = browser.find_element_by_xpath(element5)
        btn6 = browser.find_element_by_xpath(element6)
        btn7 = browser.find_element_by_xpath(element7)
        btn8 = browser.find_element_by_xpath(element8)
        btn9 = browser.find_element_by_xpath(element9)
        btn10 = browser.find_element_by_xpath(element10)
        btn11 = browser.find_element_by_xpath(element11)
        btn12 = browser.find_element_by_xpath(element12)
        btn1.click()
        btn2.click()
        btn3.click()
        btn4.click()
        btn5.click()
        btn6.click()
        btn7.click()
        btn8.click()
        btn9.click()
        btn10.click()
        btn11.click()
        btn12.click()

        browser.find_element_by_class_name('sbt_1').click()
        time.sleep(1)
        type_name = browser.find_element_by_xpath('//*[@id="main"]/h2[4]').text
        
        df.loc[num] = [type_name[0:4], str(option1), str(option2), str(option3), str(option4), str(option5), str(option6), str(option7), str(option8), str(option9), str(option10), str(option11), str(option12)]
        
        num = num + 1
        
        ## For Debug 
        # if option10==2:
        #     break

    df.to_csv('16personalities.csv', index=False, mode='w', encoding='utf-8')
    browser.quit()

def scrape_answers():
    browser = webdriver.Chrome()
    browser.get(start_url)
    
    q1a1 = browser.find_element_by_xpath('//*[@id="form1"]/p[1]/label[1]')
    q2a1 = browser.find_element_by_xpath('//*[@id="form1"]/p[2]/label[1]')
    q3a1 = browser.find_element_by_xpath('//*[@id="form1"]/p[3]/label[1]')
    q4a1 = browser.find_element_by_xpath('//*[@id="form1"]/p[4]/label[1]')
    q5a1 = browser.find_element_by_xpath('//*[@id="form1"]/p[5]/label[1]')
    q6a1 = browser.find_element_by_xpath('//*[@id="form1"]/p[6]/label[1]')
    q7a1 = browser.find_element_by_xpath('//*[@id="form1"]/p[7]/label[1]')
    q8a1 = browser.find_element_by_xpath('//*[@id="form1"]/p[8]/label[1]')
    q9a1 = browser.find_element_by_xpath('//*[@id="form1"]/p[9]/label[1]')
    q10a1 = browser.find_element_by_xpath('//*[@id="form1"]/p[10]/label[1]')
    q11a1 = browser.find_element_by_xpath('//*[@id="form1"]/p[11]/label[1]')
    q12a1 = browser.find_element_by_xpath('//*[@id="form1"]/p[12]/label[1]')

    q1a2 = browser.find_element_by_xpath('//*[@id="form1"]/p[1]/label[2]')
    q2a2 = browser.find_element_by_xpath('//*[@id="form1"]/p[2]/label[2]')
    q3a2 = browser.find_element_by_xpath('//*[@id="form1"]/p[3]/label[2]')
    q4a2 = browser.find_element_by_xpath('//*[@id="form1"]/p[4]/label[2]')
    q5a2 = browser.find_element_by_xpath('//*[@id="form1"]/p[5]/label[2]')
    q6a2 = browser.find_element_by_xpath('//*[@id="form1"]/p[6]/label[2]')
    q7a2 = browser.find_element_by_xpath('//*[@id="form1"]/p[7]/label[2]')
    q8a2 = browser.find_element_by_xpath('//*[@id="form1"]/p[8]/label[2]')
    q9a2 = browser.find_element_by_xpath('//*[@id="form1"]/p[9]/label[2]')
    q10a2 = browser.find_element_by_xpath('//*[@id="form1"]/p[10]/label[2]')
    q11a2 = browser.find_element_by_xpath('//*[@id="form1"]/p[11]/label[2]')
    q12a2 = browser.find_element_by_xpath('//*[@id="form1"]/p[12]/label[2]')
    
    df = pd.DataFrame(columns=['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12'])
    df1 = pd.Series([str(q1a1), str(q2a1), str(q3a1) ,str(q4a1) ,str(q5a1) ,str(q6a1) ,str(q7a1) ,str(q8a1) ,str(q9a1) ,str(q10a1) ,str(q11a1) ,str(q12a1)], index=df.columns)
    df2 = pd.Series([str(q1a2), str(q2a2), str(q3a2) ,str(q4a2) ,str(q5a2) ,str(q6a2) ,str(q7a2) ,str(q8a2) ,str(q9a2) ,str(q10a2) ,str(q11a2) ,str(q12a2)], index=df.columns)
    
    df.append(df1, ignore_index=True)
    df.append(df2, ignore_index=True)
    
    df.to_csv('personalities_Questions_list.csv', index=False, mode='w', encoding='utf-8')
    browser.quit()

if __name__ == "__main__":
    scrape_4096patterns()
    # time.sleep(1)
    # print("------DEBUG-------")
    # scrape_answers()
    print("------FINISH------")
