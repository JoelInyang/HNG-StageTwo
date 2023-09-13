Person API Documentation


The Person API allows you to manage records of individuals, including their name, age, and address. This API supports basic CRUD (Create, Read, Update, Delete) operations on person records.

API Base URL

The base URL for the Person API is: https://yourdomain.com/api/persons/

1. Create a New Person
Endpoint: POST /api/persons/
Description: Create a new person record.
Request Format:
JSON Body:

{
  "name": "Linda Tom",
  "age": 30,
  "address": "34 light Str"
}


Response Format:
Status Code: 201 (Created)
JSON Body (Response):
{
  "id": 1,
  "name": "Linda Tom",
  "age": 30,
  "address": "34 light Str"
}




2. Retrieve a Person
Endpoint: GET /api/person/1/  #where 1 is the person_id
Description: Retrieve details of a person by their unique ID.
Request Format: No request body required.
Response Format:
Status Code: 200 (OK)
JSON Body (Response):
{
  "id": 1,
  "name": "Linda Tom",
  "age": 30,
  "address": "34 light Str"
}


3. Update a Person
Endpoint: PUT /api/person/1/  #where 1 is the person_id
Description: Modify details of an existing person by their unique ID.

Request Format:
JSON Body (Request):
{
  "name": "Jane Smith",
  "age": 35,
  "address": "456 Elm St"
}


Response Format:
Status Code: 200 (OK)
JSON Body (Response):
{
  "id": 1,
  "name": "Jane Smith",
  "age": 35,
  "address": "456 Elm St"
}


4. Delete a Person
Endpoint: DELETE /api/person/1/ #where 1 is the person_id
Description: Remove a person record by their unique ID.
Request Format: No request body required.
Response Format:
Status Code: 204 (No Content)



Dynamic Parameter Handling

The API allows dynamic parameter handling for filtering by name. You can use the name query parameter to filter results by name.

Example:

Retrieve all persons with the name "Linda Tim":
GET /api/person/?name=Linda%20Tim









Sample Usage
Here are some sample API requests and responses:
1. Create a new person:

Request:

POST /api/persons/
Content-Type: application/json

{
  "name": "Jane Smith",
  "age": 35,
  "address": "456 Elm St"
}

Response:

{
  "id": 2,
  "name": "Jane Smith",
  "age": 35,
  "address": "456 Elm St"
}


2. Retrieve a person by ID:

Request:

GET /api/person/2/

Response:

{
  "id": 2,
  "name": "Alice Johnson",
  "age": 25,
  "address": "789 Oak Ave"
}


3. Update a person's details:

Request:

PUT /api/person/2/
Content-Type: application/json

{
  "name": "Alice Smith",
  "age": 26,
  "address": "789 Oak Ave, Apt 2"
}
Response:

{
  "id": 2,
  "name": "Alice Smith",
  "age": 26,
  "address": "789 Oak Ave, Apt 2"
}

4. Delete a person:

Request:

DELETE /api/person/2/
Response: No content (Status Code: 204)


Notes
- Ensure that valid JSON data is sent in the request body for create and update operations.
- The API supports dynamic filtering by name using the name query parameter.