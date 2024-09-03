#return string[::-1]

def reverse_string(string):
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return print(reversed_string)

reverse_string('frase invertida')