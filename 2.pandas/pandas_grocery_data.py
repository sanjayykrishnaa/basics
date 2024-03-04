import requests
import pandas as pd
import json 
import re
def getitem(search_term,category,site):
    with open('/home/mykel/works/Rotech/week_10/configs/competitors.json', 'r') as file:
            competitor = json.load(file)[site]     
    URL = f"{competitor['store_api']}{category}/{search_term}"
    HEADERS = { 
        'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
        'Cookie':competitor['cookie']
    }
    status=404
    item_found="No item Found"
    response = requests.get(URL, headers=HEADERS)
    data = response.json()
    items=data.get('items')
    data_df = pd.DataFrame(items)

    data_df=data_df[['name','base_price','categories']]
    # data_df['categories'] = data_df['categories'].apply(lambda x: [category['name'] for category in x])
    data_df['name'] = data_df['name'].str.lower().str.replace('\d+', '')
    data_df['categories'] = data_df['categories'].apply(lambda x: [re.sub('\d+', '', category['name'].lower()) for category in x])
    # data_df['categories'] = data_df['categories'].apply(lambda x: [category['name'].lower().replace('\d+', '', regex=True) for category in x])
    data_df.to_excel('example.xlsx', index=False, engine='openpyxl')
    return data_df['categories']
        
print(getitem('apple','fruits','sprouts'))