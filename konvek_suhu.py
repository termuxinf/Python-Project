#Membuat program konversi suhu

#Input
suhu = float(input())
asal = input()
tujuan = input()


# Proses
hasil=None

	# Konversi Celcius
if asal == "C" and tujuan == "F":
	hasil = suhu * 1.8 + 32
elif asal == "C" and tujuan == "K":
	hasil = suhu + 273.15
elif asal == "C" and tujuan == "Ra":
	hasil = suhu * 1.8 + 32 + 459,67
elif asal == "C" and tujuan =="R":
	hasil = suhu * 1.8 + 50
else:
	()

	# Konversi Kelvin
if asal == "K" and tujuan == "C":
	hasil = suhu - 273.15
elif asal == "K" and tujuan == "F":
	hasil = suhu * 1.8 - 459.67
elif asal == "K" and tujuan == "Ra":
	hasil = suhu * 1.8 
elif asal == "K" and tujuan =="R":
	hasil = (suhu -273.15) * 1.8
else:
	()

	# Konversi Fahrenheit
if asal == "F" and tujuan == "C":
	hasil = (suhu - 32) / 1.8
elif asal == "F" and tujuan == "K":
	hasil = (suhu + 459.670) / 1.8
elif asal == "F" and tujuan == "Ra":
	hasil = suhu + 459.67
elif asal == "F" and tujuan =="R":
	hasil = (suhu - 32) / 2.25
else:
	()

	# Konversi Rankine
if asal == "Ra" and tujuan == "C":
	hasil = (suhu - 32 - 459.67) / 1.8
elif asal == "Ra" and tujuan == "F":
	hasil = suhu * 1.8 + 32
elif asal == "Ra" and tujuan == "K":
	hasil = suhu / 1.8
elif asal == "Ra" and tujuan == "R":
	hasil = (suhu - 32 - 459.67) / 2.25

else:
	()

	# Konversi Reanmur
if asal == "R" and tujuan == "C":
	hasil = suhu * 1.25
elif asal == "R" and tujuan == "F":
	hasil = suhu * 2.25 + 32
elif asal == "R" and tujuan == "K":
	hasil = suhu * 1.25 + 273.15
elif asal == "R" and tujuan == "Ra":
	hasil = suhu * 2.25 + 32 + 459.67 
else:
	()

# Output
print(hasil)



