import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)  # set penomeran board ke mode broadcom
GPIO.setwarnings(False)
 
# Set mode pin sebagai input untuk trigger, dan output untuk echo
GPIO_TRIGGER = 18 #sesuaikan pin trigger
GPIO_ECHO = 24 #sesuaikan pin echo
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)  
 
# Set trigger ke False (Low) untuk awal
GPIO.output(GPIO_TRIGGER, GPIO.LOW)
 
#Fungsi untuk menapatkan jarak
def get_range():
    # Kirim 10us sinyal high ke trigger
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
     
    #Stop trigger
    GPIO.output(GPIO_TRIGGER, False)
    timeout_counter = int(time.time())
    start = time.time()
 
    #dapatkan waktu start
    while GPIO.input(GPIO_ECHO)==0 and (int(time.time()) - timeout_counter) < 3:
        start = time.time()
 
    timeout_counter = int(time.time())
    stop = time.time()
    #dapatkan waktu stop
    while GPIO.input(GPIO_ECHO)==1 and (int(time.time()) - timeout_counter) < 3:
        stop = time.time()
 
    #Hitung waktu tempuh bolak-balik
    elapsed = stop-start
 
    #Hitung jarak, waktu tempuh dikalikan dengan kecepata suara (dalam centi meter)
    distance = elapsed * 34320
 
    #Jaraknya masih dalam hitungan bolak-balik, bagi dua untuk tahu jarak ke halangan
    distance = distance / 2
 
    #selesai
    return distance
 
#Panggil fungsi untuk menghitung jarak  dan cetak hasilnya
jarak = get_range()
print("Jarak halangan di depan adalah %.2f Cm" % jarak )
#outputnya seperti:
#Jarak halangan di depan adalah 331.57 Cm
