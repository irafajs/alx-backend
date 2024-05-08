import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    // Create a queue with Kue
    queue = kue.createQueue();
  });

  afterEach(() => {
    // Clear the queue
    queue.testMode.clear();
  });

  it('should throw an error if jobs is not an array', () => {
    // Enter test mode without processing the jobs
    queue.testMode.enter();

    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');

    // Exit test mode
    queue.testMode.exit();
  });
});
