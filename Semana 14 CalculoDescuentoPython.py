# Semana 14
# CalculoDescuentoPython
# Pizarra (Whiteboard)
def calcular_descuento(valor_compra, valor_descuento=10):
    descuento = (valor_compra * valor_descuento) / 100
    return descuento


valor_compra = 750
valor_final = valor_compra - calcular_descuento(valor_compra)
print(
    f'El final es: {valor_final}. Valor de compra: {valor_compra}. Valor de descuento: {calcular_descuento(valor_compra)}')

valor_compra = int(input('Ingrese valor de compra: '))
valor_descuento = int(input('Ingrese valor de descuento: '))
valor_final = valor_compra - calcular_descuento(valor_compra, valor_descuento)
print(
    f'El valor final es: {valor_final}. Valor de compra: {valor_compra}. Valor de descuento: {calcular_descuento(valor_compra, valor_descuento)}')
