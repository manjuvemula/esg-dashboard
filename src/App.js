import React, { useState } from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    if (!file) {
      alert("Please select CSV file");
      return;
    }


    const formData = new FormData();
    formData.append("company", 1);
    formData.append("csv_file", file);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/api/companies/upload/",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      console.log("RESPONSE:", data);

      setResult(data);

      alert("Upload successful");
    } catch (error) {
      console.log("ERROR:", error);
      alert("Upload failed");
    }
  };

  const chartData = result
    ? [
        {
          name: "CO2 (÷1000)",
          value: (result.esg?.co2_emissions || 0) / 1000,
        },
        {
          name: "ESG Score",
          value: result.esg?.esg_score || 0,
        },
      ]
    : [];

  return (
    <div style={{ padding: 30, fontFamily: "Arial" }}>
      <h1>🌱 ESG Dashboard</h1>

      {/* UPLOAD */}
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />

      <button onClick={handleUpload} style={{ marginLeft: 10 }}>
        Upload CSV
      </button>

      {/* CARDS */}
      {result && (
        <div style={{ display: "flex", gap: 20, marginTop: 30 }}>
          <div style={cardStyle}>
            <h3>CO₂ Emissions</h3>
            <p>{result.esg?.co2_emissions}</p>
          </div>

          <div style={cardStyle}>
            <h3>ESG Score</h3>
            <p>{result.esg?.esg_score}</p>
          </div>

          <div style={cardStyle}>
            <h3>Total Rows</h3>
            <p>{result.rows}</p>
          </div>
        </div>
      )}

      {/* CHART */}
      {result && (
        <div style={{ width: "100%", height: 300, marginTop: 40 }}>
          <ResponsiveContainer>
            <BarChart data={chartData}>
              <XAxis dataKey="name" />
              <YAxis domain={[0, "auto"]} />
              <Tooltip />
              <Bar dataKey="value" fill="#4CAF50" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      )}
    </div>
  );
}

const cardStyle = {
  padding: 20,
  border: "1px solid #ddd",
  borderRadius: 10,
  width: 150,
  textAlign: "center",
  boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
};

export default App;