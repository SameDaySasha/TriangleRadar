import React from 'react';
import { Link } from 'react-router-dom';
import './LandingPage.css'; // Ensure this path matches your CSS file's location

function LandingPage() {
  return (
    <div className="landing-page">
      <h1>Welcome to Our Application</h1>
      <div className="links">
        <Link to="/login" className="link">Login</Link>
        <br />
        <Link to="/signup" className="link">Sign Up</Link>
      </div>
    </div>
  );
}

export default LandingPage;
