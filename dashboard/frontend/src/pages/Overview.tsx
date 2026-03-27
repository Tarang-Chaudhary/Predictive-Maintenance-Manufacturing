import React, { useEffect, useState } from 'react';
import { Database, Zap, Clock, Activity, ArrowRight } from 'lucide-react';
import LiveSensorFeed from '../components/LiveSensorFeed';

interface Summary {
  total_engines: number;
  total_cycles: number;
  avg_cycles_per_engine: number;
  sensor_count: number;
  filename: string;
}

const Overview: React.FC = () => {
  const [summary, setSummary] = useState<Summary | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:8000/api/summary')
      .then(res => res.json())
      .then(data => {
        setSummary(data);
        setLoading(false);
      })
      .catch(err => console.error(err));
  }, []);

  if (loading) return <div className="loading-spinner">INITIALIZING SYSTEM...</div>;

  return (
    <div className="page fade-in">
      {/* Grid Background Effect */}
      <div style={{
        position: 'absolute',
        inset: 0,
        backgroundImage: 'linear-gradient(rgba(0,212,255,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(0,212,255,0.03) 1px, transparent 1px)',
        backgroundSize: '60px 60px',
        maskImage: 'radial-gradient(ellipse 80% 80% at 50% 50%, black 30%, transparent 100%)',
        pointerEvents: 'none',
        zIndex: -1
      }}></div>

      <div className="hero-section">
        <div className="hero-tag">
          <Zap size={12} fill="currentColor" />
          <span>Predictive Maintenance — BCSE334L CASE STUDY</span>
        </div>
        
        <h1 className="hero-title">
          Turbofan Engine<br />
          <span style={{ color: 'var(--accent)' }}>Degradation</span> Models
        </h1>

        <p className="hero-desc">
          Advancing aerospace reliability through high-fidelity simulation and deep learning. 
          Predicting Remaining Useful Life (RUL) with sub-cycle precision using the CMAPSS dataset.
        </p>
      </div>

      <div className="grid grid-cols-3">
        <div className="card">
          <div className="card-icon" style={{ color: 'var(--accent)' }}><Database size={24} /></div>
          <h3>{summary?.total_engines}</h3>
          <p>ENGINE UNITS</p>
        </div>
        <div className="card">
          <div className="card-icon" style={{ color: 'var(--accent4)' }}><Activity size={24} /></div>
          <h3>{summary?.total_cycles.toLocaleString()}</h3>
          <p>TOTAL CYCLES</p>
        </div>
        <div className="card">
          <div className="card-icon" style={{ color: 'var(--accent2)' }}><Clock size={24} /></div>
          <h3>{summary?.avg_cycles_per_engine.toFixed(0)}</h3>
          <p>AVG MAX CYCLES</p>
        </div>
      </div>

      <LiveSensorFeed />

      <div className="card" style={{ marginTop: '2.5rem' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
          <div>
            <div className="hero-tag" style={{ marginBottom: '1rem' }}>SYSTEM OBJECTIVE</div>
            <p style={{ color: 'var(--text)', fontSize: '1.1rem', maxWidth: '800px' }}>
              Employing Random Forest, Gradient Boosting, and ARIMA architectures to identify 
              multivariate degradation patterns across 21 sensor channels and 3 operational settings.
            </p>
          </div>
          <div className="card-icon" style={{ color: 'var(--accent)' }}>
            <ArrowRight size={32} />
          </div>
        </div>
        
        <div style={{ marginTop: '2.5rem', display: 'flex', gap: '3rem' }}>
          <div>
            <div style={{ fontFamily: 'Space Mono', fontSize: '0.7rem', color: 'var(--muted)', marginBottom: '0.5rem' }}>DATASET</div>
            <div style={{ color: 'var(--accent)', fontWeight: 600 }}>{summary?.filename}</div>
          </div>
          <div>
            <div style={{ fontFamily: 'Space Mono', fontSize: '0.7rem', color: 'var(--muted)', marginBottom: '0.5rem' }}>SENSORS</div>
            <div style={{ color: 'var(--accent)', fontWeight: 600 }}>21 CHANNELS</div>
          </div>
          <div>
            <div style={{ fontFamily: 'Space Mono', fontSize: '0.7rem', color: 'var(--muted)', marginBottom: '0.5rem' }}>ARCHITECTURE</div>
            <div style={{ color: 'var(--accent)', fontWeight: 600 }}>ML-PREDICTIVE</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Overview;
