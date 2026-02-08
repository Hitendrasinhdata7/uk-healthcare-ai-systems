
// ── NEW FUNCTIONALITY: Last 3 symptoms viewed history ──

const HISTORY_KEY = 'symptomHistory';
const MAX_HISTORY = 3;

function addToHistory(symptom) {
  if (!symptom || typeof symptom !== 'string') return;
  
  let history = JSON.parse(localStorage.getItem(HISTORY_KEY) || '[]');
  
  // Remove if already exists (move to front)
  history = history.filter(s => s !== symptom);
  
  // Add new one at beginning
  history.unshift(symptom);
  
  // Keep only last MAX_HISTORY
  history = history.slice(0, MAX_HISTORY);
  
  localStorage.setItem(HISTORY_KEY, JSON.stringify(history));
  
  updateHistoryDisplay();
}

function updateHistoryDisplay() {
  const container = document.getElementById('history-list');
  if (!container) return;
  
  const history = JSON.parse(localStorage.getItem(HISTORY_KEY) || '[]');
  container.innerHTML = '';
  
  if (history.length === 0) {
    container.innerHTML = '<li>No recent searches</li>';
    return;
  }
  
  history.forEach(symptom => {
    const li = document.createElement('li');
    li.textContent = symptom;
    li.style.cursor = 'pointer';
    li.style.color = '#0066cc';
    li.onclick = () => {
      document.getElementById('symptom-search').value = symptom;
      findHelp(); // assuming your existing search function is called findHelp()
    };
    container.appendChild(li);
  });
}

// Call once on page load
window.addEventListener('load', updateHistoryDisplay);

// ── You must also call addToHistory() when user views a symptom ──
// Example: add this line inside your findHelp() or show result function:
// addToHistory(input.trim());     ← add this where you process the symptom

