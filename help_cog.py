from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
COMMANDS:
!help - displays all available commands
!play or !p - plays a song from youtube   
!queue or !q - displays the current queue
!skip or !s - skips the current song
!clear - clears the queue
!leave or !disconnect - leaves the voice channel
!pause - pauses the current song
!resume - resumes the current song
```
"""

        self.text_channel_text = []

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_text.append(channel)
        await self.send_to_all(self.help_message)

    async def send_to_all(self, message):
        for channel in self.text_channel_text:
            await channel.send(message)
    
    @commands.command(name="help", help="Displays all available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)

async def setup(bot):
    await bot.add_cog(help_cog(bot))