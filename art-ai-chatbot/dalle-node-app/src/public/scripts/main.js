document.addEventListener('DOMContentLoaded', () => {
    const generateButton = document.getElementById('generateButton');
    const userInput = document.getElementById('userInput');
    const imageContainer = document.getElementById('imageContainer');

    generateButton.addEventListener('click', async () => {
        const prompt = userInput.value.trim();
        
        if (!prompt) {
            alert('Please enter a description');
            return;
        }

        try {
            generateButton.disabled = true;
            generateButton.textContent = 'Generating...';

            const response = await fetch('/api/images/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt }),
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Failed to generate image');
            }

            const img = document.createElement('img');
            img.src = data.imageUrl;
            img.alt = prompt;
            
            imageContainer.innerHTML = '';
            imageContainer.appendChild(img);

        } catch (error) {
            alert('Error: ' + error.message);
        } finally {
            generateButton.disabled = false;
            generateButton.textContent = 'Generate Image';
        }
    });
});