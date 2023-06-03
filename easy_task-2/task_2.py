def find_pattern(lst):
    length = len(lst)
    
    for pattern_length in range(1, length // 2 + 1):
        pattern = lst[:pattern_length]
        repeats = length // pattern_length
        if lst == pattern * repeats:
            return pattern, repeats
    
    return None, 0

def pattern_recognizer():
    input_list = input("Enter a list of numbers, separated by commas: ").split(",")
    input_list = [int(num) for num in input_list]
    
    pattern, repeats = find_pattern(input_list)
    
    if pattern:
        print("Pattern Found:", pattern)
        print("Number of times the pattern repeats:", repeats)
    else:
        print("Pattern Not Found")

# Example usage
pattern_recognizer()
