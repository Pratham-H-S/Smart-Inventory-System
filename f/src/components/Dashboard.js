import React from 'react';
import { Line } from 'react-chartjs-2';

function Dashboard({ inventoryData, stockAlertData }) {
    const inventoryLevelsOverTime = {
        labels: inventoryData.dates,
        datasets: [
            {
                label: 'Inventory Levels',
                data: inventoryData.levels,
                borderColor: 'blue',
                fill: false,
            },
        ],
    };

    return (
        <div>
            <h2>Inventory Dashboard</h2>
            <div>
                <Line data={inventoryLevelsOverTime} />
            </div>
        </div>
    );
}

export default Dashboard;
