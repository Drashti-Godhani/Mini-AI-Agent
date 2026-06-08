from datetime import datetime
TOOLS={}

tasks = []

def get_date():
    return datetime.now().strftime("%d-%m-%Y")

def get_time():
    return datetime.now().strftime("%H:%M:%S")

def add_task(task):
    tasks.append(task)
    return f"Task added: {task}"

def list_tasks():
    if not tasks:
        return "No tasks found."

    return "\n".join(
        [f"{i+1}. {task}" for i, task in enumerate(tasks)]
    )

def delete_task(index):
    try:
        removed_task = tasks.pop(index - 1)
        return f"Task deleted: {removed_task}"
    except IndexError:
        return "Invalid task number."

def read_file(filename):
    try:
        with open (filename,"r",encoding="utf-8")as f:
            return f.read()
    except FileNotFoundError:
        return f"file '{filename}' not found"
    except Exception as e:
        return str(e)
    
def calculate(expression):
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Calculation error: {e}"

def get_weather(city):
    weather_data = {
        "surat": "32°C, Sunny",
        "ahmedabad": "34°C, Partly Cloudy",
        "mumbai": "30°C, Rainy",
        "delhi": "38°C, Hot"
    }

    return weather_data.get(
        city.lower(),
        f"Weather data not available for {city}"
    )

TOOLS = {
    "get_date":get_date,
    "get_time":get_time,
    "add_task": add_task,
    "list_tasks": list_tasks,
    "delete_task":delete_task,
    "read_file":read_file,
    "calculate":calculate,
    "get_weather":get_weather
}
