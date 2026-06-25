print ("demarrage...")
import machine
from machine import Pin,time_pulse_us,freq
from time import sleep,sleep_us
#temoin de fonctionnement
tem=Pin(13,Pin.OUT)
tem.value(1)
#fonction de mesure de distance
def ultrason(trig,echo):
    trig.value(1)
    sleep_us(10)
    trig.value(0)
    duration=time_pulse_us(echo,1,30000)
    dist=(duration*0.0343)/2
    if dist > 0:
        return dist
    else :
        return "hors de la portee"
#verification de letatdu capteur pir
def pir(pinpir):
    if pinpir.value() == 1:
        return"il y a quelqu'un"
    elif pinpir.value() == 0:
        return"il n y a personne"
#systeme demarré
print("""
*********************************
          basic kernel
           build 1.00
*********************************""")
#les broches des composantes
trig=int(input("broche trig: "))
echo=int(input("broche echo: "))
pinpir=int(input("broche pir: "))
print("configuration des composants...")
#configuraton des capteurs
p=Pin(pinpir,Pin.IN)
t=Pin(trig,Pin.OUT)
e=Pin(echo,Pin.IN)
print ("elements detectes!")
#l'entree de la commande par l'utilisateur
while True:
    com=str(input(">_"))
    #les commandes
    if com == "help":
        print("""
----------------------------------------------------------------
                les commandes disponibles:
    dist-->afficher la distance mesuree par le capteur ultrason
    pirchck-->verifier l'état de capteur PIR
    help-->aide
    restart-->redemarrage du microcontrolleur
    shutdown-->arreter le microcontrolleur
    about-->informations sur le logiciel 
----------------------------------------------------------------
""")
    elif com == "dist":
        print(ultrason(t,e))
    elif com == "pirchck":
        print(pir(p))
    elif com == "restart":
        print("redemarrage du microcontrolleur")
        machine.reset()
    elif com == "shutdown":
        print("le microcontrolleur est eteint")
        machine.deepsleep()
    elif com == "about":
        print("""
---------------------------------
editeur: yahia
systeme: BasicKernel for esp32
version: 1 (build1.00)
---------------------------------
""")
    else:
        print(f"la commande {com} est inconnue")
    
    
