import string

rupiah = str(input("Input your rupiah : "))

cleanned_rupiah = ''.join(char for char in rupiah if char not in string.punctuation)
cleanned_rupiah = ''.join(char for char in cleanned_rupiah if char not in string.ascii_letters)
cleanned_rupiah = int(cleanned_rupiah)

print("1. USD")
print("2. Yen")
pilihan = int(input("choice : "))
if pilihan == 1:
    rupiah_to_usd = cleanned_rupiah / 16789
    print(rupiah_to_usd, "USD")
elif pilihan == 2:
    rupiah_to_yen = cleanned_rupiah / 117
    print(rupiah_to_yen, "yen")
else :
    print("choice not valid, program exiting")



