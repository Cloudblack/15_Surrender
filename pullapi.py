# import requests
# import json 
# from pprint import pprint
# import pandas as pd
# api='RGAPI-77fe8141-afd9-4f46-b65e-627797285e27'
# id='토니토니김치'
# def searchid(id):        
#     searchid=f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{id}?api_key={api}"
#     r=requests.get(searchid)
#     v=r.json()
#     pprint(v)
# def search_tier(leagues,num,page):     
#     #example : "https://kr.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/DIAMOND/IV?page=150"   
#     search_tier=f"https://kr.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{leagues}/{num}?page={page}?api_key={api}"
#     r=requests.get(search_tier)
#     v=r.json()
#     pprint(v)
# #search_tier('DIAMOND','IV',5)    
# #searchid(id)
# grandmaster = 'https://kr.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5?api_key=' + api
# r = requests.get(grandmaster)#그마데이터 호출
# league_df = pd.DataFrame(r.json())
# print(league_df.head())
# """
# ㄴㅇㄴㅇ
# """


