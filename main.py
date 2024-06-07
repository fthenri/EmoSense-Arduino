import pygame
import serial
import threading

class MenuApp:
    def _init_(self):
        # Inicializa o Pygame
        pygame.init()

        # Define as dimensões da janela
        self.largura = 1280
        self.altura = 720

        # Cria uma janela
        self.janela = pygame.display.set_mode((self.largura, self.altura))

        # Define o título da janela
        pygame.display.set_caption("Menu App")

        # Carrega os caminhos das imagens
        self.image_paths = {
            "MENU": "menu.jpg",
            "btn1": "btn1.jpg",
            "btn2": "btn2.png",
            "btn3": "btn3.jpg",
            "btn4": "btn4.jpg",
            "btn1_op1": "btn1_op1.png",
            "btn1_op2": "btn1_op2.png",
            "btn1_op3": "btn1_op3.png",
            "btn1_op4": "btn1_op4.png",
            "btn2_op1": "btn2_op1.png",
            "btn2_op2": "btn2_op2.png",
            "btn2_op3": "btn2_op3.png",
            "btn2_op4": "btn2_op4.png",
            "btn3_op1": "btn3_op1.png",
            "btn3_op2": "btn3_op2.png",
            "btn3_op3": "btn3_op3.png",
            "btn3_op4": "btn3_op4.png",
            "btn4_op1": "btn4_op1.png",
            "btn4_op2": "btn4_op2.png",
            "btn4_op3": "btn4_op3.png",
            "btn4_op4": "btn4_op4.png",
        }

        # Inicializa a porta serial
        self.serial_port = serial.Serial('COM11', 9600)  # Altere 'COM11' para a porta serial do seu Arduino

    def receive_message(self):
        while True:
            # Recebe a mensagem do Arduino
            message = self.serial_port.readline().strip().decode('utf-8')
            if message in self.image_paths:
                image_path = self.image_paths[message]
                self.show_image(image_path)

    def show_image(self, image_path):
        if image_path:  # Verifica se o caminho da imagem não está vazio
            # Carrega a imagem
            imagem = pygame.image.load(image_path)
            # Redimensiona a imagem para as dimensões da janela
            imagem = pygame.transform.scale(imagem, (self.largura, self.altura))
            # Exibe a imagem na janela
            self.janela.blit(imagem, (0, 0))
            # Atualiza a tela
            pygame.display.flip()
        else:
            print("Caminho da imagem não especificado.")

    def run(self):
        # Inicia o recebimento de mensagens do Arduino em uma thread
        pygame_thread = threading.Thread(target=self.receive_message)
        pygame_thread.daemon = True
        pygame_thread.start()

        # Loop principal do jogo
        executando = True
        while executando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    executando = False

        # Finaliza o Pygame
        pygame.quit()

if _name_ == "_main_":
    app = MenuApp()
    app.run()
