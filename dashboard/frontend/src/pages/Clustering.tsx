import React from 'react';
import PlotCard from '../components/PlotCard';

const Clustering: React.FC = () => {
  return (
    <div className="page fade-in">
      <div className="page-header">
        <h2>Engine Clustering</h2>
        <p>Unsupervised grouping of engines based on sensor degradation patterns.</p>
      </div>

      <div className="grid grid-cols-2">
        <PlotCard 
          title="PCA Cluster Projection" 
          filename="engine_clusters.png" 
          description="Engines grouped into 3 clusters using KMeans, visualized via PCA."
        />
        <PlotCard 
          title="Elbow Method" 
          filename="elbow_plot.png" 
          description="Determining the optimal number of clusters based on inertia."
        />
      </div>
    </div>
  );
};

export default Clustering;
