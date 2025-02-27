document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatOutput = document.getElementById('chat-output');

    chatForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const userMessage = chatInput.value;
        appendMessage('You: ' + userMessage);
        chatInput.value = '';

        fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userMessage })
        })
        .then(response => response.json())
        .then(data => {
            appendMessage('Glitch: ' + data.response);
        })
        .catch(error => {
            console.error('Error:', error);
            appendMessage('Glitch: Sorry, there was an error processing your request.');
        });
    });

    function appendMessage(message) {
        const messageElement = document.createElement('div');
        messageElement.className = 'mb-2 p-2'; // Add margin and padding

        if (message.startsWith('You:')) {
            const prefix = document.createElement('span');
            prefix.textContent = 'You:';
            prefix.className = 'font-bold text-blue-800'; // Bold and dark blue
            
            const content = document.createElement('span');
            content.textContent = message.substring(4); // Remove "You:" from content
            
            messageElement.appendChild(prefix);
            messageElement.appendChild(document.createTextNode(' ')); // Add space
            messageElement.appendChild(content);
        } else if (message.startsWith('Glitch:')) {
            const prefix = document.createElement('span');
            prefix.textContent = 'Glitch:';
            prefix.className = 'font-bold text-sky-600'; // Bold and sky blue
            
            const content = document.createElement('span');
            content.textContent = message.substring(7); // Remove "Glitch:" from content
            
            messageElement.appendChild(prefix);
            messageElement.appendChild(document.createTextNode(' ')); // Add space
            messageElement.appendChild(content);
        } else {
            messageElement.textContent = message;
        }

        chatOutput.appendChild(messageElement);
        chatOutput.scrollTop = chatOutput.scrollHeight; // Auto-scroll to bottom
    }
});