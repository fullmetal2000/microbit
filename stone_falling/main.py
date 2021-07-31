from microbit import *
import utime
ship1 = Image("00000:"
             "00000:"
             "00000:"
             "90000:"
             "96000")
             
ship2 = Image("00000:"
             "00000:"
             "00000:"
             "09000:"
             "69600")  
             
ship3 = Image("00000:"
             "00000:"
             "00000:"
             "00900:"
             "06960")   
             
ship4 = Image("00000:"
             "00000:"
             "00000:"
             "00090:"
             "00696")   
             
ship5 = Image("00000:"
             "00000:"
             "00000:"
             "00009:"
             "00069")   
             
rock1 = Image("00900:"
              "00000:"
              "00000:"
              "00000:"
              "00000") 
              
rock2 = Image("00000:"
              "00900:"
              "00000:"
              "00000:"
              "00000") 
             
rock3 = Image("00000:"
              "00000:"
              "00900:"
              "00000:"
              "00000") 
              
rock4 = Image("00000:"
              "00000:"
              "00000:"
              "00900:"
              "00000") 
              
rock5 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00900")         
allships=[ship1,ship2,ship3,ship4,ship5]
allrocks=[rock1,rock2,rock3,rock4,rock5]

currentShip=2

display.show(allrocks,wait=True,loop=False, delay=100)

while True:
    if button_a.is_pressed():
        display.clear()

        if currentShip > 0:
            currentShip -= 1
            display.show(allships[currentShip])
            utime.sleep_ms(200)



    if button_b.is_pressed():
        if currentShip < 4:
            currentShip += 1
            display.show(allships[currentShip])
            utime.sleep_ms(200)


            

