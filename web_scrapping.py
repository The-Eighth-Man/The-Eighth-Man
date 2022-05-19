import pandas as pd
import numpy as np
from google_play_scraper import app
from google_play_scraper import Sort, reviews_all

reviews_claro = reviews_all(
    'com.clarocolombia.miclaro',
    sleep_milliseconds=0, # defaults to 0
    lang='es_CO', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
)

df = pd.DataFrame(np.array(reviews_claro),columns=['review'])
df = df.join(pd.DataFrame(df.pop('review').tolist()))
df.to_excel('reviews_claro.xlsx')