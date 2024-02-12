# Task 2 : DETECTING UNAUTHORIZED SALES

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
  "productListings": [{"productID": "123", "authorizedSellerID": "A1"}],
  "salesTransactions": [{"productID": "123", "sellerID": "B2"}]
}
```

Response is in JSON format containing list of unauthorized sales with status code 200 OK or 400 Bad Request in case of invalid input.  
Example response:
```
{
    "unauthorizedSales": [
        {
            "productID": "123",
            "unauthorizedSellerID": [
                "B2"
            ]
        }
    ]
}
```
