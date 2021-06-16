const Bitcoin = require('@repository/bitcoin');

const create = async (req, res, next) => {
  try {
    const bitcoin = await Bitcoin.create(req.body);
    if (bitcoin) {
      // try {
      //   const timeSlot = await Timeslot.findOne(
      //     { _id: req.body.timeslotId },
      //   );
      //   if (timeSlot) {
      //     timeSlot.seats = timeSlot.seats > 0 ? timeSlot.seats - 1 : 0;
      //     await timeSlot.save();
      //   }
      // } catch (e) {
      //   console.error(e);
      // }

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
  getById,
};
