# ../datasets/babynames/ 폴더에
# yob1880.txt ~ yob2010.txt 파일들이 있습니다.
# 파일 개수만큼 DataFrame을 생성
# -> 각 데이터 프레임에 year 컬럼을 추가(파일이름에 포함된 숫자)
# 생성된 모든 데이터 프레임들을 하나의 DF로 합기치(concat)

import pandas as pd

# 텍스트 파일의 컬럼 이름(헤더) 정보.
col_names = ['name', 'gender', 'count']

years = range(1880, 2011)  # 파일 이름 접미사(연도)
all_names = []  # 각 연도별 DataFrame을 저장할 리스트
for year in years:
    path = f'../datasets/babynames/yob{year}.txt'
    # print(path)
    df = pd.read_csv(path, header=None, names=col_names)
    df['year'] = year  # 데이터 프레임마다 year 컬럼 추가
    # print(df.iloc[0])
    all_names.append(df)

print('length:', len(all_names))

# 131개의 DataFrame을 axis=0 방향으로 concat
data = pd.concat(all_names, ignore_index=True)
data.info()
print(data.iloc[:5])
print(data.iloc[-5:])








