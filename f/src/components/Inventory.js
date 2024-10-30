import React, { useState, useEffect } from 'react';
import { getInventory, addInventory } from '../api/api';

function Inventory() {
    const [inventoryItems, setInventoryItems] = useState([]);
    const [formData, setFormData] = useState({ name: '', quantity: 0, price: 0 });

    useEffect(() => {
        async function fetchInventory() {
            const response = await getInventory();
            setInventoryItems(response.data);
        }
        fetchInventory();
    }, []);

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        await addInventory(formData);
        alert('Item added successfully');
    };

    return (
        <div>
            <h2>Inventory</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    placeholder="Item Name"
                />
                <input
                    type="number"
                    name="quantity"
                    value={formData.quantity}
                    onChange={handleChange}
                    placeholder="Quantity"
                />
                <input
                    type="number"
                    name="price"
                    value={formData.price}
                    onChange={handleChange}
                    placeholder="Price"
                />
                <button type="submit">Add Item</button>
            </form>
            <div>
                <h3>Inventory List</h3>
                <ul>
                    {inventoryItems.map(item => (
                        <li key={item.id}>{item.name} - {item.quantity}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default Inventory;
