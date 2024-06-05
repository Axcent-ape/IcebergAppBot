# api id, hash
API_ID = 1488
API_HASH = 'abcd14888'

DELAYS = {
    'ACCOUNT': [5, 15],  # delay between connections to accounts (the more accounts, the longer the delay)
    'BEFORE_CLAIM': [5, 15],   # delay before claim points
    'CHANGE_STATUS_TASK': [10, 12],    #delay between change statuses of tasks delay between change statuses of tasks
}

# proxy type
PROXY_TYPE = "socks5"  # "socks4", "socks5" and "http" are supported

# session folder (do not change)
WORKDIR = "sessions/"
