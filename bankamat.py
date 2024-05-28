"""Islom taraqiyot banki mijozlar bilan foizsiz ishlaydigan yagona bank."""
# onlain dukon
from datetime import datetime
from secrets import compare_digest

person_infomation = {"Name": "Bahrom",
                     "SirtName": "Rashidov",
                     "Card": "8600041408080333",
                     "Money": 2000000,
                     "pincod": 9999,
                     "smsphone": 901830527}


# Bu pastdagi ruyhat pulni qanaqa turda olishga bogliq yani qiymati katta pul olasizmi yoki kichik hali tuliq tugamadi
# money = {"1000": 100, "2000": 100, "5000": 100, "10000": 50, "20000": 50}
# cash = {"50000": 50, "100000": 50, "200000": 50}


def main():
    lenguage = input("""
            Assalomu alaykum tilni tanalng :
            Здравствуйте, выберите язык :
            Hello, choose your language : 
                1.Uzbek 
                2.Russian 
                3.English
                    >>>>>>> """)
    if lenguage == "1":
        return uzbek()
    elif lenguage == "2":
        return russian()
    elif lenguage == "3":
        return english()
    else:
        print("Iltimos qaytadan kiriting siz kiritgan qiymat mavjud emas : ")
        return main()


def uzbek():
    print("""<<<<<<<<<<<<< Uzbek lenguage : >>>>>>>>>>>>>""")
    password = input("PIN kodni kiritng : ")
    if password.isdigit():
        password = int(password)
        s = 2
        while compare_digest(person_infomation["pincod"], password) and s != 0:
            print("ERROR")
            password = input("<<<<< PIN kodni kiritng.  >>>>>")
            s -= 1
        if compare_digest(person_infomation["pincod"], password):
            return uzbek_serves_bank()
        print("Ko'p o'rinishlar sababli kartangiz bloklandi ")
        return main()
    else:
        print("""Hurmatli mijoz siz kiritgan qiymat orasida raqamdan boshqa qiymatlar ham qatnashgan
                            Iltimos berilgan standard buyicha qiymatni raqamlar asosida kiriting """)
        return uzbek()



def uzbek_serves_bank():
    """"""
    print("""<<<<<<<<<< Uzbek Serves bankamat  >>>>>>>>>>""")
    xizmatlar = input("""
        Hurmatli mijoz xizmat turini tanlang 
            1.Balansi ko'rish
            2.Naqt pul yichish
            3.SMS xabarini o'rnatish
            4.Kartaga pul solish
            5.PIN kodini o'zgartirish
            6.Tilni Tanlash
            0.Hizmatni tugatish
            >>>>>>>>     """)
    if xizmatlar == "1":
        return uzbek_serves_balans()
    elif xizmatlar == "2":
        return uzbek_serves_pul()
    elif xizmatlar == "3":
        return uzbek_serves_sms()
    elif xizmatlar == "4":
        return uzbek_serves_cardmoney()
    elif xizmatlar == "5":
        return uzbek_serves_pincode()
    elif xizmatlar == "6":
        return main()
    elif xizmatlar == "0":
        print(""" 
            Hurmatli mijoz Islom taraqqiyotini bankidan foydalanganingiz uchun rahmat. 
                Kartangizni olishingiz mumkun!
            """)
        pass
    else:
        print("Siz kiritgan qiymat mavjud emas iltimos qaytadan kiriting !")
        return uzbek_serves_bank()


def uzbek_serves_balans():
    """pul ko'rish uchun """
    print("Balansni ko'rish ")
    balans = input("""
        1.Ekranga chiqarish
        2.Chekga chiqarish

        >>>>>   """)
    if balans == "1":
        return uzbek_balans_displayview()
    elif balans == "2":
        return uzbek_balans_chekview()
    else:
        print("""Hurmatli mijoz siz kiritgan qiymat mavjud emas iltimos qaytadan kiriting !""")
        return uzbek_serves_balans()


def uzbek_balans_displayview():
    """kartangizdagi pulni bankamat oynasida ko'rish """
    display = input(f"""
            Sizning kartangizdagi mablag' {person_infomation["Money"]} so'm    \n
            Hurmatli mijoz boshqa xizmatlarimizdan foydalanishni xohlaysizmi ? 
                1.Ha
                2.Yo'q >>>>>>> """)
    if display == "1":
        return uzbek_serves_bank()
    elif display == "2":
        print("""
        Bizdan foydalanganingiz uchun rahmat kartangizni olishingiz mumkun  :
            """)
    else:
        print("Hurmatli mijoz siz kiritgan qiymat mavjud emas iltimos qaytadan kiriting !")
        return uzbek_balans_displayview()


def uzbek_balans_chekview():
    """Kartangizdagi pulni checkga chiqarib ko'rish"""
    print("""Bizdan bankimiz Islom Taraqqiyot bankidan foydalanganingiz uchun rahmat hurmatli mijoz """)
    chec = input(f"""
                    CHECK
        Foydalanuvchi: {person_infomation["Name"]} {person_infomation["SirtName"]}
        Balans: {person_infomation["Money"]} so'm
        Card: {12 * "*" + person_infomation["Card"][-4::]}
        Time:{datetime.now()}
        Xizmat turi: AgroBank

                 Hurmatli mijoz biz bilan hamkorligingiz uchun rahmat

                Hurmatli mijoz boshqa xizmatlarimizdan foydalanishni xohlaysizmi ? 
                    1.Ha
                    2.Yo'q 
                    >>>>>>> """)
    print(chec)
    if chec == "1":
        return uzbek_serves_bank()
    elif chec == "2":
        print("""  Hurmatli mijoz hamkorlik uchun rahmat
                       kartangizni olishingiz mumkun 
                        """)
        pass
    else:
        print("""Hurmatli mijoz siz kiritgan qiymat mavjud emas iltimos shartli belgini qaytadan kiriting """)
        return check()


def check():
    chec = input("""
        Hurmatli mijoz boshqa xizmatlarimizdan foydalanishni xohlaysizmi ? 
                1.Ha
                2.Yo'q
                 >>>>>>>  """)
    print(chec)
    if chec == "1":
        return uzbek_serves_bank()
    elif chec == "2":
        print("""       Hurmatli mijoz hamkorlik uchun rahmat. Kartangizni olishingiz mumkun """)
        pass
    else:
        print("""Hurmatli mijoz siz kiritgan qiymat mavjud emas iltimos shartli belgini qaytadan kiriting """)
        return check()


def uzbek_serves_pul():
    """Bankamatdan suraladigan pulllar ruyhari"""
    pul = input(f"""
    Assalomu alaykum hurmatli mijoz kerakli mablag'ni tanlang
             1.50000                 5.300000
             2.100000                6.400000 
             3.150000                7.500000
             4.200000                8.Boshqa summa 
                                     9.Amalni bekor qilish 
                     >>>>>>> """)
    if pul == "1":
        return pul_1(50000)
    elif pul == "2":
        return pul_2(100000)
    elif pul == "3":
        return pul_3(150000)
    elif pul == "4":
        return pul_4(200000)
    elif pul == "5":
        return pul_5(300000)
    elif pul == "6":
        return pul_6(400000)
    elif pul == "7":
        return pul_7(500000)
    elif pul == "8":
        return pul_8()
    elif pul == "9":
        return uzbek_serves_bank()
    else:
        print("Hurmatli mijoz siz kiritgan qiymat qiymat mavjud emas iltimos qaytadan kiriting qiymatni")
        return uzbek_serves_pul()


def uzbek_serves_sms():
    mijoz_phone = input("""
            Assalomu alaykum hurmatli mijoz kartangizga o'langan telefon nomerni almashtirishni hohlaysizmi ?

                1.Ha
                2.Yo'q
                    >>>>>>>   """)
    if mijoz_phone == "1":
        return sms_phone()
    elif mijoz_phone == "2":
        return uzbek_serves_bank()
    else:
        print("Hurmatli mijoz siz kiritgan qiymat mavjud emas iltimos qaytadan kiritishingizni so'raymiz ")
        return uzbek_serves_pincode()


