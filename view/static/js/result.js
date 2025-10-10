window.onload = function() {
    DisplayResult();
}

function DisplayResult() {
    const resultData = JSON.parse(sessionStorage.getItem('predictionResult'));
    if (!resultData) {
        document.getElementById('result-container').innerText = 'No result data found.';
        return;
    }
    document.getElementById('result').innerText = resultData.prediction + ' - ' + resultData.faculty;
    document.body.style.background = `linear-gradient(135deg, ${resultData.color} 0%, #000000 100%)`;
}