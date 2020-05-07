def word_counting(words):
    """단어들의 목록(words)를 전달받아서,
    {word: count}로 이루어진 dict를 리턴"""
    # 1) empty dict를 생성 ({단어: 단어가 등장한 횟수})
    word_cnt = {}  # dict()
    for word in words:
        # 2) words 리스트에 있는 단어들을 하나씩 꺼내면서
        if word in word_cnt:  # 단어가 dict의 키로 존재하는 지 검사
            word_cnt[word] += 1  # dict의 키로 있다면, dict[word] += 1
        else:
            word_cnt[word] = 1  # dict의 키에 없다면, dict[word] = 1
    return word_cnt


def most_common_words(word_cnt, n=5):
    """{word: count}로 이루어진 dict를 전달받아서,
    가장 많이 등장하는 단어 n개를 찾음"""
    # {word: count} dict의 아이템들을 하나씩 꺼내면서
    # [(count, word), ...] 튜플들의 리스트를 생성
    # word_list = []
    # for word, count in word_cnt.items():
    #     word_list.append((count, word))
    word_list = [(count, word) for word, count in word_cnt.items()]
    # 리스트를 내림차순 정렬(list.sort() 함수 이용)해서,
    word_list.sort(reverse=True)  # 내림차순 정렬
    # 처음부터 n개의 원소를 리턴함.
    return word_list[:n]


if __name__ == '__main__':
    article = """Alf Ramsey (22 January 1920 – 28 April 1999) was an English football player and manager. As England manager from 1963 to 1974, he guided them to victory in the 1966 FIFA World Cup. Knighted in 1967, he also managed his country to third place in the 1968 European Championship and the quarter-finals of the 1970 World Cup and the 1972 European Championship. As a player, he was a defender and a member of England's 1950 World Cup squad, and a part of the Tottenham Hotspur side that won the English League championship in the 1950–51 season. A statue of Ramsey was dedicated at the reconstructed Wembley Stadium in 2009, and various honours have been afforded to him for his eight years as Ipswich Town manager. He is the first person to be inducted twice into the English Football Hall of Fame: in 2002 in recognition of his achievements as a manager, and again in 2010 for his achievements as a player. He remains widely regarded as one of British football's all-time great managers."""

    # str.split() 함수를 사용해서 article의 단어 목록을 리스트로 생성 - words
    words = article.split()
    print(words)

    # word counting
    word_cnt = word_counting(words)
    print(word_cnt)

    # 가장 자주 등장하는 단어 순위 10위까지
    common_words = most_common_words(word_cnt, n=10)
    print(common_words)
