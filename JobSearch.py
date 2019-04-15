
from Job import Job
import IndeedSearch
import webbrowser
import requests
from googlesearch import search
from bs4 import BeautifulSoup


def jobFormat(jobs: list):
    for i in range(len(jobs)):
        jobs[i] = jobs[i].serialize()
    return jobs


def execute(query: str):
    # major = "Computer Science"
    # jobType = "Internship"
    # location = "California"

    # query = "Indeed Computer Science"

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


if __name__ == "__main__":
    print(execute("Computer Science Internship California"))
    # for i in execute("Computer Science Internship California"):
    #     i.display()
