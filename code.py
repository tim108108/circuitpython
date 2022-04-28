import digitalio
import analogio
import board
import pwmio
import time

in1 = pwmio.PWMOut(board.IO11, frequency=5000, duty_cycle=0)
in2 = pwmio.PWMOut(board.IO12, frequency=5000, duty_cycle=0)
in3 = pwmio.PWMOut(board.IO13, frequency=5000, duty_cycle=0)
en = digitalio.DigitalInOut(board.IO14)
en.direction = digitalio.Direction.OUTPUT
i2 = analogio.AnalogIn(board.IO15)
i3 = analogio.AnalogIn(board.IO16)

def spwm():
    spwm_table=[0.5,0.75,0.933,1.0,0.933,0.75,0.5,0.25,0.066,0.0,0.066,0.25]
    en.value = True
    for i in range(12):
        in1.duty_cycle = int(65535*spwm_table[i])
        in2.duty_cycle = int(65535*spwm_table[(i+4)%12])
        in3.duty_cycle = int(65535*spwm_table[(i+8)%12])
#         time.sleep(0.01)
#         print(i2.value/ 65535*i2.reference_voltage,i3.value/ 65535*i3.reference_voltage)
#         print(i,(i+4)%12,(i+8)%12)
#         print(spwm_table[i],spwm_table[(i+4)%12],spwm_table[(i+8)%12])
#         print(int(65535*spwm_table[i]),int(65535*spwm_table[(i+4)%12]),int(65535*spwm_table[(i+8)%12]))

while True:
    spwm()
