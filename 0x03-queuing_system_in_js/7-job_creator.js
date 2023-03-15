#!/usr/bin/env node
/**
 * @module 7-job_creator
 */
import { createQueue } from 'kue';

/* Create a jobs array */
const jobs =[
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

/* Create a kue instance */
const push_notification_code = createQueue();

/* Create all jobs */
jobs.forEach((job) => {
  /* Create job */
  const newJob = push_notification_code
    .create('notification', job)
    .save((err) => {
      /* Log error message if job can't be saved */
      if (err) console.error(`Notification job #${newJob.id} failed: ${err}`);
      /* Log message if job save was successful */
      else console.log(`Notification job created: ${newJob.id}`);
    })
    .on('complete', () => {
      /* Log message when job has completed */
      console.log(`Notification job ${newJob.id} completed`);
    })
    /* Log error message when job failed */
    .on('failed', (err) => {
      `Notification job JOB_ID failed: ${err}`
    })
    /* Log Progress of the Job */
    .on('progress', (progress, _) => {
      `Notification job ${newJob.id} ${progress}% complete`
    });
});
