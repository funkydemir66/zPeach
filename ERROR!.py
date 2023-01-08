import sys
from random import choice

from g_python.gextension import Extension
from g_python.hmessage import Direction
import threading
from time import sleep


u1 = u2 = a1 = a2 = sa1 = sa2 = so1 = so2 = 999
v1 = False

v2 = False

user_id = 0

kod = 0

sec_kod = False

sc = True

fixs = True

spt = False

iv = False

oda = 0

chatc = ":c "

targett = ":t "

chatcc = ""

singles = ":ss "

mottomm = ":m "

targetr1 = ":tm1 "

targetr2 = ":tm2 "

fu = ":f "

fr = ":o "

out = ":"

tabl = ":tb "

hedef = ""

partymod = True

kodlang = ""

spamword = ":sw "

so = False

spamword2 = "yowyow"

tcho = False

yon = 1

s_idd = 999

npcs = 999

harekets = False

omotto = ""

table = ":table "

harekets2 = False

sahipsec = False

scho = False

ft = False

sp = False

t_idd = 0

pa = False

to = False

nmode = True

bg = False

tmode = False

sw = False

swo = False

sn = True

d1 = d2 = h1 = h2 = 1

canka = [1,-1]

spamkob = ('¬¬¬¬¬¬¬BULL¬¬¬¬¬¬¬¬¬SHİT¬¬¬÷÷¬¬¬¬¬¬¬¬¬¬¬¬¬3RR0R_ßL4ST3R_¬¬¬¬¬¬¬¬¬¬¬¬¬¬=)¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')

spamkod = str(spamkob)

renk = "i:3, i:2"

renk2 = choice(renk)

extension_info = {
    "title": "ERROR!",
    "description": "bots of g-earth",
    "version": "0.6",
    "author": "funkydemir66"
}

ext = Extension(extension_info, sys.argv, silent=True)
ext.start()

def chat(j):
    text = j.packet.read_string()
    global sec_kod, scho


    if text == ":b":
        j.is_blocked = True
        sec_kod = True

