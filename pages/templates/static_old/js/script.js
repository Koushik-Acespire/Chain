console.log("js is running")

document.addEventListener('DOMContentLoaded', () => {
    const burgerMenu = document.querySelector('.burger-menu');
    const navbar = document.querySelector('.navbar');
    const content = document.querySelector('.content');
    const userMsg = document.getElementById('userMessage');
    burgerMenu.addEventListener('click', () => {
        navbar.classList.toggle('active');
        content.style.paddingTop = navbar.classList.contains('active')
            ? `${navbar.offsetHeight}px` : '10px';
    }).then(response => response.json()).then(data => {
        const chat = document.getElementById('chat-section');
        chat.innerHTML += `<p><strong>You: ${userMsg}</strong></p>`;
        chat.innerHTML += `<p>Rudy: ${data.response}</p>`;
    });
});

document.addEventListener('DOMContentLoaded', () => {
    // Send message on button click
    document.getElementById('sendButton').addEventListener('click', function () {
        const userMessageInput = document.getElementById('userMessage');
        const messageText = userMessageInput.value.trim();

        if (messageText) {
            addMessage('user', messageText);
            userMessageInput.value = '';

            // Send user message to the server
            fetch('/chat', {  // Ensure this endpoint matches the one defined in Flask
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: messageText })
            })
                .then(response => response.json())
                .then(data => {
                    addMessage('bot', data.response);
                })
                .catch(error => {
                    addMessage('bot', 'Sorry, something went wrong.');
                });
        }
    });

    // Allow pressing Enter to send messages
    document.getElementById('userMessage').addEventListener('keypress', function (event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            document.getElementById('sendButton').click();
        }
    });

    // Function to add messages to the chat section
    function addMessage(sender, text) {
        const chatSection = document.getElementById('chat-section');
        const messageDiv = document.createElement('div');
        messageDiv.className = 'message ' + (sender === 'user' ? 'user-message' : 'bot-message');
        messageDiv.innerHTML = text.replace(/\n/g, '<br>');
        messageDiv.innerHTML = text.replace(/\t/g, '&nbsp;&nbsp;&nbsp;&nbsp;');
        chatSection.appendChild(messageDiv);
        chatSection.scrollTop = chatSection.scrollHeight; // Scroll to the bottom
    }
});



// bot 
document.addEventListener('DOMContentLoaded', function () {
    const chatButton = document.getElementById('chatButton');
    const chatSection = document.getElementById('chatSection');
    const closeButton = document.getElementById('closeButton');

    chatButton.addEventListener('click', function () {
        chatSection.style.display = 'block'; // Show the chat section
        chatButton.style.display = 'none'; // Hide the chat button
    });

    closeButton.addEventListener('click', function () {
        chatSection.style.display = 'none'; // Hide the chat section
        chatButton.style.display = 'block'; // Show the chat button
    });
});

document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.toggle-details').forEach(button => {
        button.addEventListener('click', function () {
            const targetId = this.getAttribute('data-target');
            const details = document.getElementById(targetId);
            const arrow = this.querySelector('.arrow');

            // Toggle the details
            if (details.classList.contains('show')) {
                details.classList.remove('show');
                arrow.classList.remove('up');
            } else {
                // Hide all details and arrows
                document.querySelectorAll('.details').forEach(detail => {
                    detail.classList.remove('show');
                });
                document.querySelectorAll('.arrow').forEach(a => {
                    a.classList.remove('up');
                });

                // Show the clicked detail and rotate arrow
                details.classList.add('show');
                arrow.classList.add('up');
            }
        });
    });
});