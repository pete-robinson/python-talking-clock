import datetime
from flask import Flask, jsonify, request
from classes.Interpreter import Interpreter
from typing import Union

# init flask
app = Flask(__name__)

# POST request - get time based on a posted value
@app.route('/api/clock/', methods=['POST'])
def fetch_time_from_value():
    # check our value exists
    if "time" not in request.json:
        raise ValueError("Invalid request")

    # marshal input data to a datetime object
    input_time = datetime.datetime.strptime(request.json['time'], "%H:%M")
    str_time = get_time(input_time)

    # send response
    return build_response({"time": str_time}, 200)


# GET request - no time parameter supplied
@app.route('/api/clock/', methods=['GET'])
def current_time():
    # set the input time to "now" and fetch as string
    str_time = get_time(datetime.datetime.now())

    # return response
    return build_response({"time": str_time}, 200)


# centralise the interpret function - accepts a timestamp
def get_time(time: datetime.datetime):
    interpreter = Interpreter(time)
    return interpreter.run()


# build response tuple (data and response code)
def build_response(data: dict, code: int):
    return jsonify(data), code


# handle errors for input values that can't be converted to a timestamp
@app.errorhandler(ValueError)
def invalid_time_error(err: ValueError):
    print(repr(err))
    return build_response({"error": "Invalid time format requested"}, 400)


# handle everything else
@app.errorhandler(TypeError)
@app.errorhandler(Exception)
def unknown_error(err: Union[TypeError, Exception]):
    print(repr(err))
    return build_response({"error": "An unknown error has occurred"}, 500)
