
class Job:

    def __init__(self, jobTitle: str, company: str, jobType: str, jobDescriptiton: str,  link: str):
        self.jobTitle = jobTitle
        self.company = company
        self.jobType = jobType
        self.jobDescription = jobDescriptiton
        self.link = link

    def getJobTitle(self):
        return self.jobTitle

    def getCompany(self):
        return self.company

    def getJobType(self):
        return self.jobType

    def getJobDescription(self):
        return self.jobDescription

    def getLink(self):
        return self.link

    def source(self):
        if("indeed" in self.link):
            return "Indeed"
        if("glassdoor" in self.link):
            return "Glassdoor"

    #Convert Job parameters to dict format for cleaner JSON seerialisation
    def serialize(self):
        return {
            "jobTitle": self.getJobTitle(),
            "company": self.getCompany(),
            "jobType": self.getJobType(),
            "jobDescription": self.getJobDescription(),
            "link": self.getLink(),
            "source": self.source()
        }
