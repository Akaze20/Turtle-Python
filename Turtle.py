import turtle

ekran = turtle.Screen()
ekran.title("Yön Tuşlarıyla Hareket")
ekran.bgcolor("lightblue")

# Kaplumbağayı oluştur
kaplumbaga = turtle.Turtle()
kaplumbaga.shape("turtle")
kaplumbaga.color("darkgreen")
kaplumbaga.speed(1)

# Hareket fonksiyonları
def yukari():
    kaplumbaga.setheading(90)  # Yukarı yön (0: sağ, 90: yukarı, 180: sol, 270: aşağı)
    kaplumbaga.forward(20)

def asagi():
    kaplumbaga.setheading(270)
    kaplumbaga.forward(20)

def sola():
    kaplumbaga.setheading(180)
    kaplumbaga.forward(20)

def saga():
    kaplumbaga.setheading(0)
    kaplumbaga.forward(20)

# Tuşları dinle
ekran.listen()
ekran.onkey(yukari, "w")
ekran.onkey(asagi, "s")
ekran.onkey(sola, "a")
ekran.onkey(saga, "d")

# Ekranı kapatmayı engelle
ekran.mainloop()
