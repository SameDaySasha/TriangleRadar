import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { fetchSystems } from '../../store/systemsSlice';
import { logout } from '../../store/session';
import './Systems.css'; // Ensure your CSS file defines .system-cell and .systems-grid

const Systems = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const { systems, status, error } = useSelector(state => state.systems);

  useEffect(() => {
    dispatch(fetchSystems());
  }, [dispatch]);

  const handleLogout = () => {
    dispatch(logout());
  };

  const calculatePosition = (id) => {
    const step = 60;
    const bottomLegStep = step * 1.98;
    let position = { x: 0, y: 0 };
    let directionPhase = 1;

    for (let i = 1; i < id; i++) {
      if (i === 10) directionPhase = 2;
      if (i === 19) directionPhase = 3;

      switch (directionPhase) {
        case 1:
          position.x += step;
          position.y += step;
          break;
        case 2:
          position.x -= bottomLegStep;
          break;
        case 3:
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

  const handleSystemClick = (id) => {
    history.push(`/systems/${id}`);
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
            <div key={system.id} className={`system-cell itemid ${system.id}`} style={positionStyle} onClick={() => handleSystemClick(system.id)}>
              <h3>{system.name}</h3>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default Systems;
