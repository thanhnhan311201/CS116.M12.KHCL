import numpy as np
import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('excel_flc.csv')
price = np.array(data['<CloseFixed>'])
price = price[::-1]

x = []
for i in range(len(price)):
    x.append(i)

vol = np.array(data['<Volume>'])
vol = vol[::-1]
vol = data['<Volume>'].astype(float)

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()

T=22
ret = (price[T:] - price[:-T]/price[:-T])

ax1.plot(x, price, color='red')
ax2.plot(x, vol, color='blue')
ax1.set_xlabel('Time')
ax1.set_ylabel('Price data', color='red')
ax2.set_ylabel('Volume data', color='blue')
ax1.set_title('VẼ BIỂU ĐỒ GIÁ - KHỐI LƯỢNG')
plt.show()