def sms_phone():
    """Kartangizga o'langan telefon raqamni sms xabarini o'chirib yoqish"""
    print(f"Kartangizning  o'langan telefon raqam: => +998 _", person_infomation["smsphone"])
    phone_sms = (input("Kartaga yangi telefon raqam kiriting : => +998 _ "))
    if phone_sms.isdigit():
        phone_sms = int(phone_sms)
        if len(str(phone_sms)) == 9:
            person_infomation["smsphone"] = phone_sms
            print("Kartangizning yangi telefon raqamga o'landi  : => +998 _", person_infomation["smsphone"])
            phone = input("""
                       Hurmatli mijoz kartangizga o'langan telefon raqam almashtirildi tabriklaymiz  \n
                           Hurmatli mijoz boshqa xizmatlardan foydalanasizmi ?
                               1.Ha
                               2.Yo'q    
                                  >>>>>>> """)
            if phone == "1":
                return uzbek_serves_bank()
            elif phone == "2":
                print("""Hurmatli mijoz biz bilan kamponiyadan foydalanganingiz uchun rahamt \n
                                 Kartangizni olishingiz mumkun.""")
            else:
                print("""Hurmatli mijoz kiritgan qiymatingiz mavjud emas iltimos qaytadan kiriting.""")
                return mestakphone()
        else:
            print("""Hurmatli mijoz siz kiritgan nomerda kamchilik bor iltimos nomerni qaytadan to'g'ri kiriting """)
            return sms_phone()

    else:
        print("Hurmatli mijoz siz kiritgan qiymat orasida integerdan boshqa qiymat ham mavjud iltimos qiymatni qaytadan kiriting\n")
        return sms_phone()

def mestakphone():
    phone = input("""
                       Hurmatli mijoz kartangizga o'langan telefon raqam almashtirildi tabriklaymiz  \n
                           Hurmatli mijoz boshqa xizmatlardan foydalanasizmi ?
                               1.Ha
                               2.Yo'q    
                                  >>>>>>> """)
    if phone == "1":
        return uzbek_serves_bank()
    elif phone == "2":
        print("""Hurmatli mijoz biz bilan kamponiyadan foydalanganingiz uchun rahamt \n
                                 Kartangizni olishingiz mumkun.""")
    else:
        print("""Hurmatli mijoz kiritgan qiymatingiz mavjud emas iltimos qaytadan kiriting.""")
        return mestakphone()

def uzbek_serves_cardmoney():
    money = input("""
            Hurmatli mijoz kartangizga pul qo'yishni hohlaysizmi ?
                     1.Ha
                     2.Yo'q 
                     >>>>>>>  """)
    if money == "1":
        return cardmoney()
    elif money == "2":
        return uzbek_serves_bank()
    else:
        print("Hurmatli mijoz siz kiritgan qiymatingiz xato iltimos qaytadan kiriting . ")
        return uzbek_serves_cardmoney()


def cardmoney():
    """Kartaga pul solish """
    print("Kartadagi pulingiz miqdori : ", person_infomation["Money"])
    money = int(input("Kartaga qancha pul solmoqchisiz : "))
    yigindi = (person_infomation["Money"] + (money - money * 0.001))
    person_infomation["Money"] = int(yigindi)

    pul = input(f"""

            Kartadagi pulingiz umumiy miqdari :{person_infomation["Money"]}  so'm  
            Data: {datetime.now()}


                Hurmatli mijoz kartangizga pul o'tgazildi Islom taraqqiyot banki mijozi bo'lganingizdan hursatmiz. \n
                Hurmatli mijoz boshqa xizmatlardan foydalanasizmi ?

                        1.Ha
                        2.Yo'q

                            >>>>> """)

    if pul == "1":
        return uzbek_serves_bank()
    elif pul == "2":
        return uzbek_serves_bank()
    else:
        print("Hurmatli mijoz siz kiritgan qiymatingiz xato iltimos qaytadan kiriting !")
        return mestak()


def mestak():
    """bu mestak kartaga pul solayotganda xatochilik chiqib qolsa qayta ulash uchun """
    mastac = input(f"""
        Hurmatli mijoz boshqa xizmatlardan foydalanasizmi ?

                        1.Ha
                        2.Yo'q

                        >>>>>>> """)

    if mastac == "1":
        return uzbek_serves_bank()
    elif mastac == "2":
        print(""" Marhamat kartangizni olishingiz mumkun .
         Islom taraqqiyot bankini tanlaganingizdan minaddormiz  
                     """)
    else:
        print("Hurmatli mijoz siz kiritgan qiymatingiz xato iltimos qaytadan kiriting !")
        return mestak()


def uzbek_serves_pincode():
    mijoz = input("""
        Assalomu alaykum hurmatli mijoz kartangizning kodni o'zgartirishni hohlaysizmi ?

            1.Ha
            2.Yo'q 
            >>>>>>>>>   """)
    if mijoz == "1":
        return pin()
    elif mijoz == "2":
        return uzbek_serves_bank()
    else:
        print("Hurmatli mijoz siz kiritgan qiymat mavjud emas iltimos qaytadan kiritishingizni so'raymiz ")
        return uzbek_serves_pincode()


# def check_file(pincode):
#     if os.path.isfile(pincode):
#         print("Fayl mavjud : ")
#         new_file = input("Fayl nomini kiritng : ")
#         os.rename(pincode, new_file)
#         print("Fayl nomi uzgartirildi : ")
#     else:
#         print("Bunday file mavjud emas : ")
# file_name = input("Fayl nomini kiriting : ")
# check_file(file_name)


def pincode_code():
    """Kartangizning pin codini almashtirish"""
    print(f"Kartangizning  kodi: => ", person_infomation["pincod"])
    pincode = input("Kartaga yangi kodini kiriting :")
    if pincode.isdigit():
        pincode = int(pincode)
        if len(str(pincode)) == 4:
            person_infomation["pincod"] = pincode
            print("Kartangizning yangi PIN kodi : => ", person_infomation["pincod"])
            coder = input("""
                    Hurmatli mijoz kartangizni kodi o'zgartirildi tabriklaymiz \n
                        Hurmatli mijoz boshqa xizmatlardan foydalanasizmi ?
                            1.Ha
                            2.Yo'q 
                            >>>>>>>> """)
            if coder == "1":
                return uzbek_serves_bank()
            elif coder == "2":
                print("Hurmatli mijoz jarayot tugatildi kartangizni olishingiz mumkun. ")
                pass

            else:
                print("""Hurmatli mijoz kiritgan qiymatingiz mavjud emas iltimos qaytadan kiriting.""")
                return pincode_code()
        else:
            print(""" Hurmarli mijoz siz keragidan ortiq qiymatdan foydalandingiz
                        Iltimos 4 xonali sondan oshmasin va kam bo'lmasin siz kiritgan qiymat """)
            return pincode_code()
    else:
        print("""Hurmatli mijoz siz kiritgan qiymat orasida raqamdan boshqa qiymatlar ham qatnashgan
                            Iltimos berilgan standard buyicha qiymatni raqamlar asosida kiriting """)
        return pincode_code()



def cash_check(money):
    """Bu yerda naqt pulni olishda chek suraydi """
    summa = input(f"""
            Hurmatli mijoz Islom Taraqqiyot banki mijozi bo'lganingizdan hursandmiz
                Amaiyotingiz muvafaqiyatli amalga oshirildi.

                Foydalanuvchi: {person_infomation["Name"]} {person_infomation["SirtName"]}
                Olingan pul miqdori: {money} so'm
                Data: {datetime.now()}
                Card: {12 * "*" + person_infomation["Card"][-4::]}
                Qolgan pul mablag'i: {person_infomation["Money"]}        



                        Hurmatli mijoz yana pul mablag'i yechasizmi 
                            1.Ha 
                            2.Yo'q 
                            >>>>>>> """)
    if summa == "1":
        return uzbek_serves_pul()
    elif summa == "2":
        return uzbek_serves_bank()
    else:
        print("Hurmarli mijoz siz kiritgan qiymat mavjud emas iltimos qaytadan kiritishingizni so'raymiz ")
        return pul_1_1()


