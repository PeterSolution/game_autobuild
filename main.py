import threading
import time
import pyautogui
from  execute_focus import focus
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

defaultfocusstring=["rhineland.png","army_innovation1.png","four_year_plan.png","autarky.png","hermann_goring.png","kdf_wagen.png","extra_research_slot.png","reichsautobahn.png","anschluss.png"
                    ,"eastern_claims.png","ussr_treaty.png","army_innovation2.png","demand_sudetenland.png","fate_of_czechoslovakia.png","westwall.png",]
foc=focus()
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
                print("nie widac "+str(defaultfocusstring[0])+".png")
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
