from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = random.randint(100)  # generates a random integeer
print(x)

y = random.rand()  # generates a random float between 0 and 1
print(y)

x = random.rand(3)  # generates a 1-dimensional array
print(x)

x = random.randint(100, size=5)  # generates array of random five integers
print(x)

print()

x = random.randint(100, size=(3, 5))  # generates a matrix or 2-dimensional array
print(x)

print()

x = random.choice([3, 5, 7, 9])  # generates a random value from an array
print(x)

print()

x = random.choice([3, 5, 7, 9], size=(3, 5))  # generates a 2-dimensional array from the values in the array given
print(x)

#  Random data distribution
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=100)  # we set our probability to how we want the
# distribution to occur, 7 will occur most and 9 will never occur, note that sum of all probabilities must be 1
print(x)

print()

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)

print()

#  Random Permutations
arr1 = np.array([1, 2, 3, 4, 5])
random.shuffle(arr1)  # rearranges the position of the original elements using shuffle
print(arr1)  # the original array is shuffled

print()

arr2 = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr2))  # permutation returns a shuffled copy of the original, does not shuffle the original
print(arr2)  # the original array remains the same.

print()

# sns.displot([0, 1, 2, 3, 4, 5])
# plt.show()

# sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
# plt.show()

# Normal or Gaussian distribution
# x = random.normal(size=(2, 3))
# print(x)
#
# x = random.normal(loc=1, scale=2, size=(2, 3))
# print(x)
#
# sns.distplot(random.normal(size=1000), hist=False)
# plt.show()

print()

#  Binomial distribution
x = random.binomial(n=10, p=0.5, size=10)
print(x)

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.xlabel('Data')
plt.ylabel('Frequency')
plt.title('Histogram of Binomial Distribution')

plt.show()
