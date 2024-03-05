// SystemsDisplay.js
import React, { useEffect, useState, useCallback } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchSystems } from '../../store/systemsSlice';

// Styles should be clearly named and ideally located near their component
import './Systems.css';

/**
 * A recursive component to display a system and its forward connections.
 * Utilizes memoization to avoid unnecessary re-renders.
 */
const SystemNode = React.memo(({ systemId, systems, visited }) => {
  // Find the current system based on systemId. If not found or already visited, don't render.
  const system = systems.find(({ id }) => id === systemId);
  if (!system || visited.has(systemId)) return null;

  // Mark the current system as visited
  visited.add(systemId);

  return (
    <div className={`system-node ${system.type.toLowerCase()}`}>
      <h3>{system.name}</h3>
      <div className="connections">
        {/* Recursively render forward connections, excluding 'filler' */}
        {system.connections.forward.filter(id => id !== "filler").map(connId => (
          <SystemNode key={connId} systemId={connId} systems={systems} visited={visited} />
        ))}
      </div>
    </div>
  );
});

/**
 * Main component for fetching and displaying systems.
 * Manages the fetching state and initiates the recursive rendering.
 */
const SystemsDisplay = () => {
  const dispatch = useDispatch();
  const { systems, status, error } = useSelector(state => state.systems);
  const [visited, setVisited] = useState(new Set());

  // Effect for fetching systems data
  useEffect(() => {
    dispatch(fetchSystems());
  }, [dispatch]);

  // Reset visited nodes when systems data changes
  useEffect(() => {
    setVisited(new Set());
  }, [systems]);

  if (status === 'loading') return <div>Loading systems...</div>;
  if (status === 'failed') return <div>Error: {error}</div>;

  // Define the starting system ID here
  const startingSystemId = 'node_kino';

  return (
    <div className="systems-display">
      <SystemNode systemId={startingSystemId} systems={systems} visited={visited} />
    </div>
  );
};

export default SystemsDisplay;
