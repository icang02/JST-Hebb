import numpy as np
import os

os.system("cls")


# Fungsi aktivasi Hard Limit
def hard_limit(x):
    return 1 if x >= 0 else -1


# Menginisialisasi bobot awal
W_initial = np.zeros((3, 3), dtype=int)

# Set data training
data_training = [
    (np.array([[1, -1, 1], [-1, 1, -1], [1, -1, 1]]), 1, "X"),
    (np.array([[1, -1, -1], [1, -1, -1], [1, 1, 1]]), -1, "L"),
]

# Menghitung nilai bobot baru
W = np.copy(W_initial)
for x, t, label in data_training:
    W += x * t

# Memasukkan inputan baru
input_user = np.zeros((3, 3), dtype=int)
print("== Masukkan nilai == ")
for i in range(3):
    for j in range(3):
        input_user[i][j] = int(input(f"Baris {i + 1}, kolom {j + 1} = "))

# Perhitungan nilai aktivasi
aktivasi = 0
for i in range(3):
    for j in range(3):
        aktivasi += input_user[i][j] * W[i][j]

# Menentukan output menggunakan fungsi hard limit
output = hard_limit(aktivasi)

# Menentukan label
output_simbol = data_training[0][2] if output >= 0 else data_training[1][2]

# Menampilkan hasil
print("\nBobot awal : ")
print(W_initial)
print("\nBobot baru :")
print(W)

print("\nInput user :")
print(input_user)
print(f"\nPerhitungan bobot ke input = {aktivasi}, maka :")
print(f"y = {output}, dikenali sebagai {output_simbol}")
