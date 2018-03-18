import pyautogui
import csv
import time

pyautogui.FAILSAFE = False # disables the fail-safe

site = 1274
parent = 3630


with open('bdarl.csv', 'r') as f:
    print("Obtendo lista...")
    print(" ")
    reader = csv.reader(f)
    lista_hoteis = list(reader)
    for i in lista_hoteis:
        nome = i[0]
        ip = i[1]

        #site
        pyautogui.moveTo(253, 331)
        pyautogui.click(button='left')
        pyautogui.typewrite(str(site))

        #name
        pyautogui.moveTo(271, 399)
        pyautogui.click(button='left')
        pyautogui.typewrite(str(nome))

        #address
        pyautogui.moveTo(267, 602)
        pyautogui.click(button='left')
        pyautogui.typewrite(str(ip))

        #eqtype
        pyautogui.moveTo(263, 788)
        pyautogui.click(button='left')
        pyautogui.moveTo(292, 546)
        pyautogui.click(button='left')

        #parent check
        pyautogui.moveTo(56, 839)
        pyautogui.click(button='left')

        #parent equip
        pyautogui.moveTo(265, 904)
        pyautogui.click(button='left')
        pyautogui.typewrite(str(parent))


        #save
        pyautogui.moveTo(1498, 1009)
        pyautogui.click(button='left')
        time.sleep(5)

