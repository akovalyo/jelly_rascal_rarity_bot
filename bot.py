import os
import json
from dotenv import load_dotenv
from discord.ext import commands


def read_json():
    path = os.path.join(os.getcwd(), "rascal_rarities.json")
    with open(path) as f:
        file = json.load(f)
        f.close()
        return file


def main():
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    bot = commands.Bot(command_prefix='!')
    db = read_json()

    @bot.command(name='rascalrarity')
    async def rascal_rarity(ctx, id: int, includeImg: str = None):
        if id < 0 or id > 6665:
            await ctx.send("IDs from 0 to 6665")
        else:
            idStr = str(id)
            rascalData = db[idStr]
            response = f"Rascal **#{idStr}**: {rascalData[0]}"
            await ctx.send(response)
            if includeImg == "img" and rascalData[1]:
                await ctx.send(rascalData[1])

    bot.run(token)


if __name__ == "__main__":
    main()
