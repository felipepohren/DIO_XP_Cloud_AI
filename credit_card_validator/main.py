
'dado um número de cartão de crédito, criar uma função em python para validar a bandeira do cartão. utilizar REGEX'
'''
Visa = começa com numero 4
Mastercard = começa com 51, 52, 53, 54 ou 55 ou entre 2221 e 2720
Elo = pode começar com vários interalos, como 4011, 4312, 4389, entre outros
American Express = começa com 34 ou 37
Discover = começa com 6011, 65, ou com a faixa entre 644 a 649
Hipercard = geralmente começa com 6062
Diners Club = começa com 300, 301, 302, 303, 304, 305, 36 ou 38
JCB = começa com 3528, 3589, 3530, 3531, 3532, 3533, 3534, 3535, 3522 ou 3528
EnRoute = começa com 2014 ou 2149
Voyager = começa com 8699
Aura = começa com 50
'''

import re

def validar_bandeira(numero_cartao):
    """
    Valida a bandeira de um cartão de crédito com base no número fornecido usando REGEX.
    :param numero_cartao: Número do cartão de crédito (string ou inteiro).
    :return: Nome da bandeira ou "Bandeira desconhecida".
    """
    numero_cartao = str(numero_cartao).replace(" ", "")  # Remove espaços

    # Visa
    if re.match(r"^4[0-9]{12}(?:[0-9]{3})?$", numero_cartao):
        return "Visa"

    # Mastercard
    if re.match(r"^(5[1-5][0-9]{14}|2(2[2-9][0-9]{12}|[3-6][0-9]{13}|7[0-1][0-9]{12}|720[0-9]{12}))$", numero_cartao):
        return "Mastercard"

    # Elo
    if re.match(r"^(4011|4312|4389)[0-9]*$", numero_cartao):
        return "Elo"

    # American Express
    if re.match(r"^3[47][0-9]{13}$", numero_cartao):
        return "American Express"

    # Discover
    if re.match(r"^6(?:011|5[0-9]{2}|4[4-9][0-9])[0-9]{12}$", numero_cartao):
        return "Discover"

    # Hipercard
    if re.match(r"^6062[0-9]*$", numero_cartao):
        return "Hipercard"

    # Diners Club
    if re.match(r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$", numero_cartao):
        return "Diners Club"

    # JCB
    if re.match(r"^(?:352[89]|35[3-8][0-9])[0-9]{12}$", numero_cartao):
        return "JCB"

    # EnRoute
    if re.match(r"^(2014|2149)[0-9]*$", numero_cartao):
        return "EnRoute"

    # Voyager
    if re.match(r"^8699[0-9]*$", numero_cartao):
        return "Voyager"

    # Aura
    if re.match(r"^50[0-9]*$", numero_cartao):
        return "Aura"

    # Caso nenhuma bandeira seja identificada
    return "Bandeira desconhecida"


# Exemplo de uso
numero = input("Digite o número do cartão de crédito: ")
bandeira = validar_bandeira(numero)
print(f"A bandeira do cartão é: {bandeira}")
