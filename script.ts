document.addEventListener('DOMContentLoaded', () => {
    const messagesElement = document.getElementById('messages');
    const inputElement = document.getElementById('input');

    // Function to add message to chat box
    function addMessage(content, sender) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', sender);

        const contentElement = document.createElement('div');
        contentElement.classList.add('content');
        contentElement.textContent = content;

        messageElement.appendChild(contentElement);
        messagesElement.appendChild(messageElement);
        messagesElement.scrollTop = messagesElement.scrollHeight;
    }

    // Event listener for input field
    inputElement.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' && inputElement.value.trim() !== '') {
            const message = inputElement.value.trim();
            addMessage(message, 'player');
            inputElement.value = '';

            // Simulate AI response
            setTimeout(() => {
                addMessage('Command received!', 'ai');
            }, 1000);
        }
    });

    // Initialize map
    const mapElement = document.getElementById('map');
    const robots = [
        { id: 'Robot1', start: { x: 1, y: 9 }, end: { x: 8, y: 2 } },
        { id: 'Robot2', start: { x: 2, y: 8 }, end: { x: 7, y: 3 } },
        { id: 'Robot3', start: { x: 3, y: 7 }, end: { x: 6, y: 4 } }
    ];

    robots.forEach(robot => {
        const startElement = document.createElement('div');
        startElement.classList.add('robot');
        startElement.style.left = `${robot.start.x * 10}%`;
        startElement.style.top = `${robot.start.y * 10}%`;
        startElement.textContent = `${robot.id} (Start)`;

        const endElement = document.createElement('div');
        endElement.classList.add('robot');
        endElement.style.left = `${robot.end.x * 10}%`;
        endElement.style.top = `${robot.end.y * 10}%`;
        endElement.textContent = `${robot.id} (End)`;

        mapElement.appendChild(startElement);
        mapElement.appendChild(endElement);
    });
});
