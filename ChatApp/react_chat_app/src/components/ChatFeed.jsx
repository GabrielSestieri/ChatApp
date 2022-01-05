import MyMessage from './MyMessage';
import TheirMessage from './TheirMessage';
import MessageForm from './MessageForm';

const ChatFeed = (props) => {
  console.log("we here");

  

  // if (!chat) return <div />;
  

  return (
    <div className="chat-feed">
      {/* <div className="chat-title-container">
        <div className="chat-title">
          Chat App
        </div>
        <div class="chat-tophead">
          <div className="chat-subtitle">
            by Tuckerman House
          </div>
        </div>
        
      </div> */}
      <div style={{ height: '100px' }}/>
      <div className="message-form-container">
        messages
      </div>
    </div> 
  );
};

export default ChatFeed;