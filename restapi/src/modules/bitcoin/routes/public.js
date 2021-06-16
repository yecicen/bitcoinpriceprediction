const router = require('express').Router();
const publicController = require('../controllers/public');

router.post('/', publicController.create);
router.get('/', publicController.getAll);
router.get('/:id', publicController.getById);

module.exports = router;
