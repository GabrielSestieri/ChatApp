import './App.css';
import React from 'react';
import Chatfeed from './components/ChatFeed';
import { BrowserRouter as Router } from "react-router-dom";
import firebase from 'firebase/app'

function App() {
  return (
    <Router>
      <div className="chat-title-container">
        <div>

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









// async function getData() {
//   //   console.log("***** PRESSED *****");
//   //   var data = {
//   //     "data": "Example"
//   //   };
//   //   await fetch("http://127.0.0.1:8000/api/index", {
//   //     method: "POST",
//   //     mode: 'cors',
//   //     cache: 'no-cache',
//   //     credentials: 'same-origin',
//   //     headers: {
//   //       'Content-Type': 'application/json',
//   //     },
//   //     body: JSON.stringify(data)
//   //   })
//   //     .then(res => res.json())
//   //     .then(
//   //       (result) => {
//   //         console.log(result)
//   //       });
