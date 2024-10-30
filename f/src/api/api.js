// import axios from 'axios';

// // Set up base URL for backend API
// const API_BASE_URL = 'http://localhost:8000';

// // Set JWT Token for Authorization
// const setAuthToken = (token) => {
//     if (token) {
//         axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
//     } else {
//         delete axios.defaults.headers.common["Authorization"];
//     }
// };

// // API calls for Authentication, Inventory, Suppliers
// export const loginUser = (data) => axios.post(`${API_BASE_URL}/auth/login`, data);
// export const registerUser = (data) => axios.post(`${API_BASE_URL}/auth/register`, data);
// export const getInventory = () => axios.get(`${API_BASE_URL}/inventory`);
// export const addInventory = (data) => axios.post(`${API_BASE_URL}/inventory`, data);
// export const getSuppliers = () => axios.get(`${API_BASE_URL}/suppliers`);
// export const addSupplier = (data) => axios.post(`${API_BASE_URL}/suppliers`, data);

// export default setAuthToken;
import axios from 'axios';

// Set up base URL for backend API

import qs from 'qs';

// Set up base URL for backend API
const API_BASE_URL = 'http://localhost:8000';

// Set JWT Token for Authorization
const setAuthToken = (token) => {
    if (token) {
        axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
    } else {
        delete axios.defaults.headers.common["Authorization"];
    }
};

// API calls for Authentication, Inventory, Suppliers
export const loginUser = async (data) => {
    try {
        // Convert data to application/x-www-form-urlencoded format
        const response = await axios.post(`${API_BASE_URL}/auth/login`, qs.stringify(data), {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        });
        return response;
    } catch (error) {
        console.error("Login Error:", error.response ? error.response.data : error.message);
        throw error; // Re-throw error for handling in the component
    }
};

export const registerUser = async (data) => {
    try {
        // Send POST request to register endpoint
        const response = await axios.post(`${API_BASE_URL}/auth/register`, data);
        return response;
    } catch (error) {
        console.error("Registration Error:", error.response ? error.response.data : error.message);
        throw error;
    }
};

export const getInventory = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/inventory`);
        return response;
    } catch (error) {
        console.error("Get Inventory Error:", error.response ? error.response.data : error.message);
        throw error;
    }
};

export const addInventory = async (data) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/inventory`, data);
        return response;
    } catch (error) {
        console.error("Add Inventory Error:", error.response ? error.response.data : error.message);
        throw error;
    }
};

export const getSuppliers = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/suppliers`);
        return response;
    } catch (error) {
        console.error("Get Suppliers Error:", error.response ? error.response.data : error.message);
        throw error;
    }
};

export const addSupplier = async (data) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/suppliers`, data);
        return response;
    } catch (error) {
        console.error("Add Supplier Error:", error.response ? error.response.data : error.message);
        throw error;
    }
};

// Export the function to set the token
export default setAuthToken;
