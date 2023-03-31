import sys
import os
import time

os.system("clear")
print("""\033[92;1m
▄▄▄▄▄ ▄ .▄▄▄▄ . ▐▄▄▄       ▄ .▄ ▐ ▄ 
•██  ██▪▐█▀▄.▀·  ·██▪     ██▪▐█•█▌▐█
 ▐█.▪██▀▐█▐▀▀▪▄▪▄ ██ ▄█▀▄ ██▀▐█▐█▐▐▌
 ▐█▌·██▌▐▀▐█▄▄▌▐▌▐█▌▐█▌.▐▌██▌▐▀██▐█▌
 ▀▀▀ ▀▀▀ · ▀▀▀  ▀▀▀• ▀█▄▀▪▀▀▀ ·▀▀ █▪
 Author : ./RedSec | Denis
 Team : Msec

 - TheJohn -
""")
pilihan = input("Masukan File Zip Kamu => ")
pilihan2 = input("Masukan Nama File Hash ( hash.txt ) => ")
os.system(f"zip2john {pilihan} > {pilihan2}")
print
print("Succses")
pilihan3 = input("Masukan File Hash Nya => ")
os.system(f"john {pilihan3}")