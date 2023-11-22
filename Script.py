import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    
    START_TXT = """<b>ʜᴇʏ {}

ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏꜰɪʟᴛᴇʀ + ᴍᴀɴᴜᴀʟꜰɪʟᴛᴇʀ + ꜰɪʟᴇsᴛᴏʀᴇ ʙᴏᴛ.

ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪ ᴡɪʟʟ ɢɪᴠᴇ ᴍᴏᴠɪᴇs ᴏʀ sᴇʀɪᴇs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘᴍ !!</b>"""

    HELP_TXT = """<b>ʜᴇʏ {}

ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʜᴇʟᴩ ꜰᴏʀ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ.</b>"""
    
    ABOUT_TXT = """<b>
🤖 ᴍʏ ɴᴀᴍᴇ : {}
👨‍💻 ᴏᴡɴᴇʀ : ʏᴇʟʟᴏᴡ ꜰʟᴀꜱʜ⚡
📝 ʟᴀɴɢᴜᴀɢᴇ : ᴘʏʀᴏɢʀᴀᴍ
📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏᴛʜᴏɴ 3
📡 ʜᴏsᴛᴇᴅ ᴏɴ : ᴠᴘs
🌟 ᴠᴇʀsɪᴏɴ : ᴠ 13.0 [ ʙᴇᴛᴀ ]

~ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ ›› <a href='https://t.me/Hari_OP'>ʜᴀʀɪ ᠰ ᴛɢ​</a></b>"""
    
    SOURCE_TXT = """<b><u><b>📝 ɴᴏᴛᴇ:</b></u>

⚠️ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ

▸ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://t.me/Hari_OP'>ʜᴇʀᴇ</a>
▸ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ʟɪɴᴋ ᴛʜɪꜱ ʙᴏᴛ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ..!

▸ ᴅᴇᴠ : <a href=https://t.me/Hari_OP>ʜᴀʀɪ ᠰ ᴛɢ</a> </b>"""
    
    MANUELFILTER_TXT = """🥀<u><b>ʜᴇʟᴘ : ꜰɪʟᴛᴇʀꜱ</b></u>
    
<code>ꜰɪʟᴛᴇʀ ɪꜱ ᴀ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ɪ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ɪɴ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ</code>

<u><b>📝 ɴᴏᴛᴇ:</b></u>

<code>1. ᴛʜɪꜱ ʙᴏᴛ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.</code>

<u><b>✨ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ:</b></u>

• /filter - <code>ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /filters - <code>ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</code>"""

    
    BUTTON_TXT = """<u><b>🥀 ʜᴇʟᴘ : ʙᴜᴛᴛᴏɴꜱ</b></u>
    
<code>ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ.</code>

<u><b>📝 ɴᴏᴛᴇ:</b></u>

<code>1. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ꜱᴇɴᴅ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, ꜱᴏ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. ʙᴜᴛᴛᴏɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀꜱᴇᴅ ᴀꜱ ᴍᴀʀᴋᴅᴏᴡɴ ꜰᴏʀᴍᴀᴛ</code>

<u><b>⌨️ ᴜʀʟ ʙᴜᴛᴛᴏɴꜱ:</b></u>

<code>[Button Text](buttonurl:https://t.me/Hs_Botz)</code>

<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ:</b>

<code>[Button Text](buttonalert:ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀʟᴇʀᴛ ᴍᴇꜱꜱᴀɢᴇ)</code>"""
    
    AUTOFILTER_TXT = """<u><b>🥀 ʜᴇʟᴘ : ᴀᴜᴛᴏ ғɪʟᴛᴇʀ</b></u>
    
<u><b>📝 ɴᴏᴛᴇ: ғɪʟᴇ ɪɴᴅᴇx</b></u>

<code>1. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏꜰ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜰ ɪᴛ'ꜱ ᴘʀɪᴠᴀᴛᴇ.
2. ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇꜱ ɴᴏᴛ ᴄᴏɴᴛᴀɪɴꜱ ᴄᴀᴍʀɪᴘꜱ, ᴘᴏʀɴ ᴀɴᴅ ꜰᴀᴋᴇ ꜰɪʟᴇꜱ.
3. ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ Qᴜᴏᴛᴇꜱ. ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ.</code>

<u><b>📂 ɴᴏᴛᴇ: ᴀᴜᴛᴏ ғɪʟᴛᴇʀ</b></u>

<code>1. ᴀᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
2. ᴜsᴇ /connect ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴛʜᴇ ʙᴏᴛ.
3. ᴜsᴇ</code> /settings <code>ᴏɴ ʙᴏᴛ's ᴘᴍ ᴀɴᴅ ᴛᴜʀɴ ᴏɴ AᴜᴛᴏFɪʟᴛᴇʀ ᴏɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ.</code>"""
    
    CONNECTION_TXT = """<u><b>🥀 ʜᴇʟᴘ : ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</b></u>
    
<code>ᴜꜱᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ꜰᴏʀ ᴍᴀɴᴀɢɪɴɢ ꜰɪʟᴛᴇʀꜱ 
ɪᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.</code>

<u><b>📝 ɴᴏᴛᴇ:</b></u>

1. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. ꜱᴇɴᴅ <code>/ᴄᴏɴɴᴇᴄᴛ</code> ꜰᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴘᴍ

<u><b>✨ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ:</b></u>

• /connect  - <code>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ</code>
• /disconnect  - <code>ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ</code>
• /connections - <code>ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</code>"""

    IMDB_TEMPLATE_TXT = """<b>
📟 ᴛɪᴛʟᴇ: {qurey}
📆 ʏᴇᴀʀ: <a href={url}/releaseinfo>{year}</a>
⏰ ᴅᴜʀᴀᴛɪᴏɴ : {runtime} Minutes</b>"""
    
    EXTRAMOD_TXT = """<u><b>🥀 ʜᴇʟᴘ : ᴇxᴛʀᴀ ᴍᴏᴅᴜʟᴇs</b></u>

<u><b>📝 ɴᴏᴛᴇ:</b></u>

<code>ᴛʜᴇꜱᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ꜰᴇᴀᴛᴜʀᴇꜱ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ</code>

<u><b>✨ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ:</b></u>

• /id - <code>ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.</code>
• /info  - <code>ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.</code>
• /imdb  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.</code>
• /search  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ.</code>"""
    
    ADMIN_TXT = """<u><b>🥀 ʜᴇʟᴘ : ᴀᴅᴍɪɴ ᴍᴏᴅs</b></u>

<u><b>📝 ɴᴏᴛᴇ:</b></u>

<code>ᴛʜɪs ᴍᴏᴅᴜʟᴇ ᴏɴʟʏ ᴡᴏʀᴋs ғᴏʀ ᴍʏ ᴀᴅᴍɪɴs</code>

<u><b>✨ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ:</b></u>

• /logs - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ. [Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</code>
• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ</code>
• /leave  - <code>ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /ban  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>
• /broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ</code>
• /grp_broadcast - <code>Tᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /gfilter - <code>ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /gfilters - <code>ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /delg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>
• /request - <code>Tᴏ sᴇɴᴅ ᴀ Mᴏᴠɪᴇ/Sᴇʀɪᴇs ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ʙᴏᴛ ᴀᴅᴍɪɴs. Oɴʟʏ ᴡᴏʀᴋs ᴏɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ. [Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</code>
• /delallg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ Gғɪʟᴛᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /deletefiles - <code>Tᴏ ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD Fɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>"""

    FILE_STORE_TXT = """<u><b>🥀 ʜᴇʟᴘ : ғɪʟᴇ sᴛᴏʀᴇ</b></u>

<u><b>📝 ɴᴏᴛᴇ:</b></u>
    
<code>ғɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>

<u><b>✨ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ:</b></u>

• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""

    ALL_FILTERS = """
