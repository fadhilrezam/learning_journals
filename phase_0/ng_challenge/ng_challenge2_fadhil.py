# Buatlah sebuah function yang dapat mengkonversi suhu dari kelvin ke celcius, dan celcius ke kelvin.
# Buatlah sebuah function yang dapat mengkonversi suhu ke fahrenheit. 
# Tambahkan parameter untuk memastikan bahwa argumen yang dimasukan adalah celcius atau kelvin. 
# Panggil function yang pertama jika diperlukan.▪
# Buatlah sebuah function yang dapat mengkonversi suhu dari fahrenheit.
# Berikan argumen untuk memastikan bahwa outputnya dalah celcius atau kelvin.▪Berikan dokumentasi pada setiap baris kode yang kalian tulis.

def konversi_suhu (suhu):
    #rumus
    kelvin = suhu + 273 #output suhu dalam kelvin
    celcius = suhu - 273 #output suhu dalam celcius

    #cetak
    print(f"{suhu} derajat celcius : {kelvin} derajat kelvin")
    print(f"{suhu} derajat kelvin: {celcius} derajat celcius")
    return suhu
def konversi_ke_fahrenheit (suhu):
    #rumus
    fahrenheit = (9/5*suhu)+32

    #cetak
    print(f"{suhu} derajat celcius: {fahrenheit} derajat fahrenheit")
    return suhu

def konversi_dari_fahrenheit (suhu):
    #rumus
    kelvin = (suhu + 459.67)*5/9
    kelvin
    #cetak
    print(f"{suhu} derajat fahrenheit: {kelvin:.2f} derajat kelvin")
konversi_suhu(100)
konversi_ke_fahrenheit(150)
konversi_dari_fahrenheit(300)





    








