import wiringpi as pi
import time

SPI_CH = 0

READ_CH = 0

pi.wiringPiSPISetup(SPI_CH, 1000000 )

while True:
    buffer = 0x6800 |  (0x1800 * READ_CH ) 
    buffer = buffer.to_bytes( 2, byteorder='big' )

    pi.wiringPiSPIDataRW( SPI_CH, buffer )
    value = ( buffer[0] * 256 + buffer[1] ) & 0x3ff
    volt = value * 3.3 / float(1023)    

    print ("Value:", value, "  Volt:", volt )

    time.sleep(1)
