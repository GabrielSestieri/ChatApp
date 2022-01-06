import './App.css';
import React from 'react';
import Chatfeed from './components/ChatFeed';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  async function getData() {
    console.log("***** PRESSED *****");
    var data = {
      "data": "Example"
    };
    await fetch("http://127.0.0.1:8000/api/index", {
      method: "POST",
      mode: 'cors',
      cache: 'no-cache',
      credentials: 'same-origin',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(
        (result) => {
          console.log(result)
        });

  }
  return (
    <Router>
      <div className="chat-title-container">
        <div className="chat-title">
          Chat App
        </div>
        <div className="chat-tophead">
          <div className="chat-subtitle">
            by Tuckerman House
          </div>
          <div className="chat-nav-links">
            <nav className="nav">
              <a href="/">Chat</a>
              <a href="/">Friends</a>
              <a href="/">Groups</a>
              <a href="/">Logout</a>
            </nav>
          </div>
        </div>

      </div>
      <div className="container">
        <div className="roomBox">
          <p>Rooms</p>
          <div className="roomCont">

          </div>
        </div>
        <Chatfeed />
        <div className="friendBox">
          <p>Friends</p>
          <div className="friendCont">

          </div>
        </div>
      </div>

    </Router>
  );
}

export default App;
