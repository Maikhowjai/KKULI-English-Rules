Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course InfoBot</title>
    <link rel="icon" type="image/png" href="{{ url_for('static', filename='kku_english_logo.png') }}">
    <style>
        body { font-family: sans-serif; margin: 20px; background-color: #f4f4f4; }
        #logo {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 110px;
            margin-bottom: 10px;
            margin-top: 10px;
        }
        #chatbox {
            width: 90%;
            max-width: 600px;
            height: 400px;
            border: 1px solid #ccc;
            overflow-y: scroll;
            padding: 10px;
            margin-bottom: 10px;
            background-color: #fff;
            border-radius: 5px;
        }
        .message {
            margin-bottom: 10px;
            padding: 8px;
            border-radius: 5px;
        }
        .user-message {
            background-color: #d1e7dd; /* Light green for user */
            text-align: right;
            margin-left: 40px;
        }
        .bot-message {
            background-color: #f8d7da; /* Light red/pink for bot */
            text-align: left;
            margin-right: 40px;
        }
        #userInput {
            width: calc(90% - 60px); /* Adjust width considering the button */
            max-width: 530px;
            padding: 10px;
            margin-right: 5px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            padding: 10px 15px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover { background-color: #0056b3; }
    </style>
</head>
<body>
    <!-- Logo at the very top -->
    <img id="logo" src="{{ url_for('static', filename='kku_english_logo.png') }}" alt="KKU English Icon">
    
    <h1 style="text-align:center;">Course InfoBot</h1>
    <div id="chatbox">
        <!-- Initial bot message will be injected here by Flask -->
        <div class="message bot-message">{{ initial_message | safe }}</div>
    </div>
    <div>
        <input type="text" id="userInput" placeholder="Ask something..." autofocus>
        <button onclick="sendMessage()">Send</button>
    </div>

    <script>
        // Get the initial message passed from Flask and display it
        // (This part is now handled directly in the HTML template above with {{ initial_message }})

        const chatbox = document.getElementById('chatbox');
        const userInput = document.getElementById('userInput');

        function appendMessage(message, sender) {
            const messageDiv = document.createElement('div');
            messageDiv.classList.add('message');
            messageDiv.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
            messageDiv.innerHTML = message; // Use innerHTML to render <br> tags
            chatbox.appendChild(messageDiv);
            chatbox.scrollTop = chatbox.scrollHeight; // Auto-scroll to bottom
        }
... 
...         async function sendMessage() {
...             const messageText = userInput.value.trim();
...             if (messageText === "") return;
... 
...             appendMessage(messageText, 'user');
...             userInput.value = ""; // Clear input field
... 
...             try {
...                 const response = await fetch('/get_response', {
...                     method: 'POST',
...                     headers: {
...                         'Content-Type': 'application/x-www-form-urlencoded', // Standard for form data
...                     },
...                     body: `user_message=${encodeURIComponent(messageText)}`
...                 });
... 
...                 if (!response.ok) {
...                     throw new Error(`HTTP error! status: ${response.status}`);
...                 }
... 
...                 const data = await response.json();
...                 appendMessage(data.bot_response, 'bot');
...             } catch (error) {
...                 console.error('Error sending message:', error);
...                 appendMessage("Sorry, something went wrong. Please try again.", 'bot');
...             }
...         }
... 
...         // Allow sending message with Enter key
...         userInput.addEventListener('keypress', function(event) {
...             if (event.key === 'Enter') {
...                 sendMessage();
...             }
...         });
...     </script>
... </body>