def moneys(money):
    if money >= person_infomation["Money"]:
        print("Hurmatli mijoz sizning kartangizda yetarli mablag' mavjuz emas iltimos mablag'ni qaytadan kiriting ")
        return moneys(money)
    else:
        mablag = person_infomation["Money"] - (money + money * 0.001)
        person_infomation["Money"] = mablag
    # print(f"Hurmatli mijoz siz olgan pul mablag miqdori : {pul}")
    # print(person_infomation["Money"])
    cash_chakc = input("""
            Hurmatli mijoz olayotgan mablag'ingizni chekni olishni hohlaysizmi ?

                    1.Chek bilan
                    2.Cheksiz
                    >>>>>>>> """)
    if cash_chakc == "1":
        return cash_check(money)
    elif cash_chakc == "2":
        print(f""" Olingan pul miqdori : => {money} so'm """)
        return pul_1_1()
    else:
        print("Hurmatli mijoz siz ortiqcha belgilardan foydalandingiz iltimos belgini qaytadan kiriting")
        return moneys(money)


def pul_1(money):
    return moneys(money)

def pul_2(money):
    return moneys(money)

def pul_3(money):
    return moneys(money)

def pul_4(money):
    return moneys(money)

def pul_5(money):
    return moneys(money)

def pul_6(money):
    return moneys(money)

def pul_7(money):
    return moneys(money)

def pul_8():
    """Bu yerda ixtiyoriy pul suray uchun kod yozilgan """
    money = int(input("Hurmatli mijoz qancha mablag' olmoqchisiz : "))
    if money >= person_infomation["Money"]:
        print("Hurmatli mijoz sizning kartangizda yetarli mablag' mavjuz emas iltimos mablag'ni qaytadan kiriting ")
        return pul_8()
    else:
        mablag = person_infomation["Money"] - (money + money * 0.001)
        person_infomation["Money"] = int(mablag)
    # print(f"Hurmatli mijoz siz olgan pul mablag miqdori : {pul}")
    # print(person_infomation["Money"])
    cash_chakc = input("""
                Hurmatli mijoz olayotgan mablag'ingizni chekni olishni hohlaysizmi ?

                        1.Chek bilan
                        2.Cheksiz
                        >>>>>>>> """)
    if cash_chakc == "1":
        return cash_check(money)
    elif cash_chakc == "2":
        print(f""" Olingan pul miqdori : => {money} so'm """)
        return pul_1_1()
    else:
        print("Hurmatli mijoz siz ortiqcha belgilardan foydalandingiz iltimos belgini qaytadan kiriting")
        return moneys(money)

def pul_1_1():
    pul = input(f"""
            Hurmatli mijoz yana pul mablag'i yechasizmi 
                        1.Ha 
                        2.Yo'q >>>>>>> """)
    if pul == "1":
        return uzbek_serves_pul()
    elif pul == "2":
        return uzbek_serves_bank()
    else:
        print("Hurmarli mijoz siz kiritgan qiymat mavjud emas iltimos qaytadan kiritishingizni so'raymiz ")
        return pul_1_1()

def pin():
    print(""" \nHurmatli mijoz kartaga yangi PIN kod o'rnatmoqchi bo'lsangiz avval eski kodini kiriting """)
    password = input("Kartadagi eski PIN kodni kiritng : ")
    if password.isdigit():
        password = int(password)
        if len(str(password)) == 4:
            s = 2
            while compare_digest(person_infomation["pincod"], password) and s != 0:
                print(f"""Hurmatli mijoz karta kodingiz xato iltimos qaytadan kiriting  {s} marta o'rinish qoldi """)
                password = input("Kartadagi eski PIN kodni kiritng :  >>>>>")
                s -= 1
            if compare_digest(person_infomation["pincod"], password):
                return pincode_code()
            print("""\n Ko'p o'rinishlar sababli kartangizga yangi parol o'rnatolmaysiz\n
                            Hurmatli mijoz boshqa hizmatlardan foydalanishingiz mumkun.""")
            return uzbek_serves_bankpin()
        else:
            print(
                "Hurmatli mijoz siz kiritayotgan qiymay yetrli emas iltimos hurmatli mijoz standat buyicha 4 xonali qiymat kiriting")
            return pin()
    else:
        print("""Hurmatli mijoz siz kiritgan qiymat orasida raqamdan boshqa qiymatlar ham qatnashgan
                    Iltimos berilgan standard buyicha qiymatni raqamlar asosida kiriting """)
        return pin()


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< pin >>>>>>>>>>>>>>>>>>>>>>>

def uzbekpin():
    print("""<<<<<<<<<<<<< Uzbek lenguage : >>>>>>>>>>>>>""")
    password = input("PIN kodni kiritng : ")
    if password.isdigit():
        password = int(password)
        s = 2
        while person_infomation["pincod"] != password and s != 0:
            print("ERROR")
            password = input("<<<<< PIN kodni kiritng.  >>>>>")
            s -= 1
        if person_infomation["pincod"] == password:
            return uzbek_serves_bankpin()
        print("Ko'p o'rinishlar sababli kartangiz bloklandi ")
        return mainpin()
    else:
        print("""Hurmatli mijoz siz kiritgan qiymat orasida raqamdan boshqa qiymatlar ham qatnashgan
                            Iltimos berilgan standard buyicha qiymatni raqamlar asosida kiriting """)
        return uzbekpin()

def mainpin():
    lenguage = input("""
            Assalomu alaykum tilni tanalng :
            Здравствуйте, выберите язык :
            Hello, choose your language : 
                1.Uzbek 
                2.Russian 
                3.English
                    >>>>>>> """)
    if lenguage == "1":
        return uzbekpin()
    elif lenguage == "2":
        return russian()
    elif lenguage == "3":
        return english()
    else:
        print("Iltimos qaytadan kiriting siz kiritgan qiymat mavjud emas : ")
        return mainpin()


def uzbek_serves_bankpin():
    """"""
    print("""<<<<<<<<<< Uzbek Serves bankamat  >>>>>>>>>>""")
    xizmatlar = input("""
        Hurmatli mijoz xizmat turini tanlang 
            1.Balansi ko'rish
            2.Naqt pul yichish
            3.SMS xabarini o'rnatish
            4.Kartaga pul solish
            5.Tilni Tanlash
            0.Hizmatni tugatish
            >>>>>>>>     """)
    if xizmatlar == "1":
        return uzbek_serves_balanspin()
    elif xizmatlar == "2":
        return uzbek_serves_pulpin()
    elif xizmatlar == "3":
        return uzbek_serves_smspin()
    elif xizmatlar == "4":
        return uzbek_serves_cardmoneypin()
    elif xizmatlar == "5":
        return mainpin()
    elif xizmatlar == "0":
        print(""" 
            Hurmatli mijoz Islom taraqqiyotini bankidan foydalanganingiz uchun rahmat. 
                Kartangizni olishingiz mumkun!
            """)
        pass
    else:
        print("Siz kiritgan qiymat mavjud emas iltimos qaytadan kiriting !")
        return uzbek_serves_bankpin()


def uzbek_serves_balanspin():
    """pul ko'rish uchun """
    print("Balansni ko'rish ")
    balans = input("""
        1.Ekranga chiqarish
        2.Chekga chiqarish

        >>>>>   """)
    if balans == "1":
        return uzbek_balans_displayviewpin()
    elif balans == "2":
        return uzbek_balans_chekviewpin()
    else:
        print("""Hurmatli mijoz siz kiritgan qiymat mavjud emas iltimos qaytadan kiriting !""")
        return uzbek_serves_balanspin()


def uzbek_balans_displayviewpin():
    """kartangizdagi pulni bankamat oynasida ko'rish """
    display = input(f"""
            Sizning kartangizdagi mablag' {person_infomation["Money"]} so'm    \n
            Hurmatli mijoz boshqa xizmatlarimizdan foydalanishni xohlaysizmi ? 
                1.Ha
                2.Yo'q (Hizmatni to'gatish) 
                >>>>>>> """)
    if display == "1":
        return uzbek_serves_bankpin()
    elif display == "2":
        print("""
            Bizdan foydalanganingiz uchun rahmat kartangizni olishingiz mumkun  :
            """)
    else:
        print("Hurmatli mijoz siz kiritgan qiymat mavjud emas iltimos qaytadan kiriting !")
        return uzbek_balans_displayviewpin()


