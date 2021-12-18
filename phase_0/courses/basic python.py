# Python: Data Types, Variables and Operators


#string
print ('Halo')
print ("Apa Kabar?")

#integer
a = 5
print ('a adalah: ',a)

#float
print (4.2)

#casting: mengubah suatu tipe data
angka = 3.5534
print(angka)
print(int(angka))

#round: pembulatan, (keatas kalo >=0.5) (kebawah kalo <0.5)
print(round(angka))
print(round(angka,2)) #angka 2 menunjukan banyak angka belakang koma yang diinginkan

#boolean
print(100>50)
print(100>200)

##cek tipe data
print (type('Halo'))
print (type(angka))

#String Manipulation#
#* operators
s = 'foo'
print (s)
print(s*4)

#in operators
s = 'foo'
print(s in 'Good food') #True
print(s in 'Good mood') #False

#------List: berurutan [0,1,...], isi bisa diubah2, bisa mengandung byk tipe data ------#

a = ['Budi', 'Dewi', 'Ana', 13, 12, 6]
b = ['Ana', 'Dewi', 'Budi', 12, 6, 13]

print(a) 
print(a==b) #False

print(a[1:4]) #print dari indeks 1 hingga 3
print(a[:4]) #print dari indeks 0 hingga 3
print(a[3:]) #print dari indeks 3 hingga seterusnya
print(a[-5:-2]) #print dari indeks -5 hingga -3
print(a[-3:]) #print dari indeks -3 hingga selesai
print(a[:4:2]) #start:stop:step(lewat 2)

#len(), min(), max()
c = ['3', 'bar', 'qux', 'Qux', 'corge']
print (c)
print(len(c))
print(min(c))
print(max(c))

#Modify Single List
c[0] = '4'
c[2] = '5'
print(c)

#Hapus isi List
del c[4]
print(c)

#Modify Multiple List
d = ['roti', 'telor', 'susu', 'madu' , 'jahe']
d [1:4] = ['waw', 'wew', 'wow', 'wiw'] #hapus isi indeks 1 hingga 3 ganti dengan isi variable d
print (d)

d2 = ['mie', 'sayur']
d.extend(d2)
print (d)

d.append('air')
print(d)

#set {} : ga ada index, urutan acak, tidak bisa di copy (satu set ada dua atau lebih elemen sama)
thisset = {'motor', 'mobil', 'sepeda', 'sepeda', 'becak'}
print(thisset)

#Dictionary {}, key:value
person ={'Nama': 'Fadhil',
'Umur': '23 Tahun',
'Gender': 'Pria'}

print(person['Nama'])

person ['Hobi'] = 'Game'
print (person)

del person ['Umur']
print (person)

#Tuple