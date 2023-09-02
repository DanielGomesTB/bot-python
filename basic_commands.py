import settings
import random
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('handled error globally')
    
    @bot.command(
            aliases=['p'],
            help="This is help",
            description="This is description",
            brief="This is brief",
            # enable=False,
            # hidden=True,
    )
    async def ping(ctx):
        """ Answers with pong """
        await ctx.send("pong")

    @bot.command()
    async def say(ctx, what = "What?"):
        await ctx.send(what)
    
    @bot.command()
    async def say2(ctx, *what):
        await ctx.send(''.join(what))

    @bot.command()
    async def say3(ctx, what = "What?", why = "Why?"):
        await ctx.send(what + why)

    @bot.command()
    async def choices(ctx, *options):
        await ctx.send(random.choice(options))

    @bot.command()
    async def add(ctx, one: int, two: int):
        await ctx.send(one + two)

    # @add.error
    # async def add_error(ctx, error):
    #     if isinstance(error, commands.MissingRequiredArgument):
    #         await ctx.send('handled error locally')

    @bot.command()
    async def add2(ctx, *numbers: int):
        await ctx.send(sum(numbers))

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()