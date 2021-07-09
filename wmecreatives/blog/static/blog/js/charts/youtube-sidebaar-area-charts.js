var ctx = document.getElementById("myChart").getContext('2d');

var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ["Jan", "Feb", "March",  "April", "May",  "June"],
        datasets: [
        // {
        //     label: 'Jan - March', 
        //     data: [500, 50, 2424, 14040,  14141,  4111, 4544, 47, 5555, 6811], 
        //     fill: true,
        //     borderColor: '#2196f3', 
        //     backgroundColor: '#43AEC4', 
        //     borderWidth: 1 
        // },
                  {
            label: 'Total video clicks changes for the past 6 months', // Name the series
            data: [1288,  88942,  44545,  7588, 99, 242], // Specify the data values array
            fill: true,
            borderColor: '#4CAF50', // Add custom color border (Line)
            backgroundColor: '#4CAF50', // Add custom color background (Points and Fill)
            borderWidth: 1 // Specify bar border width
        }]
    },
    options: {
      responsive: true, // Instruct chart js to respond nicely.
      maintainAspectRatio: false, // Add to prevent default behaviour of full-width/height 
    }
});