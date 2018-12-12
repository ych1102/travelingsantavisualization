import matplotlib.pyplot as plt
import numpy as np
import csv

file_name = "result_coordinate"

with open(file_name, "r") as ins:
    csv_reader = csv.reader(ins, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count ==0:
            x = row
        elif line_count == 1:
            y = row
        else:
            z = row
        line_count += 1
    x = [float(ele) for ele in x]
    y = [float(ele) for ele in y]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(x, y)
    # for a,b,c in zip(x, y, z):  # <--
    #     ax.annotate('%s' % c, xy=(a,b), textcoords='data')  # <--
    plt.show()

#
# x=[316.836739061509,308.608834287432,314.494243312195,308.903690863706,315.092520044541,320.997523957835,314.716006798186,316.836739061509]
# y=[2202.34070733524,2185.79795356423,2186.64674767296,2178.86836182647,2179.84653261954,2186.42278175365,2193.8888357871,2202.34070733524]
# plt.figure()
# plt.plot(x, y)
# plt.show()