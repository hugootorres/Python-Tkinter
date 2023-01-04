import requests
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get(
        "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,ETH-BRL,GBP-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_libra = requisicao_dic['GBPBRL']['ask']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']
    cotacao_eth = requisicao_dic['ETHBRL']['ask']

    texto = f'''
    Dólar: R$ {cotacao_dolar}
    Euro: R$ {cotacao_euro}
    Libra: R$ {cotacao_libra}
    BTC: R$ {cotacao_btc}
    ETH: R$ {cotacao_eth}'''

    texto_cotacoes["text"] = texto


janela = Tk()
janela.title("Cotação Atual de Moedas")  # titulo da janela
# janela.geometry("295x250")
sw = janela.winfo_screenwidth()  # comando para centralizar a janela no app
sh = janela.winfo_screenheight()
ww = 310
wh = 250
x = (sw - ww) / 2
y = (sh - wh) / 2
janela.geometry("%dx%d+%d+%d" % (ww, wh, x, y))


texto_orientacao = Label(
    janela, text="Clique no botão para ver as cotações das moedas")
texto_orientacao.grid(column=0, row=0, padx=20, pady=10)

botao = Button(janela, text="Buscar Cotações", bg="gray",
               fg="white", width=30, height=2, command=pegar_cotacoes)
# pad é os espacamentos entre o eixo X e Y #ipad tamanho do botao
botao.grid(column=0, row=1, padx=10, pady=10)
# botao.pack(side = BOTTOM)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
