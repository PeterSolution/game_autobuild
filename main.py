import threading
import time
import pyautogui
import tkinter as tk
from  execute_focus import focus
from multiprocessing import Process,Lock

width=pyautogui.size().width
height=pyautogui.size().height

# Focuses Elwolf
# air_innov2.png air_innovations.png anschluss.png army_innovation1.png army_innovation2.png
# around_maginot.png autarky.png coal_liq.png danzig.png demand_sudetenland.png
# eastern_claims.png extra_research_slot.png fate_of_czechoslovakia.png
# form_reichskommissariats.png four_year_plan.png gerfoc1.png gerfoc2.png
# german_war_eco.png grosraumwirtschaft.png hermann_goring.png hungary.png
# integrate_war_eco.png kdf_wagen.png national_focus_completed.png
# reichsautobahn.png rhineland.png romania.png
# strat_air.png tactical_air.png synthetic_rubber.png
# ussr_treaty.png westwall.png


root = tk.Tk()
root.mainloop()
defaultfocusstring=["rhineland.png","army_innovation1.png","four_year_plan.png","autarky.png","hermann_goring.png","kdf_wagen.png","extra_research_slot.png","reichsautobahn.png","anschluss.png"
                    ,"eastern_claims.png","ussr_treaty.png","army_innovation2.png","demand_sudetenland.png","fate_of_czechoslovakia.png","westwall.png",]
foc=focus()
lock=Lock()
for i in defaultfocusstring:
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
# while (1==1):
#     print(pyautogui.position())
#     time.sleep(1)
#flag x=41, y=37
infocus=0

foccomp=0

def foccompletecheck():
    while(True):
        if(foccomp==1):
            try:
                pyautogui.locateCenterOnScreen("focus_completed.png")
            except:
                print("waiting for end of focus")
                time.sleep(0.5)

def opengov():
    pyautogui.moveTo(40,36)
    pyautogui.click()

def openfocus():
    try:
        poz = pyautogui.locateCenterOnScreen("select_a_national_focus.png")
        if poz is not None:
            1==1
        else:
            time.sleep(0.5)
        pyautogui.moveTo(poz)
        poz=None
        pyautogui.click()
    except:
        print("did not find open national focus button")
        opengov()
        try:
            poz = pyautogui.locateCenterOnScreen("select_a_national_focus.png")
            if poz is not None:
                1 == 1
            else:
                time.sleep(0.5)
            pyautogui.moveTo(poz)
            poz = None
            pyautogui.click()
        except:
            1==1

def selectfocus():


openfocus()



# def focus():
#     end=0
#     focuscount=0
#
#     help = 0
#     while(True):
#         if foccomp==0:
#             if end==0:
#
#                 #with lock:
#                 try:
#                     if(infocus==0):
#                         pyautogui.moveTo(40,36)
#                         pyautogui.click()
#                         poz=pyautogui.locateCenterOnScreen("select_a_national_focus.png")
#                         if poz is not None:
#                             1==1
#                         else:
#                             time.sleep(0.5)
#                         pyautogui.moveTo(poz)
#                         poz=None
#                         pyautogui.click()
#                         infocus=1
#                     try:
#                         poz = pyautogui.locateCenterOnScreen(table[focuscount])
#                         if poz is not None:
#                             1==1
#                         else:
#                             time.sleep(0.5)
#                         pyautogui.moveTo(poz)
#                         poz = None
#                         pyautogui.click()
#                         pyautogui.press('enter')
#                         help=0
#                         infocus=0
#                     except:
#                         if (help==0):
#                             pyautogui.moveTo(1879,144)
#                             pyautogui.mouseDown(button='left')
#                             pyautogui.moveTo(24,144)
#                             pyautogui.mouseUp(button='left')
#                             help=1
#                         else:
#                             if(help==1):
#                                 pyautogui.moveTo(1881, 1048)
#                                 pyautogui.mouseDown(button='left')
#                                 pyautogui.moveTo(1881, 144)
#                                 pyautogui.mouseUp(button='left')
#                                 help=2
#                             else:
#                                 if(help==2):
#                                     pyautogui.moveTo(24, 144)
#                                     pyautogui.mouseDown(button='left')
#                                     pyautogui.moveTo(1879, 144)
#                                     pyautogui.mouseUp(button='left')
#                                     help = 3
#                                 else:
#                                     if (help == 3):
#                                         pyautogui.moveTo(1881, 144)
#                                         pyautogui.mouseDown(button='left')
#                                         pyautogui.moveTo(1881, 1048)
#                                         pyautogui.mouseUp(button='left')
#                                         help = 0
#                                         #pyautogui.moveTo(poz)
#                     #print(poz)
#
#                     focuscrount=focuscount+1
#
#                 except Exception as e:
#                     print("nie widac "+str(defaultfocusstring[0]))
#                     time.sleep(1)
#             if defaultfocusstring[-1]==table[focuscount]:
#                 end=1
#             else:
#                 break
#         else:
#             time.sleep(1)

#focus()



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

# t1=threading.Thread(target=focus)
# t1.start()

# t2=threading.Thread(target=research)
# t2.start()
# t1.start()

# t2=threading.Thread(target=research)
# t2.start()
