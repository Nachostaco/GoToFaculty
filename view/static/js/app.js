async function predictText() {
questions = document.querySelectorAll('.question-textarea');
submitBtn = document.getElementById('submit-btn');
submitBtn.addEventListener('click', async () => {
    let questionData = [];
    questions.forEach((question, index) => {
        questionData.push({
            id: index + 1,
            text: question.value
        });
    });
    console.log(questionData);
    const response = await fetch('/predict/api', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(questionData)
    });
    const result = await response.json();
    console.log(result);
});
    
}