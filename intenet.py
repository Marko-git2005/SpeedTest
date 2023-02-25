import speedtest 
from datetime import datetime
import schedule
import time

def speed():
   test = speedtest.Speedtest(secure=True)
   print ("Searchingh for the best server...")
   test.get_servers()
   print ("Found the best server! ")
   best = test.get_best_server()
   print (f"Found {best['host']} located in {best['country']}")
   print("Measuring download speed...")
   brzinadown = test.download()
   print (f'Download speed:{brzinadown/1000000} mbs')
   print("Mesuring upload speed...")
   brzinaup = test.upload()
   print (f'Upload speed: {brzinaup/1000000} mbs')
   print("Measuring ping...")
   pingrezultat = test.results.ping
   print (f"Ping: {pingrezultat} ms")
   datum =  datetime.now().strftime('%d/%m/%Y')
   print (f'Date: {datum}')
   cas = datetime.now().strftime('%H:%M')
   print (f'Time: {cas}')
   with open('net.txt', 'a') as f:
    f.write(f'''

Server: {best ['host']}
Download: {brzinadown/1000000} mbps
Upload: {brzinaup/1000000} mbps
Ping: {pingrezultat} ms
Datum: {datum}
Cas: {cas}''')
   


brzina()
schedule.every(10).minutes.do(brzina)
while 1: 
    schedule.run_pending()
    time.sleep(1)

