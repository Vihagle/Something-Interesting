import random
#做一个发牌器，将四种花色和13种数字大小随机生成7种组合，即发7张牌
def dealer(num = 7):
    suit = ['H','D','C','S']
    rank = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    hand = []
    for _ in range(num):
        Suit = random.choice(suit)
        Rank = random.choice(rank)
        hand.append(Rank+Suit)
    return hand

import itertools
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
print(hand)
#输出当前手牌最好的组合与其等级
print(best_hand(hand))
print(f'最好的手牌为等级{hand_rank(hand)[0]}')