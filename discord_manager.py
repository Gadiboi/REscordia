import constants
import data_management
import os
import discord
import discord_embeds
import discord_ui
import interface

from error_msgs import *
from discord.ext import commands

# Discord token from VENV
DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')

# Bot initialization
intents = discord.Intents.all()
activity = discord.Activity(type=discord.ActivityType.watching, name="!help")
bot = commands.Bot(command_prefix='!', intents=intents, activity=activity)
bot.remove_command('help')


@bot.command()
async def start(ctx):
    '''
    !start command
    Creates a new character
    '''
    no_error, msgs = interface.create_player(ctx.author.name)
    if no_error:
        await ctx.send(f'Welcome, {ctx.author.mention}, to the world of Escordia.\nWe recommend you see the `!tutorial`.')
    else:
        await ctx.send(f'**Escordia Error** - {ctx.author.mention}: {msgs_to_msg_str(msgs)}')


@bot.command()
async def fight(ctx):
    '''
    !fight command
    Makes the player fight a random enemy from current area
    '''
    no_error, msgs = interface.begin_battle(ctx.author.name, False)
    if no_error:
        battle = data_management.search_cache_battle_by_player(ctx.author.name)
        await ctx.send(embed=discord_embeds.embed_fight_msg(ctx, battle.player, battle.enemy), view=discord_ui.ActionMenu(ctx))
    else:
        await ctx.send(f'**Escordia Error** - {ctx.author.mention}: {msgs_to_msg_str(msgs)}')


@bot.command()
async def boss(ctx):
    '''
    !boss command
    Makes the player fight the boss of current area
    '''
    no_error, msgs = interface.begin_battle(ctx.author.name, True)
    if no_error:
        battle = data_management.search_cache_battle_by_player(ctx.author.name)
        await ctx.send(embed=discord_embeds.embed_fight_msg(ctx, battle.player, battle.enemy),
                       view=discord_ui.ActionMenu(ctx))
    else:
        await ctx.send(f'**Escordia Error** - {ctx.author.mention}: {msgs_to_msg_str(msgs)}')


@bot.command()
async def attack(ctx):
    '''
    !attack command
    Attack enemy fighting the player
    '''
    no_error, msgs = interface.normal_attack(ctx.author.name)
    await discord_ui.continue_battle(no_error, msgs, ctx)


@bot.command()
async def rest(ctx):
    """
    !rest command
    Fully recovers the player
    """
    no_error, msgs = interface.player_rest(ctx.author.name)
    if no_error:
        msg_str = msgs_to_msg_str(msgs)
        await ctx.send(msg_str)
    else:
        await ctx.send(f'**Escordia Error** - {ctx.author.mention}: {msgs_to_msg_str(msgs)}')


@bot.command()
async def inventory(ctx):
    """
    !inventory command
    Shows player's inventory
    """
    no_error, msgs = interface.show_player_inventory(ctx.author.name)
    if no_error:
        await ctx.send(msgs_to_msg_str(msgs))
    else:
        await ctx.send(f'**Escordia Error** - {ctx.author.mention}: {msgs_to_msg_str(msgs)}')


@bot.command()
async def profile(ctx):
    """
    !profile command
    Shows player's profile
    """
    no_error, msgs = interface.show_player_profile(ctx.author.name)
    if no_error:
        await ctx.send(embed=discord_embeds.embed_player_profile(ctx, ctx.author.name, msgs_to_msg_str(msgs)))
    else:
        await ctx.send(f'**Escordia Error** - {ctx.author.mention}: {msgs_to_msg_str(msgs)}')


@bot.command()
async def shop(ctx):
    """
    !shop command
    Shows the shop of the current area
    """
    no_error, msgs = interface.show_shop_inventory(ctx.author.name)
    if no_error:
        item_list = data_management.search_cache_shop_by_area(data_management.search_cache_player(ctx.author.name).current_area).item_list
        await ctx.send(f"Please select an item to buy, {ctx.author.mention}", view=discord_ui.ItemBuySelectView(ctx, item_list))
    else:
        await ctx.send(f'**Escordia Error** - {ctx.author.mention}: {msgs_to_msg_str(msgs)}')


@bot.command()
async def equipment(ctx):
    """
    !equipment command
    Shows player's equipment
    """

    player_inst = data_management.search_cache_player(ctx.author.name)
    if player_inst is None:
        await ctx.send(f'**Escordia Error** - {ctx.author.mention}: {ERROR_CHARACTER_DOES_NOT_EXIST}')
        return

    await ctx.send(f"This is your current equipment, {ctx.author.mention}:")
    for e_type in constants.EQUIPMENT_TYPES:
        item_list = player_inst.inventory.get_items_from_type(e_type)
        if len(item_list) == 0 and player_inst.equipment[e_type] is None:
            await ctx.send(f"**{e_type}**\nYou don't have any.")
        else:
            await ctx.send(f"**{e_type}**", view=discord_ui.EquipmentSelectView(ctx, item_list, player_inst.equipment[e_type]))


@bot.command()
async def job(ctx):
    """
    !job command
    Shows player's job, also allows to change it
    """
    no_error, msgs = interface.show_player_job(ctx.author.name)
    if no_error:
        await ctx.send(msgs_to_msg_str(msgs), view=discord_ui.JobSelectView(ctx, ['Novice']))
    else:
        await ctx.send(f'**Escordia Error** - {ctx.author.mention}: {msgs_to_msg_str(msgs)}')


def msgs_to_msg_str(msgs: list) -> str:
    """
    Converts a list of messages to a string

    :param msgs: List of messages
    :return: String containing all messages.
    """
    return "\n".join(msgs)


data_management.load_everything()
bot.run(DISCORD_TOKEN)
