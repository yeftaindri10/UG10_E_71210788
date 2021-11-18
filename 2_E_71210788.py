suhu = float (input("Masukkan suhu tubuh anda : "))
if suhu < 32:
    print("Anda kedinginan! Silahkan cari sesuatu yang hangat!")
elif (suhu == 32) or (suhu <= 37.5):
    print("Suhu anda normal!")
elif (suhu > 37.5) and (suhu <= 50):
    print("Anda demam! Jangan berpergian ke tempat umum!")
else:
    print("Anda bukan manusia :)")
