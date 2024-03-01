// Inside /src/components/systems/Systems.js
import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchSystems } from '../../store/systemsSlice';
import './Systems.css';

const Systems = () => {
  const dispatch = useDispatch();
  const { systems, status, error } = useSelector((state) => state.systems);

  useEffect(() => {
    dispatch(fetchSystems());
  }, [dispatch]);

  // Simplified render function to display systems
  const renderSystems = (systems) => {
    return systems.map((system, index) => (
      <div key={index} className="system">
        <h2>{system.name}</h2>
        <p>Status: {system.status}</p>
        <p>Threat Level: {system.threat_level}</p>
        {/* Simplified for clarity; add more details as needed */}
      </div>
    ));
  };

  if (status === 'loading') {
    return <div>Loading systems...</div>;
  }

  if (status === 'failed') {
    return <div>Error: {error}</div>;
  }

  return (
    <div className="systems-layout">
      {renderSystems(systems)}
    </div>
  );
};

export default Systems;
