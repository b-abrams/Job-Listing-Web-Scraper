
from Job import Job
import IndeedSearch
import webbrowser
import requests
from googlesearch import search
from bs4 import BeautifulSoup

#Take jobs retrieved from search and format them as dicts using serialize
def jobFormat(jobs: list):
    serialized = []
    for i in range(len(jobs)):
        serialized.append(jobs[i].serialize())
    return serialized

# Execute a job search using a given querey string
def execute(query: str):
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
    return jobFormat(indeed)

