async function predictText() {
questions = document.querySelectorAll('.question-textarea');
submitBtn = document.getElementById('submit-btn');
let questionData = {};
questions.forEach((question, index) => {
    if (question.value.trim() === '') {
        showError('Please fill in all the questions before submitting.');
        return;
    }
    questionData[`question${index + 1}`] = question.value;
});
    submitBtn.disabled = true;
    showElements('loading-indicator');
    hideElements('error-message');
    console.log(questionData);

    try{
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(questionData)
        });
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'An error occurred while processing your request.');
        }
        const result = await response.json();
        sessionStorage.setItem('predictionResult', JSON.stringify(result));
        window.location.href = '/result';
    } catch(error){
        console.error('Error:', error);
        showError("Wystąpił błąd: " +error.message);
        submitBtn.disabled = false;
        submitBtn.innerText = 'Dowiedz się do jakiego wydziału należysz';
        hideElements('loading-indicator');
    }
    
}
showError = (message) => {
    const errorDiv = document.getElementById('error-message');
    errorDiv.innerText = message;
    errorDiv.classList.remove('hidden');
}
showElements = (id) => {
    document.getElementById(id).classList.remove('hidden');
}
hideElements = (id) => {
    document.getElementById(id).classList.add('hidden');
}