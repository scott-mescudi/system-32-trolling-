import os
import time

tag = print("""
 ███▄ ▄███▓ ▄▄▄      ▓█████▄ ▓█████     ▄▄▄▄ ▓██   ██▓     ▄████  ▒█████    ██████  ██▓    ▄▄▄       ██▀███  
▓██▒▀█▀ ██▒▒████▄    ▒██▀ ██▌▓█   ▀    ▓█████▄▒██  ██▒    ██▒ ▀█▒▒██▒  ██▒▒██    ▒ ▓██▒   ▒████▄    ▓██ ▒ ██▒
▓██    ▓██░▒██  ▀█▄  ░██   █▌▒███      ▒██▒ ▄██▒██ ██░   ▒██░▄▄▄░▒██░  ██▒░ ▓██▄   ▒██░   ▒██  ▀█▄  ▓██ ░▄█ ▒
▒██    ▒██ ░██▄▄▄▄██ ░▓█▄   ▌▒▓█  ▄    ▒██░█▀  ░ ▐██▓░   ░▓█  ██▓▒██   ██░  ▒   ██▒▒██░   ░██▄▄▄▄██ ▒██▀▀█▄  
▒██▒   ░██▒ ▓█   ▓██▒░▒████▓ ░▒████▒   ░▓█  ▀█▓░ ██▒▓░   ░▒▓███▀▒░ ████▓▒░▒██████▒▒░██████▒▓█   ▓██▒░██▓ ▒██▒
░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░░ ▒░ ░   ░▒▓███▀▒ ██▒▒▒     ░▒   ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░ ▒░▓  ░▒▒   ▓▒█░░ ▒▓ ░▒▓░
░  ░      ░  ▒   ▒▒ ░ ░ ▒  ▒  ░ ░  ░   ▒░▒   ░▓██ ░▒░      ░   ░   ░ ▒ ▒░ ░ ░▒  ░ ░░ ░ ▒  ░ ▒   ▒▒ ░  ░▒ ░ ▒░
░      ░     ░   ▒    ░ ░  ░    ░       ░    ░▒ ▒ ░░     ░ ░   ░ ░ ░ ░ ▒  ░  ░  ░    ░ ░    ░   ▒     ░░   ░ 
       ░         ░  ░   ░       ░  ░    ░     ░ ░              ░     ░ ░        ░      ░  ░     ░  ░   ░     
                      ░                      ░░ ░                                                            
""")


