#include<iostream>
using namespace std;

typedef int Chave;
typedef int Posicao;

// Item
class Codigo
{
private:
	Chave indice;
	string conteudoLinha;
public:
	Codigo() {}
	Codigo(Chave indice,string contLinha)
	{
		this->indice = indice;
		this->conteudoLinha = contLinha;
	}
	Chave getIndice();
	string getConteudo();
	void setIndice(Chave);
	void setConteudo(string);
	void print();
};

string Codigo::getConteudo()
{
	return conteudoLinha;
}

Chave Codigo::getIndice()
{
	return indice;
}
void Codigo::setConteudo(string conteudo){
	this->conteudoLinha = conteudo;
}
void Codigo::setIndice(Chave index){
	this->indice = index;
}
void Codigo::print()
{
	cout << indice;
	cout << conteudoLinha << endl;
}

template <typename T>
class Lista
{
private:
	T *item; 
	int tamVetor;
	int tamLista; // tamanho corrente da lista
	bool vazia();
public:
	Lista() {}

	Lista(int tam)
	{
		tamLista = 0;
		tamVetor = tam;
		item = new T[tamVetor];
	}
	int getTamVet(){
		return tamVetor;	
	}
	int getTamListaa(){
		return tamLista;
	}
	T getItem(){
		return item;
	}
	
	void insere(T);
	void print();
	T* busca(Chave);
};


template <typename T>
void Lista<T>::insere(T codigo)
{
	if (tamLista < tamVetor)
	{
		tamLista++;
		item[tamLista] = codigo;
	}
	else
	{
		//cout << "Lista cheia!\n";
	}
}

template <typename T>
void Lista<T>::print()
{
	for (int i = 1; i <= tamLista; i++)
	{
		item[i].print();
		//cout << endl;
	}
}

template <typename T>
T* Lista<T>::busca(Chave descricao)
{
	item[0].setIndice(descricao); // sentinela
	int i = tamLista;
	while (descricao != item[i].getIndice())
	{
		i--;
	}
	if (i > 0) return &item[i];
	else return NULL;
}


template <typename T>
bool Lista<T>::vazia()
{
	return tamLista == 0;
}

template <typename T>
class No
{
private:
	T numero;
	No *prox;
public:
	No()
	{
		prox = NULL;
	}
	No* getProx()
	{
		return prox;
	}
	void setProx(No *prox)
	{
		this->prox = prox;
	}
	T getNumero()
	{
		return numero;
	}
	void setNumero(T numero)
	{
		this->numero = numero;
	}
};


template <typename T>
class Pilha
{
private:
	No<T> *topo, *fundo;
public:
	Pilha<T>()
	{
		fundo = new No<T>();
		fundo->setProx(NULL);
		topo = fundo;
	}
	bool vazia();
	void empilha(int);
	void desempilha(int&);
	void mostrarPilha();
};

template <typename T>
bool Pilha<T>::vazia(){
	return fundo == topo;
}

template <typename T>
void Pilha<T>::empilha(int numero)
{
	No<T> *aux = new No<T>();
	topo->setNumero(numero);
	aux->setProx(topo);
	topo = aux;
}

template <typename T>
void Pilha<T>::desempilha(int& numero)
{
	No<T> *aux = topo;
	topo = topo->getProx();
	numero = topo->getNumero();
	delete aux;
}
template <typename T>
void Pilha<T>::mostrarPilha()
{
	cout << endl;
	for (No<T> *nav = topo->getProx(); nav != NULL; nav = nav->getProx())
	{
		nav->getNumero().print();
	}
}


class InterpretadorNi {
private:
	Lista<Codigo> codigoEntrada;
	Pilha<int> pilha;
	string resultadoFinal;
	//int posZ;
	Posicao posFimZ;
public:
	InterpretadorNi(Lista<Codigo> codigoEntrada,Pilha<int> pilha){
		this->codigoEntrada = codigoEntrada;
		this->pilha = pilha;
	}
	
