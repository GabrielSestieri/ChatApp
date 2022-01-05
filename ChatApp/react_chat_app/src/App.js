import logo from './logo.svg';
import './App.css';
import React from 'react';
import  { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import ChatFeed from './components/ChatFeed';
import { ChatApp } from "bootstrap-chat"



function App() {
  // var express = require('express')
  // app = express.createServer();
  // app.get('http://127.0.0.1:8000', function (req, res, next) {
  //   res.header("Acces-Control-Allow-Orgin", "*");
  //   res.header("Acces-Control-Allow-Headers", "X-Requested-With");
  //   next();
  // });
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
      <Routes>
        <Route path='/' element={<ChatFeed />}></Route>
      </Routes>
    </Router>
  );
}

export default App;
