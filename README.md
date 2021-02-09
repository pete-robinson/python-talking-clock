# Python Clock-to-Text
Returns a human-readable representation of a given time

Contains a simple command and a REST API using Flask as interfaces

## Notes
Built to run on Python 3.7
Contains a loose test package

Could very well use the `inflect` PIP package, but where would the fun be in that?

## Packages
- Flask
- Pytest
- Pytest-cov

## Usage: Command
Ensure command is executable before running.


```
./command.py 13:40
```

Will return a text representation of the input time.

Time argument is optional - if left blank, will return a text representation of the current time

### Errors
Running a command with an invalid parameter such as:

```
./command.py 33:33
```

Will return the response:

```
ERROR: Invalid time requested
```

## Usage: API

### Start Flask
```
flask run
```

The app base URL will run on the URL listed in the response from the Flask run command.

### Requests
#### GET /api/clock/

Will return a human readable representation of the time (British English, i.e. "Quarter to ten" as opposed to "ten forty five")

Successful JSON response:
```json
{
	"time": "Twenty five minutes to one"
}
```

#### POST /api/clock
##### Request payload
The digital time sig that we want converted to text
```json
{
    "time": "11:33"
}
```

##### Response
API returns a human readable representation of the current time:
```json
{
    "time": "11:33"
}
```

#### Errors
An invalid payload structure or a time value that cannot be converted to a timestamp will result in a 400 error.

```
{
	"error": "Invalid time format requested",
}
```
