let currentQuestion = null;

// Screen management
function showScreen(screenId) {
    document.querySelectorAll('.screen').forEach(screen => screen.classList.remove('active'));
    document.getElementById(screenId).classList.add('active');
}

// File upload handling
document.getElementById('fileInput').addEventListener('change', async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();

        if (response.ok) {
            loadQuestion();
            showScreen('quizScreen');
        } else {
            alert(data.error);
        }
    } catch (error) {
        alert('Error al cargar el archivo');
    }
});

// Quiz functionality
async function loadQuestion() {
    try {
        const response = await fetch('/question');
        const data = await response.json();
        
        if (response.ok) {
            currentQuestion = data;
            document.getElementById('question').textContent = data.pregunta;
            document.getElementById('answer').textContent = data.respuesta;
            document.getElementById('answer').style.display = 'none';
        } else {
            alert(data.error);
        }
    } catch (error) {
        alert('Error al cargar la pregunta');
    }
}

// Button handlers
document.getElementById('correctBtn').addEventListener('click', async () => {
    await submitAnswer(true);
    loadQuestion();
});

document.getElementById('skipBtn').addEventListener('click', async () => {
    await submitAnswer(false);
    loadQuestion();
});

document.getElementById('hintBtn').addEventListener('click', () => {
    document.getElementById('answer').style.display = 'block';
});

document.getElementById('restartBtn').addEventListener('click', () => {
    showScreen('uploadScreen');
});

// Submit answer
async function submitAnswer(correct) {
    try {
        const response = await fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                correct,
                pregunta: currentQuestion.pregunta,
                respuesta: currentQuestion.respuesta
            })
        });
        
        const data = await response.json();
        
        if (data.total >= 10) {  // Show results after 10 questions
            showResults();
        }
    } catch (error) {
        alert('Error al enviar respuesta');
    }
}

// Show results
async function showResults() {
    try {
        const response = await fetch('/results');
        const data = await response.json();
        
        document.getElementById('percentage').textContent = data.percentage;
        
        const reviewList = document.getElementById('reviewList');
        reviewList.innerHTML = '';
        data.review_questions.forEach(q => {
            const item = document.createElement('div');
            item.className = 'review-item';
            item.innerHTML = `
                <p><strong>Pregunta:</strong> ${q.pregunta}</p>
                <p><strong>Respuesta:</strong> ${q.respuesta}</p>
            `;
            reviewList.appendChild(item);
        });
        
        showScreen('resultsScreen');
    } catch (error) {
        alert('Error al cargar resultados');
    }
}