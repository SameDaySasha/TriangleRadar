import React from 'react';

// SystemComponent is responsible for rendering a single system and its connections
const SystemComponent = ({ system, systems }) => {
  if (!system) return null;

  // Find the systems connected to this one
  const connectedSystems = system.connections.forward.map(connId => 
    systems.find(sys => sys.id === connId)
  );

  return (
    <div style={{ margin: '10px', border: '1px solid #ddd', padding: '10px' }}>
      <h3>{system.name} ({system.status})</h3>
      <div>
        <strong>Connections:</strong>
        <ul>
          {connectedSystems.map((connSystem, index) => (
            <li key={index}>
              <SystemComponent system={connSystem} systems={systems} />
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default SystemComponent;