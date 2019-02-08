import os
import pandas as pd
from bs4 import BeautifulSoup


def scraping():
    current_dir = os.getcwd()
    print(current_dir)
    os.chdir(current_dir + "/htmls")
    print(os.getcwd())

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

    df = pd.DataFrame(columns=['num','type', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12'])

    for option1, option2, option3, option4, option5, option6, option7, option8, option9, option10, option11, option12 in combinations:
        binary_number = "0b" + str(option1-1) + str(option2-1) + str(option3-1) + str(option4-1) + str(option5-1) + str(option6-1) + str(option7-1) + str(option8-1) + str(option9-1)+ str(option10-1) + str(option11-1) + str(option12-1)
        oct_num = str(int(binary_number, 2) + 1)
        print("Scrape " + oct_num + ".html")
        soup = BeautifulSoup(open(oct_num + ".html"), "html.parser")
        type_name = soup.h1.string
        df.loc[int(oct_num)] = [int(oct_num), type_name[10:14], str(option1), str(option2), str(option3), str(option4), str(option5), str(option6), str(option7), str(option8), str(option9), str(option10), str(option11), str(option12)]
        
        ## For debug
        #if oct_num == "300":
        #    break   

    df.to_csv('16personalities.csv', index=False, mode='w', encoding='utf-8')



if __name__ == "__main__":
    scraping()
    print("------FINISH------")
