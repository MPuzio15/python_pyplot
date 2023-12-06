# BMI = waga / wzrost w metrach do kwadratu


def check_bmi(h, w):

    height_m = float(h) / 100
    bmi = w // (height_m ** 2)
    print("Twoje BMI: ", bmi)
    if 18.5 <= bmi <= 24.99:
        return print("Waga prawidlowa")
    elif 25 <= bmi <= 29.9:
        return print("Nadwaga")
    elif 30 <= bmi <= 34.99:
        return print("Pierwszy stopien otylosci")
    elif 35 <= bmi <= 39.99:
        return print("Drugi stopien otylosci")
    else:
        return print("Poza skala")


def handle_bmi_check():
    while True:
        try:
            height_cm = float(input("Podaj wzrost w cm: "))
            weight_kg = float(input("Podaj wage w kg: "))
            check_bmi(height_cm, weight_kg)
            break
        except ValueError:
            print("Niepoprawna wartosc")


handle_bmi_check()







