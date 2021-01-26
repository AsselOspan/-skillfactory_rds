#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter


# In[2]:


data = pd.read_csv('movie_bd_v5.csv')
data


# In[3]:


data.describe()


# # Предобработка

# In[4]:


answers = {} # создадим словарь для ответов
# тут другие ваши предобработки колонок например:

#the time given in the dataset is in string format.
#So we need to change this in datetime format
# ...


# # 1. У какого фильма из списка самый большой бюджет?

# Использовать варианты ответов в коде решения запрещено.    
# Вы думаете и в жизни у вас будут варианты ответов?)

# In[5]:


# в словарь вставляем номер вопроса и ваш ответ на него
# Пример: 
answers['1'] = '2. Spider-Man 3 (tt0413300)'
# запишите свой вариант ответа
answers['1'] = '723. Pirates of the Caribbean: On Stranger Tides (tt1298650)'
#+
# если ответили верно, можете добавить комментарий со значком "+"


# In[6]:


# тут пишем ваш код для решения данного вопроса:
data[data.budget==data.budget.max()]


# ВАРИАНТ 2

# In[7]:


# можно добавлять разные варианты решения
data.groupby(['original_title'])['budget'].sum().sort_values(ascending=False)


# # 2. Какой из фильмов самый длительный (в минутах)?

# In[8]:


# думаю логику работы с этим словарем вы уже поняли, 
# по этому не буду больше его дублировать
answers['2'] = '1157. Gods and Generals (tt0279111)'


# In[9]:


data[data.runtime==data.runtime.max()]


# # 3. Какой из фильмов самый короткий (в минутах)?
# 
# 
# 
# 

# In[10]:


answers['3'] = '768. Winnie the Pooh (tt1449283)'


# In[11]:


data[data.runtime==data.runtime.min()]


# # 4. Какова средняя длительность фильмов?
# 

# In[12]:


answers['4']=109.6585494970884


# In[13]:


data.runtime.mean()


# # 5. Каково медианное значение длительности фильмов? 

# In[14]:


answers['5']=107.0


# In[15]:


data.runtime.median()


# # 6. Какой самый прибыльный фильм?
# #### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) 

# In[16]:


answers['6']='239. Avatar (tt0499549)'


# In[17]:


# лучше код получения столбца profit вынести в Предобработку что в начале
data['profit']=data['revenue']-data['budget']
data[data.profit==data.profit.max()]


# # 7. Какой фильм самый убыточный? 

# In[18]:


answers['7']='1245.The Lone Ranger (tt1210819)'


# In[19]:


data[data.profit==data.profit.min()]


# # 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

# In[20]:


answers['8']=1478


# In[21]:


len(data[data.revenue>data.budget])


# # 9. Какой фильм оказался самым кассовым в 2008 году?

# In[22]:


answers['9']='599. The Dark Knight (tt0468569)'


# In[23]:


data[(data.release_year==2008) & (data.revenue>data.budget)].sort_values('revenue', ascending=False)


# # 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?
# 

# In[24]:


answers['10']='1245. The Lone Ranger (tt1210819)'


# In[25]:


data2=data[(data.release_year>=2012) & (data.release_year<=2014) & (data.revenue<data.budget)]
data2[data2.profit==data2.profit.min()]


# # 11. Какого жанра фильмов больше всего?

# In[26]:


answers['11']='Drama'


# In[27]:


# эту задачу тоже можно решать разными подходами, попробуй реализовать разные варианты
# если будешь добавлять функцию - выноси ее в предобработку что в начале
pd.Series(data['genres'].str.cat(sep='|').split('|')).value_counts()


# ВАРИАНТ 2

# # 12. Фильмы какого жанра чаще всего становятся прибыльными? 

# In[28]:


answers['12']='Drama'


# In[29]:


data=pd.read_csv('movie_bd_v5.csv')
data['genres']=data['genres'].apply(lambda x:x.split('|'))
data_explode=data.explode('genres')
data['profit']=data['revenue']-data['budget']
data3=data[data.profit>0].sort_values(by='profit', ascending=False).explode('genres')
data3['genres'].value_counts()


# # 13. У какого режиссера самые большие суммарные кассовые сборы?

# In[30]:


answers['13']= 'James Cameron'


# In[31]:


data[data.revenue==data.revenue.max()]


# # 14. Какой режисер снял больше всего фильмов в стиле Action?

# In[32]:


answers['14']= 'Michael Bay'


# In[55]:


data=pd.read_csv('movie_bd_v5.csv')
data['genres']=data['genres'].apply(lambda x:x.split('|'))
data_explode=data.explode('genres')
data_explode
act=data_explode[data_explode.genres=='Action']
act
act.groupby(['director'])['genres'].value_counts().sort_values(ascending=False)


# # 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? 

# In[34]:


answers['15']= 'Robert Downey Jr.'


# In[35]:


data=pd.read_csv('movie_bd_v5.csv')
data['cast']=data['cast'].apply(lambda x:x.split('|'))
data_cast=data.explode('cast')
data_cast[(data_cast.revenue>0) & (data_cast.release_year==2012)].sort_values(by='revenue', ascending=False)


