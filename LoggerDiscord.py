# coding: utf-8
import discord
from discord.ext import commands
import os
import requests
from colorama import Fore
import ctypes
import json

ctypes.windll.kernel32.SetConsoleTitleW("LoggerDiscord - Fait par IDRALOU#6966 - Messages Supprimés: 0 | Messages Modifiés: 0")
os.system('echo \033[1m')
os.system('cls')

print("Webhook URL: ")
url = str(input(">>> "))
edit = 0
delete = 0


client = commands.Bot(command_prefix='!', self_bot=True, help_command=None)

def read_json(filename):
    with open(f"{filename}.json", "r") as file:
        data = json.load(file)
    return data

@client.event
async def on_connect():
    os.system('cls')
    print(f"{Fore.GREEN}Le logger est prêt")


@client.event
async def on_message_delete(message):
    if not message.author.bot:
        data = read_json("config")
        global delete
        if message.guild.id in data["guilds"]:
            delete += 1
            payload = {
                "username": "Logger",
                "avatar_url": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/241/page-with-curl_1f4c3.png",
                "embeds": [{ 
                    "author": {"name": str(message.author), "icon_url": str(message.author.avatar_url)},
                    "description": f"Message supprimé sur **{message.guild.name}** dans <#{int(message.channel.id)}>",
                    "fields": [{"name": "Contenu du message supprimé", "value": message.content}],
                    "color": "14177041"
                }]
            }
            requests.post(url, json=payload)
            ctypes.windll.kernel32.SetConsoleTitleW(f"LoggerDiscord - Fait par IDRALOU#6966 - Messages Supprimés: {delete} | Messages Modifiés: {edit}")
        elif "all" in data["guilds"]:
            delete += 1
            payload = {
                "username": "Logger",
                "avatar_url": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/241/page-with-curl_1f4c3.png",
                "embeds": [{ 
                    "author": {"name": str(message.author), "icon_url": str(message.author.avatar_url)},
                    "description": f"Message supprimé sur **{message.guild.name}** dans <#{int(message.channel.id)}>",
                    "fields": [{"name": "Contenu du message supprimé", "value": message.content}],
                    "color": "14177041"
                }]
            }
            requests.post(url, json=payload)
            ctypes.windll.kernel32.SetConsoleTitleW(f"LoggerDiscord - Fait par IDRALOU#6966 - Messages Supprimés: {delete} | Messages Modifiés: {edit}")


@client.event
async def on_message_edit(before, after):
    if not after.author.bot:
        data = read_json("config")
        global edit
        if after.guild.id in data["guilds"]:
            if before.content != after.content:
                edit += 1
                payload = {
                    "username": "Logger",
                    "avatar_url": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/241/page-with-curl_1f4c3.png",
                    "embeds": [{
                        "author": {"name": str(after.author), "icon_url": str(after.author.avatar_url)},
                        "description": f"Message modifié par <@{int(after.author.id)}> sur **{after.guild.name}** dans <#{int(after.channel.id)}>\n[Aller au message](https://discord.com/channels/{after.guild.id}/{after.channel.id}/{after.id})",
                        "fields": [{"name": "Contenu antérieur", "value": before.content}, {"name": "Contenu actuel", "value": after.content}],
                        "color": "14177041"
                    }]
                }
                requests.post(url, json=payload)
                ctypes.windll.kernel32.SetConsoleTitleW(f"LoggerDiscord - Fait par IDRALOU#6966 - Messages Supprimés: {delete} | Messages Modifiés: {edit}")
        elif "all" in data["guilds"]:
            if before.content != after.content:
                edit += 1
                payload = {
                    "username": "Logger",
                    "avatar_url": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/241/page-with-curl_1f4c3.png",
                    "embeds": [{
                        "author": {"name": str(after.author), "icon_url": str(after.author.avatar_url)},
                        "description": f"Message modifié par <@{int(after.author.id)}> sur **{after.guild.name}** dans <#{int(after.channel.id)}>\n[Aller au message](https://discord.com/channels/{after.guild.id}/{after.channel.id}/{after.id})",
                        "fields": [{"name": "Contenu antérieur", "value": before.content}, {"name": "Contenu actuel", "value": after.content}],
                        "color": "14177041"
                    }]
                }
                requests.post(url, json=payload)
                ctypes.windll.kernel32.SetConsoleTitleW(f"LoggerDiscord - Fait par IDRALOU#6966 - Messages Supprimés: {delete} | Messages Modifiés: {edit}")

data = read_json("config")
try:
   client.run(data["token"], bot=False)
except discord.errors.LoginFailure:
   print(f"{Fore.RED}Le token spécifié dans config.json est invalide.")
   os.system('pause')
   os.system('exit')
