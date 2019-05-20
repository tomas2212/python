import threading
import urllib2
import re
from Queue import Queue

queue = Queue()

class MyThread(threading.Thread):

    def __init__(self, inter):
        threading.Thread.__init__(self)
        self.inter = inter

    def run(self):
        while(True):
            url = queue.get()
            if url == None:
                break
            try:
                html = urllib2.urlopen(url).read()
            except Exception:
                continue
            match = re.search('<title>(.*)</title>', html)
            if match:
                self.inter.write(match.group(1))

def titles(url):
    queue.put(url)

