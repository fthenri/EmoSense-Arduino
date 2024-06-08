# EmoSense

## Descrição
Para o projeto da faculdade, o grupo 17 desenvolveu uma solução inovadora
destinada a facilitar a comunicação de crianças com Transtorno do Espectro Autista (TEA).  
Com base nas soluções já existentes, criamos o EmoSense, uma solução figital (física e
digital) que visa proporcionar uma experiência mais eficiente e inclusiva.  
Este ReadMe foi criado com o intuito de explicar detalhadamente o funcionamento do nosso
protótipo e fornecer orientações passo a passo sobre como utilizá-lo. Esperamos que, através
desta solução, possamos contribuir significativamente para melhorar a comunicação e a
qualidade de vida das crianças com TEA.  

- Para o protótipo, é essencial contar com o auxílio de um computador para conectar o Arduino.
## Requisitos

### Hardware
- Placa Arduino Uno
- Notebook
- Botões (pelo menos 4: um para cada emoção)
- Resistores (4, para os botões)
- Jumpers macho-macho (10, para ligar os componentes)
- Protoboard

### Software
- Arduino IDE
- Python 3.x
  - Bibliotecas Python: Pyserial, Tkinter

## Instalação e Montagem

### Instalação
```sh
git clone https://github.com/fthenri/EmoSense-Arduino.git
```
### Montagem
Conexão dos Botões  
- Botão 1:  
Um terminal do botão ao pino digital 13 do Arduino.  
Outro terminal do botão ao GND.  
- Botão 2:  
Um terminal do botão ao pino digital 12 do Arduino.  
Outro terminal do botão ao GND.  
- Botão 3:  
Um terminal do botão ao pino digital 11 do Arduino.  
Outro terminal do botão ao GND.  
- Botão 4:  
Um terminal do botão ao pino digital 10 do Arduino.  
Outro terminal do botão ao GND.  
- Carregar o Código no Arduino  
- Baixe ou clone o repositório do projeto.  
- Abra o arquivo .ino na Arduino IDE.  
- Conecte o Arduino ao computador via USB.  
- Selecione a placa e porta correta na Arduino IDE.  
- Clique em Upload.  
- Configurar o Ambiente Python  
- Instalar Python  
- Baixe e instale Python 3.x a partir de python.org.  
- Instalar Bibliotecas Necessárias  
- Abra um terminal (ou prompt de comando) e execute:  

```sh
pip install pygame
pip install serial
pip install threading
```

## Como usar o dispositivo?

### Funcionamento: Após a montagem e a inserção do código funcional no Arduino, siga os passos abaixo:

- Insira um cabo USB na entrada de energia do Arduino e o conecte a uma entrada USB de seu computador.
- Execute o funcionamento do Arduino.
- Após confirmação de bom funcionamento do arduino, escolha um dos botões.
Cada botão irá iniciar uma seleção de imagens na tela do seu computador.
- O  botão vermelho é referente à sentimentos negativos, o verde á sentimentos positivos, o amarelo á vontades e o azul á necessidades.
- Após apertar o botão, 4 imagens referente a sua escolha vão aparecer na tela.
- Escolha a imagem que mais se assemelha a sua situação com os botões e aperte o mesmo botão novamente para confirmação.
- Quando confirmada, haverá disparo de um som e a imagem permanecerá em sua tela.
- Para nova escolha repita o procedimento.
## Licença

### Este projeto está licenciado sob a MIT License

## Autores
- Bernardo Marques de Araujo - bma2@cesar.school
- Carlos Eduardo Espósito Cardoso - ceec@cesar.school
- Guilherme Mourão Vieira Coelho - gmvc@cesar.school
- Henrique Figueirêdo Tefile - hft@cesar.school
- José Gabriel Santiago de Santana - jgss@cesar.school
- Lucas Rodrigues Campos - lrc@cesar.school
- Luiz Felipe Andreto Nogueira - lfan@cesar.school
- Maria Clara Leite de Vasconcelos - mclv@cesar.school
- Mariana Fernandes da Silva - mfs5@cesar.school
