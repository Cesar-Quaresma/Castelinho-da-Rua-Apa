print("\033[4:37m  Fazendo deliberações iniciais sobrevindas à esse projeto, à muito trata-se tão apenas de uma criação \nem meio há uma situação hipotética e inexistênte, para fins tão somente da exposição de conhecimentos estudados,\nbem como direcionados aos ensinamentos dentro da área de Programação.\n  Muito embora, no que se refere ao presente projeto e, mesmo que feito de maneira simples (e por um iniciante no caso), \no mesmo carrega um pesado fardo em expor acontecimentos tendo estes ocorridos acerca em um cruzamento, pela Avenida São \nJoão em São Paulo (SP), no dia 12 de maio de 1937.")
print("\033[0:31m caso real:\033[0:33m Tendo a localização na região central de São Paulo, o \033[1:34mCastelinho da Rua Apa\033[0:33m, construida sob influência \n'medieval francês' em cerca de 5 anos em construção,fora palco de mortes e mistérios obscuros até os dias presentes. \nÁlvaro de 45 anos, na versão oficial dos fatos, - e duvidosa segundo os legistas - após uma discussão sobre negócios de \nenvolvimento familiar, o impulsionou a assassinar seu próprio irmão Armando de 43 anos de idade,\ne sua própria mãe, Maria Cândida de 73 anos, tendo depois praticado o suicidado, com o sublinhar de que \ntodos os fatos ora ocorridos e restritos foram concluídos 'dentro' do Castelinho Da Rua Apa.\nTrês pessoas foram encontradas mortas naquela noite,e como prova: uma pistola automática Parabellum calibre 9,\nque segundo os médicos e legistas, apontaram falhas sob o laudo da policia da época, mirando-se em Armando como autor \ndos disparos. Segundo a perícia original, Álvaro teria se suicidado com '2(dois) tiros no peito' (isso mesmo). Ainda, porém as balas no corpo \nde Maria Cândida não teriam sido providas da mesma pistóla, e sim, de outra arma, dando margem para mais uma quarta pessoa na cena do crime. E desconhecida. \n Os três morreram um ao lado do outro, estranhamente.")
print("\033[0:31m fatos estranhos: \033[0:32m Fatos assustadores como incendios; gritos de: '- Foi ele!', também como: '- Procure..', ou:\n'- ..Pare!', ouvidas aos sons de uma mulher, à tambêm aparições de um rosto colado no vidro da janela do Castelo, \nsão relatos corriqueiros no local. Moradores de rua após habitarem o Castelinho, em meio as pressas se afastaram do local, \ntendo os relatado em desfavor ao ambiênte desgradavel à um nível extremo, atribuidas como tal sensação sobrevindas \nao próprio local, aponto de pelo fato de exalar algo ruim, à classificaram-na como tendo uma vida própria, aponto de buscarem um outro abrigo.")
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