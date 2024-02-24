// Inside /src/components/systems/Systems.js
import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchSystems } from '../../store/systemsSlice';
import './Systems.css'; // Make sure the path to your CSS file is correct

const Systems = () => {
  const dispatch = useDispatch();
  const { systems, status, error } = useSelector((state) => state.systems);

  useEffect(() => {
    dispatch(fetchSystems());
  }, [dispatch]);

  const renderSystemsInRows = (systems) => {
    const rows = [];
    let currentRow = [];
    let itemsInRow = 1;

    systems.forEach((system, index) => {
      currentRow.push(
        <div key={system.id} className="system">
          {system.name}
        </div>
      );
      if (currentRow.length === itemsInRow) {
        rows.push(
          <div key={index} className="system-row">
            {currentRow}
          </div>
        );
        currentRow = [];
        itemsInRow++;
      }
    });

    // In case the last row isn't full
    if (currentRow.length > 0) {
      rows.push(
        <div className="system-row">
          {currentRow}
        </div>
      );
    }

    return rows;
  };

  if (status === 'loading') {
    return <div>Loading systems...</div>;
  }

  if (status === 'failed') {
    return <div>Error: {error}</div>;
  }

  return (
    <div className="triangle-layout">
      {renderSystemsInRows(systems)}
    </div>
  );
};

export default Systems;
