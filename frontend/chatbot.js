const chatbotWindow = document.getElementById('chatbot-window');
const chatbotMessages = document.getElementById('chatbot-messages');
const chatbotInput = document.getElementById('chatbot-input');
const chatbotSend = document.getElementById('chatbot-send');
const chatbotBtn = document.getElementById('chatbot-button');
// chatbotBtn.innerHTML = '...'; // Removed to preserve custom icon from HTML

const closeBtn = document.getElementById('close-chatbot');

let conversationHistory = [];

function toggleChat() {
    const isVisible = chatbotWindow.style.display === 'flex';
    chatbotWindow.style.display = isVisible ? 'none' : 'flex';
    if (!isVisible && chatbotMessages.children.length === 0) {
        loadWelcomeMessage();
    }
}

chatbotBtn.addEventListener('click', toggleChat);
closeBtn.addEventListener('click', toggleChat);

async function loadWelcomeMessage() {
    try {
        const response = await fetch('http://localhost:8000/welcome');
        const data = await response.json();
        addMessage(data.message, 'bot');
    } catch (error) {
        addMessage("Hello 👋 Welcome to XYZON Support! How can I assist you today?", 'bot');
    }
}

function addMessage(text, sender) {
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message', `${sender}-message`);
    msgDiv.innerText = text;
    chatbotMessages.appendChild(msgDiv);
    chatbotMessages.scrollTop = chatbotMessages.scrollHeight;

    conversationHistory.push({ role: sender === 'bot' ? 'bot' : 'user', content: text });
}

async function sendMessage() {
    const text = chatbotInput.value.trim();
    if (!text) return;

    addMessage(text, 'user');
    chatbotInput.value = '';

    // Show typing indicator
    const typingIndicator = document.createElement('div');
    typingIndicator.innerText = 'XYZON Innovations is processing...';
    typingIndicator.classList.add('typing');
    chatbotMessages.appendChild(typingIndicator);

    try {
        const response = await fetch('http://localhost:8000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                message: text,
                history: conversationHistory
            })
        });

        const data = await response.json();
        chatbotMessages.removeChild(typingIndicator);
        addMessage(data.response, 'bot');
    } catch (error) {
        chatbotMessages.removeChild(typingIndicator);
        addMessage("Sorry, I'm having trouble connecting to the server. Please try again later.", 'bot');
    }
}

chatbotSend.addEventListener('click', sendMessage);
chatbotInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});

// Auto-open chatbot popup on website load
window.onload = () => {
    setTimeout(() => {
        if (chatbotWindow.style.display !== 'flex') {
            toggleChat();
        }
    }, 1000); // Small delay for better UX
};

