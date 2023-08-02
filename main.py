import crescent
import hikari
from os import getcwd

from misc.model import Model

def get_token(path: str):
    with open(f"{getcwd()}/{path}", "r") as f:
        return f.read()

bot = hikari.GatewayBot(get_token("./token.txt"))
client = crescent.Client(bot, model=Model(
    config_path="./data/Config.toml",
    runtime_path="./data/runtime.json" 
))

client.plugins.load_folder(".plugins")

if __name__ == "__main__":

    bot.run(
        status=hikari.Status.ONLINE,
        activity=hikari.Activity(
            name="blåhaj > blåvingad",
            type=hikari.ActivityType.PLAYING
        )
    )