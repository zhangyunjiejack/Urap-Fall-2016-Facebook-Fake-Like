from bs4 import BeautifulSoup
import sys, os, datetime, types
import pandas as pd
import re



input_html = 'matthew.melone_home.html'


class Person:
    def __init__(self, id = -1, gender = '', name = '', live_in = '', hometown = '', work = '', num_friends = '', education = ''):
        self.id = id
        self.name = name
        self.gender = gender
        self.live_in = live_in
        self.hometown = hometown
        self.work = work
        self.num_friends = num_friends
        self.education = education
    
    def print_all(self):
        print "id: " + str(self.id)
        print "name: " + str(self.name)
        print "gender: " + str(self.gender)
        print "live in: " + str(self.live_in)
        print "hometown: " + str(self.hometown)
        print "work: " + str(self.work)
        print "number of friends: " + str(self.num_friends)
        print "education: " + str(self.education)


with open(input_html, 'r') as f:
	html = f.read()
content=BeautifulSoup(html, 'html.parser')

texts=content.findAll(text=True)
userName = content.head.contents[0].contents[0]
def visible(element):
	try:
	    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
	        return False
	    elif re.match('<!--.*-->', str(element)):
	        return False
	    return True
	except UnicodeEncodeError:
		pass
visible_texts = filter(visible, texts)

def create_person(texts):
    p = Person()
    for i in range(len(texts)):
        if texts[i] == "Menu":
            p.name = texts[i + 1]
        if texts[i] == "Lives in" or texts[i] == "Current City":
            p.live_in = texts[i + 1]
        if texts[i] == "From" or texts[i] == "Hometown":
            p.hometown = texts[i + 1]
        if texts[i] == "Friends":
            s = str(texts[i + 1])
            p.num_friends = filter(str.isdigit, s)
        if texts[i] == "Gender":
            p.gender = texts[i + 1]
        if texts[i] == "Education" and "Places He's Lived" in  texts:
            # Places Hs's Lived'
            p.education = texts[i + 1]
    return p


            
p = create_person(visible_texts)
p.print_all()
print(visible_texts)
