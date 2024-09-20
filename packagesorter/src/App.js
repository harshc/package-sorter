import React, { useState } from "react";
import logo from "./logo.svg";
import "./App.css";

const InputForm = () => {
  const [inputs, setInputs] = React.useState({
    width: "",
    height: "",
    length: "",
    mass: "",
  });

  const [apiData, setApiData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    if (!isNaN(parseFloat(value)) && parseFloat(value) > 0) {
      setInputs((prevState) => ({ ...prevState, [name]: value }));
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setApiData(null);

    try {
      // Construct the URL with query parameters
      const url = new URL("http://127.0.0.1:5000/sort");
      Object.keys(inputs).forEach((key) =>
        url.searchParams.append(key, inputs[key])
      );

      const response = await fetch(url, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include", // This line is important for including cookies if needed
      });
      console.log(url);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      setApiData(data);
    } catch (e) {
      setError("Failed to fetch data: " + e.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-md mx-auto mt-8">
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="text"
          name="width"
          value={inputs.width}
          onChange={handleChange}
          placeholder="0.00"
          className="w-full px-3 py-2 border rounded-md"
        />
        <input
          type="text"
          name="height"
          value={inputs.height}
          onChange={handleChange}
          placeholder="0.00"
          className="w-full px-3 py-2 border rounded-md"
        />
        <input
          type="text"
          name="length"
          value={inputs.length}
          onChange={handleChange}
          placeholder="0.00"
          className="w-full px-3 py-2 border rounded-md"
        />
        <input
          type="text"
          name="mass"
          value={inputs.mass}
          onChange={handleChange}
          placeholder="0.00"
          className="w-full px-3 py-2 border rounded-md"
        />
        <button
          type="submit"
          className="w-full px-4 py-2 text-white bg-blue-500 rounded-md hover:bg-blue-600"
          disabled={loading}
        >
          {loading ? "Loading..." : "Submit"}
        </button>
      </form>

      {error && <p className="mt-4 text-red-500">{error}</p>}

      {apiData && (
        <div className="mt-4">
          <h2 className="text-xl font-bold mb-2">API Response:</h2>
          <pre className="bg-gray-100 p-4 rounded-md overflow-auto">
            {JSON.stringify(apiData, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
};

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <InputForm />
      </header>
    </div>
  );
}

export default App;
