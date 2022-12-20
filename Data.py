#🪄🔎🔮💫♻️🚀🍁🎺🖥️⚔️🖌️🎧👻👹👨‍💻🧑‍💻👨‍✈️🕵️🤘👋🖐️🪄🎉✨🎞️🎀🎁♥️♦️🔊🎧🛠️🔒⚙️⛓️🔗📲📸📡🎥📷📹📼🔍🔍🔎📘📙📚🔖💵💶🪙💸💷💴

from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
🍁Hello {}

Welcome to {}

I m Force Subscribe Bot !
Send /help Visit My Help Menu

🙈 For All Users 👇👇

🔥 Powered By CrownBots ✓
☘️ Simple & Friendly BOT ✓
🪤 Keep Original Appearance ✓
🎯 Group Supported ✓
⚡️ Fast Response ✓
✅ 24 Hour Active ✓
🤩 New OS ✓

🚀Powerd By @projectcrown

    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏛️ Return Home 🏛️", callback_data="home")],
        [InlineKeyboardButton("☣ Emo Bot Devolopers ☣", url="https://t.me/little_little_hackur")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🪄Updates", url="https://t.me/projectcrown")],
        [
            InlineKeyboardButton("❔ How to Use ❔", callback_data="help"),
            InlineKeyboardButton("♾️ About ♾️", callback_data="about")
        ],
        [InlineKeyboardButton("👨‍💻 Devoloper 👨‍💻", url="https://t.me/little_little_hackur")],
        [InlineKeyboardButton("💬 Support 💬", url="https://t.me/crownbotzsupport")],
    ]

    # Help Message
    HELP = """
1) Add me as **Admin** to a group.

2) Add me to the particular chat as **Admin** where you want to force your users to join. It can be any group or channel, public or private.

3) Use /fsub chat_id/username to make me functional. Use /id if you need chat id.
Example : `/fsub @projectcrown` or `/forcesubscribe @projectcrown`

4) [Optional] Use /settings to change settings!

5) You are good to go. Leave the rest to me.

🔅 **Available Commands** 🔅

/fsub - See current force subscribe chat
/fsub chat_id/username - Force users to join the particular chat
/settings - Change Group Settings
/id - Get the chat id of any group or channel
/about - About The Bot
/help - This Message
/start - Start the Bot

**Note** - You can also use `/forcesubscribe` instead of `/fsub`

🔥 Powerd By [Crown Network](https://t.me/projectcrown)
    """

    # About Message
    ABOUT = """
**About This Bot** 

A Telegram Force Subscribing Bot by @ImRishmika

🪄Powerd By : @projectcrown

🍁Framework : [Pyrogram](docs.pyrogram.org)

🍁Language : [Python](www.python.org)

🍁Developer : [𝐁𝐥𝐚𝐜𝐤 𝐇𝐚𝐭](https://t.me/little_little_hackur) 

🖥️ Host Sever : .......... 
    """
