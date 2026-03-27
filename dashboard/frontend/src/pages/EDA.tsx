import React from 'react';
import PlotCard from '../components/PlotCard';

const EDA: React.FC = () => {
  return (
    <div className="page fade-in">
      <div className="page-header">
        <h2>Exploratory Data Analysis</h2>
        <p>Understanding sensor behavior and correlations across engine life cycles.</p>
      </div>

      <div className="grid grid-cols-1">
        <PlotCard 
          title="Sensor Degradation Trends" 
          filename="sensor_trends.png" 
          description="Key sensor trends for Engine Unit 1. Notice how values drift as the engine approaches failure."
        />
        <PlotCard 
          title="Sensor Correlation Heatmap" 
          filename="sensor_correlation.png" 
          description="Visualizing relationships between different sensors to identify redundant features."
        />
      </div>
    </div>
  );
};

export default EDA;
