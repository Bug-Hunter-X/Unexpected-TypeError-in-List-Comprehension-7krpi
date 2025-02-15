def function_with_uncommon_error_solution(data):
    if not isinstance(data, list):
        print("Error: Input data must be a list.")
        return []
    result = []
    for item in data:
        if isinstance(item, dict) and 'value' in item:
            result.append(item['value'])
        else:
            print(f"Warning: Skipping invalid item: {item}")
    return result

data = [{'value': 1}, {'value': 2}, 3]
result = function_with_uncommon_error_solution(data)
print(f"Result: {result}")

data2 = [{'value': 1}, {'value': 2}, {'other':3}]
result2 = function_with_uncommon_error_solution(data2)
print(f"Result2: {result2}") 