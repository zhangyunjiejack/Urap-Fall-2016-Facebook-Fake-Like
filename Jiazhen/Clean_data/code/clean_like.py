"""
@author Jiazhen Chen

"""

import sys, os, datetime, glob, random, re
import pandas as pd
import numpy as np

#read file in input dir
filePath = '../input/profile_likes_excel.xlsx'
dir = os.path.dirname(__file__)
lst = os.path.relpath(filePath, dir)
df_lst = pd.read_excel(lst, encoding="UTF-8")

df_out = pd.DataFrame(columns=['Name', 'FBurl', 'like_page'])
#print(df_out)

#index = 0
#df_lst[['content1']] = df_lst[['content1']].astype('unicode')


#Patterns
PATTERN = '[0-9]+Comments'
pattern = re.compile(PATTERN)

index = 0
#print list(df_lst.columns.values)
for i, row in df_lst.iterrows():
	current = row[3]
	if type(current) is unicode:
		current = current.encode('UTF-8', 'ignore')
	else:
		current = str(current)

	#cleaning name
	current_clean = re.sub(r'More About.*', '', current)

	name = re.sub(r'Add Friend.*', '', current)
	name = re.sub(r'MessageTime', '', name)
	#name = re.sub(r'FollowMessage.*', '', name)
	follomessage = 'FollowMessage'
	guideline = 'GUIDELINE'
	aboutfriend = 'lineAboutFriends'
	name = re.sub(r'FollowMessage.*', '', name)
	name = re.sub(r'Follow', '', name)
	#name = name.split(follomessage, 1)[0]
	name = name.split(guideline, 1)[0]
	name = name.split(aboutfriend, 1)[0]
	name = name.split('\n', 1)[0]
	print(name)

	FB = row[2].encode('UTF-8', 'igmnore')

	current_clean = re.sub(r'.*LikesAll ', '', current)
	current_clean = re.sub(r'.*a friend request.Request Sent.', '', current_clean)
	current_clean = re.sub(r'More About .*', '', current_clean)
	current_clean = current_clean.split('\n', 1)[0]

	current_lst = current_clean.split("Like")
	for cur in current_lst:
		if cur != '':
			row_lst = [name, FB, cur]
			df_out.loc[index] = row_lst
			index += 1
	#print current_clean
	#if i == 2:
	#break

df_out.to_csv('../output/profile_likes_excel_split.csv', encoding='UTF-8')