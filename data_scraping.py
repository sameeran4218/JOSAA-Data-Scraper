#the neccessary imports
import logging_in
import re
import pandas as pd
from bs4 import BeautifulSoup

#creating an onject of BeautifulSoup
soup=BeautifulSoup(logging_in.html_content, 'lxml')

#create lists to store the values
round_no=[]
year=[]
institutes=[]
branches=[]
genders=[]
quotas=[]
categories=[]
opening_ranks=[]
closing_ranks=[]

#find the table element containing all the values
table=soup.find('div',class_='table-responsive')
table_row=table.find_all_next('tr')

#append the values to their respective lists
for tr in table_row:
    info=tr.find_all_next('td')
    institutes.append(info[0].text)
    branches.append(info[1].text)
    quotas.append(info[2].text)
    categories.append(info[3].text)
    genders.append(info[4].text)
    opening_ranks.append(info[5].text)
    closing_ranks.append(info[6].text)

#for explicitly adding round and year to the data frame
for i in range(len(institutes)):
    round_no.append(logging_in.round)
    year.append(logging_in.year)

#create a dataframe with the lists(of extracted data ) as columns
df=pd.DataFrame(list(zip(year,round_no,institutes,branches,quotas,categories, genders, opening_ranks,closing_ranks)),
         columns=['Year','Round','Institutes','Academic Program','Quota','Seat Type','Gender', 'Opening Rank','Closing Rank'])



# saving the data to csv file
df.to_csv(path_or_buf=logging_in.year+'-'+logging_in.institute_type_entered+'-'+logging_in.round+'.csv')
