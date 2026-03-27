import React from 'react';

interface PlotCardProps {
  title: string;
  filename: string;
  description?: string;
}

const PlotCard: React.FC<PlotCardProps> = ({ title, filename, description }) => {
  return (
    <div className="card plot-card">
      <div className="plot-info">
        <h3>{title}</h3>
        {description && <p>{description}</p>}
      </div>
      <div className="img-container">
        <img src={`http://localhost:8000/images/${filename}`} alt={title} />
      </div>
    </div>
  );
};

export default PlotCard;
