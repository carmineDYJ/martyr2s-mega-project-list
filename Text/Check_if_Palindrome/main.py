while True:
    string_input = input('Try to enter a string, the program can check whether it is a palindrome\n>>> ')
    left, right = 0, len(string_input) - 1
    palindrome_flag = True
    while left < right:
        if string_input[left] != string_input[right]:
            palindrome_flag = False
            break
        left += 1
        right -= 1
    if palindrome_flag:
        print(string_input + ' is a palindrome')
    else:
        print(string_input + ' is not a palindrome')