	Posicao getFimZ(){
		return posFimZ;
	}
	
	void inserirCodigoLista();
	void concatenarPrint(string);		
	void percorrerZ();
	void percorrerFuncoes(Posicao);
	void printarResultado();
	
};

void InterpretadorNi::printarResultado(){
	cout << resultadoFinal << endl;
}

void InterpretadorNi::inserirCodigoLista(){
	string linha = "";
	Codigo cod;
	int cont=1;
	while(getline(cin, linha) && linha != "~"){
		cod.setConteudo(linha);
		cod.setIndice(cont);
		codigoEntrada.insere(cod);
		/*if(linha == "Z :"){
			posZ = cont;
		}*/
		cont++;
	}
}

void InterpretadorNi::concatenarPrint(string linha){
	if(linha.size() == 11){
		resultadoFinal = resultadoFinal + linha[10] + " ";	
	} else if(linha.size() == 12){
		resultadoFinal = resultadoFinal + linha[10] + linha[11] + " ";
	}
}
void InterpretadorNi::percorrerZ(){
	Codigo* linha;
	//Codigo* teste;
	int posZ;
	int i,j;
	for(i = 1;i <= codigoEntrada.getTamListaa();i++){	
		linha = codigoEntrada.busca(i);
		if(linha->getConteudo() == "Z :"){
			posZ = i;
			j = i+1;
			do{
				linha = codigoEntrada.busca(j);		
				if(linha->getConteudo() == ""){
		   	   		j--;
					posFimZ = j;
					break;
	        	}
	        	j++;
			} while(linha->getConteudo() != "");
			break;
		}
	}
	
	Codigo* linhaSeguinte;
	for(i = posZ+1;i <= posFimZ;i++){
		linha = codigoEntrada.busca(i);
		int pos = linha->getIndice()+1;
		if(linha->getConteudo().size() == 5){
			linhaSeguinte = codigoEntrada.busca(linha->getIndice()+1);
			pilha.empilha(linhaSeguinte->getIndice()+1);			
			percorrerFuncoes(linha->getIndice());
			break;
		} else if(linha->getConteudo().size() >= 11){
			concatenarPrint(linha->getConteudo());			
		}
	}
}
void InterpretadorNi::percorrerFuncoes(Posicao pos){
	Codigo* linhaFuncao;
	int posicao;
	while(!pilha.vazia() && (linhaFuncao->getIndice() != this->getFimZ())){
		linhaFuncao = codigoEntrada.busca(pos);
		if(linhaFuncao->getConteudo().size() == 5){
			if(linhaFuncao->getConteudo() != ""){
				pilha.empilha(linhaFuncao->getIndice()+1);	
			}
			
			for(int i = 1;i <= codigoEntrada.getTamListaa();i++){
				Codigo* linha;
				linha = codigoEntrada.busca(i);
				if(linha->getConteudo()[0] == linhaFuncao->getConteudo()[4]){
					percorrerFuncoes(linha->getIndice());							
				}
			}
		} else if(linhaFuncao->getConteudo().size() >= 11){
			concatenarPrint(linhaFuncao->getConteudo());
		} else if(linhaFuncao->getConteudo() == "" && (!pilha.vazia())){
			posicao = linhaFuncao->getIndice();
			pilha.desempilha(posicao);
			percorrerFuncoes(posicao);
		}
		pos++;
	}
}

int main(int argc, const char * argv[])
{
	int const MAX =200;
	//unsigned int const TAMCHAMADAFUNCAO = 5;
 	//unsigned int const TAMPRINT = 11;
	//unsigned int const TAMDECFUNCAO = 3;
	
	Lista<Codigo> codigoEntrada(MAX);
	Pilha<int> pilha;
	InterpretadorNi interpretador(codigoEntrada,pilha);
	
	interpretador.inserirCodigoLista();
	interpretador.percorrerZ();
	
	interpretador.printarResultado();
	
	return 0;
}
