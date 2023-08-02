import crescent
from crescent import Plugin
from hikari import Embed, GatewayBot
from misc.model import Model


plugin = Plugin[GatewayBot, Model]()

@plugin.include
@crescent.command(name="default", description="default")
class Support:
    async def callback(self, ctx: crescent.Context) -> None:
        embed = Embed(
            title=f"title",
            color=plugin.model.c["Embed"]["Color"]["Orange"],
            description=f"description"
        )
        embed.set_thumbnail(plugin.model.c["Embed"]["Icon"]["PC"])

        await ctx.respond(embed=embed, ephemeral=True)
