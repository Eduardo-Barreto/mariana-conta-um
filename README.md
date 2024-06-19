# mariana-conta-um

Aplicação de uma CNN num serviço de detecção de números usando o dataset MNIST.

O backend é implementado em Flask, e a interface de usuário é construída com Bulma e HTMX.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/mariana-conta-um/mnist-digit-recognizer.git
   cd mnist-digit-recognizer
   ```

2. Crie um ambiente virtual e instale as dependências:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Execute o servidor Flask:

   ```bash
   flask run
   ```

4. Acesse a aplicação em [http://localhost:5000](http://localhost:5000).

## Vídeo de Demonstração

[Link para o vídeo](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## Como Funciona

- `/predict`: Rota que recebe uma imagem e retorna o dígito previsto.
- `/`: Rota que exibe a página HTML com o formulário para envio de uma imagem.

## Modelo

O modelo CNN foi treinado utilizando o dataset MNIST e está salvo no arquivo `pesos.h5`.

---

creditos para luiza do nome do repositorio
