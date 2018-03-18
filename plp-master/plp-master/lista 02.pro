1)
pai(joão,joaquim).
pai(joão,joaquina).
pai(joaquim,marina).
pai(joaquim,martinha).
pai(armando,hugo).
pai(armando,artur).
pai(armando,balbina).
pai(justino,alcides).
pai(andré,jorge).
pai(jorge,alcineia).
pai(alcides,augusta).


mãe(maria,joaquim).
mãe(maria,joaquina).
mãe(andreia,marina).
mãe(andreia,martinha).
mãe(joaquina,hugo).
mãe(joaquina,artur).
mãe(joaquina,balbina).
mãe(martinha,alcides).
mãe(balbina,jorge).
mãe(alcineia,estevão).
mãe(gilda,augusta).

homem(joão).
homem(joaquim).
homem(armando).
homem(justino).
homem(andré).
homem(jorge).
homem(alcides).
homem(hugo).
homem(artur).
homem(estevão).

mulher(maria).
mulher(joaquina).
mulher(andreia).
mulher(marina).
mulher(martinha).
mulher(alcineia).
mulher(balbina).
mulher(gilda).
mulher(augusta).


casado(joão,maria).
casado(armando,joaquina).
casado(joaquim,andreia).
casado(andré,balbina).
casado(justino,martinha).
casado(alcides,gilda).

%REGRAS

irmão(A,B):- homem(A), pai(X,A),pai(X,B), (A\==B).
irmã(A,B):- mulher(A), mãe(X,A), mãe(X,B),(A\==B).
tio(A,B):- homem(A),(pai(Z,B);mãe(Z,B)), irmão(A,Z).
tia(A,B):- mulher(A),(pai(Z,B);mãe(Z,B)),irmã(A,Z).
avô(A,B):- homem(A), pai(A,X), pai(X,B),tio(X,B),tia(X,B).
avó(A,B):- mulher(A),mãe(A,X),mãe(X,B).
primo(A,B):- homem(A),(mãe(Z,A);pai(Z,A)), (tia(Z,B);tio(Z,B)).
sogra(A,B):- mulher(A),mãe(A,Z),(casado(Z,B); casado(B,Z)).%para determinar a nora
sogro(A,B):- homem(A) , pai(A,Z),(casado(Z,B); casado(B,Z)).
nora(A,B):- mulher(A), (sogro(B,A);sogra(B,A)).
neto(A,B):- homem(A), (avô(B,A);avó(B,A)).


2)
A-
informa_classe(S,'D') :- (S =< 700).
informa_classe(S,'C') :- (S > 700),(S =< 3500).
informa_classe(S,'B') :- (S > 3500),(S =< 9500).
informa_classe(S,'A') :- (S > 9500).
B)
soma([],0).
soma([C|L], V) :- soma(L, V2), V is V2 + C.
C)
cubo:-write('Digite o numero: '),read(X),imp(X).
imp(fim) :- !,write('Fim de Processamento'). %encerra o processamento se for digitado fim
imp(Z):-VARIAVEL is  (Z*Z*Z),write('O cubo do número é :'),write(VARIAVEL),nl,cubo. % calcula o cubo do número, caso não for digitado fim.

D)
inserir(X,L,[X|L]).

// verifica se na 2 tá tudo certo ai manow, a 1 tb se tu poderes
