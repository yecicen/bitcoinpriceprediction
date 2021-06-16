const router = require('express').Router();
const bookingModule = require('./modules/booking');

router.use('/booking', bookingModule.router);

module.exports = router;
