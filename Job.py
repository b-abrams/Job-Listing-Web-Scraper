
class Job:
    def __init__(self, jobTitle: str, company: str, jobType: str, jobDescriptiton: str,  link: str):
        self.jobTitle = jobTitle
        self.company = company
        self.jobType = jobType
        self.jobDescription = jobDescriptiton
        self.link = link

    def getJobTitle(self):
        return self.jobTitle.encode()

    def getCompany(self):
        return self.company.encode()

    def getJobType(self):
        return self.jobType.encode()

    def getJobDescription(self):
        return self.jobDescription.encode()

    def getLink(self):
        return self.link

    def getSource(self):
        if("indeed" in self.link):
            return "Indeed"
        if("glassdoor" in self.link):
            return "Glassdoor"

    def display(self):
        print(self.getJobTitle(),
              self.getCompany(), self.getJobType(), sep="    ")
