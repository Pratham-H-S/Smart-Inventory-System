import React, { useState } from 'react';
import { registerUser } from '../api/api';
import '../style/Register.css'; // Import the CSS file for styling

function Register({ setIsLogin }) {
  const [registerData, setRegisterData] = useState({
    
    email: '',
    password: '',
    role: '', // Added role to the state
  });

  const handleChange = (e) => {
    setRegisterData({
      ...registerData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await registerUser(registerData);
      alert('Registration successful. Please log in.');
      setIsLogin(true); // Switch to login page after successful registration
    } catch (error) {
      console.error('Registration failed', error);
      alert('Registration failed. Please try again.');
    }
  };

  return (
    <div className="register-page">
      <div className="form">
        <h2>Create an Account</h2>
        <form onSubmit={handleSubmit}>
          
          <input
            type="email"
            name="email"
            value={registerData.email}
            onChange={handleChange}
            placeholder="Email"
            required
          />
          <input
            type="password"
            name="password"
            value={registerData.password}
            onChange={handleChange}
            placeholder="Password"
            required
          />
          <input
            type="text"
            name="role"
            value={registerData.role}
            onChange={handleChange}
            placeholder="Role" // Added role input field
            required
          />
          <button type="submit">Register</button>
          <p className="message">
            Already have an account?{' '}
            <a href="#" onClick={() => setIsLogin(true)}>
              Sign In
            </a>
          </p>
        </form>
      </div>
    </div>
  );
}

export default Register;
