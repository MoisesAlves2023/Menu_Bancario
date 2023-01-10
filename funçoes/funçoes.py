def subtitulos_tabela(arquivo):
    for linha in arquivo:
        data = linha.split(',')[0]
        categoria = linha.split(',')[1]
        centrodecusto = linha.split(',')[2]
        descriçao = linha.split(',')[3]
        açao = linha.split(',')[4]
        status = linha.split(',')[5]
        observaçao = linha.split(',')[6]
        responsavel = linha.split(',')[7]



def passar_dados():
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