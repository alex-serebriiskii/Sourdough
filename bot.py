from fastapi import FastAPI
import discord
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

app = FastAPI()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await message.channel.send('message recieved!')

@app.get("/test")
async def bruh():
    return {"test":"test"}

@app.get("/button")
async def button():
    print("button press")
    await client.get_guild().get_channel().send("test")
    return {"status":"success"}

async def run_bot():
    try:
        await client.start("")
    except:
        print("failed to launch discord bot")

asyncio.create_task(run_bot())