#imports
import qrcode
import random

#funcao que armazena a informacao que sera colocada no QrCode
informacao = input ('Digite o texto ou URL para virar Qr Code: ')
print (informacao) 

#funcao que gera chama o usuario para anotar um nome para o mesmo e gerar a imagem
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(informacao)
qr.make(fit=True)
nome = input ('Digite o nome do QrCode: ')

#Caso nome nao tenha sido deeterminado vai ser gerado um nome random entre esses 2 nomes
if nome == "":
    palavras = ['Qrcode','QRcode']
    nome = random.choice(palavras)

#parte responsavel por escolher a cor do seu qr code
cor_primaria = input ('Digite o nome da cor primaria: ')
cor_secundaria = input ('Digite o nome da cor secundaria: ')

#caso as cores sejam vazias sera gerado um qr code padrao preto e banco
if cor_primaria == "":
    cor_primaria = "black"

if cor_secundaria == "":
    cor_secundaria = "white"


img = qr.make_image(fill_color= cor_primaria, back_color= cor_secundaria)
img.save(nome +'.png')
print("Qr Code gerado com sucesso!!!")
