edad = 14
tiene_credencial = True
tiene_adeudo = False
if edad >= 18:
    es_mayor = True
else:
    es_mayor = False
if tiene_credencial:
    documento_valido = True
else:
    documento_valido = False
if tiene_adeudo:
    sin_adeudo = False
else:
    sin_adeudo = True
if es_mayor and documento_valido and sin_adeudo:
    autorizado = True
else:
    autorizado = False
print(autorizado)