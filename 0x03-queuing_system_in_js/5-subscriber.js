import redis from "redis";

const subscriber = redis.createClient();

subscriber
  .on("connect", () => {
    console.log("Redis client connected to the server");
  })
  .on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  });

subscriber.subscribe('holberton school channel');

subscriber.on('message', (channel, message) => {
    console.log(`Received message: ${message}`);
  
if (message === 'KILL_SERVER') {
    subscriber.unsubscribe('holberton school channel');
    subscriber.quit();
    }
});
