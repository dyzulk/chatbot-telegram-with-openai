<p align="center">
  <a  href="https:t.me/EndayWithGPTBot"><img alt="Avatar Bot Image" src="https://raw.githubusercontent.com/dyzulk/dyzulk/main/favicon.png" width="250px" /> </a>
  <h1 align="center">EndayWithOpenAI</h1>
</p>

# Introduction

This project is created to fulfill one of the requirements for the selection stage of OPREC LAB SEIC ITPLN 👨🏻‍💻 ⚡
Firstly, I would like to express my sincere gratitude to all my friends who have provided support and offered constructive criticism and suggestions.

In this project, I implemented Chat OpenAI with a Telegram bot. The main objective of this project is to create a bot that can communicate with users through messages and provide responses based on user requests.

At the beginning of the source code, several modules and libraries are imported such as ```os```, ```openai```, ```dotenv```, ```aiogram```, and ```keep_alive```. Then, environment variables are retrieved using the ```os.getenv()``` method, and the Telegram bot token is stored in the ```tgBot_token``` variable. The OpenAI API key is also retrieved and stored in the ```openAi_token``` variable.

Next, message handlers are defined using the ```dp.message_handler()``` decorator. There are message handlers for the ```/start```, ```/command```, ```/help```, and ```/stop``` commands. The ```welcome``` function is used to provide a welcome message to the user and introduce the purpose of this project. The ```left``` function provides a list of available commands. The ```documentation``` function gives instructions and tactics for getting better responses. The ```gpt``` function is the default message handler used to send the user's prompt to the OpenAI model and generate a response that is sent back to the user.

At the end of the source code, the ```keep_alive()``` function is called to keep the bot active, and the program starts monitoring incoming messages using the ```executor.start_polling(dp)``` method.

Thus, this source code allows the development of a Telegram bot that uses the OpenAI GPT model to engage in conversations with users.

# How To Install

### Prerequisites

- Python 3.7. or higher. <a href="https://www.python.org/downloads" target="_blank"><strong>Download Here</strong></a>
    - Install Modul/Framework/Library

        ```
        pip install os
        ```
        ```
        pip install openai
        ```
        ```
        pip install python-dotenv
        ```
        ```
        pip install aiogram
        ```
        and this optional :
        ```
        pip install keep_alive
        ```

### Clone The Repository

1. Open a terminal (Command Prompt on Windows or Terminal on macOS/Linux).
2. Navigate to the directory where you want to save the cloned repository (e.g., cd /path/to/folder).
3. Type the git clone command followed by the copied repository URL 
4. Copy this :  and press Enter.
```sh
git clone https://github.com/dyzulk/chatbot-telegram-with-openai.git
```
5. Wait for a moment until the cloning process is complete. Once finished, you will have a local copy of the repository in the specified directory.
6. By following these steps, you have successfully cloned the project from the GitHub repository to your local machine.

### Or Download This Release

<a href="https://github.com/dyzulk/chatbot-telegram-with-openai/archive/refs/heads/main.zip"><img alt="Download Button" src="https://cdn.dyzulk.com/assets/image/download-button.png" width="150px" /></a>

### Change The API Token

```sh
tgBot_token=API_TOKEN_BOT
openAi_token=API_TOKEN_OPENAI
```

To replace them with valid API tokens, you need to obtain the tokens from the respective services. For example, if you want to use the Telegram Bot API token, you need to register your bot with BotFather and obtain a valid bot token from there. Similarly, if you want to use the OpenAI API token, you need to have an OpenAI account and obtain a valid API token from your account's settings panel.

Once you have the valid tokens, replace "API_TOKEN_BOT" with the provided Telegram bot token and replace "API_TOKEN_OPENAI" with the provided OpenAI token. Make sure to remove the double quotation marks around the tokens to ensure they are recognized as valid strings in the code.

By making these replacements, you will set the values of the tgBot_token and openAi_token variables according to the required API tokens for your application.

If the .env file does not exist, create a duplicate of the .env.example file then change the name to .env

### Change reply message

You can change reply message on

```
async def welcome(message: types.Message):
  await message.reply(
    "FILL_CHAT_MESSAGE_HERE"
  )
```

Or message with a separate chat bubble

```
  async def welcome(message: types.Message):
  await message.reply(
    "FILL_CHAT_MESSAGE_HERE"
  )
  await message.reply(
    "FILL_CHAT_MESSAGE_HERE"
  )
```


# Support Us

You can support me on the SociaBuzz platform! Your support would be greatly appreciated, but even starring this project would be really helpful!

<a href="https://sociabuzz.com/dyzulkdeveloper/support" target="_blank"><strong>Support Here</strong></a>
