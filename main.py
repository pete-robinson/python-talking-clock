import datetime
from flask import Flask, jsonify
from classes.Interpreter import Interpreter

# init flask
app = Flask(__name__)

# define routes - with time and without (without returns current time)
@app.route('/api/clock/', defaults={'time': None})
@app.route('/api/clock/<time>', methods=['GET'])
def fetch_time(time):
    # set the input time to "now" - this will be overwritten if an argument is provided
    input_time = datetime.datetime.now()
    response_code = 200

    try:
        # check for argument, create a datetime object from it
        # if an invalid parameters are provided, it'll throw a ValueError exception
        if time:
            # if time is valid, assign it to input_time variable
            input_time = datetime.datetime.strptime(time, "%H:%M")

        # init and run the interpretter
        interpreter = Interpreter(input_time)
        result = interpreter.run()

        # construct response data
        response = {"status": "OK", "response": result}

    # ValueError exception triggered if input format is incorrect
    except ValueError:
        response_code = 400
        response = {"status": "ERROR", "response": "Invalid time format requested"}

    # TypeError thrown if an error is found in the Interpreter class
    except TypeError as e:
        response_code = 500
        response = {"status": "ERROR", "response": repr(e)}

    # return json response with status code
    return jsonify(response), response_code
