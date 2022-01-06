import React from 'react'
import ChatFeed from './ChatFeed'
import '../home.css'
import FriendBox from './FriendBox'
import Rooms from './Rooms'

const Home = (prop) => {

    return (
        <div className="chat-title-container">
            <div className="container">
                <Rooms />
                <ChatFeed />
                <FriendBox />
            </div>
        </div>
    )
}

export default Home;
