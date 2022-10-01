import sys
sys.stdin = open("input.txt","r")
n = int(sys.stdin.readline())
front, rear, no = 0, 0, n
cards=[None]*n
for i in range(n):
    cards[i]= i+1

def enqueue(card) :
    global front, rear, no, cards
    cards[rear] = card
    no += 1
    if rear == n-1 :
        rear = 0
    else:
        rear +=1

def dequeue() :
    global front, rear, no, cards
    dequeued_card = cards[front] 
    cards[front] = None
    no -= 1
    if front == n-1 :
        front = 0
    else:
        front +=1
    return dequeued_card


while no > 1 : 
    dequeue()
    enqueue(dequeue())
print(cards[front])


