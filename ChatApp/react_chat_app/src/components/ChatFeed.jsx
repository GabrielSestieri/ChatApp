import MyMessage from './MyMessage';
import TheirMessage from './TheirMessage';
import MessageForm from './MessageForm';

const ChatFeed = (props) => {
  console.log("we here");



  // if (!chat) return <div />;


  return (
    <div className="msgBox">
      <p>Messages</p>
      <div className="msgCont">
        <form>
          <input type="text" placeholder="Message"></input>
          <button type="submit" >Send</button>
        </form>
      </div>
    </div>
  );
};

export default ChatFeed;