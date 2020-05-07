from collections import defaultdict
from collections import Counter

# from py08_collections.ex01 import most_common_words

article = """Alf Ramsey (22 January 1920 – 28 April 1999) was an English football player and manager. As England manager from 1963 to 1974, he guided them to victory in the 1966 FIFA World Cup. Knighted in 1967, he also managed his country to third place in the 1968 European Championship and the quarter-finals of the 1970 World Cup and the 1972 European Championship. As a player, he was a defender and a member of England's 1950 World Cup squad, and a part of the Tottenham Hotspur side that won the English League championship in the 1950–51 season. A statue of Ramsey was dedicated at the reconstructed Wembley Stadium in 2009, and various honours have been afforded to him for his eight years as Ipswich Town manager. He is the first person to be inducted twice into the English Football Hall of Fame: in 2002 in recognition of his achievements as a manager, and again in 2010 for his achievements as a player. He remains widely regarded as one of British football's all-time great managers."""

words = article.split()  # 단어들의 리스트

word_cnt = defaultdict(int)  # defaultdict 클래스 타입 인스턴스 생성
# dict의 값(value)의 데이터 타입을 int로 설정

for word in words:
    word_cnt[word] += 1

print(word_cnt)

# Counter 클래스를 이용한 단어 개수 세기
counter = Counter(words)
print(counter)
print(counter.most_common(5))