# # 16. Какой актер снялся в большем количестве высокобюджетных фильмов?

# In[36]:


answers['16']= 'Adam Sandler'


# In[37]:


data=pd.read_csv('movie_bd_v5.csv')
data['cast']=data['cast'].apply(lambda x:x.split('|'))
data_cast=data.explode('cast')
data_cast.groupby(['cast'])['budget'].value_counts().sort_values(ascending=False)


# # 17. В фильмах какого жанра больше всего снимался Nicolas Cage? 

# In[38]:


answers['17']= 'Action'


# In[39]:


data=pd.read_csv('movie_bd_v5.csv')
data['cast']=data['cast'].apply(lambda x:x.split('|'))
data_cast=data.explode('cast')
NC=data_cast[data_cast.cast=='Nicolas Cage']
NC
NC['genres']=NC['genres'].apply(lambda x:x.split('|'))
NC_genres=NC.explode('genres')
NC_genres
NC_genres.groupby(['cast'])['genres'].value_counts()


# # 18. Самый убыточный фильм от Paramount Pictures

# In[40]:


answers['18']= 'K-19: The Widowmaker'


# In[41]:


data=pd.read_csv('movie_bd_v5.csv')
data['production_companies']=data['production_companies'].apply(lambda x:x.split('|'))
data_prod=data.explode('production_companies')
data_prod['profit']=data_prod['revenue']-data_prod['budget']
data_prod
ParPic=data_prod[data_prod.production_companies=='Paramount Pictures']
#ParPic.groupby(['original_title'])['profit'].value_counts().sort_values(ascending=False)
ParPic[ParPic.profit==ParPic.profit.min()]        


# # 19. Какой год стал самым успешным по суммарным кассовым сборам?

# In[42]:


answers['19']= 2015


# In[43]:


data=pd.read_csv('movie_bd_v5.csv')
data['release_year'].sort_values(ascending=False)
data_year=data.groupby(['release_year'])['revenue'].sum().sort_values(ascending=False)
data_year


# # 20. Какой самый прибыльный год для студии Warner Bros?

# In[44]:


answers['20']= 2011


# In[45]:


data=pd.read_csv('movie_bd_v5.csv')
data_warn=[]
for i in range(len(data.production_companies)):
    if 'Warner Bros.' in data.production_companies.loc[i]:
        data_warn.append(data.loc[i]) 
data_warn_bro=pd.DataFrame(data_warn)  
data_20=data_warn_bro.explode('production_companies').groupby(['production_companies', 'release_year'])['revenue'].aggregate('sum').unstack()
data_20.loc['Warner Bros.'].sort_values(ascending=False)


# # 21. В каком месяце за все годы суммарно вышло больше всего фильмов?

# In[46]:


answers['21']= 9


# In[47]:


data=pd.read_csv('movie_bd_v5.csv')
data['release_date']=data['release_date'].apply(lambda x:x.split('/'))
data_month=data.release_date.explode('release_date')
data_month_2=data_month[0::3]
data_month_2.value_counts()


# # 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)

# In[48]:


answers['22']=450


# In[49]:


data=pd.read_csv('movie_bd_v5.csv')
data['release_date']=data['release_date'].apply(lambda x:x.split('/'))
data_month=data.release_date.explode('release_date')
data_month_2=data_month[0::3]
dm=pd.DataFrame(data_month_2)
dm['release_date']=dm['release_date'].astype('int64')
dm[(dm.release_date>=6) & (dm.release_date<=8)].value_counts().sum()


# # 23. Для какого режиссера зима – самое продуктивное время года? 

# In[50]:


answers['23']=


# In[51]:


data=pd.read_csv('movie_bd_v5.csv')
data['release_date']=data['release_date'].apply(lambda x:x.split('/'))
data_month=data.explode('release_date')
dm=data_month[0::3].groupby(['director', 'revenue'])['release_date'].value_counts()
dm2=pd.DataFrame(dm)
dm2
#dm2[(dm2.release_date==1) & (dm2.release_date==2) & (dm2.release_date==12)]

#dm2=data_month.release_date.astype('int64')
#dm2[::3]
# .groupby(['director'])['release_date'].value_counts()
#data_month3=pd.DataFrame(data_month)
#data_month3
# data_month_2=data_month[0::3]
# data_month_2
# dm=pd.DataFrame(data_month_2)
# dm['release_date']=dm['release_date'].astype('int64')
# dm[(dm.release_date==6) & (dm.release_date<=8)].value_counts().sum()


# # 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?

# In[ ]:





# # 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?

# In[ ]:





# # 26. Какие фильмы входят в 1 процент лучших по рейтингу? 
# по vote_average

# In[ ]:





# # 27. Какие актеры чаще всего снимаются в одном фильме вместе?
# 

# ВАРИАНТ 2

# # Submission

# In[52]:


# в конце можно посмотреть свои ответы к каждому вопросу
answers


# In[53]:


# и убедиться что ни чего не пропустил)
len(answers)


# In[ ]:





# In[ ]:




