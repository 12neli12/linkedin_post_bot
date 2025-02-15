# LinkedIn Post Bot

This script uses Selenium and OpenAI libraries to generate content for Linedin. It takes the title from a text file. 
Then it is used as prompt to generate content from gpt-4 model. The post then is posted in the account using Selenium.

## Features

- Logs into LinkedIn using Selenium.
- Reads a post title from a file.
- Generates a stylish LinkedIn post using OpenAI's GPT-4.
- Automates the posting process.

## Installation

### Prerequisites

Make sure Python and Google Chrome are installed. If you don't want to use Google Chrome change Webdrivers.

### Setup

1. Clone the rep:
   ```sh
   git clone https://github.com/12neli12/linkedin_post_bot.git
   cd linkedin-post-bot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Write your credentials:
   - In `main.py` and add your email and password.
   - In `post_gen.py` add your OpenAI API key.
4. Add the post title inside posts/post_titles.txt.

## Usage

Run the script:

```sh
py main.py
```

## Dependencies

- Selenium
- OpenAI API
- Requests

## Notes

- Ensure you have a stable internet connection while running the bot.
- Make sure to leave a ⭐!
