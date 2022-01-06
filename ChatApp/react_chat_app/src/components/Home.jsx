import React from 'react'
import ChatFeed from './ChatFeed'
import '../home.css'
import '../chatfeed.css';
import FriendBox from './FriendBox'
import Rooms from './Rooms'
import { useState, useRef, useEffect } from 'react';
import firebase from 'firebase/compat/app';
import 'firebase/compat/firestore';
import 'firebase/compat/auth';

import { useAuthState } from 'react-firebase-hooks/auth';
import { useCollectionData } from 'react-firebase-hooks/firestore';


const Home = (prop) => {

    const auth = firebase.auth();
    const firestore = firebase.firestore();

    function ChatRoom() {
        const webhook = useRef();
        const messagesRef = firestore.collection('messages');
        const query = messagesRef.orderBy('createdAt');
        const [messages] = useCollectionData(query, { idField: 'id' });
        const [formValue, setFormValue] = useState('');

        useEffect(() => {
            if (webhook.current) {
                scrollToBottom();
            }
        })

        const sendMessage = async (e) => {
            e.preventDefault();

            const { uid, photoURL } = auth.currentUser;

            await messagesRef.add({
                text: formValue,
                createdAt: firebase.firestore.FieldValue.serverTimestamp(),
                uid,
                photoURL
            })

            setFormValue('');
            webhook.current.scrollIntoView({ behavior: 'smooth' });
        }

        const scrollToBottom = () => {
            webhook.current.scrollIntoView({ behavior: 'smooth' });
        }

        return (
            <>
                <main>
                    {messages && messages.map(msg => <ChatMessage key={msg.id} message={msg} />)}
                    <span ref={webhook}></span>
                </main>
                <form onSubmit={sendMessage}>
                    <input value={formValue} placeholder='Send a message...' onChange={(e) => setFormValue(e.target.value)} />
                    <button type="submit" disabled={!formValue}>Send</button>
                </form>
            </>
        )
    }

    function ChatMessage(props) {
        const { text, uid, photoURL } = props.message;
        const messageClass = uid === auth.currentUser.uid ? 'sent' : 'received';
        return (<>
            <div className={`message ${messageClass}`}>
                <img src={photoURL} />
                <p>{text}</p>
            </div>

        </>)

    }

    const [currentScreen, setCurrentScreen] = useState(1);

    const GetScreen = () => {
        if (currentScreen == 1) {
            return <Rooms />
        }
        else if (currentScreen == 2) {
            return <ChatRoom />
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
