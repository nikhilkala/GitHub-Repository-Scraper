>  # GitHub-Repository-Scraper
This is a github repository scraper which uses Python to scrape users and store their public profiles in MongoDB. There is also a react webpage to view the data using FastAPI based REST server.

The Python script to scrape github repos is script directory.
It takes user inputs the github usernames and stores the scraped repos for the users.

> **Run:** python main.py

The server contains the files for REST server which has APIs for getting the users in database and repositories for a user in the MongoDB. The APIs are written in FastAPI.

The client contains the react front-end which runs on 3000 port. To run the react app, go to client directory.
> **Run:** npm start

The mongodb is setup and needs the command 
> **Run:** brew services restart mongodb/brew/mongodb-community

This assumes that you have mongodb setup using brew on mac on the port 27017.