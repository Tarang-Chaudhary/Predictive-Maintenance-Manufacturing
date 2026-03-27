import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, AreaChart, Area } from 'recharts';
import { motion } from 'framer-motion';

const LiveSensorFeed: React.FC = () => {
  const [data, setData] = useState<{ time: number; value: number }[]>([]);
  const [sensorType, setSensorType] = useState('T50');

  useEffect(() => {
    const interval = setInterval(() => {
      setData(prevData => {
        const nextTime = prevData.length > 0 ? prevData[prevData.length - 1].time + 1 : 0;
        const newValue = 500 + Math.random() * 50 + (Math.sin(nextTime / 5) * 20);
        const newData = [...prevData, { time: nextTime, value: newValue }];
        return newData.slice(-20); // Keep last 20 points
      });
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="card" style={{ marginTop: '2rem' }}>
      <div className="hero-tag" style={{ marginBottom: '1.5rem' }}>
        <motion.div
          animate={{ opacity: [1, 0.4, 1] }}
          transition={{ duration: 1.5, repeat: Infinity }}
          style={{ width: 8, height: 8, borderRadius: '50%', background: 'var(--accent4)', marginRight: 8 }}
        />
        LIVE TELEMETRY FEED — SENSOR_{sensorType}
      </div>

      <div style={{ height: '300px', width: '100%' }}>
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={data}>
            <defs>
              <linearGradient id="colorValue" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="var(--accent)" stopOpacity={0.3}/>
                <stop offset="95%" stopColor="var(--accent)" stopOpacity={0}/>
              </linearGradient>
            </defs>
            <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" vertical={false} />
            <XAxis 
              dataKey="time" 
              hide 
            />
            <YAxis 
              domain={['auto', 'auto']} 
              stroke="var(--dim)" 
              fontSize={10}
              tickFormatter={(val) => val.toFixed(0)}
            />
            <Tooltip 
              contentStyle={{ background: '#0f1420', border: '1px solid rgba(255,255,255,0.07)', fontSize: '12px' }}
              itemStyle={{ color: '#00d4ff' }}
            />
            <Area 
              type="monotone" 
              dataKey="value" 
              stroke="var(--accent)" 
              fillOpacity={1} 
              fill="url(#colorValue)" 
              isAnimationActive={false}
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>
      
      <div style={{ display: 'flex', gap: '1rem', marginTop: '1rem' }}>
        {['T50', 'P30', 'Nf', 'Nc'].map(s => (
          <button 
            key={s}
            onClick={() => { setSensorType(s); setData([]); }}
            style={{
              padding: '4px 12px',
              fontSize: '10px',
              fontFamily: 'Space Mono',
              background: sensorType === s ? 'var(--accent)' : 'transparent',
              color: sensorType === s ? 'var(--bg)' : 'var(--muted)',
              border: '1px solid var(--border)',
              borderRadius: '2px',
              cursor: 'pointer'
            }}
          >
            {s}
          </button>
        ))}
      </div>
    </div>
  );
};

export default LiveSensorFeed;
