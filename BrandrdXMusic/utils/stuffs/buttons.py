from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("ᴄʜᴀᴛ-ɢᴘᴛ", callback_data="mplus HELP_Chatgpt"),InlineKeyboardButton("ʜɪsᴛᴏʀʏ", callback_data="mplus HELP_History"),InlineKeyboardButton("ʀᴇᴇʟ", callback_data="mplus HELP_Reel")],
    [InlineKeyboardButton("ᴛᴀɢ-ᴀʟʟ", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("ɪɴғᴏ", callback_data="mplus HELP_Info"),InlineKeyboardButton("ᴇxᴛʀᴀ", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("ᴄᴏᴜᴘʟᴇs", callback_data="mplus HELP_Couples"),
    InlineKeyboardButton("ᴀᴄᴛɪᴏɴ", callback_data="mplus HELP_Action"),InlineKeyboardButton("sᴇᴀʀᴄʜ", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("ғᴏɴᴛ", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("ʙᴏᴛs", callback_data="mplus HELP_Bots"),InlineKeyboardButton("ᴛᴇʟᴇɢʀᴀᴘʜ", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("sᴏᴜʀᴄᴇ", callback_data="mplus HELP_Source"),
    InlineKeyboardButton("ᴛʀᴜᴛʜ-ᴅᴀʀᴇ", callback_data="mplus HELP_TD"),InlineKeyboardButton("ǫᴜɪᴢ", callback_data="mplus HELP_Quiz")], 
    [InlineKeyboardButton("ᴛᴛs", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("ʀᴀᴅɪᴏ", callback_data="mplus HELP_Radio"),InlineKeyboardButton("ǫᴜᴏᴛʟʏ", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton("• ɴᴇxᴛ •", callback_data=f"settings_back_helper"),
     InlineKeyboardButton("• ʙᴀᴄᴋ •", callback_data=f"mbot_cb"), 
    InlineKeyboardButton("• ɴᴇxᴛ •", callback_data=f"managebot123 settings_back_helper"),
    ]]
