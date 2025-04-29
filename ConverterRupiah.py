import string

rupiah = str(input("Input your rupiah : "))

cleanned_rupiah = ''.join(char for char in rupiah if char not in string.punctuation)
cleanned_rupiah = ''.join(char for char in cleanned_rupiah if char not in string.ascii_letters)
cleanned_rupiah = int(cleanned_rupiah)

rupiah_to_usd = cleanned_rupiah / 16789

print(rupiah_to_usd, "USD")