def start(s):
    (idd, command) = s.packet.read('is')
    global kod, user_id, so, yon, tcho, harekets, v1,harekets2, npcs, t_id, ft, d1 ,d2, scho, sahipnick, ss, v1 ,v2, u1, h1, dinle, dinle2, sp, to, harekets, tcho, iv, nmode, tmode, r_id1, r_id2, sw, spamword2, spamword, sn, partymod, spamkod,swo,hedef, spt, target, renk, renk2


    def main():
        while so:
            ext.send_to_server('{out:Whisper}{s:"Demiria exit"}{i:0}')

    def swoff():
        while swo:
            ext.send_to_server('{out:ChangePosture}{i:1}')
            sleep(0.5)

    def spam():
        while sp:
            if sc:
                ext.send_to_server('{out:Quit}')
                sleep(0.3)
                if tmode:
                    ext.send_to_server('{out:GetGuestRoom}{i:' + str(r_id1) + '' + str(r_id2) + '}{i:0}{i:1}')
                    sleep(0.5)
                if nmode:
                    ext.send_to_server('{out:FollowFriend}{i:' + str(kod) + '}')
                    sleep(0.5)
                if sw:
                    ext.send_to_server('{out:Shout}{s:"'+str(spamword2)+'"}{i:3}')
                    sleep(0.4)
                if sn:
                    ext.send_to_server('{out:Shout}{s:"'+str(spamkod)+'"}{i:3}')
                    sleep(0.4)

    def spt2():
        global target
        while spt:
            ext.send_to_server('{out:Quit}')
            sleep(0.3)
            ext.send_to_server('{out:FollowFriend}{i:' + str(kod) + '}')
            sleep(0.5)
            ext.send_to_server('{out:Whisper}{s:"'+str(target)+' '+str(spamkod)+'"}{i:0}"')
            sleep(0.2)

    def coin():
        global harekets, v1
        while to:
            harekets = True
            v1 = True
            ext.send_to_server('{out:LookTo}{i:'+str(h1)+'}{i:'+str(h2)+'}')
            sleep(1.0)
            ext.send_to_server('{out:Sign}{i:14}')
            sleep(1.0)

    def bigo():
        global harekets, v1
        while bg:
            ext.send_to_server('{out:GetExtendedProfile}{i:' + str(kod) + '}{b:true}')
            sleep(1.1)

    if command == ":v":
        ext.send_to_server('{out:FollowFriend}{i:'+str(kod)+'}')
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:'+str(kod)+'}{s:"I visit you"}')

    if command.startswith(chatc):
        s.is_blocked = True
        if sc:
            chatcc = str(command[(len(chatc)):])
            ext.send_to_server('{out:Chat}{s:"'+str(chatcc)+'"}{i:0}{i:0}')
            ext.send_to_server('{out:SendMsg}{i:'+str(kod)+'}{s:" I Write: '+str(chatcc)+'"}')

    if command.startswith(mottomm):
        s.is_blocked = True
        if sc:
            mottom = str(command[(len(mottomm)):])
            ext.send_to_server('{out:ChangeMotto}{s:"'+str(mottom)+'"}')
            ext.send_to_server('{out:SendMsg}{i:'+str(kod)+'}{s:" I Write Motto: "'+str(mottom)+'" "}')


    if command.startswith(fu):
        s.is_blocked = True
        if sc:
            isim = str(command[(len(fu)):])
            ext.send_to_server('{out:Chat}{s:"'+str(isim)+' SIXKTIRGXIXT ANNENI SXIXKXEYIM SENIN MAL DEFOL GIT"}{i:0}{i:6}')
            ext.send_to_server('{out:SendMsg}{i:'+str(kod)+'}{s:" I Fxucxk '+str(isim)+' =^) "}')


    if command.startswith(targetr1):
        s.is_blocked = True
        if sc:
            r_id1 = str(command[(len(targetr1)):])
            ext.send_to_server('{out:SendMsg}{i:'+str(kod)+'}{s:" I Target Room_Idd1 '+str(r_id1)+'"}')
            tmode = True
            nmode = False

    if command.startswith(targetr2):
        s.is_blocked = True
        if sc:
            r_id2 = str(command[(len(targetr2)):])
            ext.send_to_server('{out:SendMsg}{i:'+str(kod)+'}{s:" I Target Room_Idd2 '+str(r_id2)+'"}')
            tmode = True
            nmode = False


    if command.startswith(spamword):
        s.is_blocked = True
        if sc:
            spamword2 = str(command[(len(spamword)):])
            ext.send_to_server('{out:SendMsg}{i:'+str(kod)+'}{s:" I Choose Spam Word: '+str(spamword2)+'"}')
            sw = True
            sn = False

    if command == ":eb on":
        so = True
        thread = threading.Thread(target=main)
        thread.start()
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"I Start Exit Blocker"}')
        s.is_blocked = True


    if command == ":eb off":
        so = False
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"I Stop Exit Blocker"}')


    if command.startswith(targett):
        s.is_blocked = True
        if sc:
            target = str(command[(len(targett)):])
            ext.send_to_server('{out:Whisper}{s:"'+str(target)+' Enemy!"}{i:0}"')
            tcho = True

    if command == ":ft on":
        s.is_blocked = True
        harekets = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"I Follow The Target"}')
        v1 = True


    if command == ":ft off":
        s.is_blocked = True
        harekets = True
        v1 = False
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"I Dont Follow The Target"}')

    if command == ":trt on":
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"I Start Troll to Target"}')
        to = True
        thread = threading.Thread(target=coin)
        thread.start()

    if command == ":trt off":
        s.is_blocked = True
        to = False
        harekets = False
        v1 = False
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"I Stop Trolling"}')


    if command == ":sp on":
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"I Start Spam"}')
        sp = True
        thread = threading.Thread(target=spam)
        thread.start()

    if command == ":sp off":
        s.is_blocked = True
        sp = False
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"I Stop Spam"}')

    if command == "bobba":
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"What you typed reads as "bobba"."}')

    if command == "bobba bobba":
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"What you typed reads as "bobba"."}')

    if command == ":dance":
        s.is_blocked = True
        ext.send_to_server('{out:Dance}{i:1}')
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"I start Dance"}')

    if command == ":sdance":
        s.is_blocked = True
        ext.send_to_server('{out:Dance}{i:0}')
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"I stop Dance"}')

    if command == ":sword":
        s.is_blocked = True
        ext.send_to_server('{out:Chat}{s:":yyxxabxa"}{i:0}{i:-1}')
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"I have sword"}')

    if command == ":tmode off":
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"I back nmode"}')
        nmode = True
        tmode = False

    if command == ":help":
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"Visit = :v, Chat = :c, Target Player = :t (nick), Follow Target = :ft on/off, Trolling Target = :trt on/off,"}')
        sleep(1)
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"Spamming = :sp on/off, Exit Blocker = :eb on/off, Start Dance = :dance, Stop Dance = :sdance,"}')
        sleep(1)
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"Bobba Player = :f (nick), Spam Room Mode = :tm1(first four xxxx of room id)&:tm2  (second four xxxx of room id,)"}')
        sleep(1)
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"Spam Word = :sw (word)/:sw off"}')
        sleep(1)

    if command == ":sw off":
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"I Back Normale Spam"}')
        sw = False
        sn = True

    if command == ":pm on":
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"Party Mode On"}')
        partymod = True
        bg = True
        thread = threading.Thread(target=bigo)
        thread.start()

    if command == ":spt on":
        s.is_blocked = True
        spt = True
        sp = False
        thread = threading.Thread(target=spt2)
        thread.start()
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"Single Spam On"}')

    if command == ":spt off":
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"Single Spam Off"}')
        spt = False

    if command == ":pm off":
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"Party Mode Off"}')
        partymod = False
        bg = False

    if command == ":pm off":
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"Party Mode Off"}')
        partymod = False
        bg = False

    if command == ":sm1":
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"Spam Mode 1"}')
        spamkod = ('‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡')

    if command == ":sm2":
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"Spam Mode 2"}')
        spamkod = ('††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††††')

    if command == ":sm3":
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"Spam Mode 3"}')
        spamkod = ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')

    if command == ":sm4":
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"Spam Mode 4"}')
        spamkod = ('℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮℮')

    if command == ":sm5":
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"Spam Mode 4"}')
        spamkod = ('ĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦĦ')

    if command.startswith(table):
        s.is_blocked = True
        if sc:
            sayi = str(omotto[(len(table)):])
            ext.send_to_server('{out:Sign}{i:'+str(sayi)+'}')

    if command == ":siw on":
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"Sit Walk On"}')
        thread = threading.Thread(target=swoff)
        thread.start()
        swo = True

    if command == ":siw off":
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"Sit Walk On"}')
        swo = False

    if command == ":pu":
        s.is_blocked = True
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"I Going Puppet"}')
        ext.send_to_server('{out:UpdateFigureData}{s:"M"}{s:"lg-280-73.hr-125-40.ha-1022-73.sh-295-64.fa-3276-82.ch-875-73-82.he-3297-82.hd-190-30"}')



