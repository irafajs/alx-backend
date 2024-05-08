const express = require('express');
const redis = require('redis');
const kue = require('kue');

const { promisify } = require('util');

const app = express();
const port = 1245;

const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

let numberOfAvailableSeats = 50;
let reservationEnabled = true;

const queue = kue.createQueue();

async function reserveSeat(number) {
    await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
    const seats = await getAsync('available_seats');
    return seats ? parseInt(seats) : 0;
}

app.get('/available_seats', (req, res) => {
    res.json({ numberOfAvailableSeats: numberOfAvailableSeats.toString() });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const currentAvailableSeats = await getCurrentAvailableSeats();
  if (currentAvailableSeats > 0) {
    const job = queue.create('reserve_seat').save((error) => {
      if (!error) {
        res.json({ status: 'Reservation in process' });
        numberOfAvailableSeats--;
      } else {
        res.json({ status: 'Reservation failed' });
      }
    });

    job.on('complete', () => {
      console.log(`Seat reservation job ${job.id} completed`);
    });

    job.on('failed', (errorMessage) => {
      console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
    });

    await reserveSeat(currentAvailableSeats - 1);
  } else {
    res.json({ status: 'Not enough seats available' });
  }
});

app.get('/process', async (req, res) => {
    res.json({ status: 'Queue processing' });
});

queue.process('reserve_seat', async (job, done) => {
  const currentAvailableSeats = await getCurrentAvailableSeats();
  if (currentAvailableSeats > 0) {
    await reserveSeat(currentAvailableSeats - 1);
    console.log(`Seat reservation job ${job.id} completed`);
    done();
  } else {
    console.log(`Seat reservation job ${job.id} failed: Not enough seats available`);
    done(new Error('Not enough seats available'));
  }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