def uzbek_balans_chekviewpin():
    """Kartangizdagi pulni checkga chiqarib ko'rish"""
    print("""Bizdan bankimiz Islom Taraqqiyot bankidan foydalanganingiz uchun rahmat hurmatli mijoz """)
    chec = input(f"""
                    CHECK
        Foydalanuvchi: {person_infomation["Name"]} {person_infomation["SirtName"]}
        Balans: {person_infomation["Money"]} so'm
        Card: {12 * "*" + person_infomation["Card"][-4::]}
        Time:{datetime.now()}
        Xizmat turi: AgroBank

                 Hurmatli mijoz biz bilan hamkorligingiz uchun rahmat

                Hurmatli mijoz boshqa xizmatlarimizdan foydalanishni xohlaysizmi ? 
                    1.Ha
                    2.Yo'q (Hizmatni to'gatish) 
                    >>>>>>> """)
    print(chec)
    if chec == "1":
        return uzbek_serves_bankpin()
    elif chec == "2":
        print("""  Hurmatli mijoz hamkorlik uchun rahmat
                       kartangizni olishingiz mumkun 
                        """)
        pass
    else:
        print("""Hurmatli mijoz siz kiritgan qiymat mavjud emas iltimos shartli belgini qaytadan kiriting """)
        return checkpin()


def checkpin():
    chec = input("""
        Hurmatli mijoz boshqa xizmatlarimizdan foydalanishni xohlaysizmi ? 
                1.Ha
                2.Yo'q (Hizmatni to'gatish) 
                >>>>>>>  """)
    print(chec)
    if chec == "1":
        return uzbek_serves_bankpin()
    elif chec == "2":
        print("""       Hurmatli mijoz hamkorlik uchun rahmat. Kartangizni olishingiz mumkun """)
        pass
    else:
        print("""Hurmatli mijoz siz kiritgan qiymat mavjud emas iltimos shartli belgini qaytadan kiriting """)
        return checkpin()


def uzbek_serves_pulpin():
    """Bankamatdan suraladigan pulllar ruyhari"""
    pul = input(f"""
    Assalomu alaykum hurmatli mijoz kerakli mablag'ni tanlang
             1.50000                 5.300000
             2.100000                6.400000 
             3.150000                7.500000
             4.200000                8.Boshqa summa 
                                     9.Amalni bekor qilish 
                     >>>>>>> """)
    if pul == "1":
        return pul_1pin(50000)
    elif pul == "2":
        return pul_2pin(100000)
    elif pul == "3":
        return pul_3pin(150000)
    elif pul == "4":
        return pul_4pin(200000)
    elif pul == "5":
        return pul_5pin(300000)
    elif pul == "6":
        return pul_6pin(400000)
    elif pul == "7":
        return pul_7pin(500000)
    elif pul == "8":
        return pul_8pin()
    elif pul == "9":
        return uzbek_serves_bankpin()
    else:
        print("Hurmatli mijoz siz kiritgan qiymat qiymat mavjud emas iltimos qaytadan kiriting qiymatni")
        return uzbek_serves_pulpin()


def uzbek_serves_smspin():
    mijoz_phone = input("""
            Assalomu alaykum hurmatli mijoz kartangizga o'langan telefon nomerni almashtirishni hohlaysizmi ?

                1.Ha
                2.Yo'q
                    >>>>>>>   """)
    if mijoz_phone == "1":
        return sms_phonepin()
    elif mijoz_phone == "2":
        return uzbek_serves_bankpin()
    else:
        print("Hurmatli mijoz siz kiritgan qiymat mavjud emas iltimos qaytadan kiritishingizni so'raymiz ")
        return uzbek_serves_pincodepin()


def sms_phonepin():
    """Kartangizga o'langan telefon raqamni sms xabarini o'chirib yoqish"""
    print(f"Kartangizning  o'langan telefon raqam: => +998 _", person_infomation["smsphone"])
    phone_sms = (input("Kartaga yangi telefon raqam kiriting : => +998 _ "))
    if phone_sms.isdigit():
        phone_sms = int(phone_sms)
        if len(str(phone_sms)) == 9:
            person_infomation["smsphone"] = phone_sms
            print("Kartangizning yangi telefon raqamga o'landi  : => +998 _", person_infomation["smsphone"])
            phone = input("""
                       Hurmatli mijoz kartangizga o'langan telefon raqam almashtirildi tabriklaymiz  \n
                           Hurmatli mijoz boshqa xizmatlardan foydalanasizmi ?
                               1.Ha
                               2.Yo'q (Hizmatni tugatish)   
                                  >>>>>>> """)
            if phone == "1":
                return uzbek_serves_bankpin()
            elif phone == "2":
                print("""Hurmatli mijoz biz bilan kamponiyadan foydalanganingiz uchun rahamt \n
                             Kartangizni olishingiz mumkun.""")
            else:
                print("""Hurmatli mijoz kiritgan qiymatingiz mavjud emas iltimos qaytadan kiriting.""")
                return mestakphonepin()
        else:
            print("""Hurmatli mijoz siz kiritgan nomerda kamchilik bor iltimos nomerni qaytadan to'g'ri kiriting """)
            return sms_phonepin()
    else:
        print("""Hurmatli mijoz siz kiritgan qiymat orasida raqamdan boshqa qiymatlar ham qatnashgan
                            Iltimos berilgan standard buyicha qiymatni raqamlar asosida kiriting """)
        return sms_phonepin()


def mestakphonepin():
    phone = input("""
                       Hurmatli mijoz kartangizga o'langan telefon raqam almashtirildi tabriklaymiz  \n
                           Hurmatli mijoz boshqa xizmatlardan foydalanasizmi ?
                               1.Ha
                               2.Yo'q    
                                  >>>>>>> """)
    if phone == "1":
        return uzbek_serves_bankpin()
    elif phone == "2":
        print("""Hurmatli mijoz biz bilan kamponiyadan foydalanganingiz uchun rahamt \n
                                 Kartangizni olishingiz mumkun.""")
    else:
        print("""Hurmatli mijoz kiritgan qiymatingiz mavjud emas iltimos qaytadan kiriting.""")
        return mestakphonepin()

def uzbek_serves_cardmoneypin():
    money = input("""
            Hurmatli mijoz kartangizga pul qo'yishni hohlaysizmi ?
                     1.Ha
                     2.Yo'q 
                     >>>>>>>  """)
    if money == "1":
        return cardmoneypin()
    elif money == "2":
        return uzbek_serves_bankpin()
    else:
        print("Hurmatli mijoz siz kiritgan qiymatingiz xato iltimos qaytadan kiriting . ")
        return uzbek_serves_cardmoneypin()


def cardmoneypin():
    """Kartaga pul solish """
    print("Kartadagi pulingiz miqdori : ", person_infomation["Money"])
    money = int(input("Kartaga qancha pul solmoqchisiz : "))
    yigindi = (person_infomation["Money"] + (money - money * 0.001))
    person_infomation["Money"] = int(yigindi)

    pul = input(f"""

            Kartadagi pulingiz umumiy miqdari :{person_infomation["Money"]}  so'm  
            Data: {datetime.now()}


                Hurmatli mijoz kartangizga pul o'tgazildi Islom taraqqiyot banki mijozi bo'lganingizdan hursatmiz. \n
                Hurmatli mijoz boshqa xizmatlardan foydalanasizmi ?

                        1.Ha
                        2.Yo'q (Hizmatni to'gatish)

                            >>>>> """)

    if pul == "1":
        return uzbek_serves_bankpin()
    elif pul == "2":
        print("""Hurmatli mijoz biz bilan kamponiyadan foydalanganingiz uchun rahamt \n
                                 Kartangizni olishingiz mumkun.""")
    else:
        print("Hurmatli mijoz siz kiritgan qiymatingiz xato iltimos qaytadan kiriting !")
        return mestakpin()


