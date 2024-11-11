import matplotlib.pyplot as plt
import serial

id = "cu.usbserial-1410"

arduino = serial.Serial(port=f'/dev/{id}', baudrate=9600, timeout=0.1)

def read():
    data = ""
    while len(data) < 1:
        data = arduino.readline()
    return data.decode('utf-8') #utf-8 same name for ascii

for i in range (100):
    msg = read()
    print(msg)

# def read():
#     data = ""
#     while len(data) < 1:
#         data = arduino.readline()
#     return data.decode('utf-8')
#
# humidity = []
# temperature = []
# time = []
# t = 0
# for i in range(5):
#     time.append(t)
#     t += 1
#     humidity.append(float(read().split(' ')[0].split(':')[1].strip('%')))
#     temperature.append(float(read().split(' ')[1].split(':')[1].strip().replace('°C', '')))
#
# fig = plt.Figure(figsize=(20, 16))
# plt.subplots_adjust(hspace=0.5)
# plt.subplot(2, 1, 1)
# plt.plot(time, humidity, color='red')
# plt.title("Humidity Graph")
# plt.xlabel("Time(Sec)")
# plt.ylabel("Humidity(%)")
# plt.subplot(2, 1, 2)
# plt.plot(time, temperature, color='black')
# plt.title("Temperature Graph")
# plt.xlabel("Time(Sec)")
# plt.ylabel("Temperature(C)")
#
# plt.show()