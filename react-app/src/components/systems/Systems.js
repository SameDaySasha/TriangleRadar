import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchSystems } from '../../store/systemsSlice'; // Path to your systemsSlice
import SystemComponent from './SystemComponent'; // Path to your SystemComponent

const SystemsContainer = () => {
  const dispatch = useDispatch();
  const { systems, status } = useSelector(state => state.systems);
  const [rootSystem, setRootSystem] = useState(null);

  useEffect(() => {
    dispatch(fetchSystems());
  }, [dispatch]);

  useEffect(() => {
    // Assuming the starting system's ID is known and is 0
    const startingSystem = systems.find(system => system.id === 0);
    setRootSystem(startingSystem);
  }, [systems]);

  if (status === 'loading') return <div>Loading...</div>;
  if (status === 'failed') return <div>Error loading systems</div>;

  return (
    <div>
      <h2>Systems Visualization</h2>
      {rootSystem && <SystemComponent system={rootSystem} systems={systems} />}
    </div>
  );
};

export default SystemsContainer;
