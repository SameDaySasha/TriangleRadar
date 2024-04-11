import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchSystems } from '../../store/systemsSlice';
import { logout } from '../../store/session';
import './Systems.css'; // Ensure your CSS file defines .system-cell and .systems-grid


const Systems = () => {
  const dispatch = useDispatch();
  const { systems, status, error } = useSelector(state => state.systems);

  useEffect(() => {
    dispatch(fetchSystems());
  }, [dispatch]);

  const handleLogout = () => {
    dispatch(logout());
    // Optional: Add any redirection here if needed
  };
  const calculatePosition = (id) => {
    const step = 60;
    const bottomLegStep = step * 1.98; // Increased step size for the bottom leg
    let position = { x: 0, y: 0 };
    let directionPhase = 1; // Start with phase 1 (southeast)
  
    for (let i = 1; i < id; i++) {
      if (i === 10) directionPhase = 2; // Change to phase 2 (left)
      if (i === 19) directionPhase = 3; // Change to phase 3 (up-right)
  
      switch (directionPhase) {
        case 1: // Southeast
          position.x += step;
          position.y += step;
          break;
        case 2: // Left
          position.x -= bottomLegStep; // Use the increased step size for the bottom leg
          break;
        case 3: // Up-right
          position.x += step;
          position.y -= step;
          break;
      }
    }
  
    return {
      left: `${position.x}px`,
      top: `${position.y}px`,
    };
  };
  
  

  if (status === 'loading') {
    return <div>Loading systems...</div>;
  }

  if (status === 'failed') {
    return <div>Error: {error}</div>;
  }

  return (
    
    <div className="systems-container">
      <button onClick={handleLogout} style={{ position: 'absolute', right: '10px', top: '10px' }}>Logout</button>
      <div className="systems-grid">
        {systems.map(system => {
          const positionStyle = calculatePosition(system.id);
          return (
            <div key={system.id} className={`itemid ${system.id}`} style={positionStyle}>
              <h3>{system.name}</h3>
            </div>
          );
        })}
      </div>
    </div>
  );
};


export default Systems;
