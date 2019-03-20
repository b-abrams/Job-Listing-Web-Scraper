class IndeedJob:
    def __init__(self, jobTitle: str, company: str, jobType: str, jobDescriptiton: str,  link: str):
        self.jobTitle = jobTitle
        self.company = company
        self.jobType = jobType
        self.jobDescription = jobDescriptiton
        self.link = link

    def getJobTitle(self):
        return self.jobTitle.encode('utf-8')

    def getCompany(self):
        return self.company.encode('utf-8')

    def getJobType(self):
        return self.jobType.encode('utf-8')

    def getJobDescription(self):
        return self.jobDescription.encode('utf-8')

    def getLink(self):
        return self.link.encode('utf-8')

    def display(self):
        return (self.jobTitle + "\n\n").encode('utf-8') + (self.company + "\n\n").encode('utf-8') + (self.jobType + "\n\n").encode('utf-8') + (self.jobDescription + "\n\n").encode('utf-8') + self.link.encode('utf-8')
