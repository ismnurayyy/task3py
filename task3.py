# Bir funksiyanız olacaq, funksiyada random kitabxanadan istifadə edərək20 nən 50 arası 5 rəqəm listə append edin. Həmən listdəki cüt  rəqəmləri math kitabxanası istifadə edərək kvadrata yüksəldin.

# try:
#     import random
#     import math
#     def reqemfunc():
#         reqemler = []
#         for  n in range(5):
#             n = random.randint(20,50)
#             reqemler.append(n)
#         print(reqemler )


#         for i in range(len(reqemler)):
#             if reqemler[i] % 2 == 0:
#                 reqemler[i]= math.pow(reqemler[i],2)
#                 # print(reqemler[i])
#         print(reqemler)
#     reqemfunc()
# except:
#     print("Xeta bas verdi")

# finally:
#     print("Emeliyyat ugurla basa catdi")
while True:
    try:
        number = int(input("Reqem daxil edin: "))
        print(number + 5)
        successfully = True

    except ValueError:
        print("Xais edirik reqem daxil edin !!!")
        successfully = False

    if successfully:
        print("Tebrikler...")
        break