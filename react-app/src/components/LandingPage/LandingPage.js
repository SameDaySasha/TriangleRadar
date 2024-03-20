import React from 'react';
import { Link } from 'react-router-dom';
import './LandingPage.css'; // Make sure this import points to your CSS file

function LandingPage() {
  return (
    <div className="landing-page d-flex align-items-center justify-content-center" style={{ height: '100vh' }}>
      <div className="text-center bg-dark p-4" style={{ borderRadius: '15px' }}>
        <h1 className="mb-4" style={{ fontFamily: 'TriglavianFont' }}>Welcome to Our Application</h1>
        <Link to="/login" className="btn btn-danger btn-lg mb-2" style={{ fontFamily: 'TriglavianFont', width: '100%' }}>Login</Link>
        <Link to="/signup" className="btn btn-danger btn-lg" style={{ fontFamily: 'TriglavianFont', width: '100%' }}>Sign Up</Link>
      </div>
    </div>
  );
}
export default LandingPage;
