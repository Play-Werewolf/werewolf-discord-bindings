import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from multiprocessing import Process


class bot_reset:

    def __init__(self):
        self.bot_proc = sb.

    def dispatch(self):
        print("hi")

if __name__ == "__main__":
    path = '.'
    event_handler = bot_reset
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1) 
    except KeyboardInterrupt:
        observer.stop()
    observer.join()