import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Overview from './pages/Overview';
import EDA from './pages/EDA';
import Regression from './pages/Regression';
import Classification from './pages/Classification';
import Clustering from './pages/Clustering';
import Forecasting from './pages/Forecasting';
import './App.css';

function App() {
  return (
    <Router>
      <Sidebar />
      <main className="main-content">
        <Routes>
          <Route path="/" element={<Overview />} />
          <Route path="/eda" element={<EDA />} />
          <Route path="/regression" element={<Regression />} />
          <Route path="/classification" element={<Classification />} />
          <Route path="/clustering" element={<Clustering />} />
          <Route path="/forecasting" element={<Forecasting />} />
        </Routes>
      </main>
    </Router>
  );
}

export default App;
