"use strict";

var express = require('express');

var axios = require('axios');

var app = express();
var PORT = 3000; // Choose any available port number
// Define routes

app.get('/', function (req, res) {
  res.send('Welcome to the Food Ordering App!');
}); // Endpoint to get restaurants

app.get('/restaurants', function _callee(req, res) {
  var response;
  return regeneratorRuntime.async(function _callee$(_context) {
    while (1) {
      switch (_context.prev = _context.next) {
        case 0:
          _context.prev = 0;
          _context.next = 3;
          return regeneratorRuntime.awrap(axios.get('https://api.talabat.com/api/v1/restaurant', {
            params: {
              latitude: req.query.latitude,
              longitude: req.query.longitude
            }
          }));

        case 3:
          response = _context.sent;
          res.json(response.data);
          _context.next = 11;
          break;

        case 7:
          _context.prev = 7;
          _context.t0 = _context["catch"](0);
          console.error('Error fetching restaurants:', _context.t0);
          res.status(500).json({
            error: 'Failed to fetch restaurants'
          });

        case 11:
        case "end":
          return _context.stop();
      }
    }
  }, null, null, [[0, 7]]);
}); // Endpoint to place an order

app.post('/orders', function _callee2(req, res) {
  return regeneratorRuntime.async(function _callee2$(_context2) {
    while (1) {
      switch (_context2.prev = _context2.next) {
        case 0:
          try {
            // Your order placement logic using Talabat API
            // Make POST request to https://api.talabat.com/api/v1/orders with the necessary data
            res.send('Order placed successfully!');
          } catch (error) {
            console.error('Error placing order:', error);
            res.status(500).json({
              error: 'Failed to place order'
            });
          }

        case 1:
        case "end":
          return _context2.stop();
      }
    }
  });
}); // Start the server

app.listen(PORT, function () {
  console.log("Server is running on http://localhost:".concat(PORT));
});