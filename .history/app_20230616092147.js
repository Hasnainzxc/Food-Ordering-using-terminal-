const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 3000; // Choose any available port number

// Define routes
app.get('/', (req, res) => {
  res.send('Welcome to the Food Ordering App!');
});

// Endpoint to get restaurants
app.get('/restaurants', async (req, res) => {
  try {
    const response = await axios.get('https://api.talabat.com/api/v1/restaurant', {
      params: {
        latitude: req.query.latitude,
        longitude: req.query.longitude
      }
    });

    res.json(response.data);
  } catch (error) {
    console.error('Error fetching restaurants:', error);
    res.status(500).json({ error: 'Failed to fetch restaurants' });
  }
});

// Endpoint to place an order
app.post('/orders', async (req, res) => {
  try {
    // Your order placement logic using Talabat API
    // Make POST request to https://api.talabat.com/api/v1/orders with the necessary data

    res.send('Order placed successfully!');
  } catch (error) {
    console.error('Error placing order:', error);
    res.status(500).json({ error: 'Failed to place order' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
