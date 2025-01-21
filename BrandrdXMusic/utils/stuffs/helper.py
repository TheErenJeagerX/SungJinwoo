# helper for strings

class Helper(object):
    HELP_M = '''ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.
ᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ

    HELP_Reel = '''Reel

Reel Commands:

/ig [URL] ➠ Temporary Removed.
/instagram [URL] ➠ Temporary Removed .
/reel [URL]  ➠ Temporary Removed .
'''
    HELP_Info = '''Info

Info Commands:

/id : Get The Current Group Id. If Used By Replying To A Message, Gets That User's Id.
'''
    HELP_History = '''History

History Commands:

These Are The Available Group Management Commands:

⊹ /Sg Or /History
Description: 
• Fetches A Random Message From A User's Message History.

Usage:
⊹ /Sg [Username/Id/Reply]

Details:
⊹ Fetches A Random Message From The Message History Of The Specified User.
⊹ Can Be Used By Providing A Username, User ID, Or Replying To A Message From The User.
⊹ Accesibe Only By The Bot's Assistants.

Exᴀᴍᴘᴇs:
⊹ /Sg Username`
⊹ /sg User_Id`
⊹ /sg [Reply To A Message]`
'''

    HELP_Extra = '''Exᴛʀᴀ

Exᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ:

⊹ /tgm • Uploads A Photo (Under 5MB) To The Cloud And Gives A Link.
⊹ /paste • Uploads A Text Snippet To The Cloud And Gives A Link.
⊹ /tr • Translates Text.
'''

    HELP_Search = '''Seaech

Search Commands:

• /google <query> : Search the google for the given query.
• /image (/imgs) <query> : Get the images regarding to your query

Example:
/google pyrogram: return top 5 reuslts.
'''

    HELP_Font = '''Font

Here Is The Help For The Font Module:

Font Module:

By Using This Module You Can Change Fonts  Of Any Text!

⊹ /font [Text]
'''
    HELP_Bots = '''Bots

Here Is The Help For The Bots Module:
Bots Module:

⊹ /bots - Get A List Of Bots In The Groul.
'''
    HELP_TG = '''Telegraph

Telegraph Commands:

Create A Telegraph Link Any Media!

⊹ /tgm [Reply To Any Media]
⊹ /tgt [Reply To Any Media]
'''
   
    HELP_TD = '''Truth-Dare

Here Is The Help For The Truth-Dare Module:

Truth And Dare
⊹ /truth : Sends A Random Truth String.
⊹ /dare : Sends A Random Dare String.
'''
    HELP_Quiz = '''Quiz

Here  Is The Help For The Quiz Module:

Quiz
⊹ /quiz - To Get An Random Quiz
'''
    HELP_TTS = '''TTS

Here Is The Help For The TTS Module:

⊹ TTS
⊹ /tts : [Text]

⊹ ᴜsᴀɢᴇ ➛ Text To Speech
'''
    HELP_Radio = '''Radio

Here Is The Help For The Radio Module:

⊹ /radio - To Play Radio In The Voice Chat.
'''
    HELP_Q = '''Quotly

Here Is The Help For Quotly Module:

⊹ /q : Create A Quote From The Message

⊹ /q r : Create A Quote From The Message With Reply
'''
    
    
    fullpromote = {
    'can_change_info': True,
    'can_post_messages': True,
    'can_edit_messages': True,
    'can_delete_messages': True,
    'can_invite_users': True,
    'can_restrict_members': True,
    'can_pin_messages': True,
    'can_promote_members': True,
    'can_manage_chat': True,
}

    promoteuser = {
    'can_change_info': False,
    'can_post_messages': True,
    'can_edit_messages': True,
    'can_delete_messages': False,
    'can_invite_users': True,
    'can_restrict_members': False,
    'can_pin_messages': False,
    'can_promote_members': False,
    'can_manage_chat': True,
}
