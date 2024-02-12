# Task 2 : OPTIMAL JOB INTERVIEW SCHEDULING

This project was built and tested with Python version 3.10

## Dependencies

- Flask 3.0.2  
For installation run (within the activated environment):
```
pip install Flask
```

## Running the project

Run the project with following command (from project root path):
```
flask --app main run
```

## Testing

Send POST request to following endpoint: `http://127.0.0.1:5000`  
Provide input data to the request body. Example:
```
{
  "start_times": [10, 20, 30, 40, 50, 60],
  "end_times": [15, 25, 35, 45, 55, 65]
}
```

Response is in JSON format containing max number of interviews a person can attend with status code 200 OK or 400 Bad Request in case of invalid input.  
Example response:
```
{
  "max_interviews : 6
}
```
