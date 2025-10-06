questions = document.querySelectorAll('.question-textarea');
submitBtn = document.getElementById('submit-btn');
submitBtn.addEventListener('click', () => {
    let questionData = {};
    questions.forEach((question, index) => {
        questionData[`question${index + 1}`] = question.value;
    });
    console.log(questionData);
});