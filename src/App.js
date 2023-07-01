import React, { useState } from 'react';

function App() {
  const [question, setQuestion] = useState('');
  const [options, setOptions] = useState([]);
  const [answer, setAnswer] = useState('');
  const [selectedOption, setSelectedOption] = useState('');
  const [popupMessage, setPopupMessage] = useState('');

  const fetchData = async () => {
    try {
      const response = await fetch('http://localhost:5000/get_poll');
      const data = await response.json();

      setQuestion(data.question);
      setOptions(data.options);
      setAnswer(data.answer);
      setPopupMessage('');
    } catch (error) {
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
  );
}

export default App;
