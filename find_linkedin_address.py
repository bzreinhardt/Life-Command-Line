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
import cookielib
import sys
import os
from BeautifulSoup import BeautifulSoup
import webbrowser

#Todo: turn name into query string
#Template for email
# Stick linkedin in name

def find_linkedin(query):
    if len(query) is 2:
        query = query[0]+'+'+query[1]
    query = query.replace(' ','+')
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
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
    print(main_url)
    r = br.open(main_url)
    html = r.read()
    soup = BeautifulSoup(html)
    links = []
    for link in soup.findAll('a'):
        href = link.get('href')
        if type(href) is unicode:
            if 'linkedin' in href:
                    links.append(href)
    start = links[0].find('https')
    stop = links[0].find('&')
    linkedin = links[0][start:stop]
    return linkedin



if __name__ == '__main__':
        name = ' '.join(sys.argv[1:])
        linkedin = find_linkedin(name)
        print(linkedin)
        pyperclip.copy(str(linkedin))

