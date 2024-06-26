function createPushNotificationJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    if (typeof jobData !== 'object' || jobData === null) {
      console.error(`Invalid job data: ${jobData}`);
      return;
    }

    const job = queue.create('push_notification_code_3', jobData)
      .save((error) => {
        if (!error) {
          console.log(`Notification job created: ${job.id}`);
        } else {
          console.error(`Failed to create notification: ${error}`);
        }
      });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('failed', (error) => {
      console.error(`Notification job ${job.id} failed: ${error}`);
    });

    job.on('progress', (progress) => {
      console.log(`Notification job #${job.id} ${progress}% complete`);
    });
  });
}

export default createPushNotificationJobs;
