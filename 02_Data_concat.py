import pandas as pd

category = ['드라마', '판타지', '공포', '로맨스', '모험', '스릴러', '다큐멘터리', '코미디', '가족', '애니메이션', '범죄', '액션', '에로']
read_csv = []

for i in category:
     read_csv.append(pd.read_csv(f'./crawling_data/crawling_data_{i}_1_30.csv'))
     read_csv.append(pd.read_csv(f'./crawling_data/crawling_data_{i}_31_60.csv'))
     read_csv.append(pd.read_csv(f'./crawling_data/crawling_data_{i}_61_90.csv'))
     read_csv.append(pd.read_csv(f'./crawling_data/crawling_data_{i}_91_120.csv'))
     read_csv.append(pd.read_csv(f'./crawling_data/crawling_data_{i}_121_150.csv'))
     read_csv.append(pd.read_csv(f'./crawling_data/crawling_data_{i}_151_180.csv'))
     read_csv.append(pd.read_csv(f'./crawling_data/crawling_data_{i}_181_210.csv'))
     read_csv.append(pd.read_csv(f'./crawling_data/crawling_data_{i}_211_240.csv'))
     read_csv.append(pd.read_csv(f'./crawling_data/crawling_data_{i}_241_270.csv'))
     read_csv.append(pd.read_csv(f'./crawling_data/crawling_data_{i}_271_300.csv'))

final_concat = pd.concat(read_csv)
print(final_concat)

final_concat.to_csv('./final_concat_data.csv', index=False)