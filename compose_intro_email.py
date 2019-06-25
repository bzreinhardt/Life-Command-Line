#!/usr/bin/env python

'''
To use this script install:
pip install pyperclip
(Other things should be in conda)
usage:
python compose_intro_email.py firstname1 lastname1 firstname2 lastname2 
Works best if you use full names not nicknames
Based on: https://gist.github.com/erogol/6658881
Benjamin Reinhardt benjaminreinhardt.com July 2018
The pro move is to add this to your bash_profile
alias intro='python <path>/compose_intro_email.py'
'''
import pyperclip
import json
import pdb
import urllib
import mechanize 
import http.cookiejar
import sys
import os
from bs4 import BeautifulSoup
import webbrowser

#Todo: turn name into query string
#Template for email
# Stick linkedin in name

def find_linkedin(query):
    if type(query) == type([]):
        query.append("linkedin")
        "+".join(query)
    if type(query) == type("string"):
        query += "+linkedin"
    query = query.replace(' ','+')
    br = mechanize.Browser()
    cj = http.cookiejar.LWPCookieJar()
    br.set_cookiejar(cj)
    
    # Browser options
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    
    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    
    # Want debugging messages?
    #br.set_debug_http(True)
    #br.set_debug_redirects(True)
    #br.set_debug_responses(True)
    
    # User-Agent (this is cheating, ok?)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    
    main_url = 'https://www.google.com.tr/search?q='+query
    r = br.open(main_url)
    html = r.read()
    soup = BeautifulSoup(html)
    links = []
    for link in soup.findAll('a'):
        href = link.get('href')
        if type(href) == type("string"):
            if 'www.linkedin' in href:
                    links.append(href)
    start = links[0].find('https')
    stop = links[0].find('&')
    linkedin = links[0][start:stop]
    return linkedin

def create_one_sided_intro(recipient, subject):
    linkedin = find_linkedin(subject)
    template = "%s, please meet %s. She/he is STUFF ABOUT PERSON. \n \n  %s \n"%(recipient.split(' ')[0].title(), subject.split(' ')[0].title(), linkedin)
    return template

def create_two_sided_intro(first_person, second_person):
    template = '%s\n%s\nI\'ll let you two take it from here.\nBest,\nBen'%(create_one_sided_intro(first_person, second_person), create_one_sided_intro(second_person, first_person))
    print("Copying to clipboard:")
    print(template)
    #todo - need to open linkedin profiles to verify
    return template



if __name__ == '__main__':
        names = [sys.argv[1] + " " + sys.argv[2], sys.argv[3] + " " + sys.argv[4]] 
        template = create_two_sided_intro(names[0], names[1])
        pyperclip.copy(str(template))

	