def mestakpin():
    """bu mestak kartaga pul solayotganda xatochilik chiqib qolsa qayta ulash uchun """
    mastac = input(f"""
        Hurmatli mijoz boshqa xizmatlardan foydalanasizmi ?

                        1.Ha
                        2.Yo'q

                        >>>>>>> """)

    if mastac == "1":
        return uzbek_serves_bankpin()
    elif mastac == "2":
        print(""" Marhamat kartangizni olishingiz mumkun .
         Islom taraqqiyot bankini tanlaganingizdan minaddormiz  
                     """)
    else:
        print("Hurmatli mijoz siz kiritgan qiymatingiz xato iltimos qaytadan kiriting !")
        return mestakpin()


def uzbek_serves_pincodepin():
    mijoz = input("""
        Assalomu alaykum hurmatli mijoz kartangizning kodni o'zgartirishni hohlaysizmi ?

            1.Ha
            2.Yo'q 
            >>>>>>>>>   """)
    if mijoz == "1":
        return pin()
    elif mijoz == "2":
        return uzbek_serves_bankpin()
    else:
        print("Hurmatli mijoz siz kiritgan qiymat mavjud emas iltimos qaytadan kiritishingizni so'raymiz ")
        return uzbek_serves_pincodepin()


# def check_file(pincode):
#     if os.path.isfile(pincode):
#         print("Fayl mavjud : ")
#         new_file = input("Fayl nomini kiritng : ")
#         os.rename(pincode, new_file)
#         print("Fayl nomi uzgartirildi : ")
#     else:
#         print("Bunday file mavjud emas : ")
# file_name = input("Fayl nomini kiriting : ")
# check_file(file_name)


def pincode_codepin():
    """Kartangizning pin codini almashtirish"""
    print(f"Kartangizning  kodi: => ", person_infomation["pincod"])
    pincode = input("Kartaga yangi kodini kiriting :")
    if pincode.isdigit():
        pincode = int(pincode)
        if len(str(pincode)) == 4:
            person_infomation["pincod"] = pincode
            print("Kartangizning yangi PIN kodi : => ", person_infomation["pincod"])
            coder = input("""
                    Hurmatli mijoz kartangizni kodi o'zgartirildi tabriklaymiz \n
                        Hurmatli mijoz boshqa xizmatlardan foydalanasizmi ?
                            1.Ha
                            2.Yo'q (Hizmatni to'gatish)
                            >>>>>>>> """)
            if coder == "1":
                return uzbek_serves_bankpin()
            elif coder == "2":
                print("Hurmatli mijoz jarayot tugatildi kartangizni olishingiz mumkun. ")
                pass

            else:
                print("""Hurmatli mijoz kiritgan qiymatingiz mavjud emas iltimos qaytadan kiriting.""")
                return pincode_codepin()
        else:
            print(""" Hurmarli mijoz siz keragidan ortiq qiymatdan foydalandingiz
                        Iltimos 4 xonali sondan oshmasin va kam bo'lmasin siz kiritgan qiymat """)
            return pincode_codepin()
    else:
        print("""Hurmatli mijoz siz kiritgan qiymat orasida raqamdan boshqa qiymatlar ham qatnashgan
                            Iltimos berilgan standard buyicha qiymatni raqamlar asosida kiriting """)
        pincode_codepin()



def cash_checkpin(money):
    """Bu yerda naqt pulni olishda chek suraydi """
    summa = input(f"""
            Hurmatli mijoz Islom Taraqqiyot banki mijozi bo'lganingizdan hursandmiz
                Amaiyotingiz muvafaqiyatli amalga oshirildi.

                Foydalanuvchi: {person_infomation["Name"]} {person_infomation["SirtName"]}
                Olingan pul miqdori: {money} so'm
                Data: {datetime.now()}
                Card: {12 * "*" + person_infomation["Card"][-4::]}
                Qolgan pul mablag'i: {person_infomation["Money"]}        



                        Hurmatli mijoz yana pul mablag'i yechasizmi 
                            1.Ha 
                            2.Yo'q 
                            >>>>>>> """)
    if summa == "1":
        return uzbek_serves_pulpin()
    elif summa == "2":
        return uzbek_serves_bankpin()
    else:
        print("Hurmarli mijoz siz kiritgan qiymat mavjud emas iltimos qaytadan kiritishingizni so'raymiz ")
        return pul_1_1pin()


def moneyspin(money):
    if money >= person_infomation["Money"]:
        print("Hurmatli mijoz sizning kartangizda yetarli mablag' mavjuz emas iltimos mablag'ni qaytadan kiriting ")
        return moneyspin(money)
    else:
        mablag = person_infomation["Money"] - (money + money * 0.001)
        person_infomation["Money"] = mablag
    # print(f"Hurmatli mijoz siz olgan pul mablag miqdori : {pul}")
    # print(person_infomation["Money"])
    cash_chakc = input("""
            Hurmatli mijoz olayotgan mablag'ingizni chekni olishni hohlaysizmi ?

                    1.Chek bilan
                    2.Cheksiz
                    >>>>>>>> """)
    if cash_chakc == "1":
        return cash_checkpin(money)
    elif cash_chakc == "2":
        print(f""" Olingan pul miqdori : => {money} so'm """)
        return pul_1_1pin()
    else:
        print("Hurmatli mijoz siz ortiqcha belgilardan foydalandingiz iltimos belgini qaytadan kiriting")
        return moneyspin(money)


def pul_1pin(money):
    return moneyspin(money)

def pul_2pin(money):
    return moneyspin(money)

def pul_3pin(money):
    return moneyspin(money)

def pul_4pin(money):
    return moneyspin(money)

def pul_5pin(money):
    return moneyspin(money)

def pul_6pin(money):
    return moneyspin(money)

def pul_7pin(money):
    return moneyspin(money)

def pul_8pin():
    """Bu yerda ixtiyoriy pul suray uchun kod yozilgan """
    money = int(input("Hurmatli mijoz qancha mablag' olmoqchisiz : "))
    if money >= person_infomation["Money"]:
        print("Hurmatli mijoz sizning kartangizda yetarli mablag' mavjuz emas iltimos mablag'ni qaytadan kiriting ")
        return pul_8pin()
    else:
        mablag = person_infomation["Money"] - (money + money * 0.001)
        person_infomation["Money"] = int(mablag)
    # print(f"Hurmatli mijoz siz olgan pul mablag miqdori : {pul}")
    # print(person_infomation["Money"])
    cash_chakc = input("""
                Hurmatli mijoz olayotgan mablag'ingizni chekni olishni hohlaysizmi ?

                        1.Chek bilan
                        2.Cheksiz
                        >>>>>>>> """)
    if cash_chakc == "1":
        return cash_checkpin(money)
    elif cash_chakc == "2":
        print(f""" Olingan pul miqdori : => {money} so'm """)
        return pul_1_1pin()
    else:
        print("Hurmatli mijoz siz ortiqcha belgilardan foydalandingiz iltimos belgini qaytadan kiriting")
        return moneyspin(money)


def pul_1_1pin():
    pul = input(f"""
            Hurmatli mijoz yana pul mablag'i yechasizmi 
                        1.Ha 
                        2.Yo'q >>>>>>> """)
    if pul == "1":
        return uzbek_serves_pulpin()
    elif pul == "2":
        return uzbek_serves_bankpin()
    else:
        print("Hurmarli mijoz siz kiritgan qiymat mavjud emas iltimos qaytadan kiritishingizni so'raymiz ")
        return pul_1_1pin()

#<<<<<<<<<<<<<<<<<<<<<<<<<<<< english >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
def english():
    print("""<<<<<<<<<<<<< English lenguage : >>>>>>>>>>>>>""")
    password = int(input("Enter the PIN code : "))
    s = 2
    while person_infomation["pincod"] != password and s != 0:
        print("ERROR")
        password = int(input("<<<<< Enter the PIN code.  >>>>>"))
        s -= 1
    if person_infomation["pincod"] == password:
        return uzbek_serves_bank_1()
    print("Your card has been blocked due to too many views ")
    return main()

