import kue from 'kue'

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '073364646',
  message: 'Mobile number'
};

const job = queue.create('push_notification_code', jobData)
.save((error) => {
  if (!error) {
    console.log(`Notification Job created: ${job.id}`);
  } else {
    console.error('Failed to create notification job:', error);
  }
});
