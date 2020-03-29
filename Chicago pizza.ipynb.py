#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from urllib.request import urlopen, urljoin

url_base='https://www.chicagomag.com'
url_sub='/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/'
url = url_base + url_sub

html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")

soup


# In[2]:


print(soup.find_all('div', 'sammy'))


# In[3]:


len(soup.find_all('div','sammy'))


# In[4]:


print(soup.find_all('div','sammy')[0])


# In[5]:


tmp_one = soup.find_all('div','sammy')[0]
type(tmp_one)


# In[6]:


tmp_one.find(class_='sammyRank')


# In[7]:


tmp_one.find(class_='sammyRank').get_text()


# In[8]:


tmp_one.find(class_='sammyListing').get_text()


# In[9]:


tmp_one.find('a')['href']


# In[10]:


import re

tmp_string = tmp_one.find(class_='sammyListing').get_text()

re.split(('\n|\r\n'), tmp_string)

print(re.split(('\n|\r\n'), tmp_string)[0])
print(re.split(('\n|\r\n'), tmp_string)[1])


# In[12]:


rank = []
main_menu = []
cafe_name = []
url_add=[]

list_soup = soup.find_all('div', 'sammy')

for item in list_soup:
    rank.append(item.find(class_='sammyRank').get_text())
                
    tmp_string = item.find(class_='sammyListing').get_text()

    main_menu.append(re.split(('\n|\r\n'), tmp_string)[0])
    cafe_name.append(re.split(('\n|\r\n'), tmp_string)[1])
                     
    url_add.append(urljoin(url_base, item.find('a')['href']))


# In[13]:


rank[:5]


# In[14]:


main_menu[:5]


# In[15]:


cafe_name[:5]


# In[16]:


url_add[:10]


# In[17]:


len(rank), len(main_menu), len(cafe_name), len(url_add)


# In[18]:


import pandas as pd

data = {'Rank':rank, 'Menu':main_menu, 'Cafe':cafe_name, 'URL':url_add}
df= pd.DataFrame(data)
df.head()


# In[19]:


df = pd.DataFrame(data, columns=['Rank', 'Cafe', 'Menu', 'URL'])
df.head(5)


# In[20]:


df['URL'][0] 


# In[23]:


html= urlopen(df['URL'][0] )

soup_tmp = BeautifulSoup(html, "html.parser")
soup_tmp


# In[24]:


print(soup_tmp.find('p', 'addy'))


# In[25]:


price_tmp = soup_tmp.find('p', 'addy').get_text()
price_tmp


# In[26]:


price_tmp.split()


# In[27]:


price_tmp.split()[0]


# In[28]:


price_tmp.split()[0][:-1]


# In[29]:


''.join(price_tmp.split()[1:-2])


# In[30]:


price = []
address = []

for n in df.index[:3]:
    html = urlopen(df['URL'][n])
    soup_tmp = BeautifulSoup(html, 'lxml')
    
    gettings = soup_tmp.find('p','addy').get_text()
    
    price.append(gettings.split()[0][:-1])
    address.append(''.join(gettings.split()[1:-2]))


# In[31]:


price


# In[32]:


address


# In[33]:


df = pd.read_csv('../data/03. best_sandwiches_list_chicago2.csv', index_col=0)
df.head(5)


# In[ ]:


# google maps location 관련해서는 나중에 google api key 받아서 추가 