<b>ʜᴇʏ {}, ᴛʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""

    SETTING_TXT = """    
<u><b>sᴇᴛᴛɪɴɢs</u></b>

<code>sᴇᴛᴛɪɴɢs ɪs ᴍᴏsᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ғᴇᴀᴛᴜʀᴇs ɪɴ ᴛʜɪs ʙᴏᴛ.
ʏᴏᴜ ᴄᴀɴ ᴇᴀsɪʟʏ ᴄᴜsᴛᴏᴍɪᴢᴇ ᴛʜɪs ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.</code>

<u><b>📝 ɴᴏᴛᴇ:</b></u>

<code>1. ᴏɴʟʏ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴄʜᴀɴɢᴇs sᴇᴛᴛɪɴɢs.
2. ɪᴛ ᴡᴏʀᴋs ᴏɴʟʏ ᴡʜᴇɴ ʏᴏᴜ ᴀʟʀᴇᴀᴅʏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ.</code>

<u><b>✨ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ:</b></u>

<b>• /settings</b> - <code>ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ</code>"""

    RESTART_TXT = """
<b><u>🥀 ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ !!!✨</u>

📅 ᴅᴀᴛᴇ : <code>{}</code>
⏰ ᴛɪᴍᴇ : <code>{}</code>
🌐 ᴛɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ ʙᴜɪʟᴅ sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""
    
    RULE_TXT = """
<b><u>🥀 ɢʀᴏᴜᴘ ʀᴜʟᴇs ✨</u>

<u>sᴇᴀʀᴄʜ ᴍᴏᴠɪᴇ ᴡɪᴛʜ ᴄᴏʀʀᴇᴄᴛ sᴘᴇʟʟɪɴɢ</u>

