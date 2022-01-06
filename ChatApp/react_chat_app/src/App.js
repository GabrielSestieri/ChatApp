import './App.css';
import React from 'react';
import { useState } from 'react';
import Chatfeed from './components/ChatFeed';
import Home from './components/Home'

import firebase from 'firebase/compat/app';
import 'firebase/compat/firestore';
import 'firebase/compat/auth';

import { useAuthState } from 'react-firebase-hooks/auth';
import { useCollectionData } from 'react-firebase-hooks/firestore';


firebase.initializeApp({
  apiKey: "AIzaSyBad9zRHCMMjFN53OW1tBg-fzNpY6ZjnCM",
  authDomain: "chatapp-e003c.firebaseapp.com",
  projectId: "chatapp-e003c",
  storageBucket: "chatapp-e003c.appspot.com",
  messagingSenderId: "598157875529",
  appId: "1:598157875529:web:a74c3c4fa61a926cc8e298",
  measurementId: "G-3CLSQ7D7R6"
})

const auth = firebase.auth();
const firestore = firebase.firestore();

function App() {

  const [user] = useAuthState(auth);

  return (
    <div className="App">
      <section>
        {user ? <Home /> : <SignIn />}
      </section>
    </div>
  );
}

function SignIn() {
  const signInWithGoogle = () => {
    const provider = new firebase.auth.GoogleAuthProvider();
    auth.signInWithPopup(provider);
  }

  return (
    <div>
      <button onClick={signInWithGoogle}>Sign in with Google</button>
    </div>
  )
}

function SignOut() {
  return auth.currentUser && (
    <button onClick={() => auth.signOut()}>Sign Out</button>
  )
}

function ChatRoom() {

  const messagesRef = firestore.collection('messages');
  const query = messagesRef.orderBy('createdAt').limit(25);
  const [messages] = useCollectionData(query, { idField: 'id' });
  const [formValue, setFormValue] = useState('');
  const sendMessage = async (e) => {
    e.preventDefault();

    const { uid, photoURL } = auth.currentUser;

    await messagesRef.add({
      text: formValue,
      createdAt: firebase.firestore.FieldValue.serverTimestamp(),
      uid,
      photoURL
    });
  }

  return (
    <>
      <div>
        {messages && messages.map(msg => <ChatMessage key={msg.id} message={msg} />)}
      </div>

      <form onSubmit={sendMessage}>
        <input value={formValue} onChange={(e) => setFormValue(e.target.value)} />
        <button type="submit">Send</button>

      </form>
    </>
  )
}

function ChatMessage(props) {
  const { text, uid, photoURL } = props.message;

  const messageClass = uid === auth.currentUser.uid ? 'sent' : 'received'

  return (
    <div className='message ${messageClass}'>
      <img src={photoURL} />
      <p>{text}</p>
    </div>

  )
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