def uzbek_serves_bank_1():
    print("""<<<<<<<<<< English Serves bankamat  >>>>>>>>>>""")
    xizmatlar = input("""
        Dear customer, select a service type
             1. View the balance
             2. Cash withdrawal
             3. Set SMS message
             4. Payment to the card
             5. Change PIN code
             6.Lenguage selection
             0.Termination of service
            >>>>>>>>     """)
    if xizmatlar == "1":
        return uzbek_serves_balans_e()
    elif xizmatlar == "2":
        return uzbek_serves_pul_e()
    elif xizmatlar == "3":
        return uzbek_serves_sms_e()
    elif xizmatlar == "4":
        return uzbek_serves_cardmoney_e()
    elif xizmatlar == "5":
        return uzbek_serves_pincode_e()
    elif xizmatlar == "6":
        return main()
    elif xizmatlar == "0":
        print(""" 
            Dear customer, Thank you for working with us
                 You can get your card!
            """)
        pass

    else:
        print("The value you entered does not exist. Please re-enter !")
        return uzbek_serves_bank_1()

def uzbek_serves_balans_e():
    print("Balans view ")
    balans = input("""
         1. Display
         2. Check out

        >>>>>   """)
    if balans == "1":
        return uzbek_balans_displayview_e()
    elif balans == "2":
        return uzbek_balans_chekview_e()
    else:
        print("""Dear customer, the value you entered does not exist, please enter again !""")
        return uzbek_serves_balans_e()

def uzbek_balans_displayview_e():
    display = input(f"""
            Balance on your card {person_infomation["Money"]} found    \n
            Dear customer, do you want to use our other services?
                     1. Yes
                     2. No >>>>>> """)
    if display == "1":
        return uzbek_serves_bank_1()
    elif display == "2":
        print("""
        You can get your thank you card for using us:
            """)
        return uzbek_serves_bank_1()
    else:
        print("Dear customer, the value you entered does not exist, please enter again !")
        return uzbek_balans_displayview_e()

def uzbek_balans_chekview_e():
    print("""Thank you for using us, dear customer """)
    chec = input(f"""
                    CHECK
        User: {person_infomation["Name"]} {person_infomation["SirtName"]}
        Balans: {person_infomation["Money"]} so'm
        Card: {12 * "*" + person_infomation["Card"][-4::]}
        Time: {datetime.now()}
        Type of service: AgroBank
            """)
    print(chec)
    return main()

def uzbek_serves_pul_e():
    pul = input(f"""
    Hello, dear customer, select the required amount
             1.50000                 5.300000
             2.100000                6.400000 
             3.150000                7.500000
             4.200000                8.Another amount 
                                     9.Other services 
                                      >>>>>>>> """)
    if pul == "1":
        return pul_1_e(50000)
    elif pul == "2":
        return pul_2_e(100000)
    elif pul == "3":
        return pul_3_e(150000)
    elif pul == "4":
        return pul_4_e(200000)
    elif pul == "5":
        return pul_5_e(300000)
    elif pul == "6":
        return pul_6_e(400000)
    elif pul == "7":
        return pul_7_e(500000)
    elif pul == "8":
        return pul_8_e()
    elif pul == "9":
        return uzbek_serves_bank_1()
    else:
        print("Dear customer, the value you entered does not exist, please re-enter the value")
        return uzbek_serves_pul_e()

def uzbek_serves_sms_e():
    mijoz_phone = input("""
            Hello dear customer, would you like to change the phone number on your card?

                 1. Yes
                 2. No

                >>>>>>>   """)
    if mijoz_phone == "1":
        return sms_phone_e()
    elif mijoz_phone == "2":
        return uzbek_serves_bank_1()
    else:
        print("Dear customer, the value you entered does not exist, please enter it again ")
        return uzbek_serves_pincode_e()

def sms_phone_e():
    print(f"The phone number of your card: => ", person_infomation["smsphone"])
    pincode = int(input("Enter the new code on the card :"))
    person_infomation["smsphone"] = pincode
    print("Your card has been transferred to a new phone number  : => ", person_infomation["smsphone"])
    phone = input("""
           Dear customer, the phone number on your card has been replaced. Congratulations \n
                Dear customer, do you use other services?
                    1. Yes
                    2. No 
                    >>>>>>                                         
                   """)
    if phone == "1":
        return uzbek_serves_bank_1()
    elif phone == "2":
        return uzbek_serves_bank_1()

    else:
        print("""Dear customer, the value you entered does not exist, please enter it again.""")
        return sms_phone_e()

def uzbek_serves_pincode_e():
    mijoz = input("""
        Hello dear customer, do you want to change the code of your card?

             1. Yes
             2. No

            >>>>>>>   """)
    if mijoz == "1":
        return pincode_code_e()
    elif mijoz == "2":
        return uzbek_serves_bank_1()
    else:
        print("Dear customer, the value you entered does not exist, please enter it again ")
        return uzbek_serves_pincode_e()

def pincode_code_e():
    print(f"Your card code: => ", person_infomation["pincod"])
    pincode = int(input("Enter the new code on the card :"))
    person_infomation["pincod"] = pincode
    print("Your new card code : => ", person_infomation["pincod"])
    coder = input("""
        Dear Customer, Congratulations, your card code has been changed \n
             Dear customer, do you use other services?
                 1. Yes
                 2. No

                """)
    if coder == "1":
        return uzbek_serves_bank_1()
    elif coder == "2":
        print(""" Уважаемый клиент, Спасибо, что используете нас. .""")
        pass

    else:
        print("""Dear customer, the value you entered does not exist, please enter it again.""")
        return pincode_code_e()

def uzbek_serves_cardmoney_e():
    money = input("""
            Dear customer, would you like to add money to your card?
                      1. Yes
                      2. No

         >>>>>  """)
    if money == "1":
        return cardmoney_e()
    elif money == "2":
        return uzbek_serves_bank_1()
    else:
        print("Dear customer, the value you entered is incorrect, please re-enter . ")
        return uzbek_serves_cardmoney_e()

def cardmoney_e():
    print("The amount of money you have on the card : ", person_infomation["Money"])
    money = int(input("How much money do you want to put on the card? : "))
    yigindi = (person_infomation["Money"] + money)
    person_infomation["Money"] = yigindi

    pul = input(f"""

            The total amount of money you have on the card: {person_infomation["Money"]}  found 
            Data: {datetime.now()}


               Dear customer, the money has been transferred to your card. \n
             Dear customer, do you use other services?

                         1. Yes
                         2. No 
                         >>>>>>> """)

    if pul == "1":
        return uzbek_serves_bank_1()
    elif pul == "2":
        print(""" You can get your thank you card.
          Dear customer, thank you for using our campaign 
                     """)
    else:
        print("Dear customer, the value you entered is incorrect, please re-enter !")
        return mestak_e()

def mestak_e():
    mastac = input(f"""
        Dear customer, do you use other services?

                         1. Yes
                         2. No

                            >>>>> """)

    if mastac == "1":
        return uzbek_serves_bank_1()
    elif mastac == "2":
        print(""" You can get your thank you card.
          Dear customer, thank you for using our campaign
                     """)
    else:
        print("Dear customer, the value you entered is incorrect, please re-enter !")
        return mestak_e()

def money_e(money):
    if money >= person_infomation["Money"]:
        print("Dear customer, your card does not have enough funds, please re-enter funds")
        return money_e(money)
    else:
        mablag = person_infomation["Money"] - (money+money*0.001)
        person_infomation["Money"] = mablag
    # print(f"Hurmatli mijoz siz olgan pul mablag miqdori : {pul}")
    # print(person_infomation["Money"])
    cash_chakc = input("""
               Dear customer, would you like to receive a check?

                        1. By check
                        2. Unlimited
                       >>>>>>>> """)
    if cash_chakc == "1":
        return cash_check_e(money)
    elif cash_chakc == "2":
        print(f""" The amount of money received : => {money} so'm """)
        return pul_1_1_e()
    else:
        print("Dear customer, you have used too many characters, please re-enter the character")
        return money_e(money)

