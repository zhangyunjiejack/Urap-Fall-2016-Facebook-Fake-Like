import csv 
import array
import os
import pandas as pd



file1 = pd.read_csv("people_combined_friends_like_20160916.csv")
file2 = pd.read_csv("profile_html_EXCEL_split_horizontal.csv")

#with open("people_combined_friends_like_20160916.csv", "r") as file_in:
#    with open("people_combined_friends_like_20160916.csv", "w") as file_out:
#        writer = csv.writer(file_out)
#        for row in csv.reader(file_in):
#            writer.writerow(row[:2] + row[3:])

result = file2.merge(file1, on = 'id')
result.to_csv('merged.csv', index = False)