import logging

import requests

from pymongo import MongoClient

from pyrogram import Client, filters

from pyrogram.types import Message

from pyrogram.errors.exceptions.bad_request_400 import AccessTokenExpired, AccessTokenInvalid

from FallenRobot import API_ID, API_HASH, DRAGONS

from FallenRobot import MONGO_DB_URI as MONGO_URL

mongo_client = MongoClient(MONGO_URL)

mongo_db = mongo_client["cloned_bots"]

expired_bots = []

class clonedme(object):

    ME = None

    U_NAME = None

    B_NAME = None

@Client.on_message((filters.regex(r'\d[0-9]{8,10}:[0-9A-Za-z_-]{35}')) & filters.private)

async def on_clone(client, message):

    try:

        user_id = message.from_user.id

        user_name = message.from_user.first_name

        bot_token = re.findall(r'\d[0-9]{8,10}:[0-9A-Za-z_-]{35}', message.text, re.IGNORECASE)

        bot_token = bot_token[0] if bot_token else None

        bot_id = re.findall(r'\d[0-9]{8,10}', message.text)

        if not str(message.forward_from.id) != "6198858059":

            msg = await message.reply_text(f" <code>{bot_token}</code>\n\n ♻️ɪ'ᴍ ᴛʀʏɪɴɢ ᴛᴏ ᴄʟᴏɴᴇ ᴛʜɪs ʙᴏᴛ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ..♻️")

            try:

                ai = Client(

                    f"{bot_token}", API_ID, API_HASH,

                    bot_token=bot_token,

                    plugins={"root": "clone_plugins"},

                )

                await ai.start()

                bot = await ai.get_me()

                details = {

                    'bot_id': bot.id,

                    'is_bot': True,

                    'user_id': user_id,

                    'name': bot.first_name,

                    'token': bot_token,

                    'username': bot.username

                }

                mongo_db.bots.insert_one(details)

                clonedme.ME = bot.id

                clonedme.U_NAME = bot.username

                clonedme.B_NAME = bot.first_name

                await msg.edit_text(f"ʙᴏᴛ ᴄʟᴏɴᴇ sᴜᴄᴄᴇssғᴜʟʟʏ @{bot.username} .\n\n⚠️ <u>ᴅᴏ ɴᴏᴛ sᴇᴍᴅ ᴀɴʏ ᴏɴᴇ</u> ᴛʜᴇ ᴍᴀssᴀɢᴇ ᴡɪᴛʜ <u>ᴛʜᴇ ᴛᴏᴋᴇɴ</u> ᴏғ ᴛʜᴇ ʙᴏᴛ, ᴡʜᴏ ʜᴀs ɪᴛ ᴄᴏɴᴛʀᴏʟ ʏᴏᴜʀ ʙᴏᴛ !\n<i>ɪғ ʏᴏᴜ ᴛʜɪɴᴋ sᴏᴍᴇᴏɴᴇ ɪs ғᴏᴜɴᴅ ᴏᴜᴛ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ, ɢᴏ ᴛᴏ @Botfather, ᴜsᴇ /revoke ᴀɴᴅ sᴇʟᴇᴄᴛᴇ @{bot.username}</i>")

            except BaseException as e:

                logging.exception("Error while cloning bot.")

                await msg.edit_text(f"⚠️ <b>𝙱𝚘𝚝 𝙴𝚛𝚛𝚘𝚛:</b>\n\n<code>{e}</code>\n\n❔ 𝙵𝚘𝚛𝚠𝚊𝚛𝚍 𝚃𝚑𝚒𝚜 𝙼𝚎𝚜𝚜𝚊𝚐𝚎 𝚃𝚘 my admin 𝚃𝚘 𝙱𝚎 𝙵𝚒𝚡𝚎𝚍.")

    except Exception as e:

        logging.exception("Error while handling message.")

async def get_bot():

    await ai.start()

    crazy = await ai.get_me()

    await ai.stop()

    return crazy

@Client.on_message(filters.command("clonedbots") & filters.private)

async def cloned_bots_list(client, message):

    try:

        user_id = message.from_user.id

        user_name = message.from_user.first_name

        bots = list(mongo_db.bots.find({'user_id': user_id}))

        if len(bots) == 0:

            await message.reply_text("You haven't cloned any bots yet.")

            return

        text = "<b>Your cloned bots:</b>\n\n"

        for bot in bots:

            text += f"- @{bot['username']} ({bot['name']})\n"

            text += f"  Bot ID: {bot['bot_id']}\n"

            text += f"  Token: {bot['token']}\n"

            text += "\n"

        await message.reply_text(text)

    except Exception as e:

        logging.exception("𝙴𝚛𝚛𝚘𝚛 𝚆𝚑𝚒𝚕𝚎 𝙷𝚊𝚗𝚍𝚕𝚒𝚗𝚐 𝙲𝚕𝚘𝚗𝚎𝚍 𝙱𝚘𝚝𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍.")

@Client.on_message(filters.command('cloned_count') & filters.private)

