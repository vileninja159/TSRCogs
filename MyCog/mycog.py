from redbot.core import commands

class Mycog(commands.Cog):
    """My custom cog"""

    @commands.command()
  async def mycom(ctx):
     await ctx.send(ctx.message.guild.default_role)