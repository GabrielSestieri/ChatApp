import React from 'react'
import ChatFeed from './ChatFeed'
import '../home.css'
import FriendBox from './FriendBox'
import Rooms from './Rooms'
import { useState, useRef, useEffect } from 'react';


const Home = (prop) => {

    const [currentScreen, setCurrentScreen] = useState(1);

    const GetScreen = () => {
        if (currentScreen == 1) {
            return <Rooms />
        }
        else if (currentScreen == 2) {
            return <ChatFeed />
        }
        else {
            return <FriendBox />
        }
    }

    const setScreen = (screenState) => {
        if (screenState == 1) {
            setCurrentScreen(1)
        }
        else if (screenState == 2) {
            setCurrentScreen(2)
        }
        else {
            setCurrentScreen(3)
        }
    }

    const OrderNavs = () => {
        if (currentScreen == 1) {
            return (<div className="newNav">
                <button onClick={function () {
                    setScreen(1);
                }} className="rooms">Rooms</button>
                <button onClick={function () {
                    setScreen(2);
                }} className="chat">Chat</button>
                <button onClick={function () {
                    setScreen(3);
                }} className="friends">Friends</button>
            </div>);
        }
        else if (currentScreen == 2) {
            return (<div className="newNav">

                <button onClick={function () {
                    setScreen(2);
                }} className="chat">Chat</button>
                <button onClick={function () {
                    setScreen(1);
                }} className="rooms">Rooms</button>
                <button onClick={function () {
                    setScreen(3);
                }} className="friends">Friends</button>
            </div>);
        }
        else {
            return (<div className="newNav">
                <button onClick={function () {
                    setScreen(3);
                }} className="friends">Friends</button>
                <button onClick={function () {
                    setScreen(1);
                }} className="rooms">Rooms</button>
                <button onClick={function () {
                    setScreen(2);
                }} className="chat">Chat</button>

            </div>);
        }
    }

    return (
        <div className="chat-title-container">
            <OrderNavs />
            <div className="container">
                <GetScreen />
            </div>
        </div>
    )
}

export default Home;
