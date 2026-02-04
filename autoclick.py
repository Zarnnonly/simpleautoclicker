import os
import pyautogui
import time
import random
from pynput import keyboard

print ("Tekan 'l' untuk menyimpan posisi mouse")
print ("Tekan 'm' untuk mengunci dan menjalankan autoclicker")
print ("Tekan 'p' untuk berhenti")
print ("Tekan 'c' untuk cancel")


cord = []

def saveCord(tombol):
   global cord
   try:  
         if tombol.char == 'l': #keybind set position
          tempCord = pyautogui.position()
          cord.append(tempCord)
          print(f"Locked and Loaded! Posisi Ke-{len(cord)} di {tempCord}")

         elif tombol.char == 'm': #keybind save position
            if len(cord) > 0:
               print(f"Posisi tersimpan! total ada {len(cord)} posisi!")
               return False
            else:
               print ("Mana posisinya woila?")
         
         elif tombol.char == 'c': #keybind cancel
            print(f"Oke, Cancel. See ya!")
            os._exit(0)
         else:
            print ("Lu pencet apaan?")
   except:
      pass

listen = keyboard.Listener(on_press=saveCord)
listen.start()
listen.join()

jalan = True

def dengerStop(tombolStop):
   global jalan
   try: 
    if tombolStop.char == 'p': #keybind stop
      jalan = False
      print ("See ya next time!")
      return False
   except:
      pass

listen = keyboard.Listener(on_press=dengerStop)
listen.start()

print("Gensh- i mean, Autoclicker diluncurkan! Klik P untuk stop\n")

while jalan:
   i = 1
   for tempCord in cord:
      print (f"Lagi mencet posisi {i}!: {tempCord}")
      i+=1

      if jalan == False:
         break

      try:
       speed = random.uniform(0.2, 0.5) #set kecepatan kursor disini
       pyautogui.moveTo(tempCord, duration=speed, tween=pyautogui.easeInOutQuad)
       pyautogui.click(tempCord)
       print ("Cord sudah diklik!")
       time.sleep(0.1) # delay per klik
      except:
       pass

