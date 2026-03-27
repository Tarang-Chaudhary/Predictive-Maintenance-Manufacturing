import React, { useState } from 'react';
import PlotCard from '../components/PlotCard';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell } from 'recharts';
import { motion, AnimatePresence } from 'framer-motion';

const Regression: React.FC = () => {
  const [activeModel, setActiveModel] = useState('Gradient Boosting');

  const modelData = [
    { name: 'Gradient Boosting', RMSE: 33.8, MAE: 24.1, R2: 0.75, color: 'var(--accent)' },
    { name: 'Random Forest', RMSE: 35.1, MAE: 25.4, R2: 0.72, color: 'var(--accent3)' },
    { name: 'Linear Regression', RMSE: 42.5, MAE: 32.1, R2: 0.58, color: 'var(--accent2)' },
  ];

  const chartData = modelData.map(m => ({
    name: m.name,
    RMSE: m.RMSE,
    color: m.color
  }));

  return (
    <div className="page fade-in">
      <div className="page-header">
        <h2>RUL Prediction Analysis</h2>
        <p>REMAINING USEFUL LIFE ARCHITECTURE & PERFORMANCE</p>
      </div>

      <div className="grid grid-cols-2">
        <div className="card">
          <div className="hero-tag" style={{ marginBottom: '1.5rem' }}>MODEL PERFORMANCE COMPARISON</div>
          
          <div style={{ height: '250px', width: '100%', marginBottom: '2rem' }}>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={chartData}>
                <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" vertical={false} />
                <XAxis dataKey="name" stroke="var(--dim)" fontSize={10} />
                <YAxis stroke="var(--dim)" fontSize={10} label={{ value: 'RMSE', angle: -90, position: 'insideLeft', fill: 'var(--dim)', fontSize: 10 }} />
                <Tooltip 
                  cursor={{ fill: 'rgba(255,255,255,0.05)' }}
                  contentStyle={{ background: '#0f1420', border: '1px solid rgba(255,255,255,0.07)' }}
                />
                <Bar dataKey="RMSE" radius={[2, 2, 0, 0]}>
                  {chartData.map((entry, index) => (
                    <Cell 
                      key={`cell-${index}`} 
                      fill={entry.name === activeModel ? entry.color : 'var(--border2)'}
                      style={{ cursor: 'pointer' }}
                      onClick={() => setActiveModel(entry.name)}
                    />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>

          <div className="metrics-display">
            <AnimatePresence mode="wait">
              <motion.div
                key={activeModel}
                initial={{ opacity: 0, x: -10 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: 10 }}
                transition={{ duration: 0.2 }}
              >
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '1rem' }}>
                  {['RMSE', 'MAE', 'R2'].map(metric => {
                    const model = modelData.find(m => m.name === activeModel);
                    const val = model ? (model as any)[metric] : 0;
                    return (
                      <div key={metric} style={{ padding: '1rem', background: 'rgba(255,255,255,0.02)', border: '1px solid var(--border)' }}>
                        <div style={{ fontFamily: 'Space Mono', fontSize: '0.65rem', color: 'var(--muted)', marginBottom: '0.25rem' }}>{metric}</div>
                        <div style={{ fontSize: '1.25rem', fontWeight: 700, color: 'var(--accent)' }}>{val}</div>
                      </div>
                    );
                  })}
                </div>
              </motion.div>
            </AnimatePresence>
          </div>
        </div>

        <PlotCard 
          title="Feature Importance" 
          filename="feature_importance.png" 
          description="Multivariate sensor contribution analysis for RUL prediction."
        />
      </div>

      <div style={{ marginTop: '2rem' }}>
        <PlotCard 
          title="Actual vs Predicted RUL" 
          filename="feature_importance.png" // Reusing this as placeholder if real one doesn't exist
          description="Temporal validation of predicted remaining useful life against ground truth."
        />
      </div>
    </div>
  );
};

export default Regression;
