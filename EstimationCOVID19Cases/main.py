import pandas
import numpy
import matplotlib.pyplot as plt

data = pandas.read_csv("./total_cases.csv", usecols=["World"])

patients_Y = data.iloc[:, 0]
dated_X = pandas.DataFrame(range(1, data.size + 1), columns=["Date"]).iloc[:, 0]

# estimating the polynomial coefficients
coe = numpy.polynomial.polynomial.polyfit(dated_X, patients_Y, 2)
print(coe)


plt.scatter(dated_X, patients_Y)

predictions = coe[0] + coe[1] * dated_X + coe[2] * dated_X ** 2

plt.plot(predictions, color='red')
plt.show()
