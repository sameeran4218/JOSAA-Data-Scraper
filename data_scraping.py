#the neccessary imports
import logging_in
import re
import pandas as pd
from bs4 import BeautifulSoup

#creating an onject of BeautifulSoup
soup=BeautifulSoup(logging_in.html_content, 'lxml')

# extract the branch names
branch_id1='ctl00_ContentPlaceHolder1_GridView1_ctl'
branch_id2='_lblBranch'
branches=[]
for i in range(2,25):

        if i<10:
            branch_number = '0'+str(i)
            branch_id = branch_id1 + branch_number + branch_id2
            branch = soup.find('span', id=branch_id)
            cleaned_branch_text = re.sub(r"[\"']", "", branch.text)
            branches.append(cleaned_branch_text)
        else:
            branch_number = str(i)
            branch_id = branch_id1 + branch_number + branch_id2
            branch = soup.find('span', id=branch_id)
            cleaned_branch_text = re.sub(r"[\"']", "", branch.text)
            branches.append(cleaned_branch_text)

# extract the opening ranks
OR_id1='ctl00_ContentPlaceHolder1_GridView1_ctl'
OR_id2='_lblOpenRank'
opening_ranks=[]
for i in range(2,25):

        if i<10:
            or_id = '0'+str(i)
            opening_rank_id = OR_id1 + or_id + OR_id2
            OR = soup.find('span', id=opening_rank_id)
            opening_ranks.append(OR.text)
        else:
            or_id = str(i)
            opening_rank_id = OR_id1 + or_id + OR_id2
            OR = soup.find('span', id=opening_rank_id)
            opening_ranks.append(OR.text)

# extract the closing ranks
CR_id1='ctl00_ContentPlaceHolder1_GridView1_ctl'
CR_id2='_lblCloseRank'
closing_ranks=[]
for i in range(2,25):

        if i<10:
            cr_id = '0'+str(i)
            closing_rank_id = CR_id1 + cr_id + CR_id2
            CR = soup.find('span', id=closing_rank_id)
            closing_ranks.append(CR.text)
        else:
            cr_id = str(i)
            closing_rank_id = CR_id1 + cr_id + CR_id2
            CR = soup.find('span', id=closing_rank_id)
            closing_ranks.append(CR.text)

# extract the gender
gender_id1='ctl00_ContentPlaceHolder1_GridView1_ctl'
gender_id2='_lblGender'
genders=[]
for i in range(2, 25):

    if i < 10:
        gr_id = '0' + str(i)
        gender_id = gender_id1 + gr_id + gender_id2
        gender = soup.find('span', id=gender_id)
        genders.append(gender.text)
    else:
        gr_id = str(i)
        gender_id = gender_id1 + gr_id + gender_id2
        gender = soup.find('span', id=gender_id)
        genders.append(gender.text)

#create a dataframe with the lists(of extracted data ) as columns
df=pd.DataFrame(list(zip(branches, genders, opening_ranks,closing_ranks)),
         columns=['Academic Program','Gender', 'Opening Rank','Closing Rank'])

# saving the data to csv file
df.to_csv(path_or_buf=logging_in.year+'-'+logging_in.round+'.csv')
