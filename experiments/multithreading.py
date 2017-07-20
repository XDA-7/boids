import threading
import time

class Proclaimer (threading.Thread):
    def __init__(self, proclamation):
        self.proclamation = proclamation
        threading.Thread.__init__(self)
    def run(self):
        proclaim_eternally(self.proclamation)

def proclaim(proclamation):
    """Proclaim"""
    world_list = []
    for word in proclamation.split(' '):
        world_list.append(word.capitalize())
    print(' '.join(world_list) + '!')

def proclaim_eternally(proclamation):
    """Proclaim Eternally(every two seconds)"""
    while True:
        proclaim(proclamation)
        time.sleep(2)

one = Proclaimer('praise kek')
two = Proclaimer('sieg heil')
three = Proclaimer('hail satan')
four = Proclaimer('maga')
five = Proclaimer('long live the king')

one.start()
two.start()
three.start()
four.start()
five.start()