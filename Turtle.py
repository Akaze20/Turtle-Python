import turtle
import random

# Global puan değişkeni
puan = 0

# Ekranı kur
ekran = turtle.Screen()
ekran.bgcolor("lightblue")
ekran.title("Kaplumbağa Tıklama Oyunu")

# Kaplumbağayı oluştur
kaplumbaga = turtle.Turtle()
kaplumbaga.shape("turtle")
kaplumbaga.penup()
kaplumbaga.speed(0)  # anında hareket

# Skoru yazdırmak için ayrı turtle
yazi = turtle.Turtle()
yazi.hideturtle()
yazi.penup()
yazi.goto(0, 200)
yazi.write("Puan: 0", align="center", font=("Arial", 20, "bold"))


# Rastgele konuma zıplama
def rastgele_konum():
    if puan < 3:
        x = random.randint(-200, 200)
        y = random.randint(-150, 150)
        kaplumbaga.teleport(x, y)
        # 1 saniye sonra tekrar zıplasın
        ekran.ontimer(rastgele_konum, 800)


# Tıklama olayında puan artır
def tiklandi(x, y):
    global puan
    puan += 1
    yazi.clear()
    yazi.write(f"Puan: {puan}", align="center", font=("Arial", 20, "bold"))

    if puan >= 3:
        kaplumbaga.hideturtle()
        yazi.goto(0, 0)
        yazi.write("🎉 Oyun Bitti! 🎉", align="center", font=("Arial", 24, "bold"))
    else:
        rastgele_konum()


# Kaplumbağaya tıklanınca puan kazan
kaplumbaga.onclick(tiklandi)

# Oyunu başlat
rastgele_konum()

# Sonsuz döngü
turtle.done()

