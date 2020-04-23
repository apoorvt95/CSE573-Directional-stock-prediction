import nltk
import json
import os
import pandas as pd
data_published=[]
data_text=[]
with os.scandir('News/') as folders:
    for folder in folders:
        print(folder.name)
        if folder.name!=".DS_Store":
            with os.scandir('News/'+folder.name) as entries:
                for entry in entries:
                    with open("News/"+folder.name+"/"+entry.name, encoding="latin1") as f:
                        data = json.load(f, )
                    if data['published']=="":
                        data_published.append("No Value")
                    else:
                        data_published.append(data['published'])
                    if data['text']=="":
                        data_text.append("No Value")
                    else:
                        data_text.append(data['text'])

df=pd.DataFrame({
    'time':data_published,
    'text':data_text
})
print(df.columns.values)
current_data=df
from datetime import datetime
date=df.loc[1]['time']
print(date)
print(df.columns.values)
# load_date=datetime.strftime(date,'%Y-%m-%d %H:%M:%S')
d=pd.to_datetime(date, format="%Y/%m/%d %H:%M:%S")
print(d.year,d.month,d.day)
day=[]
time=[]
for i in range(len(df)):
    date=df.loc[i]['time']
    time_stamp=pd.Timestamp(date)
    day.append(time_stamp.date())
    time.append(time_stamp.time())
df['day']=day
df['24_time']=time
df.drop(['time'],axis=1,inplace=True)

col_names = ['text', 'day', '24_time']
my_df  = pd.DataFrame(columns = col_names)
for index, row in df.iterrows():
    print(index)
    text=row['text'].lower()
    day=row['day']
    time24=row['24_time']

    paragraphs = nltk.sent_tokenize(text)
    sentences=[]
    for para in paragraphs:
        sentences_list = para.split("\n")
        for sentence in sentences_list:
            if 'amazon' in sentence or 'apple' in sentence or 'aapl' in sentence or 'amzn' in sentence:
                my_df.loc[len(my_df)] =[sentence,day,time24]
            
print(my_df)
my_df.sort_values(["day","24_time"], axis = 0, ascending = (True, True), 
                 inplace = True)

my_df.to_csv('ExtractedNewsSentenceWise2.csv')