import React from 'react';
import PlotCard from '../components/PlotCard';

const Forecasting: React.FC = () => {
  return (
    <div className="page fade-in">
      <div className="page-header">
        <h2>Time Series Forecasting</h2>
        <p>Using ARIMA and Autoregressive models to forecast future sensor values.</p>
      </div>

      <div className="grid grid-cols-1">
        <PlotCard 
          title="ARIMA Model Forecast" 
          filename="arima_forecast.png" 
          description="A 30-cycle forecast for Sensor 11 using the ARIMA model. Blue lines represent the prediction interval."
        />
        <PlotCard 
          title="AR Model Fit" 
          filename="ar_model_fit.png" 
          description="Performance of a simpler Autoregressive model on historical data."
        />
      </div>
    </div>
  );
};

export default Forecasting;