async def cloned_count(client, message):

    user_id = message.from_user.id

    if user_id not in DRAGONS:

        await message.reply_text("𝚈𝚘𝚞 𝙰𝚛𝚎 𝙽𝚘𝚝 𝙰𝚞𝚝𝚑𝚘𝚛𝚒𝚣𝚎𝚍 𝚃𝚘 𝚄𝚜𝚎 𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍.")

        return

    cloned_bots = mongo_db.bots.find()

    count = cloned_bots.count()

    if count == 0:

        await message.reply_text("𝙽𝚘 𝙱𝚘𝚝𝚜 𝙷𝚊𝚟𝚎 𝙱𝚎𝚎𝚗 𝙲𝚕𝚘𝚗𝚎𝚍 𝚈𝚎𝚝.")

    else:

        bot_usernames = [f"@{bot['username']}" for bot in cloned_bots]

        bot_usernames_text = '\n'.join(bot_usernames)

        await message.reply_text(f"{count} bots have been cloned:\n\n{bot_usernames_text}")

@Client.on_message(filters.command(["removebot"]) & filters.user(DRAGONS))

async def remove_bot(client: Client, message: Message):

    bot_username = message.text.split(" ", maxsplit=1)[1].strip()

    bot_data = mongo_db.bots.find_one_and_delete({"username": bot_username})

    if bot_data:

        bot_id = bot_data["bot_id"]

        cloned_sessions = mongo_db.cloned_sessions.find({"bot_id": bot_id})

        if cloned_sessions.count() > 0:

            for session in cloned_sessions:

                await session.stop()

                mongo_db.cloned_sessions.delete_one({"_id": session["_id"]})

        await message.reply_text(f"Bot @{bot_username} removed successfully.")

    else:

        await message.reply_text(f"Bot @{bot_username} is not in the cloned bots list.")

@Client.on_message(filters.command("deletecloned") & filters.private)

async def delete_cloned_bot(client, message):

    try:

        bot_token = re.findall(r'\d[0-9]{8,10}:[0-9A-Za-z_-]{35}', message.text, re.IGNORECASE)

        bot_token = bot_token[0] if bot_token else None

        bot_id = re.findall(r'\d[0-9]{8,10}', message.text)

        cloned_bot = mongo_db.bots.find_one({"token": bot_token})

        if cloned_bot:

            mongo_db.bots.delete_one({"token": bot_token})

            await message.reply_text("The cloned bot has been removed from the list and its details have been removed from the database.")

        else:

            await message.reply_text("The bot token provided is not in the cloned list.")

    except Exception as e:

        logging.exception("Error while deleting cloned bot.")

        await message.reply_text("An error occurred while deleting the cloned bot.")

async def restart_bots():

    logging.info("Restarting all bots........")

    bots = list(mongo_db.bots.find())

    for bot in bots:

        bot_token = bot['token']

        try:

            ai = Client(

                f"{bot_token}", API_ID, API_HASH,

                bot_token=bot_token,

                plugins={"root": "clone_plugins"},

            )

            await ai.start()

            logging.info(f"Bot @{ai.username} restarted.")

        except Exception as e:

            logging.exception(f"Error while restarting bot with token {bot_token}: {e}")

    #logging.info("All bots restarted.")

@Client.on_message(filters.command("restartall") & filters.user(DRAGONS))

async def on_restart_all_bots(client: Client, message: Message):

    await message.reply_text("Restarting all cloned bots...")

    await restart_bots()

    await message.reply_text("All cloned bots have been restarted.")

async def check_bots_expiry():

    logging.info("Checking bots expiry...")

    bots = list(mongo_db.bots.find())

    current_time = datetime.now().timestamp()

    for bot in bots:

        bot_id = bot['_id']

        bot_token = bot['token']

        try:

            ai = Client(

                f"{bot_token}", API_ID, API_HASH,

                bot_token=bot_token,

                plugins={"root": "clone_plugins"},

            )

            await ai.start()

            if isinstance(ai, Client):

                await ai.stop()

            else:

                expired_bots.append(bot_id)

        except AccessTokenInvalid:

            expired_bots.append(bot_id)

        except AccessTokenExpired:

            expired_bots.append(bot_id)

        except Exception as e:

            logging.exception(f"Error while checking bot expiry for bot {bot_id}: {e}")

    logging.info(f"Bots expiry checked. Expired bots: {expired_bots}")

@Client.on_message(filters.command("checkexpiry") & filters.user(DRAGONS))

async def on_check_bots_expiry(client: Client, message: Message):

    await message.reply_text("Checking bots expiry...")

    await check_bots_expiry()

    if expired_bots:

        expired_bots_data = mongo_db.bots.find({"_id": {"$in": expired_bots}})

        expired_bots_text = "\n".join([f"@{bot['username']}" for bot in expired_bots_data])

        await message.reply_text(f"The following bots have expired and need to be refreshed:\n\n{expired_bots_text}")

    else:

        await message.reply_text("No bots have expired.")

