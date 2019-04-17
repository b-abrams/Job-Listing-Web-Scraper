
from Job import Job
from multiprocessing import Pool, Manager
import webbrowser
import requests
from bs4 import BeautifulSoup

## Scraping process ## 
"""
1. After a google search from JobSearch.py, an indeed.com link for a 
    given job search query is passed to this file and will be used to 
    conduct scraping.

2. The HTML on the page is parsed using BeautifulSoup

3. Each job listing on the page contains a subdirectory. This is appended to
    the base URL: indeed.com, and added to a list of links to full job postings

4. Repeat Steps 2 and 3 for pages 1-6 for the given indeed query

5. Once all the job links ar in the list, each individual link is accessed

    5a. For each link accessed, the HTML is parsed and a Job class is created to 
            hold specific data members on the page
    5b. Once a Job is created and populated with data, it is added to the jobList

6. The program returns jobList: a list of all the scraped job information.
"""


# Base URL to append job subdirectories to#
BASE_URL = "https://indeed.com"

# List to hold scraped subdirectories
# Subdirectories are appended to the base url before appended to list
jobLinks = Manager().list()

#Once jobs are formatted into a Job class, they are added to this list and returned
jobList = Manager().list()


# Gets the page the scraper is currently on in an indeed.com search for a given query
def getPaginationHref(soup):
    href = soup.find('div', class_="pagination").find("a").get('href')
    return href[0:(len(href) - 2)]

# Scrapes all the subdirectories for jobs on the current page
# Subdirectories are appended to the base url and the entire link is appended to the jobLinks list
def scrapeJobLinks(soup):
    for href in (soup.findAll('a', {'class': ['jobtitle', 'turnstileLink']})):
        if(("clk?" in href.get('href')) or ("company" in href.get('href'))):
            jobLinks.append(BASE_URL + href.get('href'))

# Information on a page is scraped and converted to a job class
def convertToIndeedJob(link):
    jobSoup = BeautifulSoup(requests.get(link,
                                         headers={'user-agent': 'Chrome/63.0.3239.132'}).content, 'lxml')
    try:
        jobList.append(Job(jobSoup.find(
            'h3', class_="jobsearch-JobInfoHeader-title").text, jobSoup.find(
            'div', class_="icl-u-lg-mr--sm").text, jobSoup.find(
            'div', class_="jobsearch-JobMetadataHeader-item").text, jobSoup.find(
            'div', class_="jobsearch-JobComponent-description").text, link))
    except:
        return


def getJobLinks(tuple):
    link = BASE_URL + tuple[0] + str(tuple[1])
    req = requests.get(link,
                       headers={'user-agent': 'Chrome/63.0.3239.132'})
    soup = BeautifulSoup(req.content, 'lxml')
    scrapeJobLinks(soup)

# Executes the web scraping and parses job information as described in 
#   the comment at the top of the file
def execute(link):
    req = requests.get(link, headers={
        'user-agent': 'Chrome/63.0.3239.132'})
    soup = BeautifulSoup(req.content, 'lxml')
    PAGE_CHANGE_HREF = getPaginationHref(soup)
    pages = [(PAGE_CHANGE_HREF, 0), (PAGE_CHANGE_HREF, 10), (PAGE_CHANGE_HREF, 20),
             (PAGE_CHANGE_HREF, 30), (PAGE_CHANGE_HREF, 40), (PAGE_CHANGE_HREF, 50), (PAGE_CHANGE_HREF, 60)]
    p = Pool(10)
    p.map(getJobLinks, pages)
    p.terminate()
    p.join()
    q = Pool(40)
    q.map(convertToIndeedJob, jobLinks)
    q.terminate()
    q.join()

    return jobList
