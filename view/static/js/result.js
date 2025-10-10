window.onload = function() {
    DisplayResult();
}

function DisplayResult() {
    const resultData = JSON.parse(sessionStorage.getItem('predictionResult'));
    if (!resultData) {
        document.getElementById('result-container').innerText = 'No result data found.';
        return;
    }
    document.getElementById('result').innerText = resultData.prediction;
}