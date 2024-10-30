import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';
import Inventory from './components/Inventory';
import setAuthToken from './api/api';
import InventoryManager from './components/InventoryManager';
import Reports from './components/Reports';

function App() {
    const [token, setToken] = useState(localStorage.getItem('token'));

    if (token) {
        setAuthToken(token);
    }

    return (
        <Router>
            <Routes>
                <Route path="/login" element={<Login setToken={setToken} />} />
                <Route path="/register" element={<Register />} />
                <Route path="/reports" element={<Reports />} />
                <Route path="/inventory" element={<Inventory />} />
                <Route path="/inventorymanager" element={<InventoryManager />} />
            </Routes>
        </Router>
    );
}

export default App;
