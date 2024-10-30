import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate
import { loginUser, registerUser } from '../api/api';
import '../style/Login.css';

function Login({ setToken }) {
  const navigate = useNavigate(); // Create a navigate function

  const [isLogin, setIsLogin] = useState(true);
  const [loginData, setLoginData] = useState({ username: '', password: '' });
  const [registerData, setRegisterData] = useState({ name: '', email: '', password: '' });

  const handleLoginChange = (e) => {
    setLoginData({
      ...loginData,
      [e.target.name]: e.target.value,
    });
  };

  const handleRegisterChange = (e) => {
    setRegisterData({
      ...registerData,
      [e.target.name]: e.target.value,
    });
  };

  const handleLoginSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await loginUser({
        username: loginData.username,
        password: loginData.password,
      });
      const token = response.data.access_token;
      localStorage.setItem('token', token);
      setToken(token);
      alert('Login successful');
      
      // Redirect to reports page using navigate
      navigate('/reports'); // Change this to your reports route
    } catch (error) {
      console.error('Login failed', error);
      alert('Login failed. Please check your credentials.');
    }
  };

  const handleRegisterSubmit = async (e) => {
    e.preventDefault();
    try {
      await registerUser({
        username: registerData.name,
        email: registerData.email,
        password: registerData.password,
      });
      alert('Registration successful. Please login.');
      setIsLogin(true);
    } catch (error) {
      console.error('Registration failed', error);
      alert('Registration failed. Please try again.');
    }
  };

  const toggleForm = (e) => {
    e.preventDefault();
    setIsLogin(!isLogin);
  };

  return (
    <div className="login-page">
      <div className="form">
        {isLogin ? (
          <form className="login-form" onSubmit={handleLoginSubmit}>
            <input
              type="text"
              name="username"
              value={loginData.username}
              onChange={handleLoginChange}
              placeholder="username"
              required
            />
            <input
              type="password"
              name="password"
              value={loginData.password}
              onChange={handleLoginChange}
              placeholder="password"
              required
            />
            <button type="submit">login</button>
            <p className="message">
              Not registered?{' '}
              <a href="#" onClick={toggleForm}>
                Create an account
              </a>
            </p>
          </form>
        ) : (
          <form className="register-form" onSubmit={handleRegisterSubmit}>
            <input
              type="text"
              name="name"
              value={registerData.name}
              onChange={handleRegisterChange}
              placeholder="name"
              required
            />
            <input
              type="password"
              name="password"
              value={registerData.password}
              onChange={handleRegisterChange}
              placeholder="password"
              required
            />
            <input
              type="email"
              name="email"
              value={registerData.email}
              onChange={handleRegisterChange}
              placeholder="email address"
              required
            />
            <button type="submit">create</button>
            <p className="message">
              Already registered?{' '}
              <a href="#" onClick={toggleForm}>
                Sign In
              </a>
            </p>
          </form>
        )}
      </div>
    </div>
  );
}

export default Login;
