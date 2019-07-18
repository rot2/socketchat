import time
import socket
import sys


print('Client başlatıldı...')

time.sleep(1)

soc = socket.socket()

shost = socket.gethostname()

ip = socket.gethostbyname(shost)


print(shost, '({})'.format(ip))
sunucu_host = input('Sunucu ip adresini gir:')

ad = input('İsmini gir: ')

port = 80

print('Sunucuya bağlanılıyor: {}, ({})'.format(sunucu_host, port))

time.sleep(1)
soc.connect((sunucu_host, port))
print("Bağlandı...\n")

soc.send(ad.encode())
sunucu_isim = soc.recv(1024)
sunucu_isim = sunucu_isim.decode()

print('{} Katıldı...'.format(sunucu_isim))

print('Çıkmak için #q yaz.')


while True:
   msj = soc.recv(1024)
   msj = msj.decode()
   
   print(sunucu_isim,msj)
   
   msj = input(str("Ben: "))
   if msj == "#q":
      msj = "Ayrıldı."
      
      soc.send(msj.encode())
      
      print("\n")
      break
   soc.send(msj.encode())
