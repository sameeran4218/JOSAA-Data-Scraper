#the neccessary imports
import time
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver import Keys
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# set up the web driver
service=Service(executable_path="chromedriver.exe")
driver=webdriver.Chrome(service=service)

# take the input from the user
# here we consider user wants to see al the institutes of a given type for specified year and round
# if you want to search for a specific institute,branch or seat type just change 'ALL' to whatever you want
year=input('Enter the year')
round=input('Enter the round number')
institute_type_entered=input('Enter the type of institute')
print("Fetching the data for you")

#navigating to the JOSAA website
driver.get('https://josaa.admissions.nic.in/applicant/seatmatrix/OpeningClosingRankArchieve.aspx')

# make the  dropdown visible first then select

#select the year
driver.execute_script("document.getElementById('ctl00_ContentPlaceHolder1_ddlYear').style.display = 'block';")
year_no=driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_ddlYear')
select_year_no=Select(year_no)
select_year_no.select_by_visible_text(year)

#select the round no
driver.execute_script("document.getElementById('ctl00_ContentPlaceHolder1_ddlroundno').style.display = 'block';")
round_no=driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_ddlroundno')
select_round_no=Select(round_no)
select_round_no.select_by_visible_text(round)



# select the institute type
driver.execute_script("document.getElementById('ctl00_ContentPlaceHolder1_ddlInstype').style.display = 'block';")
institute_type=driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_ddlInstype')
select_institute_type=Select(institute_type)
select_institute_type.select_by_visible_text(institute_type_entered)



#select the institute name
driver.execute_script("document.getElementById('ctl00_ContentPlaceHolder1_ddlInstitute').style.display = 'block';")
institute_name=driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_ddlInstitute')
select_institute_name=Select(institute_name)
select_institute_name.select_by_visible_text('ALL')



#select the academic program
driver.execute_script("document.getElementById('ctl00_ContentPlaceHolder1_ddlBranch').style.display = 'block';")
branch_name=driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_ddlBranch')
select_branch_name=Select(branch_name)
select_branch_name.select_by_visible_text('ALL')



#select the seat type/category
driver.execute_script("document.getElementById('ctl00_ContentPlaceHolder1_ddlSeatType').style.display = 'block';")
seat_type=driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_ddlSeatType')
select_seat_type=Select(seat_type)
select_seat_type.select_by_visible_text('ALL')



#click the submit button
driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_btnSubmit').click()

# transfer the page source to another variable for further use
html_content=driver.page_source

time.sleep(3)
