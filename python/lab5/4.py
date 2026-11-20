def crypt_calc(x, y):
    if x >= ord("A") and x <= ord("Z"):
        return chr((x + (y % 26)))
    elif x >= ord("a") and x <= ord("z"):
        return chr((x + (y % 26)))
    else:
        return chr(x)

def dcrypt_calc(x, y):
    if x >= ord("A") and x <= ord("Z"):
        return chr((x - (y % 26)))
    elif x >= ord("a") and x <= ord("z"):
        return chr((x - (y % 26)))
    else:
        return chr(x)

def encrypt(words, shift_value):
    map_list = map(lambda x: crypt_calc(ord(x), shift_value), words)    
    return list(map_list) 

def decrypt(words, shift_value):
    map_list = map(lambda x: dcrypt_calc(ord(x), shift_value), words)    
    return list(map_list) 

def arr_to_str(words):
    return "".join(words)

print(arr_to_str(decrypt(encrypt("Hello World", 3), 3)))
