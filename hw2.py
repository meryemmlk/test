import numpy as np
from matplotlib import pylab

def read_csv(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    header = lines[0].strip().split(',')
    data = [ line.strip().split(',') for line in lines[1:] ]
    data = np.array(data).astype('float')
    return header,data

filename_one = "data/dataset-one.csv"
header,data = read_csv(filename_one)
examples,labels = data[:,:-1],data[:,-1]

print("=== header")
print(header)
print("=== first 10 examples")
print(examples[:10])
print("=== first 10 labels")
print(labels[:10])

def plot(examples, labels, intercept, a):
    pylab.scatter(examples, labels, label='Data Points')
    x_values = np.linspace(min(examples), max(examples), 100)
    y_values = intercept + a * x_values
    pylab.plot(x_values, y_values, color='red', label='Regression Line')
    pylab.xlabel('exercise')
    pylab.ylabel('cholestrol')
    pylab.legend()
    pylab.title('Linear Regression')
    pylab.show()