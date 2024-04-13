import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { fetchSystemById } from '../../store/systemsSlice';
import './systemDetails.css'; // Ensure your CSS file defines .system-cell and .systems-grid
const SystemDetailPage = () => {
  const { id } = useParams();  // Extract the system ID from URL
  const dispatch = useDispatch();
  const systemDetails = useSelector(state => state.systems.currentSystem);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    dispatch(fetchSystemById(id))
      .unwrap()
      .then(() => setLoading(false))
      .catch(err => {
        setError(err.toString());
        setLoading(false);
      });
  }, [dispatch, id]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error loading system details: {error}</div>;
  }

  if (!systemDetails) {
    return <div>No system found.</div>;
  }

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>System Details: {systemDetails.name}</h1>
      <p><strong>ID:</strong> {systemDetails.id}</p>
      <p><strong>Description: This is a test description to make sure that this works. Bazinga</strong> {systemDetails.description}</p>
      {/* Add more fields as needed */}
    </div>
  );
};

export default SystemDetailPage;
