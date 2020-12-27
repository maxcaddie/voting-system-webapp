import React, { useState, useEffect } from 'react';

function App() {
  const [currentTime, setCurrentTime] = useState(0);


  function updateTime(){
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }
  useEffect(() => {
    updateTime();
    fetch('/get');
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>The current time is {currentTime}.</p>
      </header>
      <form action="http://localhost:5000/uploader" method = "POST" encType="multipart/form-data">
        <input type="file" name="file" />
        <input type="submit" />
      </form>
    </div>
  );
}

export default App;