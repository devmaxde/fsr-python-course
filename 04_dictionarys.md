
# Python Dictionaries

## Introduction to Dictionaries

Dictionaries in Python are used to store data values in key-value pairs. A dictionary is a collection which is unordered, changeable, and does not allow duplicates.

### Basic Usage

Dictionaries are defined within braces `{}` with each item being a pair in the form `key: value`. Keys must be unique and immutable types (such as strings, numbers, or tuples), while values can be of any data type.

**Example**
```python
my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
```

### Accessing Items

You can access the items of a dictionary by referring to its key name.

**Example**
```python
x = my_dict["model"]
```

### Changing Values

You can change the value of a specific item by referring to its key name.

**Example**
```python
my_dict["year"] = 2018
```

## Dictionary Methods

### keys()

Returns a list of all the keys in the dictionary. The order of the keys is arbitrary.

**Example**
```python
keys = my_dict.keys()
print(keys) # ["brand", "model", "year"]
```

### values()

Returns a list of all the values in the dictionary. The order of the values is arbitrary.

**Example**
```python
values = my_dict.values()
print(values) # ["Ford", "Mustang", 2018]
```

### items()

Returns a list of tuples, each tuple containing a key-value pair.

**Example**
```python
items = my_dict.items()
print(items) # [("brand", "Ford"), ("model", "Mustang"), ("year", 2018)]
```

### pop()

Removes the element with the specified key.

**Example**
```python
my_dict.pop("model")
```

#### `clear()`

Removes all the elements from the dictionary.

**Example**
```python
my_dict.clear()
```
