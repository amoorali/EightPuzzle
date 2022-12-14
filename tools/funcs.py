def index(item, list):
    try:
        return list.index(item)
    except:
        return -1

class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        try:
            pass
        except IndexError:
            pass


class HashMap:
    def __init__(self) -> None:
        self.hashmap = [PriorityQueue() for _ in range(10)]

    def put(self, obj, key):
        hashed_key = self.hash(key)
        self.hashmap[hashed_key].enqueue(obj)

    def get(self, key):
        hashed_key = self.hash(key)
        return self.hashmap[hashed_key].dequeue()

    def hash(self, key):
        return key % len(self.hashmap)
