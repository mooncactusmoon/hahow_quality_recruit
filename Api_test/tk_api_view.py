import tkinter as tk
from api_test import ApiTest

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.test_api = ApiTest()
        self.title("徵才小專案 - API 篇")
        self.minsize(300, 300)
        self.maxsize(400, 400)

        self.initialize_ui()

    def initialize_ui(self):
        # 定義問題按钮
        btn1 = tk.Button(self, text="第 1 題 : 有多少不同種族的人出現在第六部", command=lambda: self.button_click(1))
        btn1.grid(row=0, column=0, sticky="we", padx=10)

        btn2 = tk.Button(self, text="第 2 題 : 依據電影集數去排序電影名字", command=lambda: self.button_click(2))
        btn2.grid(row=1, column=0, sticky="we", padx=10)

        btn3 = tk.Button(self, text="第 3 題 : 找出電影裡所有的車輛，馬力超過1000的", command=lambda: self.button_click(3))
        btn3.grid(row=2, column=0, sticky="we", padx=10)

        # 定義文字框
        self.text_box = tk.Text(self, height=10, width=30)
        self.text_box.tag_configure("color_red", foreground="red", justify="center")

        init_text = "!注意! \n 此專案的回答速度較慢 \n 請耐心等候 \n 謝謝 :>"
        self.text_box.insert(tk.END, init_text, "color_red")
        self.text_box.grid(row=3, sticky="we", padx=10, pady=10)

        # 退出按钮
        exitBtn = tk.Button(self, text="!!結束!!", command=self.destroy)
        exitBtn.grid(row=4, column=0, pady=10)

    def button_click(self, btn):
        self.text_box.delete("1.0", tk.END)
        if btn == 1:
            species_count = self.test_api.get_species_count_in_episode(6)
            self.text_box.insert(tk.END, f'總共有 "{species_count}" 種不同種族的人出現在第六部')
        elif btn == 2:
            films_order = self.test_api.print_films_in_order()
            self.text_box.insert(tk.END, films_order)
        elif btn == 3:
            powerful_vehicles = self.test_api.find_powerful_vehicles()
            self.text_box.insert(tk.END, powerful_vehicles)


if __name__ == "__main__":
    api_ui = Application()
    api_ui.mainloop()