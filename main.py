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

def read_ini():
    conf = configparser.ConfigParser()
    path = sys.argv[0].replace("ifnikkiRPC.exe", "appinfo.ini")  # .replace("main.py", "appinfo.ini")
    conf.read(path, encoding="UTF-8")
    return conf["PROFILE"]["AppVersion"]

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class taskTray:
    def __init__(self):
        self.status = False

        image = Image.open(resource_path("icon.PNG"))
        version = read_ini()
        menu = Menu(
            MenuItem(f"Version: {version}", None),
            MenuItem("Exit", self.stop_program),
        )

        self.icon = Icon(name="ifnikkiRPC", title="ifnikkiRPC", icon=image, menu=menu)

    def stop_program(self, icon):
        self.status = False
        icon.stop()

    def run_program(self):
        self.status = True
        self.icon.run()

def get_config():
    with open("config.json", "r") as f:
        data = json.load(f)

    uid = data["UID"]
    btn_label = data["BtnLabel"]
    btn_url = data["BtnUrl"]

    if data["UIDVisible"]:
        details = f"UID: {uid}"
    else:
        details = f"UID: ****"
    return details, btn_label, btn_url

def process_check():
    for proc in psutil.process_iter():
        try:
            get_proc = proc.exe()
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            pass
        else:
            if "X6Game-Win64-Shipping.exe" in get_proc:
                return proc.pid
    return False

def rpc(details, label, url):
    cid = "1293228317943529483"
    start_time = int(time.time())
    version = read_ini()

    data = [{
        "details": details,
        "timestamps": {
            "start": start_time
        },
        "assets": {
            "large_image": "ifnikkik",
            "large_text": "ifnikkiRPC",
            "small_image": "ifnsmallk",
            "small_text": version
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
                if (details, label, url) != get_config():
                    details, label, url = get_config()
                    data[0]["details"] = details
                    data[0]["buttons"][0]["label"] = label
                    data[0]["buttons"][0]["url"] = url
                    presence.set(data[0])
                time.sleep(15)
            else:
                break

def log_write(dt, status, app, content):
    os.makedirs("log", exist_ok=True)

    logger = logging.getLogger(__name__)
    log_path = f"./log/rpc{dt}.log"
    logging.basicConfig(filename=log_path, encoding="utf-8", level=logging.INFO, format="[%(asctime)s] %(message)s")
    if status == "ok":
        if app:
            info_text = f"InfinityNikki is running(PID: {app}). Executes an RPC function."
        else:
            info_text = f"InfinityNikki is not running. waiting..."
        logger.info(info_text)
    elif status == "error":
        taskTray().stop_program(taskTray().icon)
        logger.error(f"Unexpected error occurred.\n{content}")


def app_run():
    dt_now = datetime.now().strftime("%Y%m%d%H%M%S%f")
    try:
        details, label, url = get_config()
    except Exception as e:
        log_write(dt=dt_now, status="error", app=None, content=e)
        return
    while True:
        try:
            pid = process_check()
            if pid:
                log_write(dt=dt_now, status="ok", app=pid, content=None)
                rpc(details, label, url)
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