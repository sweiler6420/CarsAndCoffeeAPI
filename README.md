# README

Simple setup and further fastapi documentation follow instruction at 
https://www.youtube.com/watch?v=VSQZl43jFzk

## SETTING UP VIRTUAL ENV IN TERMINAL
1. Open root repo folder

2. Create new virtual environment using below command
```
py -m venv venv
```

## CLONING REPO AND SETUP
1. Create a new virtual environment with Python 3.7.9. Follow above instructions

2. Activate your virtual environment using below command on windows cmd
```
.\venv\Scripts\activate
```
3. Install necessary libraries using supplied requirement.txt file after activating venv
```
pip install -r requirements.txt
```

## PUSHING CHANGES FOR EASY PULLING
1. Verify all updates are working as necessary

2. Cache required libraries for later pulling
```
pip freeze > requirements.txt
```
3. Push changes into bugfix or feature branch

4. Create PR to dev and get code reviewed and merged

5. Create PR from dev to master to get reviewed and merged!

## SETTING UP RAILWAY DB
1. Follow directions in https://www.youtube.com/watch?v=HEV1PWycOuQ

2. Need to update connection settings with new user and password

## CREATING FAST API BASICS
1. Follow video tutorial https://www.youtube.com/watch?v=Lj7ivxUvSog

## Running FASTAPI
1. Run fast api server locally by running 
```
uvicorn cac.api.main:app --reload 
```

## INITIALIZING ALEMBIC 
1. Run alembic initialization command
```
alembic init alembic
```

2. This will create a subfolder called alembic and an alembic.ini file in the root

3. Update connection variable in alembic.ini file (sqlalchemy.url) You can find the connection URL in railway.app

## CREATE ALEMBIC DB MIGRATION
1. Once Alembic has been initialized run command
```
alembic revision -m "init"
```

2. This will create a version folder in alembic with a new version pythong file

3. Open the newest version python file

4. Implement new upgrade and downgrade functions similar to previous versions

5. Now we can run the migration against the railway postgresql database using command 
```
alembic upgrade head
```

6. Final step is to check the db in railway to ensure the migration was successful

## RUN GET REQUEST WITH CURL
1. Run command below and update the ?= value to whatever value you want to try to query
```
curl --request GET "localhost:8000?username=sweiler6420"
```

## FASTAPI SWAGGER DOCS
1. Once the api is running with uvicorn, go to http://localhost:8000/docs
