import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

# launch Chrome Headless browser
# options = Options()
# options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options = options)
browser = webdriver.Chrome()

start_url = "https://www.motivation-up.com/whats/16type.html"

def scraping():
    browser.get(start_url)
    time.sleep(1)
    btn1 = browser.find_element_by_xpath('//*[@id="form1"]/p[1]/label[1]/input')
    btn2 = browser.find_element_by_xpath('//*[@id="form1"]/p[2]/label[1]/input')
    btn3 = browser.find_element_by_xpath('//*[@id="form1"]/p[3]/label[1]/input')
    btn4 = browser.find_element_by_xpath('//*[@id="form1"]/p[4]/label[1]/input')
    btn5 = browser.find_element_by_xpath('//*[@id="form1"]/p[5]/label[1]/input')
    btn6 = browser.find_element_by_xpath('//*[@id="form1"]/p[6]/label[1]/input')
    btn7 = browser.find_element_by_xpath('//*[@id="form1"]/p[7]/label[1]/input')
    btn8 = browser.find_element_by_xpath('//*[@id="form1"]/p[8]/label[1]/input')
    btn9 = browser.find_element_by_xpath('//*[@id="form1"]/p[9]/label[1]/input')
    btn10 = browser.find_element_by_xpath('//*[@id="form1"]/p[10]/label[1]/input')
    btn11 = browser.find_element_by_xpath('//*[@id="form1"]/p[11]/label[1]/input')
    btn12 = browser.find_element_by_xpath('//*[@id="form1"]/p[12]/label[1]/input')
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
    
    type_name = browser.find_element_by_xpath('//*[@id="main"]/h2[4]').text
    print(type_name)
    print(type_name[0:4])



def scrapin():
    # initialization
    test = ["1"]
    # 大分類
    large_classification_tag = []
    large_classification = []
    # 中分類
    middle_url = []
    middle_classification_tag = []
    middle_classification = []
    # 小分類
    small_url = []
    small_classification_tag = []
    small_classification = []
    small_classification_url = []

    df = pd.DataFrame()

    html = requests.get(start_url)
    soup = BeautifulSoup(html.text, "html.parser")
    elements = soup.find_all("ul", class_ = "listB01")
    # print(rows)
    # get urls
    for large_classification_tag in elements:
        for large_a in large_classification_tag.find_all("a"):
            # print(large_a)
            middle_url.append(base_url + large_a.attrs["href"])
    # print("----------------------")
    # 中分類
    for middle_count in range(len(large_classification_tag)):
        time.sleep(1)
        middle_html = requests.get(middle_url[middle_count])
        soup = BeautifulSoup(middle_html.text, "html.parser")
        middle_elements = soup.find_all("ul", class_= "listB01")
        for middle_classification_tag in middle_elements:
            for middle_a in middle_classification_tag.find_all("a"):
                small_url.append(base_url + middle_a.attrs["href"])
        # print(small_url)
        # 小分類
        for small_count in range(2):
            time.sleep(1)
            small_html = requests.get(small_url[small_count])
            soup = BeautifulSoup(small_html.text, "html.parser")
            small_elements = soup.find_all("ul", class_= "listB01")
    
            for small_classification_tag in small_elements:
                for small_a in small_classification_tag.find_all("a"):
                    large_classification.append(soup.find("h1").string)
                    middle_classification.append(soup.find("p", class_="headingI01").string)
                    small_classification.append(small_a.string)
                    small_classification_url.append(base_url + small_a.attrs["href"])

    print(large_classification)
    print(middle_classification)
    print(small_classification)
    print(small_classification_url)

if __name__ == "__main__":
    scraping()
