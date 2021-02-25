import random
#做一个发牌器，将四种花色和13种数字大小随机生成7种组合，即发7张牌，其中存在红、黑两种颜色的Joker的情况
def dealer(num = 7):
    #将Joker划分到花色suit这个列表里
    suit = ['H','D','C','S','?B','?R']
    rank = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    hand = []
    count = 0
    while count != num:
        Suit = random.choice(suit)
        Rank = random.choice(rank)
        #如果发到Joker的牌，则将suit列表中相对应Joker牌拿掉，避免重复发到Joker牌
        if (Suit == '?B') or (Suit == '?R'):
                hand.append(Suit)
                suit.remove(Suit)
                count += 1
        #如果发到的牌与手里的牌重复，则重新发过
        elif (Rank+Suit) in hand:
            continue
        else:
            hand.append(Rank+Suit)
            count += 1
    return hand


import itertools
#此处定义Joker牌的规则，如果抽到红色Joker，则可以将其换成方块（Diamond）或红桃（Heart）花色任意大小的牌，同样，如果是黑Joker，则可以替换成黑桃（Spade）或梅花（Club）花色任意大小的牌
all_rank = '23456789TJQKA'
redcard = [r+s for r in all_rank for s in 'DH']
blackcard = [r+s for r in all_rank for s in 'SC']

def best_wild_hand(hand):
    # for h in itertools.product(*map(replacement, hand)):
    #     print(h)
    '''
    这里用了比较tricky的方法，将手里的牌放到map函数里面，一一将手牌遍历到replacement里面的函数，得到Joker所能替换的所有手牌列表，然后利用itertools.product函数，将所有情况进行组合，
    再遍历所有组合，放到best_hand函数里面去，获得不同组合所能出现最好手牌的集合。
    '''
    hands = set(best_hand(h)for h in itertools.product(*map(replacement,hand)))
    #取得每个组合的最高等级的手牌
    return max(hands,key = hand_rank)

#此处replacement的作用是将Joker牌替换成所有能替换的手牌形成的列表
def replacement(card):
        if card == '?B':
            return blackcard
        elif card == '?R':
            return redcard
        else:
            return [card]

#将发下来的7张手牌，随机抽取5张，通过hand_rank判断抽取的5张手牌属于那种类型组合，并通过等级大小判断选出最好的手牌
def best_hand(hand):
    return max(list(itertools.combinations(hand,5)),key = hand_rank)

#判断手牌存在哪种类型的组合
def hand_rank(hand):
    #获取经过排序后的手牌索引列表
    ranks = card_ranks(hand)
    #如果同时存在顺子类型和同花类型，则为等级8（最高等级），输出尾数最大的同花顺牌
    if straight(ranks) and flush(hand):
        return (8,max(ranks))
    #如果存在4张大小一样的牌（不论花色），则为等级7，根据剩余一张数字最大来输出手牌
    elif kind(4,ranks):
        return (7,kind(4,ranks),kind(1,ranks))
    #如果存在3张大小一样而且还有两张对子的手牌，则为等级6，根据剩余两张对子数字最大来输出手牌
    elif kind(3,ranks) and kind(2,ranks):
        return (6,kind(3,ranks),kind(2,ranks))
    #如果只存在5张全部同样花色的手牌（不论数字大小），则为等级5
    elif flush(hand):
        return (5,ranks)
    #如果只存在5张按顺序排序的手牌（不论花色），则为等级4
    elif straight(ranks):
        return (4,max(ranks))
    #如果只存在3张大小一样的手牌（剩余两张不是对子），则为等级3
    elif kind(3,ranks):
        return (3,kind(3,ranks),ranks)
    #如果存在含有两副对子的手牌，则为等级2
    elif two_pair(ranks):
        return (2,two_pair(ranks),ranks)
    #如果存在含有一副对子的手牌（剩余三张不论大小），则为等级1
    elif kind(2,ranks):
        return (1,kind(2,ranks),ranks)
    #如果上述情况都不存在，则为等级0
    else:
        return (0,ranks)

#将获取的手牌转化为索引大小并进行排序
def card_ranks(hand):
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse = True)
    return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks

#定义同花类型的牌
def flush(hand):
    suit = [s for r,s in hand]
    return len(set(suit)) == 1

#定义顺子类型的牌
def straight(ranks):
    return (max(ranks) - min(ranks) == 4) and (len(set(ranks)) == 5)

#定义不同数量的同数字的牌的组合
def kind(n,ranks):
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None
#定义对子类型的牌
def two_pair(ranks):
    pair = kind(2,ranks)
    lowpair = kind(2,list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair,lowpair)
    else:
        return None


hand = dealer(num=7)
#输出当前手牌
print(f'当前的手牌是：{hand}')
#输出当前手牌最好的组合与其等级
print(f'当前手牌最好的组合是：{best_wild_hand(hand)}')
