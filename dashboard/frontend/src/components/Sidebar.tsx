import React from 'react';
import { NavLink } from 'react-router-dom';
import { LayoutDashboard, Activity, Target, AlertCircle, Layers, TrendingUp } from 'lucide-react';
import './Sidebar.css';

const Sidebar: React.FC = () => {
  const menuItems = [
    { id: 'overview', label: 'Overview', icon: <LayoutDashboard size={20} />, path: '/' },
    { id: 'eda', label: 'EDA & Sensors', icon: <Activity size={20} />, path: '/eda' },
    { id: 'regression', label: 'RUL Prediction', icon: <Target size={20} />, path: '/regression' },
    { id: 'classification', label: 'Failure Risk', icon: <AlertCircle size={20} />, path: '/classification' },
    { id: 'clustering', label: 'Engine Clustering', icon: <Layers size={20} />, path: '/clustering' },
    { id: 'forecasting', label: 'Forecasting', icon: <TrendingUp size={20} />, path: '/forecasting' },
  ];

  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <h1>Predictive <br /><span>Analytics</span></h1>
      </div>
      <nav className="sidebar-nav">
        {menuItems.map((item) => (
          <NavLink
            key={item.id}
            to={item.path}
            className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}
          >
            {item.icon}
            <span>{item.label}</span>
          </NavLink>
        ))}
      </nav>
      <div className="sidebar-footer">
        <p>CMAPSS Turbofan Project</p>
      </div>
    </aside>
  );
};

export default Sidebar;
