# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET '/questions'
GET '/categories/<category_type/questions'>
DELETE '/questions/<int:question_id>'
POST  '/questions'
POST '/questions/search'
POST '/quizzes'


1. GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs.
- Returns: total of categories
 - command example: curl -X GET  http://127.0.0.1:5000/categories
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sport"
  }, 
  "success": true, 
  "total": 6
}


2. GET '/questions'

-Fetches:
        * a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category;
        *dictionaries of paginated questions  (10 questions per page); 
-Request Arguments: 
            - page: 
            command example:http://127.0.0.1:5000/questions?page=3
- Returns:  An object with  three keys
        *questions: a list of dictionaries that contains up to 10 paginated questions objects per page. Each dictionary contains:
            -int: id: Question id
            -str: question: Question text.
            -int: difficulty: Question difficulty level.
            -int:category: question category id    
        * categories: a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category   
        * int: total_questions: an interger that cointains total of questions per page  
        *bol: success: a boolean that returns true when the request is succeed 
                
command example: http://127.0.0.1:5000/questions

{
  "category": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sport"
  }, 
  "questions": [
    {
      "answer": "Post-it Notes", 
      "category": "2", 
      "difficulty": 3, 
      "id": 1, 
      "question": "What does Pam steal in the first season?"
    }, 
    {
      "answer": "Post-it Notes", 
      "category": "2", 
      "difficulty": 3, 
      "id": 2, 
      "question": "What does Pam steal in the first season?"
    }, 
    {
      "answer": "Michael", 
      "category": "4", 
      "difficulty": 5, 
      "id": 3, 
      "question": "who dates pam s  mother"
    }, 
    {
      "answer": "Philip", 
      "category": "5", 
      "difficulty": 5, 
      "id": 4, 
      "question": "What do Pam and Angela both want to name their babies?"
    }
  ], 
  "success": true, 
  "total_questions": 4
}

3.  GET '/categories/<int:category_id/questions'>

-Fetches:
        * a dictionary of paginated questions that are in the categoty specified in the URL paramenters.
-Request Arguments: 
        * Optional URL queries:
            - page: return a dictionary of paginated questions at a specif page 
            command example:http://127.0.0.1:5000/categories/3/questions?page=3
            -default: 1
- Returns:  An object with  three keys
        *questions: a list of dictionaries that contains up to 10 paginated questions objects per page. Each dictionary contains:
            -int: id: Question id
            -str: question: Question text.
            -int: difficulty: Question difficulty level.
            -int:category: question category id    
        * categories: a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category   
        * int: total_questions: an interger that cointains total questions in db.  
        *bol: success: a boolean that returns true when the request is succeed 
            
command example:curl -X GET  http://127.0.0.1:5000/categories/2/questions

{
  "questions": [
    {
      "answer": "Post-it Notes", 
      "category": "2", 
      "difficulty": 3, 
      "id": 1, 
      "question": "What does Pam steal in the first season?"
    }, 
    {
      "answer": "Post-it Notes", 
      "category": "2", 
      "difficulty": 3, 
      "id": 2, 
      "question": "What does Pam steal in the first season?"
    }
  ], 
  "success": true, 
  "total_questions": 2
}

4. DELETE '/questions/<int:question_id>'

-Deletes the questions correspondent to the id specified in the URL parameters.
-Request Arguments: None
-Returns:
    int: deleted: key that contains the the deleted question id 
    bol: success:  boolean that returns true when the request is succeed 
command example: curl -X DELETE http://localhost:5000/questions/2

    {
    "deleted": 2, 
    "success": true, 
    }


5.POST  '/questions'

- Post a new question
-Request Arguments:
    - Json Object:
        *str: question: contains the question.
        *str: answer : contains the aswer.
        *int: difficulty: contains the level of difficulty from 1 to 5.
        *str: an string that contains the category id.
Returns: 
    * int: created_id: the newly created question id.
    * questions: list of paginated questions.
    * str: question_new: the newly created question.
    * int: total_questions: an interger that cointains total questions in db.  
    *bol: success: a boolean that returns true when the request is succeed 

-Command Example: curl -X POST http://localhost:5000/questions -H "Content-Type: application/json" -d '{ "question": "What is the name?", "answer": "Loo", "difficulty": 2, "category": "1"}'

{ 
  "created_id": 5, 
  "question": [
    {
      "answer": "Post-it Notes", 
      "category": "2", 
      "difficulty": 3, 
      "id": 1, 
      "question": "What does Pam steal in the first season?"
    }, 
    {
      "answer": "Philip", 
      "category": "5", 
      "difficulty": 5, 
      "id": 4, 
      "question": "What do Pam and Angela both want to name their babies?"
    }, 
    {
      "answer": "Loo", 
      "category": "1", 
      "difficulty": 2, 
      "id": 5, 
      "question": "What is the name?"
    }
  ], 
  "question_new": "What is the name?", 
  "success": true, 
  "total_questions": 3
}


6.POST '/questions/search'

- Search for questions that contains a specific searchTerm.
-Request Arguments:
    - JSON object:
    * str: searchTern: string to be pecified in the URL paramenter.
-Returns:
    - returns paginated questions that has the search substring
-Command Example : curl -X POST http://localhost:5000/questions/search -H "Content-Type: application/json" -d '{"searchTerm": "name"}'
{
  "questions": [
    {
      "answer": "Philip", 
      "category": "5", 
      "difficulty": 5, 
      "id": 4, 
      "question": "What do Pam and Angela both want to name their babies?"
    }, 
    {
      "answer": "Loo", 
      "category": "1", 
      "difficulty": 2, 
      "id": 5, 
      "question": "What is the name?"
    }, 
    {
      "answer": "Loo", 
      "category": "1", 
      "difficulty": 2, 
      "id": 6, 
      "question": "What is the name?"
    }, 
    {
      "answer": "Loo", 
      "category": "1", 
      "difficulty": 2, 
      "id": 7, 
      "question": "What is the name?"
    }
  ], 
  "success": true, 
  "total_questions": 5
}

7. POST '/quizzes'

- User get questions to play a quiz game. It will  take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
-Request Arguments:
    * previous_questions: list that contains the ids of the previous questions
    *quiz_category: a dictionary that contains category type and id.
-Returns:
    - returns paginated questions that has the search substring
    - bol: success: a boolean that returns true when the request is succeed     
-Command Example : curl -X POST -H "Content-Type: application/json" -d '{"previous_questions": [2, 6], "quiz_category": {"type": "Entertainment", "id": "5"}}' http://127.0.0.1:5000/quizzes

    {
    "random_question": {
        "answer": "Philip", 
        "category": "5", 
        "difficulty": 5, 
        "id": 4, 
        "question": "What do Pam and Angela both want to name their babies?"
    }, 
    "success": True
    }

```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```