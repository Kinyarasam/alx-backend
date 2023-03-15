#!/user/bin/env node
/**
 * @module 6-job_creator
 */
import kue from 'kue';

/* Create a kue instance */
const push_notification_code = kue.createQueue({
  name: 'push_notification_node'
});

/* Prepare a job data object */
const jobData = {
  phoneNumber: '123456789',
  message: '#Happy_coding!',
};

/* Create a job from jobData */
const newJob = push_notification_code
  .create('notification', jobData)
  .save((err) => {
    if (err) console.log(err);
    else console.log(`Notification job created: ${newJob.id}`);
  });

/* Log completion message when job completes */
newJob.on('complete', () => {
  console.log('Notification job completed');
});

// Log error message whwn job fails
newJob.on('failed', () => {
  console.log('Notification job failed');
});
