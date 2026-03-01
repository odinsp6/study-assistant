const chat = document.getElementById('chat');
const form = document.getElementById('chat-form');
const textarea = document.getElementById('message');
const sendBtn = document.getElementById('send-btn');

function addMessage(text, role) {
  const div = document.createElement('div');
  div.className = `message ${role}`;
  div.textContent = text;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const message = textarea.value.trim();
  if (!message) return;

  addMessage(message, 'user');
  textarea.value = '';
  sendBtn.disabled = true;

  try {
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message }),
    });

    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.error || 'Noe gikk galt.');
    }

    addMessage(data.reply, 'assistant');
  } catch (error) {
    addMessage(`Feil: ${error.message}`, 'assistant');
  } finally {
    sendBtn.disabled = false;
    textarea.focus();
  }
});

addMessage('Hei! Hva vil du lære i dag?', 'assistant');
