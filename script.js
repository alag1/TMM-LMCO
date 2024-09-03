document.addEventListener("DOMContentLoaded", function() {
    const chatBox = document.querySelector('.chat-box');
    
    function addMessage(message) {
        const chatMessage = document.createElement('div');
        chatMessage.classList.add('chat-message');

        const aiSymbol = document.createElement('span');
        aiSymbol.classList.add('ai-symbol');
        aiSymbol.textContent = '🤖';

        const messageText = document.createElement('span');
        messageText.classList.add('message');
        messageText.textContent = message;

        chatMessage.appendChild(aiSymbol);
        chatMessage.appendChild(messageText);

        chatBox.appendChild(chatMessage);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    // Example of adding a new message
    addMessage("New mission objective: Reach the marked location.");
});
