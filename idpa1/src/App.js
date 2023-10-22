import React, { useState } from "react";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const handleQueryChange = (e) => {
    setQuery(e.target.value);
  };

  const handleRunQuery = () => {
    // Here, you can implement the logic to process the user's query and update the results state.
    // For simplicity, we'll just set a sample result here.
    setResults(["Sample result 1", "Sample result 2"]);
  };

  return (
    <div className="main">
      <div>
        <h1>Semi-Structured Document Search</h1>
      </div>

      <div>
        <textarea
          className="textarea"
          placeholder="Enter your semi-structured document fragment..."
          value={query}
          onChange={handleQueryChange}
        />
        {/* <textarea
          className="textarea"
          placeholder="Enter your query..."
          value={query}
          onChange={handleQueryChange}
        /> */}
      </div>
      
      <div>
        <button className="button" onClick={handleRunQuery}>Run Query</button>
      </div>

      <div className="results">
        <h2>Results:</h2>
        <ul>
          {results.map((result, index) => (
            <li key={index}>{result}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
