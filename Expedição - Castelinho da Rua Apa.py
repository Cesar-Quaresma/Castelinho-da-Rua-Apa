print("\033[4:37m Inicialmente, esse projeto é uma criação que aborda uma situação hipotética e visa, tão somente, exercitar\nos meus parcos conhecimentos sobre programação. 'Prima facie', ao iniciar esse projeto, sentimentos estranhos \nme acometeram durante minha narrativa sobre os acontecimento reais descritos logo abaixo. ")
print("\033[0:31m caso real:\033[0:33m O 'Castelinho', situado em um cruzamento da Avenida São João, na cidade de São Paulo, no ano de 1937, foi manchete \nde jornal em todo pais. \nConstruido sob influência medieval francês, o 'Castelinho' foi edificado em cinco anos e fora palco de mortes e mistérios no passado e \nhoje é tido como um dos lugares mais terrificanes do Brasil, quiça do mundo.\n Em 12 de maio de 1937, Álvaro, de 45 anos, após uma discussão sobre negócios de familia, foi tomado por impulsos \nsombrios e, segundo a versão oficial da época, assassinou seu próprio irmão Armando de 43 anos e sua mãe, Maria Cândida de 73,\nse dando, em seguida, '2 tiros' no peito, suicidando-se.\n A história conta que, 3 pessoas foram encontradas mortas naquela noite e, como prova, 'uma pistola automática \nparabellum - calibre 9'.\n  Sérias dúvidas remanescem até os dias de hoje sobre o laudo policial da época que apontava 'Armando' como autor \ndos disparos e vítima de suicídio, com '2' tiros no peito, isso mesmo - 'suicídio com 2 tiros no peito'.\n  Outra polêmica sobre o caso: os projéteis encontrados no corpo de Maria Cândida provinham de outra arma, nunca \nencontrada. Existiria uma quarta pessoa desconhecida envolvida nesse crime?\nCerto é que os 'três' foram encontrados um ao lado do outro, estranhamente, afastando a possibilidade de ter havido \numa luta corporal.Após este bárbaro acontecimento, o 'Castelinho' foi fechado por um longo tempo.")
print("\033[0:31m fatos estranhos: \033[0:32m Pessoas que lá estiveram relatam fatos estranhos e assustadores como gritos de uma mulher:'-Foi ele' ; \n'-Procure'; '-Pare'.Muitos, que lá estiveram, afirmam que terem presenciado 'aparições de um rosto colado no vidro de uma janela'.'Moradores de rua' que invadiram o 'Castelinho' para se abrigarem em noites de frio, ao se depararem com os acontecimentos \nestranhos fugiam em desabalada carreira e diziam que a 'casa' possuía 'vida própria'.\n  Enfim, o 'Castelinho' ficou conhecido como um lugar 'assombrado', despertando a atenção de todos. Alguns até tentaram \nrealizar produções cinematográficas no local e o resultado foi um incêndio misterioso e inexplicável.")
print("\033[0:31m Muito Bêm!\nVocês farão uma expedição à esse local!")
print("\033[0:34m Segue se o regramento para a Expedição abaixo:")
print("A-) De carater obrigatório, farão formação em fila, em um total de 10 pessoas;")
print("B-) Se organizarão em grupo de Pares entre Homens e Mulheres, formando duplas - tudo, em nome da igualdade, sem dar predile-\n-ções a quêm quer que seja;")
print("C-) Dando margem à suposta eventualidade de, caso o número de homens ou mulheres forem superior ao sexo oposto (ou ho-\n-mens, ou mulheres), à predisposição de acompanhante, um dos grupos (de homens ou mulheres) terão que esperar o retorno de um outro par,\n para que algum membro deste e do sexo oposto à 'este', possa agora fazer a função de o acompanhante 'à aquele' que ficou na espera;")
print("D-) A atribuição do tempo estimado da permanência ora equivalente 'aos riscos (segundo relatos de pessoas que entraram ao local) e \ninsalubridade' que de maneira inexperada, determinada pessoa sobrevenha à passar de mal-estares, o tempo será de '66 minutos por par', \nem decorrência aos riscos e também de históricos percorrentes de pessoas que já tiveram algum mal súbito no local.\033[0:38m")
homens = 0
mulheres = 0
for c in range(1,11):
  nome = str(input("Digite o nome: "))
  sexo = str(input("Digite o seu Sexo, entre 'M ou m', ou 'F ou f': ")).upper()
  if sexo in 'Mm':
    homens += 1
  elif sexo in 'Ff':
    mulheres += 1
if homens == mulheres:
    print(f"A quantidade entre Homens: {homens}, e Mulheres: {mulheres}, 'são iguais.' Podem Entrar!")
else:
    print("Nessa ocasião, a quantidade entre Homens: {}, e Mulheres: {}, são diferentes.\n Fiquem sob a espera de um acompanhante!".format(homens,mulheres))
print("\033[4:33m Hoje, o Castelinho Da Rua Apa virou uma instituição à apoio as pessoas necessitadas.")
print("\033[0:34mPorém os fatos verídicos fazem parte de sua história. \nÉ mal assombrado? Pois bêm:\nÉ VOCÊ quem será o novo contador, dessa história!\nBOA SORTE!")
