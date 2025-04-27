# Diketahui
P = 5_300_000  # Setoran per bulan (Rp)
r = 0.10       # Bunga per bulan (10%)
n = 5 * 12     # Total bulan (5 tahun)

# Menghitung Future Value (FV) dari annuitas
FV = P * ((1 + r) ** n - 1) / r * (1 + r)

print ("FV")
