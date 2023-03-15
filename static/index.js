// Retrieve the readings data from Flask API
fetch('/oxygen')
  .then(response => response.json())
  .then(data => {
    // Extract the timestamp and oxygen_level data
    const timestamps = data.map(reading => reading.timestamp);
    const oxygenLevels = data.map(reading => reading.oxygen_level);

    // Display the data in a line chart
    const ctx = document.getElementById('chart').getContext('2d');
    const chart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: timestamps,
        datasets: [
          {
            label: 'Oxygen Level',
            data: oxygenLevels,
            borderColor: 'blue',
            fill: false
          }
        ]
      },
      options: {
        responsive: true,
        scales: {
          xAxes: [{
            type: 'time',
            time: {
              unit: 'day'
            }
          }],
          yAxes: [{
            ticks: {
              beginAtZero: true
            }
          }]
        }
      }
    });
  });