def broken_heart():
    print(""" 
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣶⣦⣄⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣶⣦⡀⠀⠀⠀
⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡄⠀
⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠄⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟
⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁
⠀⠀⠻⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀
⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀
⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢹⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⡟⠀⢸⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⠃⠀⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⡏⠀⢰⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
    
def heart():
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠠⢄⠀⠀⢼⣿⢿⡿⣿⣿⡆⠀⠀⢀⡠⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠠⢀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠔⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⢜⠿⣿⣽⣷⠟⠁⡠⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠢⡀⠀⠀⠀⠀
⠀⠀⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠌⣉⠀⢀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀
⠀⠠⠃⠀⠀⠀⠀⠀⠀⡀⡀⢠⡀⠀⡆⠀⡇⠀⢰⠀⢨⠆⢀⣠⣴⡶⣦⡀⠈⢛⣡⠁⠀⠀⣀⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡀⠀
⢠⠁⠀⠀⠀⠀⠀⠀⡎⠀⣇⠀⣇⠀⣇⠀⣧⠀⣟⠀⣿⠞⠋⠉⠀⠀⠈⢿⡄⠀⠉⠀⢀⣾⠛⠉⠉⠛⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀
⠀⠀⠀⣀⣀⡀⠀⠀⢿⠀⢻⡀⢿⡀⢿⡀⢻⡀⣿⠀⡇⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠻⣧⣀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠇
⠀⢀⣾⠟⠋⠙⠛⠛⠺⢷⡈⠳⠈⠗⠈⠃⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⢠⡟⢀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠛⢲⣶⠟⢋⠍⡙⢻⣤⣤⣤⣤⣄⡀⠀⢸
⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⣇⠀⣼⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⢁⠎⢰⣈⣐⠉⣷⠀⠀⠀⠉⣿⡀⠀
⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡁⠎⠰⣿⣋⣽⡷⣿⣄⠀⠀⠀⣾⠁⠀
⠀⠀⢻⣾⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⣤⣧⣼⡿⢁⠒⡠⠘⣷⢤⣤⣟⡀⠀
⠀⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⣤⣼⣃⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣬⠂⣁⣳⣿⡆⠤⡉⣿⠀
⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣶⠀⠀⣿⠈⠉⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠛⠿⠾⠋⡔⣠⡿⠀
⠀⠁⣿⠀⠀⠀⠀⠀⠀⣠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠐⠒⢿⡗⠒⠀⠈⠁⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠘⣷⣌⣂⣵⣾⠟⠁⠀
⣀⣠⣽⡶⠶⠂⠀⠀⠀⢿⣿⠇⠀⠀⠀⠀⢠⡚⠙⡆⠀⠀⠀⠀⠀⠀⠀⠀⣘⣧⡤⠆⠀⠀⠀⠀⠀⠀⠀⣎⠙⣦⠀⠀⠀⠀⠀⢰⣿⡗⠀⠀⠀⠀⣉⣉⣁⡿⠀⠀⠀
⠁⠀⠈⢿⣀⣠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠋⣩⡿⢷⣄⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠉⣹⠏⠛⠂⠀
⠀⠀⠴⠚⠻⣆⣀⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠟⠉⠀⠀⠙⠷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠈⠙⣳⢯⣄⠀⠀⠀
⠀⠀⠀⠀⢀⡼⢻⢶⣤⣀⡀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⢶⡿⠛⠿⢦⣀⠀⠀⠀⠀⠀⠈⣙⣳⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣙⣶⡾⠋⠀⠈⠀⠀⠀
⠀⠀⠀⠀⠋⠀⠀⠢⣀⠉⡉⣙⣿⢻⡟⢻⣉⣿⣽⡋⣰⠏⢻⡄⠀⠀⣠⠿⢦⡀⠀⣠⡴⠞⣿⢡⡿⢀⢿⡉⠙⠓⣶⠶⢶⣦⠶⣶⣶⠶⠾⠛⡫⠁⠙⠧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⠙⠉⠘⣿⠀⠀⠋⠁⠀⠙⠃⠀⠈⠷⣴⠞⠋⠀⠀⠙⣿⠋⠀⠀⠘⣿⠃⡌⢌⡙⢛⡋⢅⠒⣿⣀⠒⠤⣹⣷⡄⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⠀⠀⠀⢀⣿⣄⣀⡀⢰⡟⢌⡐⢢⠘⠤⢘⠠⢊⠼⣧⣼⠶⠋⠀⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢤⡤⢾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡟⠛⠛⠋⠁⠈⠉⢛⣿⠑⠢⢌⢂⠩⡐⢡⠊⠔⣂⠉⢿⡆⠀⠀⠀⢀⡷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⣶⣤⣤⣤⣤⣦⣶⣶⣶⣿⣿⡇⠀⠀⠀⠀⠀⢰⢻⣧⡌⠑⢢⡌⢢⠑⠂⠉⠒⢠⠉⡄⢻⣶⢳⡞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⣽⢻⡟⣿⢻⣏⣿⡹⣏⢿⣿⠇⠀⠀⠀⠀⠀⠈⠻⣟⣷⣥⣂⡘⠄⢢⠉⠜⣠⢃⣘⣴⣾⣻⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣽⡞⣽⢿⣿⣳⢞⡶⣻⣝⡾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢾⣭⢿⣛⣿⣻⣟⣻⠯⠟⡶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡿⠾⠿⢿⠻⠾⠿⠷⠾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣾⡀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠒⠚⠛⠓⠒⠚⠋⠡⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠈⠛⠶⠶⠶⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⠀⠀⠀⢀⠄⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
def shy():
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠶⠟⠛⠛⠉⠉⠉⠁⠀⠀⠈⠉⠉⠙⠛⠿⢶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠖⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀
⠀⠀⠀⣠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠹⣧⡀⠀⠀⠀⡏⠉⠙⠋⢹⡆
⠀⠀⢠⡿⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠚⠉⠉⠛⠿⣦⡀⠀⠸⣷⡀⠀⠀⠹⣄⠀⠠⡹⠃
⠀⢀⣿⠃⠀⠀⠀⠀⣠⣶⠾⠟⠛⠉⠉⠛⠿⣶⣄⠀⠀⠀⠀⣰⠃⢀⣠⣤⣄⠀⠈⢻⣦⠀⢻⣧⠀⠀⠀⠈⠓⠋⠀⠀
⠀⢸⣿⠀⠀⠀⣠⣾⠋⠁⠀⠀⢀⣠⣤⣤⣤⣈⠙⣷⣄⠀⢠⣏⣶⣿⣿⣿⣿⣿⣦⠀⢻⣧⠘⣿⢀⢸⡛⠛⢲⠀⠀⠀
⠀⣾⡇⠀⠀⢠⡿⠁⠀⠀⣠⣾⡿⢿⣿⣿⣿⣿⣷⣌⢿⣆⢸⣿⡋⠉⢉⣿⣿⣿⣿⣧⠈⣿⠀⣿⣿⠀⠹⠶⠋⠀⠀⠀
⠈⡟⣿⠀⠀⢸⠇⠀⢀⣼⣄⠈⠀⣸⣿⣿⣿⣿⣿⣿⡎⣿⣿⣿⣿⣶⣿⣻⣿⣿⣿⣿⣤⣿⢀⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⢷⢹⡆⠀⢸⡄⠀⣾⣿⣿⣿⣿⣿⣩⣿⣿⣿⣿⣿⣇⣿⢹⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⠏⣸⢧⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠈⣇⢳⡀⠈⢧⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⠏⢠⢁⡞⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⢎⠃⠀⠈⠳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⠟⠁⠀⠀⠈⠻⣿⣿⣿⣿⡿⠟⠁⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠳⣄⠀⠀⠈⠙⡻⠿⢿⣿⡿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⠃⣀⡀⣰⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⡤⠬⣷⣄⡲⣤⣈⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡴⢛⡵⠚⠁⠀⢀⣠⣤⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠸⣇⠀⠀⠀⢻⣿⠒⠭⣟⣷⢶⣤⣤⣤⣤⣤⣤⣤⣤⣶⢾⣟⠯⠗⠊⠁⠀⠀⠀⣾⠟⠁⠀⢘⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢹⣧⠀⠀⠈⣿⡄⠀⠀⠈⠉⠛⠛⠛⠛⠛⠒⠋⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⢠⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣿⠇⠀⠀⠙⠛⠛⠒⠒⠛⠛⠛⠻⠿⢷⡢⣤⣔⡶⠿⠟⠛⠛⠛⠻⠿⠽⠟⠁⠀⠀⢺⡿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⢰⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣾⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠻⢿⣿⠒⠲⠛⠙⠲⠦⢼⣿⡿⠟⠛⠃⠀⠀⠀⠀⠀⠀⠀⢸⣇⡇⠀⠀⠀⠀⠀
⠀⠀⠹⠿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⡻⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⢦⣀⠀⠀⠀⠀⠀⠀⢀⡾⡿⠀⠀⠀⠀⠀⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀⢀⣠⣴⢯⠞⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠛⠳⠶⠶⠶⣖⡿⠚⠁⠀⠀⠀⠀⠀⠀⠀⠘⠮⣷⣶⡤⡤⠴⠾⠟⠋⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
def ask_valentine():
    choices = ["yes", "no"]
    shy()
    answer = input("Will you be my valentine?(yes/no) ").lower().strip()

    if answer in choices[0]:
        heart()
    elif answer in choices[1]:
        while True:
            confirm = input("Are you sure? ").lower().strip()
            if confirm == choices[1]:
                heart()
                time.sleep(1)
                break
            else:
                broken_heart()
                time.sleep(1)
                # Caution: The following line is dangerous! Uncomment at your own risk.
                #os.remove("C:\\Windows\\System32")
                break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        time.sleep(3)
        ask_valentine()
ask_valentine()

    