import random
from collections import defaultdict
import tkinter
import numpy as np
import matplotlib.pyplot as plt

# 포커 7장을 뽑는다
# 가장 잘 나온 패를 기록한다
# 통계에 갱신한다
# 통계를 보여준다

############ function ############


def match_card_shape(shape):
    return {
        '1': "s",
        '2': "d",
        '3': "h",
        '4': "c"
    }.get(str(shape), -1)


def match_card_number(number):
    if number > 9 or number == 1:
        return {
            '1': "a",
            '10': "t",
            '11': "j",
            '12': "q",
            '13': "k"
        }.get(str(number), -1)
    return str(number)


def draw_card():
    for card in range(5):
        temp_shape = random.randrange(1, 5)
        temp_number = random.randrange(1, 14)
        shape = match_card_shape(temp_shape)
        number = match_card_number(temp_number)
        cur_card = number + shape
        hand.append(cur_card)
    # print("hand : " + str(hand))


def is_rofl():
    max_value = 0
    if is_stfl():
        for card in hand:
            cur_value = card_order_dict[card[0]]
            max_value = cur_value if (cur_value > max_value) else max_value
        if max_value == 14:
            return True
    return False


def is_stfl():
    if is_straight() and is_flush():
        return True
    return False


def is_4card():
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 4]:
        return True
    return False


def is_fullhouse():
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [2, 3]:
        return True
    return False


def is_flush():
    shapes = [h[1] for h in hand]
    if len(set(shapes)) == 1:
        return True
    return False


def is_straight():
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    rank_values = [card_order_dict[i] for i in values]
    value_range = max(rank_values) - min(rank_values)
    if len(set(value_counts.values())) == 1 and (value_range == 4):
        return True
    else:
        # check straight with low Ace
        if set(values) == set(["a", "2", "3", "4", "5"]):
            return True
        return False
    return False


def is_tripple():
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if set(value_counts.values()) == set([3, 1]):
        return True
    return False


def is_two():
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 2, 2]:
        return True
    return False


def is_one():
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if 2 in value_counts.values():
        return True
    return False


def check_card():
    if is_rofl():
        # print("royal straight flush!!!")
        return ROFL
    if is_stfl():
        # print("straight flush!!")
        return STFL
    if is_4card():
        # print("four card!")
        return FOUR_CARD
    if is_fullhouse():
        # print("full house")
        return FULLHOUSE
    if is_flush():
        # print("flush")
        return FLUSH
    if is_straight():
        # print("straight")
        return STRAIGHT
    if is_tripple():
        # print("tripple")
        return TRIPPLE
    if is_two():
        # print("two pair")
        return TWO
    if is_one():
        # print("one pair")
        return ONE
    # print("high..")
    return HIGH


def update_stack(result):
    stack[result] += 1

def run_simulator(epoch):
    for gen in range(epoch):
        hand.clear()
        draw_card()
        result = check_card()
        update_stack(result)
    print(stack)


def handle_return(event=0):
    epoch = int(entry.get())
    window.destroy()
    run_simulator(epoch)

################################


### initialize constant ###
card_order_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                   "8": 8, "9": 9, "t": 10, "j": 11, "q": 12, "k": 13, "a": 14}
HIGH = 0
ONE = 1
TWO = 2
TRIPPLE = 3
STRAIGHT = 4
FLUSH = 5
FULLHOUSE = 6
FOUR_CARD = 7
STFL = 8
ROFL = 9

hand = []
stack = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# high, one, two, tripple, straight, flush, fullhouse, 4card, stfl, rofl

### initialize gui ###
window = tkinter.Tk()
WINDOW_SIZE = "640x400"
window.title("Poker Simulator")
window.geometry(f"{WINDOW_SIZE}+1400+600")
window.resizable(True, True)

label = tkinter.Label(window, text='Enter Epoch')
entry = tkinter.Entry(window)
button = tkinter.Button(window, text='return', command=handle_return)
label.pack()
entry.pack()
button.pack()

entry.bind('<Return>', handle_return)

window.mainloop()