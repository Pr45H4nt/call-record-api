# Call Record API
This is a Django REST framework application for managing call records.

# Installation
To install and run the application, follow these steps:

Clone the repository:
```
git clone https://github.com/your-username/call-record-api.git
```

Install the dependencies:
```
pip install -r requirements.txt

```

Run the server:
```
python manage.py runserver
```
The API will be available at http://localhost:8000.

# Endpoints
The application implements the following API endpoints:

## /initiate-call (POST)
Creates a new call record.

Payload
```
{
    "from_number": "89XXXX1132",
    "to_number": "62XXXXX232"
}
```
On request to this endpoint, the call details are saved in a database table along with the start_time timestamp.

## /call-report?phone =xxxxxx (GET)
Returns a paginated list of call records where the given number is either the caller's or the receiver's number.
Extra parameter can be given as ?page=x for pagination. Default page is 1

Parameters
phone: The phone number to filter by.
Sample Response
```
{
    "success": true,
    "data": [
        {
            "id": 1,
            "from_number": "97XXX33155",
            "to_number": "97XXX33156",
            "start_time": "2023-02-03T12:55:50.990714"
        },
        {
            "id": 2,
            "from_number": "97XXX33156",
            "to_number": "97XXX33155",
            "start_time": "2023-01-23T15:32:16.780825"
        }
    ]
} 
```
## /call-update/{id} (PUT, PATCH, DELETE)
Updates or deletes a call record.

Parameters
id: The ID of the call record to update or delete.

# Validation
The API endpoints handle request data validation and return error messages accordingly.
Validation includes *phone number should be positive integer and no longer than 15 digits*


