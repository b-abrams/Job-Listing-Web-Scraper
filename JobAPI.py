from flask import Flask
import JobSearch
app = Flask(__name__)


@app.route("/", methods=["GET"])
def serve():
    jobs = JobSearch.execute("Computer Science Internship California")
    return str(jobs[0])


if __name__ == "__main__":
    app.run()
