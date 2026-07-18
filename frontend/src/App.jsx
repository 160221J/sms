import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    axios
      .get("http://localhost:8080/health")
      .then((response) => {
        setMessage(response.data.status);
      })
      .catch((error) => {
        console.error(error);
        setMessage("Cannot connect to backend");
      });
  }, []);

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>Student Management System</h1>

      <h2>{message}</h2>
    </div>
  );
}

export default App;