import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('grey')
t.goto(0,0)
t.penup()
t.write("Harry Shabri", align=('center'),font=('Times 15 normal'))
t.goto(100,0)
t.penup()
t.write("17220385", align=('center'),font=('Times 15 normal'))
t.hideturtle()
turtle.done()

gaji = int(5000000)
harga_produk = int(input("Masukkan harga produk : Rp"))
terjual = int(input("Jumlah produk yang terjual : "))
omset = harga_produk*terjual

if terjual > 100 :
    bonus = gaji + (20/100*omset)
else:
    bonus = gaji + (10/100*omset)

total_gaji = gaji + bonus

print("Total gaji anda adalah : Rp ",total_gaji)