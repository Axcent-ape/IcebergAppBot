# api id, hash
API_ID = 1488
API_HASH = 'abcde1488'

DELAYS = {
    'ACCOUNT': [5, 15],  # delay between connections to accounts (the more accounts, the longer the delay)
    'BEFORE_CLAIM': [5, 15],   # delay before claim points
    'CHANGE_STATUS_TASK': [10, 12],    # delay between change statuses of tasks delay between change statuses of tasks
}

# title blacklist tasks (do not change)
BLACKLIST_TASKS = ['Invite 5 friends', 'Invite 10 friends', 'Invite 15 friends', 'Like the post X', 'Follow the official Cyber Finance Telegram account']

PROXY = {
    "USE_PROXY_FROM_FILE": False,  # True - if use proxy from file, False - if use proxy from accounts.json
    "PROXY_PATH": "data/proxy.txt",  # path to file proxy
    "TYPE": {
        "TG": "socks5",  # proxy type for tg client. "socks4", "socks5" and "http" are supported
        "REQUESTS": "socks5"  # proxy type for requests. "http" for https and http proxys, "socks5" for socks5 proxy.
        }
}

# session folder (do not change)
WORKDIR = "sessions/"

# timeout in seconds for checking accounts on valid
TIMEOUT = 30

SOFT_INFO = f"""{"Iceberg".center(40)}
Soft for https://t.me/IcebergAppBot; claim rewards;
start farming; complete tasks; register accounts in web app

The soft also collects statistics on accounts and uses proxies from {f"the {PROXY['PROXY_PATH']} file" if PROXY['USE_PROXY_FROM_FILE'] else "the accounts.json file"}
To buy this soft with the option to set your referral link write me: https://t.me/Axcent_ape
"""