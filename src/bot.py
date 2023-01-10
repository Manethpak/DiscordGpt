from discord import Intents, Client, Message
from openai import Completion

intents = Intents.default()
intents.message_content = True

client = Client(intents=intents)

PREFIX = ">>"

COMMANDS = {
    "ask": ">>ask",
    "ping": ">>ping",
    "private": ">>private",
    "help": ">>help",
}

EXTRAS_LINE = [
    "What else can I help you with?",
    "What else do you want to know?",
    "Any more question to ask?",
]


@client.event
async def on_ready():
    """
    Print a log when the bot is ready
    """
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message: Message):
    """
    Listen to message event
    """
    # ignore messages from the bot itself
    if message.author == client.user:
        return

    # reply to private messages normally
    if message.guild is None:
        await chat(message)

    # ignore messages in guild that don't start with the prefix
    if not message.content.startswith(PREFIX):
        return

    if message.content.startswith(COMMANDS["ask"]):
        await chat(message)

    elif message.content.startswith(COMMANDS["ping"]):
        await message.channel.send("pong!")

    elif message.content.startswith(COMMANDS["private"]):
        await message.author.send("What sup? How can I help you today?")

    elif message.content.startswith(COMMANDS["help"]):
        await message.channel.send(
            """I can help you answering your question. Just type the following command
            >>ask <text> - to ask me a question
            >>ping - to check if I am well and alive
            >>private - to have a chat with me privately
            >>help - to see this message again"""
        )
    else:
        command = message.content.split(" ")[0]
        await message.channel.send(
            f"{command} is not a valid command. Type >>help to see what I can do."
        )


async def chat(message: Message):
    try:
        command, text = message.content.split(" ", maxsplit=1)
    except ValueError:
        await message.channel.send("Please provide a question using the >>ask command")
        return

    # get reponse from openai's text-davinci-003
    response = Completion.create(
        engine="text-davinci-003",
        prompt=text,
        temperature=0.8,
        max_tokens=512,
        top_p=1,
        logprobs=10,
    )

    # Extract the response from the API response
    response_text = response["choices"][0]["text"]

    await message.channel.send(response_text)
