import tkinter as tk
from api_test import ApiTest

test_api = ApiTest()

window = tk.Tk()
window.title("徵才小專案 - API 篇")
window.minsize(300, 300)
window.maxsize(400, 400)

def button_click(btn):
    text_box.delete("1.0", tk.END)
    if btn==1:
        species_count = test_api.get_species_count_in_episode(6)
        text_box.insert(tk.END, f'總共有 "{species_count}" 種不同種族的人出現在第六部')
    elif btn==2:
        films_order = test_api.print_films_in_order()
        text_box.insert(tk.END, films_order)
    elif btn==3:
        powerful_vehicles = test_api.find_powerful_vehicles()
        text_box.insert(tk.END, powerful_vehicles)

btn1 = tk.Button(window, text="第 1 題 : 有多少不同種族的人出現在第六部", command= lambda: button_click(1))
btn1.grid(row=0, column=0, sticky="we", padx=10)

btn2 = tk.Button(window, text="第 2 題 : 依據電影集數去排序電影名字", command= lambda: button_click(2))
btn2.grid(row=1, column=0, sticky="we", padx=10)

btn3 = tk.Button(window, text="第 3 題 : 找出電影裡所有的車輛，馬力超過1000的", command= lambda: button_click(3))
btn3.grid(row=2, column=0, sticky="we", padx=10)

text_box = tk.Text(window, height=10, width=30)
text_box.tag_configure("color_red", foreground="red", justify="center")

init_text = "!注意! \n 此專案的回答速度較慢 \n 請耐心等候 \n 謝謝 :>"
text_box.insert(tk.END, init_text, "color_red")
text_box.grid(row=3, sticky="we", padx=10, pady=10)

exitBtn = tk.Button(window, text="!!結束!!", command=window.destroy)
exitBtn.grid(row=4, column=0, pady=10)

window.mainloop()