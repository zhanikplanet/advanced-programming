document.getElementById('predictButton').addEventListener('click', function() {
  var fileInput = document.getElementById('fileInput').files[0];
  var formData = new FormData();
  formData.append('file', fileInput);

  fetch('/predict', {
      method: 'POST',
      body: formData
  })
  .then(response => response.json())
  .then(data => {
      document.getElementById('predictionResult').innerText = 'Prediction: ' + data.prediction;
  })
  .catch(error => console.error('Error:', error));
});
