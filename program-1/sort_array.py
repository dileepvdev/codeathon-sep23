from collections import Counter

def sort_string_by_frequency(string):
    # Count the frequency of each character in the string
    char_count = Counter(string)
    
    # Sort the characters by frequency, then by their ASCII value
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    
    # Build the sorted string
    sorted_string = ""
    for char, count in sorted_chars:
        sorted_string += char * count
    
    return sorted_string
