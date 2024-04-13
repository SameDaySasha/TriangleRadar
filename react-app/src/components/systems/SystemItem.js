import React from 'react';
import { useHistory } from 'react-router-dom';

const SystemItem = ({ system, calculatePosition }) => {
  const history = useHistory();
  const positionStyle = calculatePosition(system.id);

  const handleClick = () => {
    // Navigate to the system detail page without fetching data
    history.push(`/systems/${system.id}`);
  };

  return (
    <div
      className="system-cell"
      onClick={handleClick}
      style={positionStyle}
    >
      <h3>{system.name}</h3>
    </div>
  );
};

export default SystemItem;
