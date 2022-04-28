import digitalio
import analogio
import board
import pwmio
import time

a1 = digitalio.DigitalInOut(board.IO36);a1.direction = digitalio.Direction.OUTPUT;
b1 = digitalio.DigitalInOut(board.IO38);b1.direction = digitalio.Direction.OUTPUT;
a2 = digitalio.DigitalInOut(board.IO37);a2.direction = digitalio.Direction.OUTPUT;
b2 = digitalio.DigitalInOut(board.IO39);b2.direction = digitalio.Direction.OUTPUT;

def wave_drive():
    wave_table = [1,0,0,0]
    for i  in range(4):
        a1.value = wave_table[i]
        b1.value = wave_table[(i+3)%4]
        a2.value = wave_table[(i+2)%4]
        b2.value = wave_table[(i+1)%4]
        time.sleep(0.1)
#         print(wave_table[i],wave_table[(i+3)%4],wave_table[(i+2)%4],wave_table[(i+1)%4])

def full_step_drive():
    full_step_table = [1,0,0,1]
    for i  in range(4):
        a1.value = full_step_table[i]
        b1.value = full_step_table[(i+3)%4]
        a2.value = full_step_table[(i+2)%4]
        b2.value = full_step_table[(i+1)%4]
        time.sleep(0.1)
#         print(full_step_table[i], full_step_table[(i+3)%4], full_step_table[(i+2)%4], full_step_table[(i+1)%4])

def half_step_drive():
    half_step_table = [[1,0,0,1],[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1]]
    for i  in range(8):
        a1.value = half_step_table[i][0]
        b1.value = half_step_table[i][1]
        a2.value = half_step_table[i][2]
        b2.value = half_step_table[i][3]
        time.sleep(0.1)
#         print(half_step_table[i][0], half_step_table[i][1], half_step_table[i][2], half_step_table[i][3])
    
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
#     wave_drive()
#     full_step_drive()
#     half_step_drive()
#     spwm()
     


