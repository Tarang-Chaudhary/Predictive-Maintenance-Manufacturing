import React from 'react';
import PlotCard from '../components/PlotCard';
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip, Legend } from 'recharts';

const Classification: React.FC = () => {
  const riskData = [
    { name: 'Low Risk', value: 12000, color: 'var(--accent4)' },
    { name: 'Medium Risk', value: 5000, color: 'var(--accent2)' },
    { name: 'High Risk', value: 3631, color: 'var(--accent)' },
  ];

  const modelMetrics = [
    { name: 'Random Forest', accuracy: '88%', auc: '0.94' },
    { name: 'SVM', accuracy: '86%', auc: '0.92' },
    { name: 'LDA', accuracy: '82%', auc: '0.89' },
  ];

  return (
    <div className="page fade-in">
      <div className="page-header">
        <h2>Failure Risk Classification</h2>
        <p>PROBABILITY ESTIMATION & BINARY CLASSIFICATION PERFORMANCE</p>
      </div>

      <div className="grid grid-cols-2">
        <div className="card">
          <div className="hero-tag" style={{ marginBottom: '1.5rem' }}>RISK TIER DISTRIBUTION</div>
          <div style={{ height: '250px', width: '100%' }}>
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={riskData}
                  cx="50%"
                  cy="50%"
                  innerRadius={60}
                  outerRadius={80}
                  paddingAngle={5}
                  dataKey="value"
                >
                  {riskData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip 
                  contentStyle={{ background: '#0f1420', border: '1px solid rgba(255,255,255,0.07)' }}
                />
                <Legend iconType="circle" />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="card">
          <div className="hero-tag" style={{ marginBottom: '1.5rem' }}>CLASSIFIER PERFORMANCE</div>
          <table className="metrics-table">
            <thead>
              <tr>
                <th>ARCHITECTURE</th>
                <th>ACCURACY</th>
                <th>ROC-AUC</th>
              </tr>
            </thead>
            <tbody>
              {modelMetrics.map(m => (
                <tr key={m.name}>
                  <td>{m.name}</td>
                  <td style={{ color: 'var(--accent)' }}>{m.accuracy}</td>
                  <td style={{ color: 'var(--accent)' }}>{m.auc}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <PlotCard 
          title="Failure Probability" 
          filename="propensity_dist.png" 
          description="Distribution of failure risk scores across validation cohort."
        />
        <PlotCard 
          title="ROC Curves" 
          filename="roc_curves.png" 
          description="Architecture sensitivity analysis across varying thresholds."
        />
      </div>
    </div>
  );
};

export default Classification;
