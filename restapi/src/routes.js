const router = require('express').Router();
const bitcoinModule = require('./modules/bitcoin');

router.use('/bitcoin', bitcoinModule.router);

module.exports = router;
