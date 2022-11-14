print("Bem-vindos a caixa de ferramentas.")
cadeia = input("Insira a cadeia de DNA a ser analisada: ").upper()
print("A cadeia a ser analisada é:", cadeia)


def principal():
    opcoes()
    n = int(input("Selecione o número da função a ser realizada: "))
    print("A função selecionada foi a:", n)
    if n == 1:
        contar_base()
        continuar()
    if n == 2:
        localizar_subcadeia()
        continuar()
    if n == 3:
        inverter_cadeia()
        continuar()
    if n == 4:
        cadeia_pareada()
        continuar()
    if n == 5:
        dimero_timina()
        continuar()
    if n == 6:
        print("Obrigado por usar a caixa de ferramentas.")


def opcoes():
    print("1 - Contar a quantidade de uma dada base de uma cadeia")
    print("2 - Localizar uma subcadeia em uma cadeia")
    print("3 - Inverter a cadeia / veriricar se a cadeia é palíndroma")
    print("4 - Criar uma cadeia pareada correspondente à cadeia dada")
    print("5 - Reparar os dímeros de timina na cadeia")
    print("6 - Sair da caixa de ferramentas")


def continuar():
    print("Deseja selecionar outra função?")
    sn = input("Selecione S para SIM e N para NÃO: ").upper()
    if sn == "S":
        principal()
    if sn == "N":
        print("Obrigado por usar a caixa de ferramentas.")


def contar_base():
    print("Na cadeia inserida existem:")
    print(cadeia.count("A"), "bases A")
    print(cadeia.count("C"), "bases C")
    print(cadeia.count("G"), "bases G")
    print(cadeia.count("T"), "bases T")


def localizar_subcadeia():
    subcadeia = input("Selecione a subcadeia para a contagem: ").upper()
    contagem = cadeia.count(subcadeia)
    print("Existem", contagem, "subacadeias na cadeia dada.")


def inverter_cadeia():
    invertida = cadeia[::-1]
    print("A cadeia invertida é:", invertida)
    if invertida == cadeia:
        print("A cadeia é palíndroma.")
    else:
        print("A cadeia não é palíndroma")


def cadeia_pareada():
    pareada1 = cadeia.replace("A", "1").replace("T", "2").replace("C", "3").replace("G", "4")
    pareada2 = pareada1.replace("1", "T").replace("2", "A").replace("3", "G").replace("4", "C")
    print("A cadeia pareada a cadeia selecionada é", pareada2)


def dimero_timina():
    dimero = cadeia.find("TT")
    if dimero == -1:
        print("Essa cadeia não possui dímero de timina. ")
    else:
        print("Essa cadeia possui dímero de timina.")
        nova = cadeia.replace("TT", "__")
        print("A cadeia que irá ser reparada sem o dímero de timina é", nova)


principal()