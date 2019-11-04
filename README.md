# Python Clock-to-Text
Returns a human-readable representation of a given time

## Notes:
Built to run on Python 3.7

### Package Installation
#### Flask
To install flask:

```
pip install flask
```

#### PyTest
To install PyTest:

```
pip install pytest
pip install pytest-cov
```


## Usage
### Command
Ensure command is executable:

```
chmod +x command.py
```
To run:

```
./command.py 13:40
```

Time argument is optional.

Will return the input time or current time (human readable).

#### Errors
Running a command with an invalid parameter such as:

```
./command.py 33:33
```

Will return the response:

```
ERROR: Invalid time requested
```

### API
#### Boot up the Flask web server

```
flask run
```

The terminal will show something along the lines of:

```
 * Serving Flask app "app.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

The app is running on the URL listed in the repsonse from Flask.

### Making a request
#### With argument
URL: `http://127.0.0.1:5000/api/clock/12:35`
Will return human-readable representation of the time given.

Successful JSON response:

```
{
	"response": "Twenty five minutes to one",
	"status": "OK"
}
```

#### Without argument
URL: `http://127.0.0.1:5000/api/clock/`
Will return a human readable representation of the current time.

#### Errors
An invalid URL parameter such as: `http://127.0.0.1:5000/api/clock/34:56`

Will return a 400 response code and the content:

```
{
	"response": "Invalid time format requested",
	"status": "ERROR"
}
```
