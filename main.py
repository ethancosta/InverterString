def inverter_string(s):
    s_invertida = ''
    for caracter in s:
        s_invertida = caracter + s_invertida
    return s_invertida


s = "Farofa"
print("String original:", s)
print("String invertida:", inverter_string(s))
