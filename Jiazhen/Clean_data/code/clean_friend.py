"""
@author Jiazhen Chen

"""

import sys, os, datetime, glob, random, re
import pandas as pd
import numpy as np

#read file in input dir
filePath = '../input/profile_friends_excel.xlsx'
dir = os.path.dirname(__file__)
lst = os.path.relpath(filePath, dir)
df_lst = pd.read_excel(lst, encoding="UTF-8")

df_out = pd.DataFrame(columns=['Name', 'FBurl', 'friend', 'num_friend'])
#print(df_out)

index = 0
#df_lst[['content1']] = df_lst[['content1']].astype('unicode')

#print list(df_lst.columns.values)
for i, row in df_lst.iterrows():
	current = row[4].encode('UTF-8', 'ignore')
	
	#clean name
	name = re.sub(r'Add Friend.*', '', current)
	name = re.sub(r'MessageTime', '', name)
	follomessage = 'FollowMessage'
	guideline = 'GUIDELINE'
	aboutfriend = 'lineAboutFriends'
	name = name.split(follomessage, 1)[0]
	name = name.split(guideline, 1)[0]
	name = name.split(aboutfriend, 1)[0]
	name = name.split('\n', 1)[0]
	name = re.sub(r'Follow', '', name)

	print(name)
	FB = row[2].encode('UTF-8', 'igmnore')
	current_clean = re.sub(r'.*Search Friends', '', current)
	print(current_clean)
	break
	current_lst = current_clean.split("Add FriendFriend Request Sent")

	friend_count = 1
	for cur in current_lst:
		if (cur != '') and (cur != name):
			row_lst = [name, FB, cur, friend_count]
			df_out.loc[index] = row_lst
			index += 1
			friend_count += 1
	#if i == 2:
	#break

#df_out.to_csv('../output/profile_friends_excel_split.csv', encoding='UTF-8')