from flask import Flask
import JobSearch
app = Flask(__name__)


@app.route("/")
def serve(environ, start_response):
    jobs = list(JobSearch.execute("Computer Science Internship California"))
    return jobs[0]


# if __name__ == "__main__":
#     app.run()
