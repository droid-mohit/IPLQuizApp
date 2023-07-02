import React, { useState } from 'react';
import "./App.css"
import CircularProgress from "@mui/material/CircularProgress";
import Box from "@mui/material/Box";
import { Typography } from '@mui/material';

function App() {
  const [question, setQuestion] = useState('');
  const [options, setOptions] = useState([]);
  const [answer, setAnswer] = useState('');
  const [selectedOption, setSelectedOption] = useState('');
  const [popupMessage, setPopupMessage] = useState('');
  const [loading, setLoading] = useState(false);
  

  const fetchData = async () => {
    try {
      setLoading(true)
      const response = await fetch('/get_poll', {
        mode: 'cors',
        method: 'GET',
        headers: {'Content-Type':'application/json', 'Access-Control-Allow-Credentials':true, 'Access-Control-Allow-Origin':'*', 'Access-Control-Allow-Methods':'GET,OPTIONS,PATCH,DELETE,POST,PUT', 'Access-Control-Allow-Headers':'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
      }
      });
      const data = await response.json();
      setLoading(false)
      setQuestion(data.question);
      setOptions(data.options);
      setAnswer(data.answer);
      setPopupMessage('');
    } catch (error) {
      setLoading(false)
      console.error('Error fetching data:', error);
    }
  };

  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
  };

  const handlePollSubmit = () => {
    if (selectedOption === answer) {
      setPopupMessage('Correct Answer!');
    } else {
      setPopupMessage('Sorry, Better Luck Next Time!');
    }
  };

  return (
    <div className="App">
      <h1>Poll App</h1>
      <button onClick={fetchData}>Load Poll</button>
      <div className="loader">
        {loading && (
          <Box
            sx={{
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              gap: '2rem'
            }}
          >
            <CircularProgress />
          </Box>
        )}
      </div>
      {!loading && (
        <div className="outputContainer">
            <div className="poll-container">
                {question && (
                  <div>
                    <h2>{question}</h2>
                    <form>
                      {options.map((option) => (
                        <div key={option}>
                          <label>
                            <input
                              type="radio"
                              value={option}
                              checked={selectedOption === option}
                              onChange={handleOptionChange}
                            />
                            {option}
                          </label>
                        </div>
                      ))}
                    </form>
                    <button onClick={handlePollSubmit}>Submit</button>
                    
                  </div>
                )}
                {popupMessage && (
                  <div className="popup">
                    <p>{popupMessage}</p>
                  </div>
                )}
            </div>
        </div>
      )}
      <Typography variant="caption" display="block" gutterBottom>
          <a href="https://github.com/droid-mohit/drd-trivia-backend" sx={{textDecoration: 'underline'}}>Powered by ChatGPT</a>
      </Typography>
    </div>
  );
}

export default App;

