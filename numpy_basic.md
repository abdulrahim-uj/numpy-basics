```python
import numpy


x = numpy.array([11, 22, 33, 44, 55])

print(x)
```

    [11 22 33 44 55]
    


```python
import numpy as np

y = np.array([100, 200, 300, 400, 500])

print(y)
```

    [100 200 300 400 500]
    


```python
print(np.__version__)
```

    1.21.5
    


```python
z = np.array((44, 55, 66, 77, 88, 99, 11))

print(z)
```

    [44 55 66 77 88 99 11]
    


```python
# TWO DI ARRAY
```


```python
x1 = np.array([[1, 2, 3, 4, 5], [11, 22, 33, 44, 55]])

print(x1)
print(x1.ndim)
```

    [[ 1  2  3  4  5]
     [11 22 33 44 55]]
    2
    


```python
# THREE DI ARRAY
```


```python
y1 = np.array([[[[1, 2, 3, 4, 5], [10, 20, 30, 40, 50], [3, 13, 23, 33, 43, 53]]]])

print(y1.ndim)
```

    3
    

    C:\Users\abdul\AppData\Local\Temp\ipykernel_17824\633101553.py:1: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
      y1 = np.array([[[[1, 2, 3, 4, 5], [10, 20, 30, 40, 50], [3, 13, 23, 33, 43, 53]]]])
    


```python
z1 = np.array(56)

print(z1)
```

    56
    


```python
# ARRAY DI CHECK
```


```python
print(z1.ndim)
```

    0
    


```python
print(x1.ndim)
```

    2
    


```python
print(y1.ndim)
```

    3
    


```python
q1 = np.array([[[1,2,3], [9,8,7], [66,88,77], [65, 45, 55]]])

print(q1)

print(q1.ndim)
```

    [[[ 1  2  3]
      [ 9  8  7]
      [66 88 77]
      [65 45 55]]]
    3
    


```python
one = np.array([10,20,30,40,50])

print(one)
print(one.ndim)

print(one[3])
```

    [10 20 30 40 50]
    1
    40
    


```python
two = np.array([[2,4,6,8,10], [10,20,30,40,50]])

print(two)
print(two.ndim)
# two[0, 2]: 0 is first dimention il 2 is second element
print(two[0, 2])
print(two[1, 3])
```

    [[ 2  4  6  8 10]
     [10 20 30 40 50]]
    2
    6
    40
    


```python
# [[[10,20,30,40], [50,60,70,80]]]
three = np.array([[[10,20,30,40], [1,2,3,4], [45, 55, 65, 75], [75,85,95,105]]])

print(three)
print(three.ndim)
# 
# [oth array, 2nd list, 3rd position]
print(three[0, 2, 3])
print(three[0, 3, 2])
```

    [[[ 10  20  30  40]
      [  1   2   3   4]
      [ 45  55  65  75]
      [ 75  85  95 105]]]
    3
    75
    95
    


```python

```
