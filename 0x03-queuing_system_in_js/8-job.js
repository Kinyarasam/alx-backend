#!/usr/bin/env node
/**
 * @module 8-job
 */

/**
 * @function createPushNotificationsJobs
 * @summary Create jobs
 * @param {array} jobs List of job objects
 * @param {kue.Queue} queue A queue instance
 */
export default function createPushNotificationsJobs(jobs, queue) {
  if (Array.isArray(jobs) !== true) {
    throw new Error('Jobs is not an array');
  }
  jobs.forEach((job) => {
    const newJob = queue.create('notification', job);
    newJob.save((err) => {
      // Log error message if job can't be saved
      if (err) console.error(`Notification job ${newJob.id} failed: ${err}`);
    });
    newJob.on('enqueue', () => {
      // Log message if job save was successful
      console.log(`Notification job created: ${newJob.id}`);
    })
      // Log message when job has completed
      .on('complete', () => {
        console.log(`Notificationn job #${newJob.id} completed`);
      })
      // Log the progress of the job
      .on('progress', (progress, _) => {
        console.log(`Notification job #${newJob.id} ${progress}% complete`);
      });
  });
}
