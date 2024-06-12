#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


# Carico il dataset
data = pd.read_csv("amazon_prime_titles.csv")

# Stampo le info di base inerenti al dataset
data.head()


# In[8]:


data.columns


# In[9]:


data.info


# In[10]:


# Estraggo la durata in minuti
data['duration_minutes'] = data['duration'].str.extract('(\d+)').astype(float)

# Creo lo scatterplot
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.scatter(data['release_year'], data['duration_minutes'], alpha=0.5)
plt.title('Scatterplot dei film per anno di rilascio e durata')
plt.xlabel('Anno di Rilascio')
plt.ylabel('Durata (minuti)')
plt.grid(True)
plt.show()


# In[13]:


# Calcolo la correlazione tra l'anno di rilascio e la durata
correlation = data[['release_year', 'duration_minutes']].corr()

correlation


# In[14]:


# Creo un istogramma con i paesi di produzione più comuni
country_counts = data['country'].value_counts().head(10)  # Prendo i primi 10 paesi più comuni

plt.figure(figsize=(12, 6))
country_counts.plot(kind='bar')
plt.title('I 10 paesi di produzione più comuni')
plt.xlabel('Paese')
plt.ylabel('Numero di produzioni')
plt.xticks(rotation=45)
plt.show()


# In[15]:


# Filtro i dati per escludere Stati Uniti e India
filtered_country_counts = data[~data['country'].isin(['United States', 'India'])]['country'].value_counts().head(10)

# Creo un istogramma con i paesi di produzione più comuni (esclusi Stati Uniti e India)
plt.figure(figsize=(12, 6))
filtered_country_counts.plot(kind='bar')
plt.title('I 10 paesi di produzione più comuni (esclusi Stati Uniti e India)')
plt.xlabel('Paese')
plt.ylabel('Numero di produzioni')
plt.xticks(rotation=45)
plt.show()


# In[16]:


# Separo i generi in una lista per ogni titolo
data['genres'] = data['listed_in'].str.split(', ')

# Metto la lista in righe separate
genres_exploded = data.explode('genres')

# Calcolo la frequenza di ogni genere
genre_counts = genres_exploded['genres'].value_counts()

# Creo un istogramma con la distribuzione dei generi
plt.figure(figsize=(12, 8))
genre_counts.plot(kind='bar')
plt.title('Distribuzione dei generi')
plt.xlabel('Genere')
plt.ylabel('Numero di produzioni')
plt.xticks(rotation=45)
plt.show()


# In[20]:


import seaborn as sns

# Creo un istogramma con la distribuzione dei generi usando Matplotlib con etichette migliorate
plt.figure(figsize=(12, 8))
plt.bar(genre_counts.index, genre_counts.values, color='skyblue')
plt.title('Distribuzione dei generi')
plt.xlabel('Genere')
plt.ylabel('Numero di produzioni')
plt.xticks(rotation=70)
plt.tight_layout()
plt.show()


# In[ ]:




