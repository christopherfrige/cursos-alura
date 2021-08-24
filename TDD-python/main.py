from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

chris = Usuario("Chris")
leticia = Usuario("Leticia")

lance_leticia = Lance(leticia, 300.0)
lance_chris = Lance(chris, 100.0)

leilao = Leilao("PC Gamer")

leilao.lances.append(lance_chris)
leilao.lances.append(lance_leticia)

for lance in leilao.lances:
    print(f"O usuario {lance.usuario.nome} deu um lance de {lance.valor}")

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f"O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}")
