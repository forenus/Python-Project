import qrcode as qr
img= qr.make("https://www.youtube.com/watch?v=BZJcNU648Tc")
img.save("sigma_web.png")