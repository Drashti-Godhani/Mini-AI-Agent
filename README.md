# Mini AI Agent

A simple AI-powered chatbot built using Python and OpenRouter/OpenAI APIs.

## Features

### 1. Basic Chat
- Ask any question and get an AI-generated response.

### 2. Memory (Last 5 Interactions)
- Stores the last 5 user-assistant interactions.
- Supports follow-up questions.

Example:
```
You: My name is John
You: What is my name?
```

### 3. Task Manager
- Add tasks
- List tasks
- Delete tasks

Commands:
```
add task Buy milk
list tasks
delete task 1
```

### 4. File Reader
Read the contents of a text file.

Command:
```
read file example.txt
```

### 5. Calculator
Perform mathematical calculations.

Command:
```
calculate 10 + 20
calculate 5 * 8
```

### 6. Weather Lookup (Mock)
Get mock weather information.

Command:
```
weather surat
weather mumbai
```

### 7. Structured Output Mode
Extract structured information in JSON format.

Command:
```
/extract John is 25 and lives in Mumbai
```

Output:
```json
{
  "name": "John",
  "age": 25,
  "city": "Mumbai"
}
```

### 8. Date & Time
Get current date and time.

Commands:
```
date
time
```

---

## Project Structure

```
Mini-AI-Agent/
│
├── agent.py
├── tools.py
├── example.txt
├── .env
└── README.md
```

---

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd Mini-AI-Agent
```

2. Create virtual environment

```bash
python -m venv venv
```

3. Activate virtual environment

Windows:

```bash
venv\Scripts\activate
```

4. Install dependencies

```bash
pip install openai python-dotenv
```

5. Create `.env` file

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

## Run the Project

```bash
python agent.py
```

Exit the chatbot:

```text
exit
```

---

## Technologies Used

- Python
- OpenRouter API
- OpenAI SDK
- python-dotenv
