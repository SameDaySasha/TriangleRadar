import React from 'react';
import { Link } from 'react-router-dom';
import { useDispatch } from 'react-redux'; // Ensure this is correctly imported from 'react-redux'
import { login } from '/Users/alexflorea/Desktop/Kyber_dar/practice-for-week-19-python-project-skeleton/react-app/src/store/session.js'; // Adjust this import path to where your auth actions are defined
import './LandingPage.css'; // Ensure this path correctly points to your CSS file

function LandingPage() {
  const dispatch = useDispatch();

  const handleDemoLogin = async () => {
    // Use the predefined demo credentials
    await dispatch(login("demo@aa.io", "password"));
    // Implement any redirection or state update needed after successful login
  };

  return (
    <div className="landing-page d-flex align-items-center justify-content-center" style={{ height: '100vh' }}>
      <div className="text-center bg-dark p-4" style={{ borderRadius: '15px' }}>
        <h1 className="mb-4" style={{ fontFamily: 'TriglavianFont' }}>Welcome to Our Application</h1>
        <Link to="/login" className="btn btn-danger btn-lg mb-2" style={{ fontFamily: 'TriglavianFont', width: '100%' }}>Login</Link>
        <Link to="/signup" className="btn btn-danger btn-lg mb-2" style={{ fontFamily: 'TriglavianFont', width: '100%' }}>Sign Up</Link>
        <button 
          className="btn btn-warning btn-lg" 
          style={{ fontFamily: 'TriglavianFont', width: '100%' }}
          onClick={handleDemoLogin}
        >
          Demo Login
        </button>
      </div>
    </div>
  );
}

export default LandingPage;
