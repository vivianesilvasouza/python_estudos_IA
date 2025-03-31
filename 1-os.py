import os 


print(os.getcwd()) # diretório atual

print(os.listdir()) # lista de arquivos e pastas

os.system('ver') # versão do sistema operacional

os.system('systeminfo') # configuração da maquina 

os.system('cls') # limpar tela

# os.system('shutdown /s') # desligar o computador

# os.system('shutdown /s /t 60') # desligar o computador em 60 segundos

# os.system('shutdown /a') # cancelar desligamento

# os.system('shutdown /r') # reiniciar o computador


def turn_off():
    os.system('shutdown /s /t 3600') # desligar o computador em 1 hora
    
def turn_off_half_an_hour():
    os.system('shutdown /s /t 1800') # desligar o computador em 30 minutos
    
def cancel_shutdown():
    os.system('shutdown /a') # cancelar desligamento
