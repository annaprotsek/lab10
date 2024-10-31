def unique_characters(input_string):
    unique_set = set()
    seen_set = set()
    
    for char in input_string:
        if char in seen_set:
            if char in unique_set:
                unique_set.remove(char)
        else:
            unique_set.add(char)
            seen_set.add(char)
    
    print("Символи, які зустрічаються один раз:", ' '.join(unique_set))

input_string = input("Введіть рядок: ")

unique_characters(input_string)