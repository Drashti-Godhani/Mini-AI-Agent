import json
import re
from openai import OpenAI
from dotenv import load_dotenv
import os
from tools import TOOLS 

load_dotenv(dotenv_path=".env")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "add_task",
            "description": "Add a task to the task list",
            "parameters": {
                "type": "object",
                "properties": {
                    "task": {
                        "type": "string",
                        "description": "Task to add"
                    }
                },
                "required": ["task"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_tasks",
            "description": "List all tasks",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
    "type": "function",
    "function": {
        "name": "delete_task",
        "description": "Delete a task by its number",
        "parameters": {
            "type": "object",
            "properties": {
                "index": {
                    "type": "integer",
                    "description": "Task number to delete"
                }
            },
            "required": ["index"]
        }
    }
    },
    {
        "type":"function",
        "function": {
            "name":"read_file",
            "description":"read from the file",
            "parameters": {
                "type":"object",
                "properties": {
                    "filename": {
                        "type":"string",
                        "description":"name of the file read"
                    }
                },
                "required":["filename"]
            }
        }
    },
    {
    "type": "function",
    "function": {
        "name": "calculate",
        "description": "Perform a mathematical calculation",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Math expression to evaluate"
                }
            },
            "required": ["expression"]
        }
    }
},
{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get weather information for a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "City name"
                }
            },
            "required": ["city"]
        }
    }
}
]

conversation_history = []

def run_agent(user_prompt):

    print("INPUT =", repr(user_prompt))

    if user_prompt.lower() == "date":
        return TOOLS["get_date"]()

    if user_prompt.lower() == "time":
        return TOOLS["get_time"]()

    if user_prompt.strip().startswith("/extract"):
        print("EXTRACT MODE")
        
        text = user_prompt.strip().replace("/extract", "", 1).strip()

        name_match = re.search(r"([A-Z][a-z]+)", text)
        age_match = re.search(r"(\d+)", text)
        city_match = re.search(r"lives in ([A-Za-z]+)", text)

        result = {
            "name": name_match.group(1) if name_match else None,
            "age": int(age_match.group(1)) if age_match else None,
            "city": city_match.group(1) if city_match else None
        }

        return json.dumps(result, indent=2)


    if user_prompt.lower().startswith("add task"):
        task = user_prompt[8:].strip()
        return TOOLS["add_task"](task)
    
    if user_prompt.lower() in ["list tasks", "show tasks"]:
        return TOOLS["list_tasks"]()
    
    if user_prompt.lower().startswith("delete task"):
        try:
            index = int(user_prompt.split()[-1])
            return TOOLS["delete_task"](index)
        except:  # noqa: E722
            return "Usage: delete task <number>"
        
    if user_prompt.lower().startswith("read file"):
        filename=user_prompt[9:].strip()
        return TOOLS["read_file"](filename)
    
    if user_prompt.lower().startswith("calculate"):
        expression = user_prompt[9:].strip()
        return TOOLS["calculate"](expression)
    
    if user_prompt.lower().startswith("weather"):
        city = user_prompt[7:].strip()
        return TOOLS["get_weather"](city)
    
    conversation_history.append(
        {"role": "user", "content": user_prompt}
    )

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=conversation_history
    )

    assistant_reply = response.choices[0].message.content

    conversation_history.append(
        {"role": "assistant", "content": assistant_reply}
    )

    if len(conversation_history) > 10:
        conversation_history[:] = conversation_history[-10:]

    return assistant_reply


if __name__ == "__main__":
    while True:
        prompt = input("You: ")

        if prompt.lower() == "exit":
            break

        print("Assistant:", run_agent(prompt))

