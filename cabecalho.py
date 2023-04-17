from tkinter import filedialog
import time
from pprint import pprint

arquivo = filedialog.askopenfilename()

with open(arquivo) as f:
    numero = input('Numero a ser procurado: ')
    audios = [i.split(";") for i in f if i.split(";")[4] == str(numero)]
    print('ok')
    pprint(audios)

time.sleep(100)
