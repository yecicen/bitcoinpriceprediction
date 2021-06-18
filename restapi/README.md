
---

A Node.js app using [Express library](http://expressjs.com/).

## Cloning Locally and installing packages

Make sure you have [Node.js](http://nodejs.org/) and the [Heroku Toolbelt](https://toolbelt.heroku.com/) installed.

```sh
npm install
```
## Configuring
Create a copy of .env.example as .env

```
cp .env.example .env
```
Edit the .env file for your configuration
## Running applicatication
```
npm start
```
Your app should now be running on [localhost:8000](http://localhost:8000/).

## Deploying to Heroku

```
heroku create
git push heroku master
heroku open
```

Alternatively, you can deploy your own copy of the app using the web-based flow:

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)