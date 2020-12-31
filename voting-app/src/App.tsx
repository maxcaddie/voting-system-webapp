import React, { useState, useEffect } from 'react';
import LoginForm from './components/authentication/login';
import CsvUploader from './components/uploads/csvUploader';

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  function updateTime() {
    fetch('/time').then((res) => res.json()).then((data) => {
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
        <p>
          The current time is {currentTime}.
        </p>
      </header>
      <p>User ID: {localStorage.getItem('userID')}</p>
      <LoginForm />
      <CsvUploader />
    </div>
  );
}

export default App;