def cash_check_e(money):
    """Here, cash is a check for receiving money """
    summa = input(f"""
                Dear customer, Thank you for using us

                    User: {person_infomation["Name"]} {person_infomation["SirtName"]}
                    The amount of money received: {money} founds
                    Data: {datetime.now()}
                    Card: {12 * "*" + person_infomation["Card"][-4::]}
                    Remaining funds: {person_infomation["Money"]}        



                            Dear customer, would you like to withdraw money again?
                                 1. Yes
                                 2. No >>>>> """)
    if summa == "1":
        return uzbek_serves_pul_e()
    elif summa == "2":
        return uzbek_serves_bank_1()
    else:
        print("Dear customer, the value you entered does not exist, please enter it again ")
        return pul_1_1_e()
def pul_1_e(money):

    return money_e(money)
def pul_2_e(money):
    return money_e(money)

def pul_3_e(money):
    return money_e(money)

def pul_4_e(money):
    return money_e(money)

def pul_5_e(money):
    return money_e(money)

def pul_6_e(money):
    return money_e(money)

def pul_7_e(money):
    return money_e(money)

def pul_8_e():
    money = int(input("Dear customer, how much do you want? : "))
    if money >= person_infomation["Money"]:
        print("Dear customer, your card does not have enough funds, please re-enter funds")
        return pul_8_e()
    else:
        mablag = person_infomation["Money"] - (money+money*0.001)
        person_infomation["Money"] = int(mablag)
    # print(f"Hurmatli mijoz siz olgan pul mablag miqdori : {pul}")
    # print(person_infomation["Money"])
    summa = input(f"""
            Dear customer, Thank you for using us

                User: {person_infomation["Name"]} {person_infomation["SirtName"]}
                The amount of money received: {money} founds
                Data: {datetime.now()}
                Card: {12 * "*" + person_infomation["Card"][-4::]}
                Remaining funds: {person_infomation["Money"]}        



                        Dear customer, would you like to withdraw money again?
                             1. Yes
                             2. No >>>>> """)
    if summa == "1":
        return uzbek_serves_pul_e()
    elif summa == "2":
        return uzbek_serves_bank_1()
    else:
        print("Dear customer, the value you entered does not exist, please enter it again ")
        return pul_1_1_e()

def pul_1_1_e():
    pul = input(f"""
            Dear customer, would you like to withdraw money again?
                             1. Yes
                             2. No 
                             >>>>>>>>> """)
    if pul == "1":
        return uzbek_serves_pul_e()
    elif pul == "2":
        return uzbek_serves_pul_e()
    else:
        print("Dear customer, the value you entered does not exist, please enter it again ")
        return pul_1_1_e()

#<<<<<<<<<<<<<<<<<<<<<<<<<<russion>>>>>>>>>>>>>>>>>>>>>>>>>>>
def russian():
    print("""<<<<<<<<<<<<< Russion lenguage : >>>>>>>>>>>>>""")
    password = int(input("Введите PIN-код : "))
    s = 2
    while person_infomation["pincod"] != password and s != 0:
        print("ERROR")
        password = int(input("<<<<< Введите PIN-код.  >>>>>"))
        s -= 1
    if person_infomation["pincod"] == password:
        return uzbek_serves_bank_r()
    print("Ваша карта заблокирована из-за слишком большого количества просмотров ")
    return main()

def uzbek_serves_bank_r():
    print("""<<<<<<<<<< Uzbek Serves bankamat  >>>>>>>>>>""")
    xizmatlar = input("""
        Уважаемый клиент, выберите тип услуги
             1. Посмотреть баланс
             2. Выдача наличных
             3. Установить SMS-сообщение
             4. Оплата на карту
             5. Изменить PIN-код.
             6. Выберите язык
             0. Прекращение обслуживания
            >>>>>>>>     """)
    if xizmatlar == "1":
        return uzbek_serves_balans_r()
    elif xizmatlar == "2":
        return uzbek_serves_pul_r()
    elif xizmatlar == "3":
        return uzbek_serves_sms_r()
    elif xizmatlar == "4":
        return uzbek_serves_cardmoney_r()
    elif xizmatlar == "5":
        return uzbek_serves_pincode_r()
    elif xizmatlar == "6":
        return main()
    elif xizmatlar == "0":
        print(""" 
            Уважаемый клиент, Спасибо, что работаете с нами
                 Вы можете получить свою карту!
            """)
        pass

    else:
        print("Введенное вами значение не существует. Пожалуйста, введите еще раз.!")
        return uzbek_serves_bank_r()

def uzbek_serves_balans_r():
    print("Посмотреть баланс ")
    balans = input("""
         1. Дисплей
         2. Выезд

        >>>>>   """)
    if balans == "1":
        return uzbek_balans_displayview_r()
    elif balans == "2":
        return uzbek_balans_chekview_r()
    else:
        print("""Уважаемый клиент, введенное вами значение не существует, введите еще раз.!""")
        return uzbek_serves_balans_r()

def uzbek_balans_displayview_r():
    display = input(f"""
            Баланс на вашей карте {person_infomation["Money"]} сум \n
             Уважаемый клиент, хотели бы вы воспользоваться другими нашими услугами? ? 
             1. Да
             2. Нет 
             >>>>>>> """)
    if display == "1":
        return uzbek_serves_bank_r()
    elif display == "2":
        print("""
        Вы можете получить открытку с благодарностью за использование нас.  :
            """)
    else:
        print("Уважаемый клиент, введенное вами значение не существует, введите еще раз.!")
        return uzbek_balans_displayview_r()

def uzbek_balans_chekview_r():
    print("""Спасибо, что пользуетесь нами, дорогой клиент """)
    chec = input(f"""
                    CHECK
        Пользователь: {person_infomation["Name"]} {person_infomation["SirtName"]}
        Balans: {person_infomation["Money"]} so'm
        Card: {12 * "*" + person_infomation["Card"][-4::]}
        Time:{datetime.now()}
        Вид обслуживания: АгроБанк

                 Уважаемый клиент, Благодарим Вас за сотрудничество с нами

                 Уважаемый клиент, хотите ли вы воспользоваться другими нашими услугами?
                 1. Да
                 2. Нет 
                 >>>>>>> """)
    print(chec)
    if chec == "1":
        return uzbek_serves_bank_r()
    elif chec == "2":
        print("""  Уважаемый клиент, спасибо за сотрудничество
                        ты можешь получить свою карту 
                        """)
        pass
    else:
        print("""Уважаемый клиент, введенное вами значение не существует. Пожалуйста введите условный символ еще раз.""")
        return check_r()

def check_r():
    chec = input("""
        Уважаемый клиент, хотите ли вы воспользоваться другими нашими услугами?
                 1. Да
                 2. Нет
                 >>>>>>>  """)
    print(chec)
    if chec == "1":
        return uzbek_serves_bank_r()
    elif chec == "2":
        print("""       Уважаемый клиент, спасибо за сотрудничество. Вы можете получить свою карту """)
        pass
    else:
        print("""Уважаемый клиент введенное вами значение не существует Пожалуйста введите условный символ еще раз. """)
        return check_r()

def uzbek_serves_pul_r():
    pul = input(f"""
    Здравствуйте, уважаемый клиент, выберите необходимую сумму
              1.50000           5.300000
              2.100000          6.400000
              3.150000          7.500000
              4.200000          8.Другая сумма 
                                9.Другие услуги
              >>>>>>>> """)
    if pul == "1":
        return pul_1_r(50000)
    elif pul == "2":
        return pul_2_r(100000)
    elif pul == "3":
        return pul_3_r(150000)
    elif pul == "4":
        return pul_4_r(200000)
    elif pul == "5":
        return pul_5_r(300000)
    elif pul == "6":
        return pul_6_r(400000)
    elif pul == "7":
        return pul_7_r(500000)
    elif pul == "8":
        return pul_8_r()
    elif pul == "9":
        return uzbek_serves_bank_r()
    else:
        print("Уважаемый клиент, введенное вами значение не существует, пожалуйста, введите значение еще раз.")
        return uzbek_serves_pul_r()

def uzbek_serves_sms_r():
    mijoz_phone = input("""
            Здравствуйте, уважаемый клиент, хотите ли вы изменить номер телефона на вашей карте?

                 1. Да
                 2. Нет

                >>>>>>>   """)
    if mijoz_phone == "1":
        return sms_phone_r()
    elif mijoz_phone == "2":
        return uzbek_serves_bank_r()
    else:
        print("Уважаемый клиент, введенное вами значение не существует, введите его еще раз. ")
        return uzbek_serves_pincode_r()

