print("\033[4:37m  Fazendo deliberações iniciais sobrevindas à esse projeto, trata-se de apenas uma criação \nem uma situação hipotética e inexistênte, para fins tão somente da exposição de conhecimentos estudados,\ndirecionados aos ensinamentos dentro da área de Programação.\n Muito embora, no que se refere ao presente projeto e mesmo que feito de maneira simples e por um iniciante, \n este projeto carrega um pesado fardo em expor acontecimentos,\n ocorridos acerca em um cruzamento pela Avenida São João em São Paulo (SP), no dia 12 de maio de 1937.")
print("\033[0:31m caso real:\033[0:33m Tendo localização na região central de São Paulo, o \033[1:34mCastelinho da Rua Apa\033[0:33m,\n dentro de uma influência 'medieval francês' e cerca de 5 anos sob construção,\nfora palco de mortes e mistérios obscuros até os dias presentes. \nÁlvaro de 45 anos, na versão oficial dos fatos, - e duvidosa segundo os legistas - apos uma discussão \nsobre negócios de envolvimento familiar, assassinou o seu próprio irmão, Armando de 43 anos de idade, e sua própria mãe \nMaria Cândida de 73 anos, e depois praticado suicidado tudo adentrado ao Castelinho Da Rua Apa.\nTrês pessoas foram encontradas mortas naquela noite,e como prova: uma pistola automática Parabellum calibre 9,\nque no qual segundo médicos e legistas apontaram falhas no laudo da policia da época, mirando se em Armando como autor \ndos disparos.Mas,as balas no corpo de Maria Cândida não teriam sido providas da mesma pistóla e sim, de\noutra arma, dando à abertura para mais uma quarta pessoa na cena do crime, e desconhecida. \n Os três morreram um ao lado do outro, estranhamente.")
print("\033[0:31m fatos estranhos: \033[0:32m Fatos assustadores como incendios, gritos de: '- Foi ele!', também como: '- Procure..', ou: '- Pare!', ouvidos aos sons da voz de uma mulher,à aparições de um rosto colado no vidro da janela do Castelo, são\n relatos corriqueiros no local. Moradores de rua, após viverem alí, se afastaram relatando sobre o ambiênte desgradavel à um \nnível extremo do Castelinho, aponto de buscarem outro abrigo. ")
print("\033[0:31m Muito Bêm!\nVocês farão uma expedição nesse local!")
print("\033[0:34m Seguem se o regramento para a Expedição: \nA - Terão que ter formação em fila, e em um total de 10 pessoas ao todo.")
print("B - Se organizarão em grupo de Pares entre Homens e Mulheres, formando duplas - tudo em nome da igualdade, sem dar predileções a quêm quer que seja.")
print("C - Sendo o número de homens ou mulheres superior ao sexo oposto ora como acompanhante, um dos grupos (de homens ou mulheres) terão que esperar \no retorno de um outro par, para que algum membro deste e do sexo oposto à este, possa agora fazer a função de acompanhante à aquele que ficou na espera!")
print("D - A atribuição do tempo estimado para permanência no local estipulado, será de '66 minutos por par', \nem decorrência ao risco de pessoas terem mal súbito no local.\033[0:38m")
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
print("\033[4:33m Hoje, o Castelinho Da Rua Apa virou uma instituição apoio as pessoas necessitadas.")
print("\033[0:34mPorém os fatos verídicos fazem parte de sua história. É mal assombrado? Pois bêm:\nÉ VOCÊ quem será o novo contador, dessa história!\nBOA SORTE!")