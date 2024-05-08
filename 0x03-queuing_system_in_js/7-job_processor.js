import kue from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    let progress = 0;
    const totalSteps = 2;
    const increment = 100 / totalSteps;

    function updateProgress() {
        progress += increment;
        job.progress(Math.min(progress, 100), 100);
    }

    updateProgress();

    if (blacklistedNumbers.includes(phoneNumber)) {
        const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
        console.error(errorMessage);
        done(new Error(errorMessage));
    } else {
        updateProgress();
        
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

        setTimeout(() => {
            updateProgress();
            done();
        }, 1000);
    }
}

const queue = kue.createQueue({ concurrency: 2 });

queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});
