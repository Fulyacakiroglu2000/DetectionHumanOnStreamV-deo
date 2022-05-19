const config = {
    apiKey: "AIzaSyC9LixRBJZ24NvjFfhFtOgjD0KPqEkwBXI",
    authDomain: "countingpeople-f2000.firebaseapp.com",
    databaseURL: "https://countingpeople-f2000-default-rtdb.europe-west1.firebasedatabase.app",
    projectId: "countingpeople-f2000",
    storageBucket: "countingpeople-f2000.appspot.com",
    messagingSenderId: "685543171251",
    appId: "1:685543171251:web:9506a5c155d4450bf37cc6",
    measurementId: "G-1LKY1ZH2NQ"
};

firebase.initializeApp(config);


const nbOfElts = 300;


firebase.database().ref('timestamped_measures').limitToLast(nbOfElts).on('value', ts_measures => {

    let timestamps = [];
    let values = [];


    ts_measures.forEach(ts_measure => {

        timestamps.push(moment(ts_measure.val().timestamp).format('YYYY-MM-DD HH:mm:ss'));
        values.push(ts_measure.val().value);
    });


    myPlotDiv = document.getElementById('myPlot');


    const data = [{
        x: timestamps,
        y: values
    }];

    const layout = {
        title: '<b>Number of People/TIMEGraph</b>',
        titlefont: {
            family: 'Courier New, monospace',
            size: 16,
            color: '#000'
        },
        xaxis: {
            title: '<b>time</b>',
            linecolor: 'black',
            linewidth: 2
        },
        yaxis: {
            title: '<b>number of people</b>',
            titlefont: {
                family: 'Courier New, monospace',
                size: 14,
                color: '#000'
            },
            linecolor: 'black',
            linewidth: 2,
        },
        margin: {
            r: 50,
            pad: 0
        }
    }

    Plotly.newPlot(myPlotDiv, data, layout, { responsive: true });
});