def sms_phone_r():
    print(f"Номер телефона вашей карты: => ", person_infomation["smsphone"])
    pincode = int(input("Введите новый код на карте :"))
    person_infomation["smsphone"] = pincode
    print("Ваша карта перенесена на новый номер телефона  : => ", person_infomation["smsphone"])
    phone = input("""
           Уважаемый клиент, номер телефона на вашей карте заменен. Поздравляем \n
                Уважаемый клиент, пользуетесь ли вы другими услугами?
                    1. Да
                    2. Нет   
                      >>>>>>> """)
    if phone == "1":
        return uzbek_serves_bank_r()
    elif phone == "2":
        return uzbek_serves_bank_r()
    else:
        print("""Уважаемый клиент, введенное вами значение не существует, введите его еще раз..""")
        return sms_phone_r()

def uzbek_serves_pincode_r():
    mijoz = input("""
        Здравствуйте, уважаемый клиент, вы хотите изменить код вашей карты?

             1. Да
             2. Нет
            >>>>>>>   """)
    if mijoz == "1":
        return pincode_code_r()
    elif mijoz == "2":
        return uzbek_serves_bank_r()
    else:
        print("Уважаемый клиент, введенное вами значение не существует, введите его еще раз. ")
        return uzbek_serves_pincode_r()

def pincode_code_r():

    print(f"Код вашей карты: => ", person_infomation["pincod"])
    pincode = int(input("Введите новый код на карте:"))
    person_infomation["pincod"] = pincode
    print("Ваш новый код карты: => ", person_infomation["pincod"])
    coder = input("""
        Уважаемый клиент, Поздравляем, код вашей карты был изменен \n
             Уважаемый клиент, пользуетесь ли вы другими услугами?
                 1. Да
                 2. Нет 
                 >>>>>>>                  
                """)
    if coder == "1":
        return uzbek_serves_bank_r()
    elif coder == "2":
        print()

    else:
        print("""Уважаемый клиент введенное вами значение не существует введите его еще раз..""")
        return pincode_code_r()

def uzbek_serves_cardmoney_r():
    money = input("""
            Уважаемый клиент, хотите ли вы пополнить свою карту?
                      1. Да
                      2. Нет 
                      >>>>>>>>  """)
    if money == "1":
        return cardmoney_r()
    elif money == "2":
        return uzbek_serves_bank_r()
    else:
        print("Уважаемый клиент, введенное вами значение неверно, пожалуйста, введите еще раз. . ")
        return uzbek_serves_cardmoney_r()

def cardmoney_r():
    print("Сумма денег, которая у вас есть на карте : ", person_infomation["Money"])
    money = int(input("Сколько денег вы хотите положить на карту? : "))
    yigindi = (person_infomation["Money"] + money)
    person_infomation["Money"] = yigindi

    pul = input(f"""

            Общая сумма денег, которая у вас есть на карте: {person_infomation["Money"]}  сумма 
            Data: {datetime.now()}


                Уважаемый клиент, деньги переведены на вашу карту. \п
             Уважаемый клиент, пользуетесь ли вы другими услугами?

                         1. Да
                         2. Нет 
                         >>>>>>>> """)

    if pul == "1":
        return uzbek_serves_bank_r()
    elif pul == "2":
        return uzbek_serves_bank_r()
    else:
        print("Уважаемый клиент, введенное вами значение неверно, пожалуйста, введите еще раз. !")
        return mestak()

def mestak_r():
    mastac = input(f"""
        Уважаемый клиент, пользуетесь ли вы другими услугами?

                         1. Да
                         2. Нет 
                         >>>>>>>>> """)

    if mastac == "1":
        return uzbek_serves_bank_r()
    elif mastac == "2":
        print(""" Вы можете получить открытку с благодарностью.
          Уважаемый клиент, спасибо за использование нашей кампании 
                     """)
    else:
        print("Уважаемый клиент, введенное вами значение неверно, пожалуйста, введите еще раз. !")
        return mestak_r()

def cumma_r(cumma):
    if cumma >= person_infomation["Money"]:
        print("Уважаемый клиент, на вашей карте недостаточно средств, пожалуйста, введите средства повторно. ")
        return cumma_r(cumma)
    else:
        mablag = person_infomation["Money"] - (cumma+cumma*0.001)
        person_infomation["Money"] = mablag
    # print(f"Hurmatli mijoz siz olgan pul mablag miqdori : {pul}")
    # print(person_infomation["Money"])
    cash_chakc = input("""
             Уважаемый клиент, хотите ли вы получить чек?

                      1. Чеком
                      2. Безлимитный
                     >>>>>>>> """)
    if cash_chakc == "1":
        return check_cumma(cumma)
    elif cash_chakc == "2":
        print(f""" Сумма полученных денег : => {cumma} so'm """)
        return pul_1_1_r()
    else:
        print("Уважаемый клиент, вы использовали слишком много символов, пожалуйста, введите символ еще раз.")
        return moneys(cumma)

def check_cumma(cumma):
    summa = input(f"""
                Уважаемый клиент, Спасибо, что используете нас.

                     Пользователь: {person_infomation["Name"]} {person_infomation["SirtName"]}
                    Сумма полученных денег: {cumma} Сумма
                    Data: {datetime.now()}
                    Card: {12 * "*" + person_infomation["Card"][-4::]}
                    Оставшиеся средства: {person_infomation["Money"]}        



                            Уважаемый клиент, хотите ли вы снова вывести деньги?
                             1. Да
                             2. Нет 
                             >>>>>>>> """)
    if summa == "1":
        return uzbek_serves_pul_r()
    elif summa == "2":
        return uzbek_serves_bank_r()
    else:
        print("Уважаемый клиент, введенное вами значение не существует, введите его еще раз. ")
        return pul_1_1_r()
def pul_1_r(cumma):
    return cumma_r(cumma)

def pul_2_r(cumma):
    return cumma_r(cumma)

def pul_3_r(cumma):
    return cumma_r(cumma)

def pul_4_r(cumma):
    return cumma_r(cumma)

def pul_5_r(cumma):
    return cumma_r(cumma)

def pul_6_r(cumma):
    return cumma_r(cumma)

def pul_7_r(cumma):
    return cumma_r(cumma)

def pul_8_r():
    pul = int(input("Уважаемый клиент, сколько вы хотите получить? : "))
    if pul >= person_infomation["Money"]:
        print("Уважаемый клиент, на вашей карте недостаточно средств, пожалуйста, введите средства повторно. ")
        return pul_8_r()
    else:
        mablag = person_infomation["Money"] - (pul+(pul*0.001))
        person_infomation["Money"] = int(mablag)
    # print(f"Hurmatli mijoz siz olgan pul mablag miqdori : {pul}")
    # print(person_infomation["Money"])
    summa = input(f"""
            Уважаемый клиент, Спасибо, что используете нас.

                 Пользователь: {person_infomation["Name"]} {person_infomation["SirtName"]}
                Сумма полученных денег: {pul} Сумма
                Data: {datetime.now()}
                Card: {12 * "*" + person_infomation["Card"][-4::]}
                Оставшиеся средства: {person_infomation["Money"]}        



                        Уважаемый клиент, хотите ли вы снова вывести деньги?
                         1. Да
                         2. Нет 
                         >>>>> """)
    if summa == "1":
        return uzbek_serves_pul_r()
    elif summa == "2":
        return uzbek_serves_bank_r()
    else:
        print("Уважаемый клиент, введенное вами значение не существует, введите его еще раз. ")
        return pul_1_1_r()

def pul_1_1_r():
    pul = input(f"""
            Уважаемый клиент, хотите ли вы снова вывести деньги?
                         1. Да
                         2. Нет 
                         >>>>>>>>> """)
    if pul == "1":
        return uzbek_serves_pul_r()
    elif pul == "2":
        return uzbek_serves_pul_r()
    else:
        print("Уважаемый клиент, введенное вами значение не существует, введите его еще раз. ")
        return pul_1_1_r()
if __name__ == "__main__":
        main()