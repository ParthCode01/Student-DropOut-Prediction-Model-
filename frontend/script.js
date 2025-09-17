async function getPrediction() {
    const data = {
        admission_grade: parseFloat(document.getElementById("admission_grade").value),
        sem_grade: parseFloat(document.getElementById("sem_grade").value),
        attendance: parseFloat(document.getElementById("attendance").value)
    };

    const response = await fetch("http://127.0.0.1:5000/predict", {
    method: "POST",  // must be POST
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
});



    const result = await response.json();
    document.getElementById("result").innerText = "Prediction: " + result.prediction;
}
