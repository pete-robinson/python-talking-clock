#!/usr/bin/env python
import sys
import datetime
from classes.Interpreter import Interpreter

# init input to datetime.now
# this will get overwritten if an argument has been passed
input_time = datetime.datetime.now()

try:
    # check for arguments
    if len(sys.argv) > 1:
        # argument found, create a datetime object from it
        # throws a ValueError if input is invalid
        input_time = datetime.datetime.strptime(sys.argv.pop(), "%H:%M")

    # run the interpreter against the input data
    interpreter = Interpreter(input_time)
    response = interpreter.run()

    # send response
    print(response)

# error management
except ValueError:
    print("ERROR: Invalid time requested")
except TypeError as error:
    print("ERROR:", repr(error))

