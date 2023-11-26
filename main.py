import threading
import time
import pyautogui
from  execute_focus import focus
width=pyautogui.size().width
height=pyautogui.size().height
focusstring=["rhineland","four_year_plan"]
foc=focus()
for i in focusstring:
    foc.addfocus(i)
    #print(foc.returnfocus())
focuscount=0
researchcount1=0
researchcount2=0
researchcount3=0
researchcount4=0
researchcount5=0
table=foc.returnfocus()
print(table)
print(table[0])
# while True:
#     pyautogui.moveTo(45,30) # flag
#     time.sleep(1)
def focus():
    end=0
    focuscount=0


    while(True):
        if end==0:
            try:
                poz = pyautogui.locateCenterOnScreen(table[0]+".png")
                #pyautogui.moveTo(poz)
                print(poz)

                focuscount=focuscount+1

            except Exception as e:
                print("nie widac "+str(focusstring[0])+".png")
            time.sleep(1)
        #     try:
        #         # pyautogui.moveTo(midle)
        #         # pyautogui.click()
        #         # time.sleep(1)
        #         # pyautogui.press('enter')
        #         # focuscount=focuscount+1
        #         # time.sleep(1)
        #     finally:
        #         time.sleep(1)
        # else:
        #     time.sleep(1)
        #     print("a")



# def research():
#     while(True):
focus()

# t1=threading.Thread(target=focus)
# t1.start()

# t2=threading.Thread(target=research)
# t2.start()