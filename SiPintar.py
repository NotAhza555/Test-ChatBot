import discord
from test import Generator 

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/halo'):
        await message.channel.send("Hi!")
    elif message.content.startswith('/bye'):
        await message.channel.send("👋")
    elif message.content.startswith('/generate'):
        await message.channel.send(Generator(10))
    else:
        await message.channel.send(message.content)

client.run("")