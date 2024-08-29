from dotenv import load_dotenv
import asyncio
import os
import discord

load_dotenv()
class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.typing_users = {}  # Initialize the typing_users dictionary
        self.MAX_WORDS = 40

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    

    async def on_message(self,message):

        # Split the message into words and count them
        word_count = len(message.content.split())

        # Check if the number of words exceeds the limit
        if word_count > self.MAX_WORDS:
            await message.channel.send(f"{self.user.mention} You've been typing for a while!")
            image_url = "class-nerd-glasses-f87a4c0f-9a9a-41de-8eee-2d236f838657-jpgrendition.jpg"
            await message.channel.send(file=discord.File(image_url))

intents = discord.Intents.all()
intents.typing = True  # Ensure typing intent is enabled
intents.messages = True  # Ensure message intent is enabled

client = MyClient(intents=intents)
client.run(os.getenv('token'))
