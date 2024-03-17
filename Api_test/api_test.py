import requests


class ApiTest():
    def __init__(self):
        self.swapi = requests.get("https://swapi.dev/api/")
        self.swapi_data = self.swapi.json()
        self.all_films = requests.get(self.swapi_data["films"]).json()
        self.films_results = self.all_films["results"]

    def get_species_count_in_episode(self, episode_number):
        """
        取得指定集數電影中出現的不同種族數量
        
        Args:
            episode_number: 集數

        Returns:
            不同種族數量
        """

        episode_data = next(
            (film for film in self.films_results if film["episode_id"] == episode_number), None
        )
        if episode_data:
            species_urls = episode_data["species"]
            species_names = set(requests.get(url).json()["name"] for url in species_urls)
            return len(species_names)
        return 0



    def print_films_in_order(self):
        """
        依據電影集數去排序電影名字
        """

        films_list = {film["episode_id"]: film["title"] for film in self.films_results}
        films_sorted = ''
        for episode_number, title in sorted(films_list.items()):
            films_sorted += f"第 {episode_number} 集 : {title}\n"
        return films_sorted


    def find_powerful_vehicles(self):
        """
        找出電影裡所有的車輛，馬力超過1000的

        Args:
            films_results: 電影資料

        Returns:
            馬力超過1000的車輛
        """

        powerful_vehicles = set()
        vehicles_result = ''
        for film in self.films_results:
            for vehicle_url in film["vehicles"]:
                vehicle_data = requests.get(vehicle_url).json()
                max_speed = vehicle_data.get("max_atmosphering_speed", "")
                
                if max_speed.isdigit() and int(max_speed) > 1000:
                    powerful_vehicles.add(vehicle_data["name"])
        vehicles_result = "馬力超過1000的車輛： \n" + "、".join(powerful_vehicles)
        return vehicles_result