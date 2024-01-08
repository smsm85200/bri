import datetime
import random
import threading
import asyncio
import telethon
from telethon import events
from queue import Queue
import requests
from telethon.sync import functions
from user_agent import generate_user_agent
import requests
from user_agent import *
from help import *
from config import *
from threading import Thread

a = 'qwertyuiopasdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'
z = 'qwertyuiopassdfghjklzxcvbnm1234567890'
k = 'qwertyuiopassdfghjklzxcvbnm1234567890_'
o = 'qwertyuiopassdfghjklzxcvbnm1234567890_'
banned = []
isclaim = ["off"]
isauto = ["off"]
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)

current_datetime = datetime.datetime.now()

que = Queue()


def check_user(username):
    url = "https://t.me/"+str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

    response = requests.get(url, headers=headers)
    if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
        return "Available"
    else:
        return "Unavailable"

def gen_user(choice):
    if choice == "1":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(z) 
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(e)
            s = random.choices(z) 
            f = [c[0], "_", d[0], "_", s[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "2":
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], "_", c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(e)
            f = [c[0], d[0], "_", c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "3":
        c = random.choices(a)
        d = random.choices(k)
        s = random.choices(o)
        f = [c[0], s[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(k) 
            s = random.choices(o)
            f = [c[0], s[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass
    if choice == "4":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(b)
        f =  [c[0], d[0], s[0], s[0], s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(e)
            s = random.choices(b)
            f =  [c[0], d[0], s[0], s[0], s[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "5":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(b)
        f =  [c[0], d[0], s[0], s[0], s[0], s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(e)
            s = random.choices(b)
            f =  [c[0], d[0], s[0], s[0], s[0], s[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "6":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(b)
        f =  [c[0], s[0], s[0], s[0], d[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(e)
            s = random.choices(b)
            f =  [c[0], s[0], s[0], s[0], d[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "7":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f =  [c[0], d[0], s[0], s[0], s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(e)
            s = random.choices(e)
            f =  [c[0], d[0], s[0], s[0], s[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "8":
        c = random.choices(a)
        d = random.choices(o)
        s = random.choices(e)
        f =  [c[0], c[0], c[0], d[0], s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(o)
            s = random.choices(e)
            f =  [c[0], c[0], c[0], d[0], s[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "9":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f =  [c[0], s[0], s[0], s[0], d[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(e)
            s = random.choices(e)
            f =  [c[0], s[0], s[0], s[0], d[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "10":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            f = [c[0], c[0], d[0], d[0], d[0], d[0]] 
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "11":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            f = [c[0], c[0], c[0], d[0], d[0], d[0]] 
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    return username

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.checker"))
async def _(event):
    if ispay2[0] == "yes":
        await event.edit(tele_checker)
        
@sython.on(events.NewMessage(outgoing=True, pattern=r"\.bandlist"))
async def _(event):
    if ispay2[0] == "yes":
        await sython.send_file(event.chat_id, 'banned.txt')


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.types"))
async def _(event):
    if ispay2[0] == "yes":
        await event.edit(tele_checker2)
# صيد عدد نوع قناة


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.chk (.*)")) 
async def _(event):
    try:
    	await sython(functions.channels.JoinChannelRequest(
    	channel='gggggggggggggggug'
    	))
    except:
    	pass
    if ispay2[0] == "yes":
        isclaim.clear()
        isclaim.append("on")
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        ch = str(msg[2])
        choice = str(msg[1])
        trys = 0
        await event.edit(f"Okay, I'll check the type `{choice}`\nFrom the ministers on `{ch}`\n , By number `{msg[0]}` Of attempts !")

        @sython.on(events.NewMessage(outgoing=True, pattern=r"\.check chk")) 
        async def _(event):
            if ispay2[0] == "yes":
                if "on" in isclaim:
                    await event.edit(f"({trys})")
                elif "off" in isclaim:
                    await event.edit("chk not start! ")
                else:
                    await event.edit("خطأ")
            else:
                pass
        for i in range(int(msg[0])):
            if ispay2[0] == 'no':
                break
            username = ""

            username = gen_user(choice)
            t = Thread(target=lambda q, arg1: q.put(
                check_user(arg1)), args=(que, username))
            t.start()
            t.join()
            isav = que.get()
            if "Available" in isav:
                await asyncio.sleep(0.0)
                try:
                    await sython(functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username))
                    await event.client.send_file(event.chat_id, "https://t.me/aaxxxa/158",caption=f'''
𝐔𝐒𝐄𝐑 𝐈𝐒 𝐃𝐎𝐍𝐄
▰▱▰▱▰▱▰▱▰▱▰
ᵿˢᴱᴿ 𓌹 @{username} 𓌺
ᶜᴸᴵᶜᴷ 𓌹{trys}𓌺
ˢᴬᵛᴱᴰ 𓌹 ᶜᴴᴬᴺᴺᴱᴸ 𓌺
▱▰▱▰▱▰▱▰▱▰▱
𝐏𝐘 @u0uu0 ↬ @aaxxxa 
    ''')
                    await event.client.send_file("@u0uu0", "https://t.me/aaxxxa/158",caption=f'''
𝐔𝐒𝐄𝐑 𝐈𝐒 𝐃𝐎𝐍𝐄
▰▱▰▱▰▱▰▱▰▱▰
ᵿˢᴱᴿ 𓌹 @{username} 𓌺
ᶜᴸᴵᶜᴷ 𓌹{trys}𓌺
ˢᴬᵛᴱᴰ 𓌹 ᶜᴴᴬᴺᴺᴱᴸ 𓌺
▱▰▱▰▱▰▱▰▱▰▱
𝐏𝐘 @u0uu0 ↬ @aaxxxa 
    ''')
                    break
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    with open("banned.txt", "a") as f:
                        f.write(f"\n{username}")
                except Exception as eee:
                    await sython.send_message("@gggggggggggggggug", f'''error with @{username}''') 
            trys += 1

        isclaim.clear()
        isclaim.append("off")
        trys = ""
        await event.client.send_message(event.chat_id, "Stop check @u0uu0 ↬ @i_m_q ↬ @aaxxxa")
Threads=[] 
for t in range(200):
    x = threading.Thread(target=_)
    le = threading.Thread(target=gen_user)
    x.start()
    le.start()
    Threads.append(x)
    Threads.append(le)
for Th in Threads:
    Th.join()