def yukle_kod(p):
    global kod, sec_kod, sahipsec

    if sec_kod:
        sec_kod = False
        user_id, _, _ = p.packet.read("iii")
        kod = str(user_id)
        sahipsec = True
        ext.send_to_server('{out:GetExtendedProfile}{i:' + str(kod) + '}{b:true}')

def tchos(k):
    global tcho, t_idd

    if tcho:
        _, _, _, _, _, _, _, t_idd = k.packet.read("iiiiiiii")
        tcho = False
        ext.send_to_server('{out:SendMsg}{i:' + str(kod) + '}{s:"Target PlayerIdd: ' + str(t_idd) + '"}')

def sahip(h):
    global harekets, d1, d2, npcs, h1, h2, t_idd, sahipsec, ss, scho

    if sahipsec:
        (_, sahipnick) = h.packet.read('is')
        ss = str(sahipnick)
        h.is_blocked = True
        ext.send_to_client('{in:Chat}{i:123456789}{s:"Player: Saved v/ '+str(sahipnick)+' "}{i:0}{i:30}{i:0}{i:0}')
        sahipsec = False
        ext.send_to_client('{out:RequestFriend}{s:"'+str(sahipnick)+'"}')




def hareket(j):
    global harekets, d1, d2, npcs, h1, h2, t_idd, s_idd

    if harekets:

        if v1:
            _, npcs, d1, d2 = j.packet.read("iiii")
            if npcs == t_idd:
                h1 = str(d1)
                h2 = str(d2)
                ext.send_to_server('{out:MoveAvatar}{i:' + str(h1) + '}{i:' + str(h2) + '}')

