import requests


def get_species_count_in_episode(episode_number):
    """
    取得指定集數電影中出現的不同種族數量
    
    Args:
        episode_number: 集數

    Returns:
        不同種族數量
    """

    episode_data = next(
        (film for film in films_results if film["episode_id"] == episode_number), None
    )
    if episode_data:
        species_urls = episode_data["species"]
        species_names = set(requests.get(url).json()["name"] for url in species_urls)
        return len(species_names)
    return 0


def print_films_in_order():
    """
    依據電影集數去排序電影名字
    """

    films_list = {film["episode_id"]: film["title"] for film in films_results}
    for episode_number, title in sorted(films_list.items()):
        print(f"第 {episode_number} 集電影名稱為 : {title}")


def find_powerful_vehicles(films_results):
    """
    找出電影裡所有的車輛，馬力超過1000的

    Args:
        films_results: 電影資料

    Returns:
        馬力超過1000的車輛
    """

    powerful_vehicles = set()
    for film in films_results:
        for vehicle_url in film["vehicles"]:
            vehicle_data = requests.get(vehicle_url).json()
            max_speed = vehicle_data.get("max_atmosphering_speed", "")
            
            if max_speed.isdigit() and int(max_speed) > 1000:
                powerful_vehicles.add(vehicle_data["name"])
    return powerful_vehicles


if __name__ == "__main__":
    """
    主程式
    """

    # 取得 Star Wars API 資料
    swapi = requests.get("https://swapi.dev/api/")
    swapi_data = swapi.json()
    all_films = requests.get(swapi_data["films"]).json()
    films_results = all_films["results"]

    # 有多少不同種族的人出現在第六部
    species_count = get_species_count_in_episode(6)
    print(f'總共有 "{species_count}" 種不同種族的人出現在第六部')

    # 依據電影集數去排序電影名字
    print_films_in_order()

    # 找出電影裡所有的車輛，馬力超過1000的
    powerful_vehicles = find_powerful_vehicles(films_results)
    print("馬力超過1000的車輛：", "、".join(powerful_vehicles))