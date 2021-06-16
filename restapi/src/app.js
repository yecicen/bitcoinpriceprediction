require('module-alias/register');
require('dotenv').config();
require('../mongodb'); // Mongodb connection
const cors = require('cors');
const express = require('express');
const bodyParser = require('body-parser');

const routes = require('./routes');

const app = express();

app.use(bodyParser.urlencoded({ extended: false }));

app.use(bodyParser.json());
app.use(cors());
app.use('/api', routes);

app.get('/', (req, res) => {
  res.send('Server is running');
});

app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).send({ msg: 'INTERNAL_SERVER_ERROR' });
});

module.exports = app;
