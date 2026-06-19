// content.js
const createToolbar = () => {
  const host = document.createElement('div');
  host.id = 'agentation-toolbar-root';
  // Position the host itself
  host.style.position = 'fixed';
  host.style.bottom = '2rem';
  host.style.left = '50%';
  host.style.transform = 'translateX(-50%)';
  host.style.zIndex = '2147483647';
  host.style.pointerEvents = 'none';

  const shadow = host.attachShadow({ mode: 'open' });

  // Load the CSS
  const link = document.createElement('link');
  link.rel = 'stylesheet';
  link.href = chrome.runtime.getURL('content.css');
  shadow.appendChild(link);

  const container = document.createElement('div');
  container.className = 'agentation-toolbar-container';
  container.innerHTML = `
    <div class="agentation-drag-handle">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M8 6H16M8 12H16M8 18H16" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
    <div class="agentation-actions">
      <button class="agentation-btn" id="agent-summarize" title="Summarize">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="21" y1="10" x2="3" y2="10"></line><line x1="21" y1="6" x2="3" y2="6"></line><line x1="21" y1="14" x2="3" y2="14"></line><line x1="14" y1="18" x2="3" y2="18"></line></svg>
      </button>
      <button class="agentation-btn" id="agent-explain" title="Explain">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
      </button>
      <button class="agentation-btn" id="agent-automate" title="Automate">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
      </button>
      <button class="agentation-btn agentation-chat-btn" id="agent-chat" title="Chat with Agent">
        <span>Agent</span>
      </button>
    </div>
  `;
  shadow.appendChild(container);
  document.body.appendChild(host);

  // Button Listeners
  container.querySelector('#agent-summarize').addEventListener('click', () => alert('Summarizing the page...'));
  container.querySelector('#agent-explain').addEventListener('click', () => alert('Explaining this content...'));
  container.querySelector('#agent-automate').addEventListener('click', () => alert('Automating workflow...'));
  container.querySelector('#agent-chat').addEventListener('click', () => alert('Opening Agent Chat...'));

  // Simple drag logic
  const handle = container.querySelector('.agentation-drag-handle');
  
  let isDragging = false;
  let currentX;
  let currentY;
  let initialX;
  let initialY;
  let xOffset = 0;
  let yOffset = 0;

  handle.addEventListener('mousedown', dragStart);
  document.addEventListener('mouseup', dragEnd);
  document.addEventListener('mousemove', drag);

  function dragStart(e) {
    initialX = e.clientX - xOffset;
    initialY = e.clientY - yOffset;
    isDragging = true;
  }

  function dragEnd(e) {
    initialX = currentX;
    initialY = currentY;
    isDragging = false;
  }

  function drag(e) {
    if (isDragging) {
      e.preventDefault();
      currentX = e.clientX - initialX;
      currentY = e.clientY - initialY;
      xOffset = currentX;
      yOffset = currentY;
      
      // Apply translation to the host element
      host.style.transform = `translate3d(calc(-50% + ${currentX}px), ${currentY}px, 0)`;
    }
  }
};

if (!document.getElementById('agentation-toolbar-root')) {
  createToolbar();
}
