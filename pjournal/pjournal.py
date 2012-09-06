#!/usr/bin/python -tt
# pJournal.py - Programming Journal
# Created by Jazzy K - 28-12-2012
# Licensed under the Creative Commons 

import time
import re
import sys
import web # You will need to install web.py from http://webpy.org/
from web import form

urls = (
  '/', 'createWebpage',
  '/new', 'pJournalWeb')

app = web.application(urls, globals(), autoreload=True)
render = web.template.render('templates/')

frm = form.Form(
form.Textbox("title",form.notnull),
form.Textarea("description",form.notnull)
)

class createWebpage:
  def GET(self):
    pjournal = pJournal()
    pjournal.openDict()
    dict1 = sorted(pjournal.journalDictionary.items(), reverse=True)
    return render.index(dict1)

class pJournalWeb:
  def GET(self):
    form = frm()
    return render.pjForm(form)
  
  def POST(self):
    form = frm()
    if not form.validates(): 
      return render.pjForm(form)
    else:
      pjournal = pJournal()
      pjournal.openDict()
      dictSorted = sorted(pjournal.journalDictionary.keys())[-1]
      autonum = int(dictSorted) + 1 # Autonum starts at 1 and is +1 each time it is called, like an autonumber. Key is autonum, value is a list
      f = open("./pjournal.txt", "a+") # Open a file for appending content to the end of
      f.writelines(str(autonum) +  ": [" + str(pjournal.date) + ", '" + str(pjournal.author) + "', '" + str(form['title'].value) + "', '" + str(form['description'].value) + "']\n")
      f.flush()
      f.close()
      raise web.seeother('/')

class pJournal:
# pJournal is an object with properties and methods
# I should be able to:
# > Insert a new entry with function new
# > View all entries in date order (newest first) with function view
# > Search through entries via a keyword with function search
  def __init__(self):
    self.date = time.gmtime()[0:]
    self.author = "Jasdeep HBS Khalsa" # Write your name into here
    self.journalDictionary = {}
        
  def new(self):
    self.openDict()
    dictSorted = sorted(self.journalDictionary.keys())[-1]
    autonum = int(dictSorted) + 1 # Autonum starts at 1 and is +1 each time it is called, like an autonumber. Key is autonum, value is a list
    f = open("pjournal.txt", "a+") # Open a file for appending content to the end of
    title = raw_input("Please enter a title: ")
    description = raw_input("Please enter a description: ")
    f.writelines(str(autonum) +  ": [" + str(self.date) + ", '" + str(self.author) + "', '" + title + "', '" + description + "']\n")
    f.flush()
    f.close()

  def openDict(self):
    f = open("pjournal.txt", "rU") # Open a file for reading content from, universally converting different line breaks to \n
    dictString = f.read()
    dictPattern = re.findall(r"(\d+):\s\[(\(\d+,\s\d+,\s\d+,\s\d+,\s\d+,\s\d+,\s\d+,\s\d+,\s\d+\)),\s[\'\"](.+)[\'\"],\s[\'\"](.+)[\'\"],\s[\'\"](.+)[\"\']\]",dictString)
    for entry in dictPattern:
      self.journalDictionary[int(entry[0])] = [entry[1], entry[2], entry[3], entry[4]] # Write a nested dictionary in format {key:autonum, [value:date, author, title, description]}
    print self.journalDictionary
    f.flush()
    f.close()
    
  def view(self):
    self.openDict()
    for k, v in sorted(self.journalDictionary.items()): # Create a list of dictionary items and sort them with latest post last (as it won't show on screen otherwise)
      print ""
      print ""
      print "Author:", v[1], "Date:", v[0][1:13]
      print "Title:", v[2]
      print v[3]

def main():
  pjournal = pJournal()
  args = sys.argv[:]
  if len(args) > 3:
    print ""
    print "Sorry. Too many arguments :("
    print ""
    print "Format: python pjournal.py 8080 (--view | --dict | --new)"
    sys.exit(1)
  elif len(args) == 3:
    print "3 args are good!"
    option = sys.argv[2]
    if option == '--view':
      pjournal.view()
    if option == '--new':
      pjournal.new()
    if option == '--dict':
      pjournal.openDict()
    elif option != '--view' or '--new' or '--dict':
      print ""
      print "Sorry. That's not a command we know of :("
      print ""
      print "Format: python pjournal.py 8080 (--view | --dict | --new)"
      sys.exit(1)
  elif len(args) == 2:
    print "You running the server on port %s you stud ;)" % (sys.argv[1])
  elif len(args) == 1:
    print "You decided to just run the server :)"

if __name__ == '__main__':
  main()
  app.run()
