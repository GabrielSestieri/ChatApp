import React from 'react'
import ChatFeed from './ChatFeed'
import '../home.css'
import FriendBox from './FriendBox'
import Rooms from './Rooms'

const Home = (prop) => {

    return (
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
            <div className="container">
                <Rooms />
                <ChatFeed />
                <FriendBox />
            </div>
        </div>
    )
}

export default Home;
