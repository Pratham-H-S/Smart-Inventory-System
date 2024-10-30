import React, { useState, useEffect } from "react";
import axios from "axios";
import { Line, Bar } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, BarElement, Title, Tooltip, Legend } from 'chart.js';
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

// Register necessary components for Chart.js
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, BarElement, Title, Tooltip, Legend);

const Reports = () => {
  const [stockAlerts, setStockAlerts] = useState({ dates: [], alerts: [] });
  const [salesInventory, setSalesInventory] = useState({ dates: [], levels: [], sales: [] });
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [startDate, setStartDate] = useState(new Date("2023-01-01"));
  const [endDate, setEndDate] = useState(new Date("2023-12-31"));

  // Fetch Stock Alerts Data
  const fetchStockAlerts = async () => {
    try {
      const response = await axios.get(`${process.env.REACT_APP_BACKEND_URL}/reports/stock-alerts-history`, {
        params: {
          start_date: startDate.toISOString().split('T')[0],
          end_date: endDate.toISOString().split('T')[0],
        },
      });

      const alertsData = response.data.reduce((acc, alert) => {
        acc.dates.push(alert.alert_date);
        acc.alerts.push(1);  // Assuming one alert per date
        return acc;
      }, { dates: [], alerts: [] });

      setStockAlerts(alertsData);
    } catch (err) {
      setError("Failed to fetch stock alerts data.");
    }
  };

  // Fetch Sales vs Inventory Data
  const fetchSalesVsInventory = async () => {
    try {
      const response = await axios.get(`${process.env.REACT_APP_BACKEND_URL}/reports/sales-vs-inventory`, {
        params: {
          start_date: startDate.toISOString().split('T')[0],
          end_date: endDate.toISOString().split('T')[0],
        },
      });

      const salesData = response.data.reduce((acc, sale) => {
        acc.dates.push(sale.sale_date);
        acc.levels.push(sale.inventory_level);
        acc.sales.push(sale.total_sale_value); // Ensure the correct field for sales
        return acc;
      }, { dates: [], levels: [], sales: [] });

      setSalesInventory(salesData);
    } catch (err) {
      setError("Failed to fetch sales vs inventory data.");
    } finally {
      setIsLoading(false); // Set loading to false after data fetching
    }
  };

  useEffect(() => {
    fetchStockAlerts();
    fetchSalesVsInventory();
  }, [startDate, endDate]); // Add dependencies to re-fetch data when dates change

  // Data for the Stock Alerts Line Graph
  const stockAlertsData = {
    labels: stockAlerts.dates,
    datasets: [
      {
        label: "Stock Alerts",
        data: stockAlerts.alerts,
        borderColor: "rgba(75, 192, 192, 1)",
        backgroundColor: "rgba(75, 192, 192, 0.2)",
        fill: true,
      },
    ],
  };

  // Data for the Sales vs Inventory Bar Graph
  const salesInventoryData = {
    labels: salesInventory.dates,
    datasets: [
      {
        label: "Inventory Levels",
        data: salesInventory.levels,
        backgroundColor: "rgba(54, 162, 235, 0.5)",
        borderColor: "rgba(54, 162, 235, 1)",
        borderWidth: 1,
      },
      {
        label: "Sales",
        data: salesInventory.sales,
        backgroundColor: "rgba(255, 99, 132, 0.5)",
        borderColor: "rgba(255, 99, 132, 1)",
        borderWidth: 1,
      },
    ],
  };

  return (
    <div>
      <h2>Reports</h2>
      {isLoading ? (
        <p>Loading data...</p>
      ) : (
        <>
          {error && <p style={{ color: "red" }}>{error}</p>}
          
          <div>
            <label>Select Start Date: </label>
            <DatePicker selected={startDate} onChange={date => setStartDate(date)} />
            <label>Select End Date: </label>
            <DatePicker selected={endDate} onChange={date => setEndDate(date)} />
          </div>
          
          <section>
            <h3>Stock Alerts</h3>
            <Line data={stockAlertsData} options={{ responsive: true }} />
          </section>

          <section>
            <h3>Sales vs Inventory</h3>
            <Bar data={salesInventoryData} options={{ scales: { y: { beginAtZero: true } } }} />
          </section>
        </>
      )}
    </div>
  );
};

export default Reports;
