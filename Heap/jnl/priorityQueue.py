# list 사용 버전
class PriorityQueue(object):
    def __init__(self):
        self.que = []
    
    def __str__(self):
        return ''.join(str[i] for i in self.que)
    
    # for checking if the queue is empty
    def is_empty(self):
        return len(self.que) == 0

    # for inserting an element in the queue
    def insert(self, data:int):
        self.que.append(data)
    
    # for popping an element based on priority
    def delete(self):
        try:
            max_val = 0
            for i in range(len(self.que)):
                if self.que[i] > self.que[max_val]:
                    max_val = i
            item = self.que[max_val]
            del self.que[max_val]
            return item
        except IndexError:
            print()
            exit()
        
