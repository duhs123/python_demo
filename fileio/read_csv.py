#coding = utf-8
import pandas as pd
fh = r'E:\dataMining\python\python_project\crawling\中国天气网城市代码.csv'
data = pd.read_csv(fh,engine='python',encoding='utf-8')
data = data.dropna()
