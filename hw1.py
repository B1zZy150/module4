def palindrome(string):
    if string[::-1] == string:
        return True
    else:
        return False
print(palindrome('лепсспел'))
print(palindrome('helloworld'))