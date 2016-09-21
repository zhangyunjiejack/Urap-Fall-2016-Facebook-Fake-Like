"""
@author Jiazhen Chen

"""

import sys, os, datetime, glob, random, re
import pandas as pd
import numpy as np

#read file in input dir
filePath = '../input/profile_html_EXCEL.xlsx'
dir = os.path.dirname(__file__)
lst = os.path.relpath(filePath, dir)
df_lst = pd.read_excel(lst, encoding="UTF-8")

df_out = pd.DataFrame(columns=['Name', 'FBurl', 'content', 'like'])
print(df_out)

index = 0
df_lst[['content1']] = df_lst[['content1']].astype('unicode')


#Patterns
PATTERN = '[0-9]+Comments'
pattern = re.compile(PATTERN)


#print list(df_lst.columns.values)
for i, row in df_lst.iterrows():
	current = row[3].encode('UTF-8', 'ignore')
	name = re.sub(r'Add Friend.*', '', current)
	current_clean = re.sub(r'Add Friend.*Request Sent\.', '', current)
	FB = row[2].encode('UTF-8', 'igmnore')

	contentlist = current_clean.split(name)
	for con in contentlist:
		like_num = pattern.findall(con)
		if like_num == []:
			likes = 0
		else:
			likes = re.sub(r"Comments", '', like_num[0])

		row_lst = [name, FB, con, int(likes)]
		df_out.loc[index] = row_lst
		index += 1

df_out.to_csv('../output/profile_html_EXCEL_split.csv', encoding='UTF-8')