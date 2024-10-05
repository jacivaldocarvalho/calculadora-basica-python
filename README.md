# CALCULADORA SIMPLES EM PYTHON

Este é um projeto de uma calculadora simples em Python que pode realizar operações básicas: soma, subtração, multiplicação e divisão. A calculadora aceita dois números e uma operação especificada por um parâmetro.

## Funcionalidades

A calculadora oferece as seguintes operações:

1. **Soma**
2. **Subtração**
3. **Multiplicação**
4. **Divisão**

Caso seja inserido um número de operação que não exista, a função retornará 0. Além disso, a divisão por zero retorna uma mensagem de erro.

## Como Usar

### Pré-requisitos

- Python 3.x instalado em seu sistema.

### Executando o Código

1. Clone o repositório ou baixe os arquivos para o seu computador.
2. Abra um terminal e navegue até o diretório onde os arquivos estão localizados.
3. Execute o script Python:

   ```bash
   python calculadora_basica.py
   ```
### Exemplo de Uso
No código, você encontrará uma função main que demonstra as operações disponíveis:

  ```python
  def main():
    print("Resultados da Calculadora:")
    print("Soma (10 + 5):", calculadora(10, 5, 1))  # Saída: 15
    print("Subtração (10 - 5):", calculadora(10, 5, 2))  # Saída: 5
    print("Multiplicação (10 * 5):", calculadora(10, 5, 3))  # Saída: 50
    print("Divisão (10 / 5):", calculadora(10, 5, 4))  # Saída: 2.0
    print("Divisão (10 / 0):", calculadora(10, 0, 4))  # Saída: Erro: Divisão por zero!
    print("Operação inválida:", calculadora(10, 5, 5))  # Saída: 0
  ```
## Contribuição
Contribuições são bem-vindas! Se você deseja melhorar este projeto, sinta-se à vontade para fazer um fork do repositório e enviar suas alterações.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE) - consulte o arquivo LICENSE para mais detalhes.

## Autor
**Jacivaldo Carvalho**  
[LinkedIn](https://www.linkedin.com/in/jacivaldocarvalho/) 



  
