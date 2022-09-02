# Rock, Paper, Scissors (RTS) game with randomness

Python uses the [mersenne twister algorithm](https://en.wikipedia.org/wiki/Mersenne_Twister) to generate random numbers. The seed is set to the current time by default. This means that the random numbers are different every time you run the program.

The askpython.com article [How to generate random numbers in Python](https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences) also has a good explanation of the random module.

# Lists in Python

Python has a built-in list type.

```python
my_list = [1, 2, 3, 4, 5]
```
You can access elements in the list by index.

```python
my_list[0] # 1
my_list[1] # 2
my_list[2] # 3
my_list[3] # 4
my_list[4] # 5
``` 
You can also access elements in the list by negative index.

```python
my_list[-1] # 5
my_list[-2] # 4
my_list[-3] # 3
my_list[-4] # 2
my_list[-5] # 1
```
You can also access elements in the list by index range.

```python
my_list[0:2] # [1, 2]
my_list[1:3] # [2, 3]
my_list[2:4] # [3, 4]
my_list[3:5] # [4, 5]
```

# How to avoid IndexOutOfBoundsError
_IndexError: list index out of range_

Check if you started counting at 0!

# Nested lists

```python
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
You can access elements in the list by index.

```python
my_list[0][0] # 1
my_list[0][1] # 2
my_list[1][0] # 4
my_list[1][1] # 5
```

