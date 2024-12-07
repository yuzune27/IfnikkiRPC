import os
from discordrp import Presence
import time
import psutil
import logging
import json
from pystray import Icon, Menu, MenuItem
from PIL import Image
from threading import Thread
import sys
from datetime import datetime
import configparser
import requests
import webbrowser

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

def read_ini():
    conf = configparser.ConfigParser()
    path = "./settings/appinfo.ini"  # .replace("main.py", "appinfo.ini")
    if os.path.isfile(path):
        conf.read(path, encoding="UTF-8")
    else:
        conf.read(rf"{script_dir}\appinfo.ini", encoding="UTF-8")
    return conf["PROFILE"]["AppVersion"]

def read_server_ini():
    url = "https://raw.githubusercontent.com/yuzune27/IfnikkiRPC/refs/heads/master/settings/appinfo.ini"
    r = requests.get(url)
    conf = configparser.ConfigParser()
    conf.read_string(r.text)
    return conf["PROFILE"]["AppVersion"]

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class taskTray:
    def __init__(self):
        self.status = False

        image = Image.open(resource_path("icon.PNG"))

        local_version = read_ini()
        server_version = read_server_ini()

        if local_version != server_version:
            visible = True
        else:
            visible = False

        menu = Menu(
            MenuItem(f"Update is available! (->v{server_version})", self.open_gitpage, visible=visible),
            MenuItem(f"Version: {local_version}", enabled=False, action=None),
            MenuItem("Exit", self.stop_program),
        )

        self.icon = Icon(name="ifnikkiRPC", title="ifnikkiRPC", icon=image, menu=menu)

    def open_gitpage(self):
        url = "https://github.com/yuzune27/IfnikkiRPC/releases"
        webbrowser.open(url)

    def stop_program(self, icon):
        self.status = False
        icon.stop()

    def run_program(self):
        self.status = True
        self.icon.run()

def get_config():
    try:
        with open("./settings/config.json", "r", encoding="UTF-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        with open(rf"{script_dir}\config.json", "r", encoding="UTF-8") as f:
            data = json.load(f)

    lang = data["Lang"]
    player = data["Player"]
    uid = data["UID"]
    fc = data["FriendCode"]
    btn_label = data["BtnLabel"]
    btn_url = data["BtnUrl"]

    if data["UIDVisible"]:
        details = f"UID: {uid}"
    else:
        details = f"UID: ****"

    if data["FCVisible"]:
        state = f"FC: {fc}"
    else:
        state = f"FC: ****"

    return lang, player, details, state, btn_label, btn_url

def process_check():
    for proc in psutil.process_iter():
        try:
            get_proc = proc.exe()
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            pass
        else:
            if "X6Game-Win64-Shipping.exe" in get_proc:  # Debug -> pycharm64.exe
                return proc.pid
    return False

def lang_to_cid(lang):
    if lang == "ja":
        cid = "1293228317943529483"
    elif lang == "en":
        cid = "1314912127919853669"
    else:
        cid = "1293228317943529483"

    return cid

def rpc(lang, player, details, state, label, url):
    start_time = int(time.time())
    version = read_ini()

    cid = lang_to_cid(lang)

    data = [{
        "details": details,
        "state": state,
        "timestamps": {
            "start": start_time
        },
        "assets": {
            "large_image": "ifnikkik_new",
            "large_text": "ifnikkiRPC v" + version,
            "small_image": "ifnsmallk",
            "small_text": player
        },
        "buttons": [
            {
                "label": label,
                "url": url
            }
        ]
    }, ]

    with Presence(cid) as presence:
        presence.set(data[0])
        while True:
            if process_check():
                if (lang, player, details, state, label, url) != get_config():
                    lang, player, details, state, label, url = get_config()
                    data[0]["assets"]["small_text"] = player
                    data[0]["details"] = details
                    data[0]["state"] = state
                    data[0]["buttons"][0]["label"] = label
                    data[0]["buttons"][0]["url"] = url
                    presence.set(data[0])
                time.sleep(15)
            else:
                break

def log_write(dt, status, app, content):
    os.makedirs("log", exist_ok=True)

    logger = logging.getLogger(__name__)
    log_path = rf"{script_dir}\log\rpc{dt}.log"
    logging.basicConfig(filename=log_path, encoding="utf-8", level=logging.INFO, format="[%(asctime)s] %(message)s")
    if status == "ok":
        if app:
            info_text = f"InfinityNikki is running(PID: {app}). Executes an RPC function."
        else:
            info_text = f"InfinityNikki is not running. waiting..."
        logger.info(info_text)
    elif status == "error":
        logger.error(f"Unexpected error occurred.\n{content}")


def app_run():
    dt_now = datetime.now().strftime("%Y%m%d%H%M%S%f")
    try:
        lang, player, details, state, label, url = get_config()
    except Exception as e:
        log_write(dt=dt_now, status="error", app=None, content=e)
        return
    while True:
        try:
            pid = process_check()
            if pid:
                log_write(dt=dt_now, status="ok", app=pid, content=None)
                rpc(lang, player, details, state, label, url)
            else:
                log_write(dt=dt_now, status="ok", app=False, content=None)
            time.sleep(15)
        except Exception as e:
            log_write(dt=dt_now, status="error", app=None, content=e)
            break


if __name__ == "__main__":
    Thread(target=app_run, daemon=True).start()
    tray = taskTray()
    tray.run_program()