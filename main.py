import discord
import random
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('$hello'):
        await message.channel.send(f'Hola, soy un bot {client.user}!')
    elif  message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
            await message.channel.send("he" * count_heh)
    elif message.content.startswith('$cual es el mejor programa de progamacion'):
        await message.channel.send('el mejor progama de progamacion es Phyton!')
    elif message.content.startswith('$este bot es chido?'):
        await message.channel.send('si, este bot es chido!')
    elif message.content.startswith('$suma'):
        # Extraemos los números del mensaje
        numbers = [int(s) for s in message.content.split() if s.isdigit()]
        # Calculamos la suma
        total_sum = sum(numbers)
        # Enviamos el resultado al canal
        await message.channel.send(f'La suma de los números es {total_sum}')
    elif message.content.startswith('$resta'):
        # Extraemos los números del mensaje
        numbers = [int(s) for s in message.content.split() if s.isdigit()]
        # Verificamos que hay al menos dos números para hacer la resta        
        if len(numbers) >= 2:
            # Realizamos la resta asegurándonos de que el resultado no sea negativo
            total_resta = numbers[0] - numbers[1] if numbers[0] >= numbers[1] else numbers[1] - numbers[0]
            # Enviamos el resultado al canal
            await message.channel.send(f'La resta de los números es {total_resta}')
        else:
            await message.channel.send('Necesito al menos dos números para hacer la resta.')
    else:
        # Si el mensaje no coincide con ningún comando, envía una respuesta por defecto
        await message.channel.send('No entendí o no tengo nada que hacer.')
        
client.run("Agrega token")