› ᴀᴠᴀᴛᴀʀ 2009 ✅
› ᴀᴠᴀᴛᴀʀ ʜɪɴᴅɪ ✅
› ᴀᴠᴀᴛᴀʀ ᴍᴏᴠɪᴇ ❌
› ᴀᴠᴀᴛᴀʀ ʜɪɴᴅɪ ᴅᴜʙʙᴇᴅ..❌

<u>sᴇᴀʀᴄʜ ᴡᴇʙ sᴇʀɪᴇs ɪɴ ᴛʜɪs ғᴏʀᴍᴀᴛᴇ</u>

› ᴠɪᴋɪɴɢs S01 ✅
› ᴠɪᴋɪɴɢs S01E01 ✅
› ᴠɪᴋɪɴɢs S01 ʜɪɴᴅɪ ✅
› ᴠɪᴋɪɴɢs S01 ʜɪɴᴅɪ ᴅᴜʙʙ. ❌
› ᴠɪᴋɪɴɢs sᴇᴀsᴏɴ 1 ❌
› ᴠɪᴋɪɴɢs ᴡᴇʙ sᴇʀɪᴇs ❌


🔹 ᴅᴏɴ'ᴛ ᴅᴏ ᴀɴʏ sᴇʟғ ᴘʀᴏᴍᴏᴛɪᴏɴ.

🔹 ᴅᴏɴ'ᴛ sᴇɴᴅ ᴀɴʏ ᴋɪɴᴅ ᴏғ ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ ᴅᴏᴄᴜᴍᴇɴᴛs, ᴜʀʟ ᴇᴛᴄ..

🔹 ᴅᴏɴ'ᴛ ʀᴇǫᴜᴇsᴛ ᴀɴʏ ᴛʜɪɴɢs ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴍᴏᴠɪᴇ sᴇʀɪᴇs ᴀɴɪᴍᴇs..

⚙️ ɴᴏᴛᴇ :- 𝖠ʟʟ ᴍᴇ𝗌𝗌ᴀɢᴇ𝗌 ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇᴅ ᴀғᴛᴇʀ 𝟷𝟶 ᴍɪɴᴜᴛᴇ𝗌 ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪ𝗌𝗌ᴜᴇ𝗌.</b>"""

    
    STATUS_TXT = """
<b>📑 ғɪʟᴇs sᴀᴠᴇᴅ: <code>{}</code>
👤 ᴛᴏᴛᴀʟ ᴜsᴇʀs: <code>{}</code>
♻️ ᴛᴏᴛᴀʟ ᴄʜᴀᴛs: <code>{}</code>
🗃️ ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ: <code>{}</code> ᴍʙ
🆓 ғʀᴇᴇ sᴛᴏʀᴀɢᴇ: <code>{}</code> ᴍʙ</b>"""

    YT_SUPPORT_TXT = """<b>🦋 ᴄʜᴀɴɴᴇʟs & ɢʀᴏᴜᴘs ᴍᴏᴅᴜʟᴇ 🦋

» ᴄᴏᴍᴘʟᴇᴛᴇ ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇsᴛɪɴɢ ɢʀᴏᴜᴘ.
» ᴀʟʟ ʟᴀɴɢᴜᴀɢᴇs ᴍᴏᴠɪᴇs & ꜱᴇʀɪᴇs.
» ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ.
» ʙᴏᴛ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ.</b>"""

    SUPPORT_TXT = """<b>🎯✨ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ sɪᴠᴇʀᴏᴢ ʟɪɴᴋᴢᴢ ❣

⚡️🍬ᴊᴏɪɴ ᴏᴜʀ ᴍᴏᴠɪᴇꜱ ᴄʜᴀɴɴᴇʟꜱ 🦋✨


<a href=https://t.me/+x2qlfSKlbu4yYWJl>🔰✥ ▷ ʜᴏʟʟʏᴡᴏᴏᴅ ᴍᴏᴠɪᴇꜱ ◁</a>

<a href=https://t.me/+nKmSHfXM9182OTg9>🔰✥ ▷ ᴅᴜʙʙᴇᴅ ᴍᴏᴠɪᴇꜱ ◁</a>

<a href=https://t.me/+ybrdZmC6FLQxOTM1>🔰✥ ▷ ʜᴏʀʀᴏʀ ᴍᴏᴠɪᴇꜱ ◁</a>

<a href=https://t.me/Siveroz_Anime>🔰✥ ▷ ᴀɴɪᴍᴇ ᴛᴀᴍɪʟ ᴅᴜʙ ◁</a>

🚀 ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ - @Siveroz_Linkzz

