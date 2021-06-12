#Web Scraper

import time
import csv
import importlib
import keys_scraper

from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver

# choose your own URL
# deleting or adding a hashtag before chrome_options will toggle browser view
PATH = "Z:\chromedriver.exe"
url = ("http://www.google.com")

input_data1 =  keys_scraper.input1
input_data2 =  keys_scraper.input2
input_data3 =  keys_scraper.input3
input_data4 =  keys_scraper.input4
input_data5 =  keys_scraper.input5
input_data6 =  keys_scraper.input6
input_data7 =  keys_scraper.input7
input_data8 =  keys_scraper.input8
input_data9 =  keys_scraper.input9
input_data10 =  keys_scraper.input10

chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(PATH, options=chrome_options)
driver.get(url)
time.sleep(1)

# start count where program fails if you have to re run program
count = 0

# start of for loop, begins at item in list that correlates with count
for i in input_data1[count:]:
    try:
        count = count + 1

        #this originally filled a form with zip codes, thus the padding of 0's if

        VariableOne = str(i).zfill(5)
        i = i + 1

        # replace element id with the element id of form entry
        Input_VarOne = driver.find_element_by_id('ContentPlaceHolder1_tZip')

        # clears the form submission
        Input_VarOne.clear()

        # enters the variable and waits x seconds 
        Input_VarOne.send_keys(VariableOne)
        time.sleep(1)

        # replace the x path with xpath of submission button, these lines click the button Then wait X Seconds
        btn_submit = driver.find_element_by_id('ContentPlaceHolder1_btnFind')
        btn_submit.click()
        time.sleep(1)

        # try loop finds inputs from the webpage after the form has been submitted, it then opens a .csv and saves the inputs to a new line in the .csv
        # replace x paths where paths of inputs you are trying to scrape
        #if element has id or name, the program will run faster. use find by xpath as last resort
        try:    
            Data_1 = driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[2]/div/table[2]/tbody/tr[3]/td[1]').text
            Data_2 = driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[2]/div/table[2]/tbody/tr[3]/td[2]').text
            Data_3 = driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[2]/div/table[2]/tbody/tr[3]/td[3]').text
            Data_4 = driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[2]/div/table[2]/tbody/tr[3]/td[4]').text
            Data_5 = driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[2]/div/table[2]/tbody/tr[3]/td[5]').text
            Data_6 = driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[2]/div/table[2]/tbody/tr[3]/td[6]').text
            Data_7 = driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[2]/div/table[2]/tbody/tr[3]/td[7]').text
            Data_8 = driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[2]/div/table[2]/tbody/tr[3]/td[8]').text
            Data_9 = driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[2]/div/table[2]/tbody/tr[3]/td[9]').text
            Data_10 = driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[2]/div/table[2]/tbody/tr[3]/td[10]').text
            Data_11 = driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[2]/div/table[2]/tbody/tr[3]/td[11]').text
            Data_12 = driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[2]/div/table[2]/tbody/tr[3]/td[12]').text

            # choose .csv name
            f = open("‪Something_Something.csv", "a") 
            #set newline on file up before the loop runs
            f.write("\n" + VariableOne + "," + Data_1 + "," + Data_2 + "," + Data_3 + "," + Data_4 + "," + Data_5 + "," + Data_5 + "," + Data_6 + "," + Data_7 + "," + Data_8 + "," + Data_10 + "," + Data_11 + "," + Data_12)
            f.close()

            # Trouble Shooting Print
            # print("exported to CSV")
            # print(VariableOne,Data_1,Data_2,Data_3,Data_4,Data_5,Data_6,Data_7,Data_8,Data_9,Data_10,Data_11,Data_12)

            # rests program for x seconds everytime the count is exactly divisble by n then prints the count
            n = 50
            if count % n == 0:
                time.sleep(30)
                print(count)
            #print(count, VariableOne)

        # skips form entries that are read as invalid
        except NoSuchElementException:
            pass
            print(count, "Error, invalid input", VariableOne)
            f = open("‪Something_Something.csv", "a") #set newline on file up before the loop runs
            f.write("\n" + VariableOne + "," + "No Data")
            f.close()

        # This breaks the program if your connection is refused
        except ConnectionRefusedError:
            driver.quit()
            break 
    # This ends the program after all item in keyscraper have been iterated through   
    except StopIteration:
     break
print(count)