def partymode(o):
    global partymod, omotto, kod, kod, user_id, so, yon, tcho, harekets, v1,harekets2, npcs, t_id, ft, d1 ,d2, scho, sahipnick, ss, v1 ,v2, u1, h1, dinle, dinle2, sp, to, harekets, tcho, iv, nmode, tmode, r_id1, r_id2, sw, spamword2, spamword, sn, partymod, bg, kodlang, spamkod, sayi, swo


    def main():
        while so:
            ext.send_to_server('{out:Whisper}{s:"Demiria exit"}{i:0}')

    def swoff():
        while swo:
            ext.send_to_server('{out:ChangePosture}{i:1}')
            sleep(0.5)

    def spam():
        while sp:
            if sc:
                ext.send_to_server('{out:Quit}')
                sleep(0.5)
                if tmode:
                    ext.send_to_server('{out:GetGuestRoom}{i:' + str(r_id1) + '' + str(r_id2) + '}{i:0}{i:1}')
                    sleep(0.5)
                if nmode:
                    ext.send_to_server('{out:FollowFriend}{i:' + str(kod) + '}')
                    sleep(0.5)
                if sw:
                    ext.send_to_server('{out:Shout}{s:"'+str(spamword2)+'"}{i:0}')
                    sleep(0.4)
                if sn:
                    ext.send_to_server('{out:Shout}{s:"‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡"}{i:0}')
                    sleep(0.4)

    def coin():
        global harekets, v1
        while to:
            harekets = True
            v1 = True
            ext.send_to_server('{out:LookTo}{i:'+str(h1)+'}{i:'+str(h2)+'}')
            sleep(1.0)
            ext.send_to_server('{out:Sign}{i:14}')
            sleep(1.0)

    if partymod:
        (kodlang, _, _, omotto) = o.packet.read('isss')
        ext.send_to_server('{out:GetExtendedProfile}{i:'+str(kod)+'}{b:true}')

    if kodlang == 1:
        o.is_blocked = True


    if omotto.startswith(chatc):
        o.is_blocked = True
        if sc:
            chatcc = str(omotto[(len(chatc)):])
            ext.send_to_server('{out:Chat}{s:"'+str(chatcc)+'"}{i:0}{i:0}')

    if omotto.startswith(mottomm):
        o.is_blocked = True
        if sc:
            mottom = str(omotto[(len(mottomm)):])
            ext.send_to_server('{out:ChangeMotto}{s:"'+str(mottom)+'"}')


    if omotto.startswith(fu):
        o.is_blocked = True
        if sc:
            isim = str(omotto[(len(fu)):])
            ext.send_to_server('{out:Chat}{s:"'+str(isim)+' SIXKTIRGXIXT ANNENI SXIXKXEYIM SENIN MAL DEFOL GIT"}{i:0}{i:6}')

    if omotto.startswith(fr):
        o.is_blocked = True
        if sc:
            frn = str(omotto[(len(fr)):])
            ext.send_to_server('{out:RequestFriend}{s:"'+str(frn)+'"}')

    if omotto.startswith(out):
        o.is_blocked = True
        if sc:
            out2 = str(omotto[(len(out)):])
            ext.send_to_server(''+str(out2)+'')

    if omotto.startswith(tabl):
        o.is_blocked = True
        if sc:
            table2 = str(omotto[(len(tabl)):])
            ext.send_to_server('{out:Sign}{i:'+str(table2)+'}}')


    if omotto.startswith(targetr1):
        o.is_blocked = True
        if sc:
            r_id1 = str(omotto[(len(targetr1)):])
            tmode = True
            nmode = False

    if omotto.startswith(targetr2):
        o.is_blocked = True
        if sc:
            r_id2 = str(omotto[(len(targetr2)):])
            tmode = True
            nmode = False


    if omotto.startswith(spamword):
        o.is_blocked = True
        if sc:
            spamword2 = str(omotto[(len(spamword)):])
            sw = True
            sn = False

    if omotto == ":eb on":
        so = True
        thread = threading.Thread(target=main)
        thread.start()
        o.is_blocked = True


    if omotto == ":eb off":
        so = False
        o.is_blocked = True


    if omotto.startswith(targett):
        o.is_blocked = True
        if sc:
            target = str(omotto[(len(targett)):])
            ext.send_to_server('{out:Whisper}{s:"'+str(target)+' Enemy!"}{i:0}"')
            tcho = True

    if omotto == ":ft on":
        o.is_blocked = True
        harekets = True
        v1 = True


    if omotto == ":ft off":
        o.is_blocked = True
        harekets = True
        v1 = False


    if omotto == ":trt on":
        o.is_blocked = True
        thread = threading.Thread(target=coin)
        thread.start()
        to = True


    if omotto == ":trt off":
        o.is_blocked = True
        to = False
        harekets = False
        v1 = False


    if omotto == ":spam on":
        o.is_blocked = True
        thread = threading.Thread(target=spam)
        thread.start()
        sp = True


    if omotto == ":spam off":
        o.is_blocked = True
        sp = False

    if omotto == ":dance":
        o.is_blocked = True
        ext.send_to_server('{out:Dance}{i:1}')

    if omotto == ":sdance":
        o.is_blocked = True
        ext.send_to_server('{out:Dance}{i:0}')

    if omotto == ":v":
        ext.send_to_server('{out:FollowFriend}{i:'+str(kod)+'}')
        o.is_blocked = True

    if omotto.startswith(table):
        o.is_blocked = True
        if sc:
            sayi = str(omotto[(len(table)):])
            ext.send_to_server('{out:Sign}{i:'+str(sayi)+'}')

    if omotto == ":siw on":
        o.is_blocked = True
        thread = threading.Thread(target=swoff)
        thread.start()
        swo = True

    if omotto == ":siw off":
        o.is_blocked = True
        swo = False

