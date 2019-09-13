import React from 'react';
import logo from './logo.svg';
import './App.css';
//import Pusher from 'pusher-js/react-native';

// Enable pusher logging - don't include this in production
//Pusher.logToConsole = true;

//var pusher = new Pusher(##PUSHER KEY##, {
//  cluster: ##PUSHER CLUSTER##,
//  forceTLS: true
//});

//var channel = pusher.subscribe('my-channel');
//channel.bind('my-event', function(data) {
//  alert(JSON.stringify(data));
//});

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
