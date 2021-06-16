const router = require('express').Router();
const privateRoute = require('./routes/private');
const publiceRoute = require('./routes/public');

router.use(privateRoute);
router.use(publiceRoute);

module.exports = {
  router,
};
