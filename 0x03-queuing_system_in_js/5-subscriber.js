#!/usr/bin/env node
/**
 * @module 5-subscriber
 */
import { createClient } from 'redis';

// Instantiate a redis client
const client = createClient();

// Capture an error event and log an error message to the console.
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Log connection success to the console
client.on('ready', () => {
  console.log('Redis client connected to the server');
});

// Listen on a message event of subscription
client.on('message', (_, msg) => {
  console.log(msg);
  if (msg === 'KILL_SERVER') client.QUIT();
});


// Subscribe to specified channel (pub/sub in effect)
client.subscribe('holberton school channel');
