const { v4: uuidv4 } = require('uuid');
const mongoose = require('mongoose');
const mongooseHidden = require('mongoose-hidden')();

const { Schema } = mongoose;

const bitcoinSchema = new Schema({
  _id: { type: String, default: uuidv4 },
  date: {
    type: String,
    required: true,
  },
  timestamp: {
    type: Number,
    required: false,
  },
  price: {
    type: Number,
    required: true,
  },
  prediction: {
    type: Number,
    required: true,
  },
  volume: {
    type: Number,
    required: false,
  },
  source: {
    type: Number,
    required: false,
  },
}, {
  toObject: {
    virtuals: true,
  },
  toJSON: {
    virtuals: true,
  },
});

// eslint-disable-next-line func-names
bitcoinSchema.virtual('id').get(function () {
  // eslint-disable-next-line no-underscore-dangle
  return this._id;
});

bitcoinSchema.plugin(mongooseHidden);

const Bitcoin = mongoose.model('Bitcoin', bitcoinSchema);

module.exports = Bitcoin;
