
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import asyncio
import random
import datetime
import time
import os


class arahabaki_ng_word(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.hannnou = 0

    @commands.command(name="off")
    async def switch_off(self, message):
        self.hannnou = 0
        await message.send("OFFにした。")

    @commands.command(name="on")
    async def switch_on(self, message):
        self.hannnou = 1
        await message.send("ONにした。")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if self.hannnou == 1:
            colour = random.randint(0x000000, 0xffffff)
            harowa_san = os.path.join(os.path.dirname(__file__), 'ngwords.txt')
            with open(harowa_san, 'r', encoding='utf-8') as file:
                bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]
            if any(bad_word in message.content for bad_word in bad_words):
                nanika = message.channel.id
                channelsss = message.guild.get_channel(nanika)
                await channelsss.send(embed=discord.Embed(title="辞めてくれ！", description=f"それはダメだ！\n{message.author.mention}", colour=colour), delete_after=10)


def setup(bot):
    bot.add_cog(arahabaki_ng_word(bot))
