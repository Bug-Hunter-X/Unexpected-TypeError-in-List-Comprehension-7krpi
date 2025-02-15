def function_with_uncommon_error(data):
    try:
        # Assume data is a list of dictionaries
        result = [item['value'] for item in data if 'value' in item]
        return result
    except KeyError as e:
        # This handles the common KeyError, but...
        print(f"KeyError: {e}")
        return []
    except TypeError as e:
        # ...this handles potential type errors if 'data' isn't a list of dicts.
        print(f"TypeError: {e}")
        return []

# Example showcasing the issue
data = [{'value': 1}, {'value': 2}, 3] #In this case, 3 is not a dict
result = function_with_uncommon_error(data)
print(f"Result: {result}")  # Result: []

data2 = [{'value': 1}, {'value': 2}, {'other':3}]
result2 = function_with_uncommon_error(data2)
print(f"Result2: {result2}") # Result2: [1,2]