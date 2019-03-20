from IndeedJob import IndeedJob
import IndeedSearch
import webbrowser
import requests
from googlesearch import search
from bs4 import BeautifulSoup

major = "Computer Science"
jobType = "Internship"
location = "California"

query = major + " " + jobType + " " + location

indeedLink = ''
glassdoorLink = ''
for x in search(query, tld='com', lang='en', num=10, stop=1, pause=1):
    if(len(indeedLink) > 1 and len(glassdoorLink) > 1):
        break
    if("indeed" in x):
        if(len(indeedLink) > 1):
            continue
        indeedLink = x
    if("glassdoor" in x):
        if(len(glassdoorLink) > 1):
            continue
        glassdoorLink = x

indeed = IndeedSearch.execute(indeedLink)
print(len(indeed))
