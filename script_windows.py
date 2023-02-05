import subprocess
import time
from pypresence import Presence

"""
You need to upload your image(s) here:
https://discordapp.com/developers/applications/<APP ID>/rich-presence/assets
"""

client_id = "861651444234846258" # application ID
RPC = Presence(client_id=client_id)
RPC.connect()

start = int(time.time())

while 1:
    process = subprocess.Popen(["powershell.exe", ".\\script.ps1"], stdout=subprocess.PIPE, universal_newlines=True)
    title = process.communicate()[0].strip()

    # use the same name that you used when uploading the image
    RPC.update(large_image="notion_1024", large_text="Notion",
                small_image="keeb_512", small_text="Organizing my life!", start=int(start), details=("Editing: " + title))

    time.sleep(15) #Can only update presence every 15 seconds
