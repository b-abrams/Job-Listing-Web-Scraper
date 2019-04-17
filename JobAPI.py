from flask import Flask, request, jsonify
import JobSearch
app = Flask(__name__)

# Get request. Must take in a parameter 'search' which denotes a job search query. 
# Returns the results of search parameter from JobSearch.py
@app.route("/", methods=["GET"])
def serve():
    req = request.args.get("search")
    jsonList = []
    for _ in list(JobSearch.execute(req)):
        if(_ not in jsonList):
          jsonList.append(_)
    jobs = jsonify(jsonList)
    jobs.headers.add('Access-Control-Allow-Origin', '*')
    return jobs


if __name__ == "__main__":
    app.run()
