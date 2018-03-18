nota1=float(input("1o Bimestre:"))
nota2=float(input("2o Bimestre:"))
nota3=float(input("3o Bimestre:"))
nota4=float(input("4o Bimestre:"))
media=(nota1+nota2+nota3+nota4)/4
print("Media Anual:",media)
if (media>7):
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado")
