const Bitcoin = require('@repository/bitcoin');

const create = async (req, res, next) => {
  try {
    const bitcoin = await Bitcoin.create(req.body);
    if (bitcoin) {
      res.send(bitcoin);
    } else {
      res.status(500).send({ msg: 'NOT_CREATED' });
    }
  } catch (error) {
    next(error);
  }
};

const getAll = async (req, res, next) => {
  try {
    const bitcoins = await Bitcoin.find({});
    res.send(bitcoins);
  } catch (error) {
    next(error);
  }
};
const getLastNRecords = async (req, res, next ) => {
  try {
    const bitcoins = await Bitcoin.find({}).sort({"timestamp":-1}).limit(480);
    res.send(bitcoins);
  } catch (error) {
    next(error);
  }
};

const getById = async (req, res, next) => {
  try {
    const bitcoin = await Bitcoin.findOne({ _id: req.params.id });
    if (bitcoin) {
      res.send(bitcoin);
    } else {
      res.status(404).send({ msg: 'NOT_FOUND' });
    }
  } catch (error) {
    next(error);
  }
};

module.exports = {
  create,
  getAll,
  getLastNRecords,
  getById,
};
