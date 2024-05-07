import redis from 'redis';
import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

const hashValue = {
  Portland:  50,
  Seattle:  80,
  'New York':  20,
  Bogota: 20,
  Cali: 40,
  Paris:2,
};

const keys = Object.keys(hashValue);
keys.forEach((key) => {
  client.hset('HolbertonSchools', key, hashValue[key], (error, reply) => {
    if (error) {
      console.error(error);
    } else {
      console.log(`Reply: ${reply}`);
    }
  });
});

client.hgetall('HolbertonSchools', (error, reply) => {
  if (error) {
    console.error(error);
  } else {
    console.log(reply);
  }
});
