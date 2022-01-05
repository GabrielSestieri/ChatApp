import logo from './logo.svg';
import './App.css';

function App() {
  function getData() {
    console.log("***** PRESSED *****");
    fetch("http://127.0.0.1:8000/api/index")
      .then(res => res.json())
      .then(
        (result) => {
          console.log(result)
        });

  }
  return (
    <div className="App">
      <h1>Hello World</h1>
      <button type="button" onClick={getData}>Get Data</button>

    </div>
  );
}

export default App;
