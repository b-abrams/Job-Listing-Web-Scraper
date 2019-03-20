from IndeedJob import IndeedJob
import webbrowser
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://indeed.com"
jobList = []
jobLinks = []


def getPaginationHref(soup):
    href = soup.find('div', class_="pagination").find("a").get('href')
    return href[0:(len(href) - 2)]


def scrapeJobLinks(soup):
    for href in (soup.findAll('a', {'class': ['jobtitle', 'turnstileLink']})):
        if(("clk?" in href.get('href')) or ("company" in href.get('href'))):
            jobLinks.append(BASE_URL + href.get('href'))


def convertToIndeedJob():
    for link in jobLinks:

        print(link)
        jobSoup = BeautifulSoup(requests.get(link,
                                             headers={'user-agent': 'Chrome/63.0.3239.132'}).content, 'lxml')
        if((jobSoup.find(
                'div', class_="icl-u-lg-mr--sm icl-u-xs-mr--xs"))is None):
            continue

        jobList.append(IndeedJob(jobSoup.find(
            'h3', class_="jobsearch-JobInfoHeader-title").text, jobSoup.find(
            'div', class_="icl-u-lg-mr--sm").text, jobSoup.find(
            'div', class_="jobsearch-JobMetadataHeader-item").text, jobSoup.find(
            'div', class_="jobsearch-JobComponent-description").text, link))


def execute(link):
    req = requests.get(link, headers={
                       'user-agent': 'Chrome/63.0.3239.132'})
    soup = BeautifulSoup(req.content, 'lxml')
    PAGE_CHANGE_HREF = getPaginationHref(soup)
    currentPage = 10
    scrapeJobLinks(soup)
    convertToIndeedJob()
    while(currentPage < 60):
        currentPage += 10
        link = BASE_URL + PAGE_CHANGE_HREF + str(currentPage)
        req = requests.get(BASE_URL + PAGE_CHANGE_HREF,
                           headers={'user-agent': 'Chrome/63.0.3239.132'})
        soup = BeautifulSoup(req.content, 'lxml')
        scrapeJobLinks(soup)
        convertToIndeedJob()
    return jobList
