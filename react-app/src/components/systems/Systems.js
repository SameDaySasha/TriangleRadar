// Inside /src/components/systems/Systems.js

import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchSystems } from '../../store/systemsSlice';
import './Systems.css'; // Assuming your CSS file is in the same directory

const Systems = () => {
  const dispatch = useDispatch();
  const { systems, status, error } = useSelector((state) => state.systems);

  useEffect(() => {
    dispatch(fetchSystems());
  }, [dispatch]);

  if (status === 'loading') {
    return <div>Loading systems...</div>;
  }

  if (status === 'failed') {
    return <div>Error: {error}</div>;
  }

  return (
    <div className="triangle-layout">
      {systems.map((system, index) => (
        <div key={system.id} className={`system system-${index}`}>
          {system.name}
        </div>
      ))}
    </div>
  );
};

export default Systems;
