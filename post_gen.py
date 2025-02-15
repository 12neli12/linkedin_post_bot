from openai import OpenAI
import requests

OPEN_AI_KEY = "" # Put OpenAI key here

# Reads 1st title, if empty throws error
def read_title():
    try:
        with open("posts/post_titles.txt", "r") as file:
            title = file.readline().strip()
            if not title:
                raise ValueError("There is no title!")
            return title
    except FileNotFoundError:
        raise ValueError(f"File'{file}' not found!")

# Generates Content
def generate_content(key, title):
    url = "https://api.openai.com/v1/chat/completions"  # Example endpoint

    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }

    # Request payload
    data = {
        "model": "gpt-4o-mini",  # Specify the model
        "messages": [{"role": "user", "content": f"Write a very good and stylish Linkedin post with title {title}. No emojis!"}],
        "temperature": 0.7
    }

    # Send the POST request
    response = requests.post(url, headers=headers, json=data)

    # Handle the response
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

# Used to pass content to main.py
def create_content():
    post_title = read_title()
    content = generate_content(OPEN_AI_KEY, post_title)

    if content:
        print(f"Content of post: {post_title} successfully generated!")
        return content
    else:
        print(f"Content of post: {post_title} could not be generated!")
        return None


