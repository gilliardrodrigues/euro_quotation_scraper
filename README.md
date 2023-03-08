# Euro Quotation Scraper
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

Pequeno projeto criado para monitorar a cotação do euro em relação ao real brasileiro pelo menos a cada minuto e enviar um alerta por e-mail caso o valor fique abaixo de um limite escolhido.

## Como utilizar:
1. Após clonar o repositório, você deve instalar as dependências necessárias através do comando:
```
$ pip install -r requirements.txt
```
2. Crie uma conta no Gmail para servir como o remetente dos alertas. 


3. Após criá-la, vá em 'myaccount.google.com/security' e clique na seção 'Senhas de app', selecione o app (neste caso 'E-mail'), o dispositivo (eu usei 'Computador Windows') e clique em 'GERAR'. Esse passo é necessário para que o Gmail permita o envio de e-mails através de scripts automatizados.


4. Em seguida, crie um arquivo chamado '.env' e preencha-o da seguinte forma:
```
SENDER_EMAIL=<E-MAIL CRIADO PARA SER O REMETENTE>
SECURE_PASSWORD=<SENHA GERADA NO PASSO ANTERIOR>
```
5. Por fim, basta rodar o seguinte comando no terminal para executar o script: 
```
$ python main.py <VALOR LIMITE> <TEMPO DE DESCANSO EM SEGUNDOS> <E-MAIL PARA ONDE OS ALERTAS DEVEM SER ENVIADOS>
```
Exemplo de uso:
```
$ python main.py 5.40 60 joaozinho@gmail.com
```
Nesse exemplo eu estou definindo que é para fazer o scraping a cada 60 segundos e enviar um e-mail para 'joaozinho@gmail.com' caso o valor do euro fique abaixo de R$5,40.