🦋 ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ :<a href=tg://settings>ᴛʜɪs ᴘᴇʀsᴏɴ 🙌</a></b>"""
    
    OWNER_TXT = """
<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ :ʏᴇʟʟᴏᴡ ꜰʟᴀꜱʜ⚡
• ᴜꜱᴇʀɴᴀᴍᴇ : @The_YellowFlash
• ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴍ ʟɪɴᴋ :<a href=https://t.me/The_YellowFlash>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>"""

    CAPTION = """<b>
📂 ғɪʟᴇ ɴᴀᴍᴇ : <code>{file_name}</code>

📑 sɪᴢᴇ : {file_size}

🎭 ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @skymovies_tamil</b>"""

    LOGO = """
𝑺𝒕𝒂𝒓𝒕𝒊𝒏𝒈.......🥵"""

    FILE_MSG = """
<b>🥀 ʜᴀʏ {} </b>

<b>📫 ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ</b>

<b>📂 ғɪʟᴇ ɴᴀᴍᴇ</b> : <code>{}</code>              
                       
<b>📑 sɪᴢᴇ</b> : <b>{}</b>"""
    
    CHANNEL_CAP = """<b>
👋 ʜᴀʏ {}

📂 <code>{}</code>

🎭 ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @skymovies_tamil</b>"""

    MVE_NT_FND = """🔎 ᴍᴏᴠɪᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱᴇ...♻️"""

    TOP_ALRT_MSG = """♻️ ᴄʜᴇᴄᴋɪɴɢ ғᴏʀ ᴍᴏᴠɪᴇ ɪɴ ᴅᴀᴛᴀʙᴀsᴇ...♻️"""

    I_CUDNT = """<b>sᴏʀʀʏ ɴᴏ ꜰɪʟᴇs ᴡᴇʀᴇ ꜰᴏᴜɴᴅ ꜰᴏʀ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ {} 😕</b>"""

    CUDNT_FND = """<b>🥀 ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}
ᴅɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏꜰ ᴛʜᴇꜱᴇ?✨</b>"""

    NORSLTS = """
<u>ɴᴏ ʀᴇsᴜʟᴛs</u>

<b>ɪᴅ : {}</b>

ɴᴀᴍᴇ : {}</b>

ᴍᴇssᴀɢᴇ : {}</b>"""
    
    RENDERING_TXT = """
⚡️ ʟɪᴠᴇ sʏsᴛᴇᴍ sᴛᴀᴛᴜs ⚡️

⇝ ʀᴀᴍ ●●●●●●●◌◌◌
⇝ ᴄᴘᴜ ●●●●●●●◌◌◌
⇝ ᴅᴀᴛᴀ ᴛʀᴀꜰɪᴄs ●●●●◌◌◌◌◌◌ 🛰

ᴠ2.7.1 [sᴛᴀʙʟᴇ] """
    
    GFILTER_TXT = """<u><b>🥀 ʜᴇʟᴘ : ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</b></u>

<u><b>📝 ɴᴏᴛᴇ:</b></u>
    
<code>ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs. ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.</b></code>

<u><b>✨ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ:</b></u>

• /gfilter - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /gfilters - <code>Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ.</code>"""

    ALRT_TXT = """🥀 ʜᴇʟʟᴏ {},
    
ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ,

ʀᴇǫᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ...✨"""

    OLD_ALRT_TXT = """🥀 ʜᴇʏ {},
    
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ,

ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇǫᴜᴇꜱᴛ ᴀɢᴀɪɴ.✨"""

    HS_START_TXT = """<b>ʜᴇʟʟᴏ {}

ᴛʜɪs ɪs ᴀ ᴘʀᴏ ᴍᴏᴠɪᴇs ᴀᴜᴛᴏꜰɪʟᴛᴇʀ-ʙᴏᴛ ᴡɪᴛʜ 4ɢʙ+ ᴍᴇᴅɪᴀ ꜰɪʟᴇs sᴜᴘᴘᴏʀᴛ.

ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ.</b>"""

    LOG_TEXT_G = """<b> #NewGroup
👥 ɢʀᴏᴜᴘ 👥 = {}(<code>{}</code>)
😇 ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs 😇 = <code>{}</code>
💌 ᴀᴅᴅᴇᴅ ʙʏ 💌 - {} </b>"""
    
    LOG_TEXT_P = """<b>#NewUser
🥀 ɪᴅ - <code>{}</code>
📑 ɴᴀᴍᴇ - {} </b>"""
    
    NOR_TXT = """
<b>📟 ᴛɪᴛʟᴇ : {}
📂 ᴛᴏᴛᴀʟ ꜰɪʟᴇs ꜰᴏᴜɴᴅᴇᴅ : {}
👩🏻‍💻 ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ : {}</b>

<code>⚠️ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇᴅ ᴀғᴛᴇʀ 𝟷𝟶 ᴍɪɴᴜᴛᴇs</code>"""
