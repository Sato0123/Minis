import os
import shutil

HOSTS_PATH = "/etc/hosts"
BACKUP_PATH = "/etc/hosts.bak"
ENTRY = "127.0.0.2 victim.local"
ENTRY_POISNED = "127.0.0.1 victim.local"


def poisining():
    if os.path.exists(BACKUP_PATH):
        shutil.copy2(BACKUP_PATH, HOSTS_PATH)
        with open(HOSTS_PATH, "a") as f:
            f.write(f"\n{ENTRY_POISNED}\n")
        print("hostsを上書きました。")
    else:
        print("make host を実行してください")


def togle():
    """デモで使用するhostsのトグルスイッチ"""
    if os.path.exists(BACKUP_PATH):
        shutil.copy2(BACKUP_PATH, HOSTS_PATH)
        os.remove(BACKUP_PATH)
        print("hostsを復元しました。")
    else:
        shutil.copy2(HOSTS_PATH, BACKUP_PATH)
        with open(HOSTS_PATH, "a") as f:
            f.write(f"\n{ENTRY}\n")
        print("hostsを上書きました。")