def error(v):
    global yon

    if sp == True:
        v.is_blocked = True

def Items(f):

    if fixs:
        f.is_blocked = True

def Items2(f):

    if fixs:
        f.is_blocked = True

def Items3(f):

    if fixs:
        f.is_blocked = True

def Items4(f):

    if fixs:
        f.is_blocked = True

def Items5(f):

    if fixs:
        f.is_blocked = True

def Items6(f):

    if fixs:
        f.is_blocked = True

def Items7(f):

    if fixs:
        f.is_blocked = True

ext.intercept(Direction.TO_SERVER, chat, 'Chat')
ext.intercept(Direction.TO_CLIENT, start, 'NewConsole')
ext.intercept(Direction.TO_SERVER, yukle_kod, 'GetRelationshipStatusInfo')
ext.intercept(Direction.TO_CLIENT, tchos, 'Whisper')
ext.intercept(Direction.TO_CLIENT, hareket, 'UserUpdate')
ext.intercept(Direction.TO_CLIENT, sahip, 'ExtendedProfile')
ext.intercept(Direction.TO_CLIENT, partymode, 'ExtendedProfile')
ext.intercept(Direction.TO_CLIENT, error, 'FollowFriendFailed')
ext.intercept(Direction.TO_CLIENT, Items, 'Objects')
ext.intercept(Direction.TO_CLIENT, Items2, 'Items')
ext.intercept(Direction.TO_CLIENT, Items3, 'LatencyPingResponse')
ext.intercept(Direction.TO_CLIENT, Items4, 'Game2AccountGameStatus')
ext.intercept(Direction.TO_CLIENT, Items5, 'ScrSendUserInfo')
ext.intercept(Direction.TO_CLIENT, Items6, 'ObjectsDataUpdate')
ext.intercept(Direction.TO_CLIENT, Items7, 'AvatarEffect')







