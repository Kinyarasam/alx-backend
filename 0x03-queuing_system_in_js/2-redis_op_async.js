#!/usr/bin/env node
/**
 * @module 0-redis_client.
 */
import { createClient, print } from 'redis';
import { promisify } from 'util';

// Instantiate a redis client Object.
const client = createClient();

// Capture an error event and log an error message to console.
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`)
});

// Log connection success to the console.
client.on('ready', async () => {
  console.log(`Redis client connected to the server`);
  await run()
});

/**
 * Save a key value in a redis instance
 * @function setNewSchool
 * @param {string} schoolName - the key to store in
 * @param {string} value - the value to store
 */
const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

/**
 * Log value of passed key to the console.
 * @function displaySchoolValue
 * @param {string} schoolName - the key to get value from
 */
const displaySchoolValue = async (schoolName) => {
    const res = await promisify(client.GET).bind(client)(schoolName);
    console.log(res);
};

const run = async () => {
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
}
