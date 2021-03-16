from redbot.core import commands
import Discord
import asyncio

class Mycog(commands.Cog):
    """My custom cog"""

    @client.event
async def on_message(message):
  text_channel = client.get_channel('806000602168819723')
  msg = '{0.author.mention}\nWrong text channel\nUse {1.mention}'.format(message,text_channel)
  if message.content.startswith('.ann'):
      await client.delete_message(message)
      await client.send_message(message.channel, msg)
  return
