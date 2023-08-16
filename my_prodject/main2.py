import discord
from discord.ext import commands 

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send(f"{gen_pass(10)}")
    else:
        await message.channel.send(message.content)

client.run('MTEzMjI3NzgyMzEyNjYzNDQ5Nw.G-k-_6.CB5Feh07ZEBZLdRcD7yzXC9DWUS0FtDdZ8aGIQ')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('$hello'):
        await message.channel.send(f'Привет! Я бот {client.user}!')
        
client.run("MTEzMjI3NzgyMzEyNjYzNDQ5Nw.G-k-_6.CB5Feh07ZEBZLdRcD7yzXC9DWUS0FtDdZ8aGIQ")

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

client.run("MTEzMjI3NzgyMzEyNjYzNDQ5Nw.G-k-_6.CB5Feh07ZEBZLdRcD7yzXC9DWUS0FtDdZ8aGIQ")

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

client.run("MTEzMjI3NzgyMzEyNjYzNDQ5Nw.G-k-_6.CB5Feh07ZEBZLdRcD7yzXC9DWUS0FtDdZ8aGIQ")

