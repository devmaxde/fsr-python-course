
# Python Dictionaries

## Introduction to Dictionaries

Dictionaries in Python are used to store data values in key-value pairs.

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

### Dictionaries are mutable

#### pop()

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

### Dictionaries are unordered

## Recap

| Operation                       | Description                                                        | Example                                        | Result                           |
|---------------------------------|--------------------------------------------------------------------|------------------------------------------------|----------------------------------|
| `d[key]`                        | Accesses the value associated with the specified key               | `value = d['key']`                            | `value` is the value associated with `'key'` |
| `d[key] = value`                | Sets the value associated with the specified key                   | `d['new_key'] = 42`                          | Adds a new key-value pair to the dictionary |
| `del d[key]`                    | Removes the key-value pair with the specified key                  | `del d['key']`                               | Removes the key `'key'` and its value      |
| `key in d`                      | `True` if the key is in the dictionary, `False` otherwise  | `exists = 'key' in d`                        | `exists` is `True` if `'key'` is in the dictionary, `False` otherwise |
| `key not in d`                  | `True` if the key is not in the dictionary, `False` otherwise | `not_exists = 'key' not in d`              | `not_exists` is `True` if `'key'` is not in the dictionary, `False` otherwise |
| `d.keys()`                      | List of all keys in the dictionary                       | `all_keys = d.keys()`                       | `all_keys` is a view of all keys in `d`    |
| `d.values()`                    | List of all values in the dictionary                     | `all_values = d.values()`                   | `all_values` is a view of all values in `d` |
| `d.items()`                     | List of all key-value pairs in the dictionary            | `all_items = d.items()`                     | `all_items` is a view of all key-value pairs in `d` |
| `d.get(key, fallback)`           | Returns the value for the specified key or a default value if the key is not present | `value = d.get('key', default_value)`     | `value` is the value associated with `'key'`, `fallback` if `'key'` is not present |
| `d.pop(key, fallback)`           | Removes the key and returns its value; returns default if key is not present | `value = d.pop('key', default_value)`     | `value` is the value associated with `'key'` or `default_value` if `'key'` is not present; removes the key `'key'` |
| `d.clear()`                     | Removes all items from the dictionary                              | `d.clear()`                                 | Removes all key-value pairs from the dictionary |
| `len(d)`                        | Returns the number of key-value pairs in the dictionary             | `size = len(d)`                            | `size` is the number of key-value pairs in the dictionary |
| `dict.copy()`                   | Returns a shallow copy of the dictionary                           | `d_copy = d.copy()`                         | `d_copy` is a shallow copy of the dictionary |

## Pass by Reference


