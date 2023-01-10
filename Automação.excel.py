import pyautogui as pg
from time import sleep
pg.PAUSE = 0.5

pg.alert("O código vai começar, não faça nada ate o código terminar!!")

# 1- apertar a tecla win
pg.press("winleft")
sleep(0.5)
# 2- digitar excel
pg.write("Excel")
sleep(1)

# 3- apertar enter pra acessar o excel
pg.press("enter")
sleep(5)

# 4- apertar esc pra fechar msgs e abrir um arquivo novo
pg.press("esc")
sleep(0.5)
pg.press("esc")
sleep(0.5)

# 5- clicar no tamanho da fonte e escolher o tamanho
pg.click(239, 86)
pg.write("18")
sleep(0.5)

# 6- clicar na primeira coluna
pg.click(71, 238)

# 7- digitar o titulo
pg.write("BANCO DE ANOMALIAS")
sleep(0.5)
pg.press("tab")

#8-mesclar e centralizar o titulo
pg.mouseDown(53, 236)
pg.moveTo(589, 236, duration = 1)
pg.mouseUp
pg.click(530, 120)
pg.click(530, 120)
sleep(0.5)
pg.press("enter")
sleep(0.5)

#informaçoes da tabela
pg.write("Data")
sleep(0.5)
pg.press("tab")
sleep(0.5)
pg.write("Categoria")
sleep(0.5)
pg.press("tab")
sleep(0.5)
pg.write("Centro de Custo")
sleep(0.5)
pg.press("tab")
sleep(0.5)
pg.write("Descricao da Anomalia")
sleep(0.5)
pg.press("tab")
sleep(0.5)
pg.write("Acao Imediata")
sleep(0.5)
pg.press("tab")
sleep(0.5)
pg.write("Status")
sleep(0.5)
pg.press("tab")
sleep(0.5)
pg.write("Observacao")
sleep(0.5)
pg.press("tab")
sleep(0.5)
pg.write("Responsavel")
pg.press("enter")

#mudar o tamanho da fonte da tabela
pg.mouseDown(53, 236)
sleep(1)
pg.moveTo(545, 267)
sleep(1)
pg.mouseUp(545, 267)
pg.click(239, 86, duration = 1)
pg.write("15")

#alinhar corretamente
pg.click(15, 215)
pg.doubleClick(155, 212, duration = 1)

#colocar bordas na tabela
pg.mouseDown(43, 236)
pg.moveTo(45, 624)
pg.mouseUp(45, 624)
pg.press("alt")
sleep(0.5)
pg.press("c")
sleep(0.5)
pg.press("b")
sleep(0.5)
pg.press("t")
sleep(0.5)

#colorir a tabela
pg.click(44, 235)
pg.click(273, 118)
pg.click(341, 275)
sleep(1)
pg.mouseDown(46, 261)
pg.moveTo(854, 260)
pg.mouseUp(773, 260)
pg.click(273, 118)
pg.click(291, 178)
sleep(0.3)
pg.click(46, 284)
sleep(0.5)

#abrir texto e passar pra planilha
with open('problemas.txt','r') as arquivo:
    for linha in arquivo:
        data = linha.split(',')[0]
        categoria = linha.split(',')[1]
        centrodecusto = linha.split(',')[2]
        descriçao = linha.split(',')[3]
        açao = linha.split(',')[4]
        status = linha.split(',')[5]
        observaçao = linha.split(',')[6]
        responsavel = linha.split(',')[7]
        
        #passando pra tabela
        pg.write(data)
        pg.press("tab")
        #sleep(0.5)
        pg.write(categoria)
        pg.press("tab")
        #sleep(0.5)
        pg.write(centrodecusto)
        pg.press("tab")
        #sleep(0.5)
        pg.write(descriçao)
        pg.press("tab")
        #sleep(0.5)
        pg.write(açao)
        pg.press("tab")
        #sleep(0.5)
        pg.write(status)
        pg.press("tab")
        #sleep(0.5)
        pg.write(observaçao)
        pg.press("tab")
        #sleep(0.5)
        pg.write(responsavel)        
        sleep(0.5)


#salvar na area de trabalho
pg.hotkey("ctrl","b")
pg.click(246, 340)
pg.click(77, 145)
sleep(0.5)
pg.click(409,344)
sleep(0.3)
pg.write("Anomalia")
sleep(0.3)
pg.click(560, 473)

pg.alert("O Codigo acabou!")

