import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchSystems } from '../../store/systemsSlice';
import './Systems.css'; // Make sure to have this CSS file

const Systems = () => {
  const dispatch = useDispatch();
  const { systems, status, error } = useSelector(state => state.systems);

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
    <div className="systems-grid">
      {systems.map((system, index) => (
        <div key={system.name} className={`system-cell ${index % 2 === 0 ? 'red' : 'black'}`}>
          <h3>{system.name}</h3>
        </div>
      ))}
    </div>
  );
};

export default Systems;
