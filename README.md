# DiscordGpt

DiscordGpt bot is a discord bot that uses OpenAI's GPT-3 API to generate responses to user questions.

## Installation

1. Clone the repository

2. Install the requirements

```bash
pipenv install
```

2.1. If you don't have pipenv installed, install it with

```bash
pip install pipenv
```

3. Create a file called `.env` in the root directory of the project and add the following lines

```bash
DISCORD_TOKEN=<your discord bot token>
OPENAI_API_KEY=<your openai api key>
```

4. Initiate virtual shell for pipenv

```bash
pipenv shell
```

5. Run the bot

```
python src/main.py
```
