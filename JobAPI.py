from flask import Flask, request, jsonify
import JobSearch
app = Flask(__name__)

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
