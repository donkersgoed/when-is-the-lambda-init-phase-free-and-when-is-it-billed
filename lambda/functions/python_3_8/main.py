import os
import time

INIT_SLEEP = int(os.environ["INIT_SLEEP"])
HANDLER_SLEEP = int(os.environ["HANDLER_SLEEP"])

start = time.time()
print("Init starting")
print(f"Sleep for {INIT_SLEEP} second(s)")
time.sleep(INIT_SLEEP)
print("Init done")


def handler(_event, _context):
    """Main Lambda handler."""
    print("Handler starting")
    print(f"Sleep for {HANDLER_SLEEP} second(s)")
    time.sleep(HANDLER_SLEEP)
    print("Handler done")
