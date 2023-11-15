def get_ascii(input):
    ascii=ord(input)
    return ascii

def get_binary(input):
    binario = bin(input)[2:]
    binario = binario.zfill(8)
    return binario

def get_results(input):
    resultado=""
    for i in range (0,len(input),1):
        ascii=get_ascii(input[i])
        binario=get_binary(ascii)
        resultado=resultado+binario+" "
        print('ASCII character value of "',input[i],'" is ',ascii,'. Binary representation of "',input[i],'" in a Byte is ',binario)
    return resultado
        