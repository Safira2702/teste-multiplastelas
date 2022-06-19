import PySimpleGUI as sg
ano = 0
idade = 0

def tela_inicio(): #tela 1
    layout = [
        [sg.Text('Bem vindo!')],
        [sg.Text('Essa é sua primeira habilitação?')],
        [sg.Button('Sim'), sg.Button('Não')]
    ]
    return sg.Window('Inicio', layout=layout, finalize=True)
def tela_cnh(): #tela 2
    layout = [
        [sg.Text('Coloque um ano válido de quando fez (de 2012 até 2022)')],
        [sg.Input(key='tempo')],
        [sg.Button('Continuar'), sg.Button('Voltar')]
    ]
    return sg.Window('CNH - Ano', layout=layout, finalize=True)
def tela_idade(): #tela 3
    layout = [
        [sg.Text('Coloque com quantos anos você fez sua carteira')],
        [sg.Input(key='age')],
        [sg.Button('Fim')]
    ]
    return sg.Window('CNH - Idade', layout=layout, finalize=True)

def tela_cnhnao(): #tela 4
    layout = [
        [sg.Text('Coloque um ano válido da sua última renovação (de 2012 até 2022)')],
        [sg.Input(key='tempo')],
        [sg.Button('Continuar'), sg.Button('Retornar')]
    ]
    return sg.Window('CNH - Idade', layout=layout, finalize=True)

def tela_idadenao(): #tela 5
    layout = [
        [sg.Text('Coloque com quantos anos você fez sua última renovação na carteira')],
        [sg.Input(key='agen')],
        [sg.Button('Fim')]
    ]
    return sg.Window('CNH - Idade', layout=layout, finalize=True)

janela1, janela2, janela3, janela4, janela5 = tela_inicio(), None, None, None, None

while True:
    window, event, values = sg.read_all_windows()
    #todas as janelas fechadas encerram o programa (exeto a 4)
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela2 and event == sg.WINDOW_CLOSED:
        break
    if window == janela3 and event == sg.WINDOW_CLOSED:
        break
    if window == janela4 and event == sg.WINDOW_CLOSED:
        break
    if window == janela5 and event == sg.WINDOW_CLOSED:
        break
    #apertou o botão sim
    if window == janela1 and event == 'Sim':
        janela2 = tela_cnh() #pergunta qual ano tu fez
        janela1.hide() #esconde a primeira tela
    #apertou o botão não
    if window == janela1 and event == 'Não':
        janela4 = tela_cnhnao() #pergunta qual ano tu renovou
        janela1.hide() #esconde a primeira tela
    #quando queremos ir para a janela anterior
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela4 and event == 'Retornar':
        janela4.hide()
        janela1.un_hide()
    #Ir para a verificação de um ano válido do botão sim
    if window == janela2 and event == 'Continuar':
        ano = int(values['tempo'])
        if 2023 > ano > 2011:
            janela2.hide()
            janela3 = tela_idade()
        else:
            sg.popup('Coloque um ano válido: de 2012 ate 2022')
            ano = 0
    #Ir para a verificação de um ano valido do botão não
    if window == janela4 and event == 'Continuar':
        ano = int(values['tempo'])
        if ano >= 2012 and ano < 2023:
            janela5 = tela_idadenao()
            janela4.hide()
        else:
            sg.popup('Coloque um ano válido: de 2012 ate 2022')
            ano = 0

    # verificação de quantos anos precisa renovar a carteira, botão não evento final
    if window == janela5 and event == 'Fim':
        idade = int(values['agen'])
        if 27 < idade <= 49:
            valor1 = ano + 10
            if valor1 < 2022:
                sg.popup('Você deverá tem que renovar a sua habilitação imedatiamente, '
                                    'pois está atrasada faz {NUM} anos!'.format(NUM=(valor1 - 2022) * -1))
                break
            else:
                sg.popup('Você deverá renovar sua habilitação em {NUM}!'.format(NUM=valor1))
                break
        elif 49 < idade < 69:
            valor1 = ano + 5
            if valor1 < 2022:
                sg.popup('Você deverá tem que renovar a sua habilitação imedatiamente,pois está atrasada faz '
                                  '{NUM} anos!'.format(NUM=(valor1 - 2022) * -1) +
                         'Você deverá renovar sua habilitação em {NUM}!'.format(NUM=valor1))
            elif idade >= 79:
                valor1 = ano + 3
                if valor1 < 2022:
                    sg.popup('Você deverá tem que renovar a sua habilitação imedatiamente, '
                                        'pois está atrasada faz {NUM} anos!'.format(NUM=(valor1 - 2022) * -1)
                             + 'Você deverá renovar sua habilitação em {NUM}!'.format(NUM=valor1))
        else:
            sg.popup('Insira uma idade válida (28 anos para cima)')
            idade = 0
    #verificação de quantos anos precisa renovar a carteira, botão sim evento final
    if window == janela3 and event == 'Fim':
        idade = int(values['age'])
        if 17 < idade < 50:
            valor1 = ano + 10
            if valor1 == 2022:
                sg.popup('Fique atento! Esse ano você precisará renovar sua carteira de motorista!')
                break
            if valor1 < 2022:
                sg.popup('Sua habilitação está vencida e não pode ser utilizada, '
                                   'faça a renovação IMEDIATAMENTE!')
                break
            else:
                sg.popup('Você deverá renovar sua habilitação em {NUM}!'.format(NUM=valor1))
                break
        elif 49 < idade < 69:
            valor1 = ano + 5
            if valor1 == 2022:
                sg.popup('Fique atento! Esse ano você precisará renovar sua carteira de motorista!')
                break
            if valor1 < 2022:
                sg.popup('Sua habilitação está vencida, faça a renovação IMEDIATAMENTE!')
                break
            else:
                sg.popup('Você deverá renovar sua habilitação em {NUM}!'.format(NUM=valor1))
                break
        elif idade >= 70:
            valor1 = ano + 3
            if valor1 == 2022:
                sg.popup('Fique atento! Esse ano você precisará renovar sua carteira de motorista!')
                break
            if valor1 < 2022:
                sg.popup('Sua habilitação está vencida, faça a renovação IMEDIATAMENTE!')
                break
            else:
                sg.popup('Você deverá renovar sua habilitação em {NUM}!'.format(NUM=valor1))
                break
        else:
            sg.popup('Coloque uma idade valida: maior de 18 anos')
            idade = 0