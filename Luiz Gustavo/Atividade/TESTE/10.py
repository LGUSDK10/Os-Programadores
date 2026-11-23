def calcular_media(temperaturas):
	"""Calcula a média das temperaturas fornecidas.

	Args:
		temperaturas: Lista não vazia de temperaturas médias diárias.

	Returns:
		A média aritmética dos valores da lista.

	Raises:
		ValueError: Se a lista estiver vazia.
	"""
	if not temperaturas:
		raise ValueError("A lista de temperaturas não pode estar vazia.")
	return sum(temperaturas) / len(temperaturas)

def analizar_temperatura(temperaturas):
	"""Retorna a média, a maior e a menor temperatura da lista.

	Args:
		temperaturas: Lista não vazia de temperaturas médias diárias.

	Returns:
		Uma tupla com a média, o maior valor e o menor valor, nessa ordem.

	Raises:
		ValueError: Se a lista estiver vazia.

	A média é calculada pela subfunção calcular_media; o maior e o menor
	valores são obtidos diretamente da lista.
	"""
	if not temperaturas:
		raise ValueError("A lista de temperaturas não pode estar vazia.")

	media = calcular_media(temperaturas)
	maior = max(temperaturas)
	menor = min(temperaturas)
	return media, maior, menor

a = [20, 22, 19, 21, 23, 18, 20]
resultado = analizar_temperatura(a)
print(f"Média: {resultado[0]}, Maior: {resultado[1]}, Menor: {resultado[2]}")