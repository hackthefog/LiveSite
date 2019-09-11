import Pusher from 'pusher-js/react-native';

// Enable pusher logging - don't include this in production
Pusher.logToConsole = true;

var pusher = new Pusher('db127c4fb0e8097a2831', {
  cluster: 'us3',
  forceTLS: true
});

var channel = pusher.subscribe('my-channel');
channel.bind('my-event', function(data) {
  alert(JSON.stringify(data));
});