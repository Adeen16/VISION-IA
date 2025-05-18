const form = document.getElementById('uploadForm');
const resultCard = document.getElementById('resultCard');

form.addEventListener('submit', function (e) {
  e.preventDefault();

  const age = document.getElementById('age').value;
  const screenTime = document.getElementById('screenTime').value;
  const diet = document.getElementById('diet').value;
  const file = document.getElementById('retinaImage').files[0];

  if (!file) {
    alert('Please upload an image');
    return;
  }

  const formData = new FormData();
  formData.append('file', file);
  formData.append('age', age);
  formData.append('screen_time', screenTime);
  formData.append('diet', diet);

  resultCard.innerHTML = `<p class="text-blue-400">Analyzing...</p>`;

  fetch('http://localhost:8000/predict', {
    method: 'POST',
    body: formData
  })
    .then(res => res.json())
    .then(data => {
      if (data.error) {
        resultCard.innerHTML = `<p class="text-red-500">${data.error}</p>`;
      } else {
        resultCard.innerHTML = `
          <h3 class="text-2xl font-semibold mb-4">Diagnosis: ${data.diagnosis}</h3>
          <p class="mb-2">Recommended Treatment: ${data.treatment}</p>
          <p class="mb-2">Lifestyle Plan:</p>
          <ul class="list-disc pl-6 mb-4">
            ${data.lifestyle.map(item => `<li>${item}</li>`).join('')}
          </ul>
          <p class="mt-4 text-green-400">Risk Score: ${data.risk_score}</p>
        `;
      }
    })
    .catch(() => {
      resultCard.innerHTML = `<p class="text-red-500">Something went wrong. Please try again.</p>`;
    });
});
