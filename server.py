import time
import socket
import sys

print('Sunucu kuruluyor...')

time.sleep(1)
soc = socket.socket()
host_isim = socket.gethostname()

ip = socket.gethostbyname(host_isim)
port = 80

soc.bind((host_isim, port))
print(host_isim, '({})'.format(ip))

ad = input('İsmini gir: ')
soc.listen(1) 

print('Bağlantılar bekleniyor...')

baglanti, adres = soc.accept()
print("Bağlantı alınıyor... ", adres[0], "(", adres[1], ")\n")
print('Bağlantı kuruldu: {}, ({})'.format(adres[0], adres[0]))

client_isim = baglanti.recv(1024)
client_isim = client_isim.decode()

print(client_isim + ' bağlandı.')
print('Çıkmak için #q yaz')
baglanti.send(ad.encode())

while True:
   msj = input('Ben: ')
   if msj == '#q':
      msj = 'Çıkış yaptı.'
      baglanti.send(msj.encode())
      print("\n")
      break
   baglanti.send(msj.encode())
   msj = baglanti.recv(1024)
   msj = msj.decode()
   print(client_isim, msj)
