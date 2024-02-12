from flask import Flask
from flask import request
from flask import Response

from Services.scheduleService import getMaxNumberOfInterviews

app = Flask(__name__)


@app.route("/", methods=['POST'])
def hello_world():

    try:
        # Read data from request body
        json_data = request.get_json(force=True)

        start_times = json_data["start_times"]
        end_times = json_data["end_times"]

        return getMaxNumberOfInterviews(start_times, end_times)

    except:
        return Response(
            "{}",
            status=400,
        )
