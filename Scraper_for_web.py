#Web Scraper

import time
import fileinput
import csv
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from keys_scraper.py import  data

# choose your own URL
url = ("www.google.com")

keyscraper =  keys_scraper.inputs
PATH = "Z:\chromedriver.exe"
chrome_options = Options()

# deleting the hashtag before chrome_options will make the browswer window dissapera
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(PATH, options=chrome_options)
driver.get(url)

time.sleep(1)

# start count where program fails if you have to re run program
count = 0


# start of for loop, begins at item in list that correlates with count
for i in keyscraper[count:]:
    try:
        count = count + 1

        #this originally filled a form with zip codes, thus the padding of 0's if len(str(i)) < 5

        VariableOne = str(i).zfill(5)
        i = i + 1

        # replace x path with the xpath of form submission path
        Input_VarOne = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_tZip"]')

        # clears the form submission
        Input_VarOne.clear()

        # enters the variable and waits x seconds 
        Input_VarOne.send_keys(VariableOne)
        time.sleep(1)

        # replace the x path with xpath of submission button, these lines click the button Then wait X Seconds
        btn_submit = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnFind"]')
        btn_submit.click()
        time.sleep(1)

        # try loop finds data from the webpage after the form has been submitted, it then opens a .csv and saves the data to a new line in the .csv
        # replace x paths where paths of data you are trying to scrape
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
            f.write("\n" + VariableOne + "," + Data_One + "," + Data_Two + "," + Data_Three + "," + Data_Four + "," + Data_5 + "," + Data_5 + "," + Data_6 + "," + Data_7 + "," + Data_8 + "," + Data_10 + "," + Data_11 + "," + Data_12)
            f.close()

            # Trouble Shooting Print
            # print("exported to CSV")
            # print(VariableOne,Data_1,Data_2,Data_3,Data_4,Data_5,Data_6,Data_7,Data_8,Data_9,Data_10,Data_11,Data_12)

            # rests program for x seconds everytime the count is exactly divisble by n then prints the count
            n = 90
            if count % n == 0:
                time.sleep(15)
                print(count)
            #print(count, VariableOne)

        # This except skips form entries that are read as invalid
        except NoSuchElementException:
            pass
            print(count, "Error, invalid input", VariableOne)
            f = open("‪Something_Something.csv", "a") #set newline on file up before the loop runs
            f.write("\n" + VariableOne + "," + "No Data")
            f.close()

        # This except breaks the program if your connection is refused
        except ConnectionRefusedError:
            driver.quit()
            break 
    # This Except ends the program after all item in keyscraper have been iterated through   
    except StopIteration:
     break


