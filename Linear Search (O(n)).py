data = [1, 3, 5, 7, 9, 11, 13]
target = int(input("Cari angka: "))
count = 0

for item in data:
    count += 1
    if item == target:
        break

print("Jumlah langkah:", count)