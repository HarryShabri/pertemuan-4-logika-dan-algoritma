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

gaji_pokok = int(input(" Masukkan gaji pokok anda : Rp "))
jam_kerja = int(input(" Masukkan jam kerja anda : "))
if jam_kerja > 200 :
    lembur = (jam_kerja-200)*20000
else:
    lembur = 0
tunjangan = 20/100*gaji_pokok
gaji = gaji_pokok + tunjangan + lembur
pajak = 10/100*gaji
diterima = gaji - pajak
print("Total gaji yang diterima adalah : Rp ", diterima)