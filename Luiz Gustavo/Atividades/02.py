import statistics

def analise_estatistica(dados: list) -> tuple:
  """
  Função que recebe uma lista de números e retorna a média, mediana, moda e desvio padrão.
  
  Parâmetros:
    dados (list): Uma lista de números.

  Retorna:
    tuple: Uma tupla contendo a média, mediana, moda e desvio padrão.
  """

  if len(dados) < 3:
    raise ValueError("A lista deve ter pelo menos 3 elementos.")

  media = statistics.mean(dados)
  mediana = statistics.median(dados)
  moda = statistics.mode(dados)
  desvio_padrao = statistics.stdev(dados)

  return media, mediana, moda, desvio_padrao

entrada = input("Digite uma lista de números separados por vírgula (ex: 1,2,3,4): ").split(",")
dados = [float(x.strip()) for x in entrada]
resultado = analise_estatistica(dados)
print(resultado)