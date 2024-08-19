deck = [0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 16 ,4]

n = int(input())
hand = 0

for card in range(n):
    draw_card = int(input())
    deck[draw_card] = deck[draw_card] - 1
    hand = hand + draw_card

x = 21 - hand

if sum(deck[:x+1]) >= sum((deck[x+1:])):
    print('VUCI')
else:
    print('DOSTA')
