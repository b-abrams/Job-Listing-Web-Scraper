
from Job import Job
from multiprocessing import Pool, Manager
import webbrowser
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://indeed.com"
jobList = Manager().list()
jobLinks = Manager().list()


def getPaginationHref(soup):
    href = soup.find('div', class_="pagination").find("a").get('href')
    return href[0:(len(href) - 2)]


def scrapeJobLinks(soup):
    for href in (soup.findAll('a', {'class': ['jobtitle', 'turnstileLink']})):
        if(("clk?" in href.get('href')) or ("company" in href.get('href'))):
            jobLinks.append(BASE_URL + href.get('href'))


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
