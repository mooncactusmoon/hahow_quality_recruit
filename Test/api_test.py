import requests

swapi = requests.get("https://swapi.dev/api/")
swapi_data = swapi.json()

all_films = requests.get(swapi_data["films"]).json()
films_results = all_films["results"]

## 有多少不同種族的人出現在第六部？
for i in range(len(films_results)):
    if films_results[i]['episode_id'] == 6:
        species_list = films_results[i]['species']
        #若 species Api 沒有重複的種族名稱，則可直接寫 "len(films_results[i]['species'])" 來取得總數

# 不確定species Api 是否有重複的種族名稱，因此以下多做此判斷處理 (利用元組可以直接濾掉重複的值之特性)
species_name_list = []

for i in range(len(species_list)):
    species_name = requests.get(species_list[i]).json()['name']
    species_name_list.append(species_name)

species_name_list_total = len(list(set(species_name_list)))

print(f'總共有 "{species_name_list_total}" 種不同種族的人出現在第六部')

## 請依據電影集數去排序電影名字？
films_list = {}

for i in range(len(films_results)):
    films_list[films_results[i]['episode_id']] = films_results[i]['title']

for i in range(len(films_results)):
    print(f'第 {i+1} 集電影名稱為 : {films_list[i+1]}')

## 請幫我挑出電影裡所有的車輛，馬力超過１０００的。
films_vehicles = []

for i in range(len(films_results)):
    for j in range(len(films_results[i]['vehicles'])):
        films_vehicles.append(films_results[i]['vehicles'][j])

films_vehicles_list = list(set(films_vehicles))

for i in range(len(films_vehicles_list)):
    vehicles = requests.get(films_vehicles_list[i]).json()
    if str.isdigit(vehicles['max_atmosphering_speed']):
        if int(vehicles['max_atmosphering_speed']) > 1000:
            print(f'{vehicles["name"]} (馬力為 {vehicles["max_atmosphering_speed"]})', end = '、')