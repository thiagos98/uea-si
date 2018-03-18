#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int const tamHash = 787;
int const base = 128;
int const n0 = 48;
int const n1 = 49;
int const n2 = 50;
int const n3 = 51;
int const n4 = 52;
int const n5 = 53;
int const n6 = 54;
int const n7 = 55;
int const n8 = 56;
int const n9 = 57;

int gerarIntString(string numeroStr);
template <typename T>
class No {
private:
	T chave;
	No* esq;
	No* dir;
	No* pai;
public:
	No() {
		esq = NULL;
		dir = NULL;
		pai = NULL;
	}
	No(T chave) {
		this->chave = chave;
		esq = NULL;
		dir = NULL;
		pai = NULL;
	}
	T getChave();
	No* getEsq();
	No* getDir();
	No* getPai();
	void setChave(T);
	void setEsq(No<T>*);
	void setDir(No<T>*);
	void setPai(No<T>*);
};

template <typename T>
T No<T>::getChave() {
	return chave;
}

template <typename T>
No<T>* No<T>::getEsq() {
	return esq;
}

template <typename T>
No<T>* No<T>::getDir() {
	return dir;
}

template <typename T>
No<T>* No<T>::getPai() {
	return pai;
}

template <typename T>
void No<T>::setChave(T x) {
	this->chave = x;
}

template <typename T>
void No<T>::setEsq(No<T>* esq) {
	this->esq = esq;
}

template <typename T>
void No<T>::setDir(No<T>* dir) {
	this->dir = dir;
}

template <typename T>
void No<T>::setPai(No<T>* pai) {
	this->pai = pai;
}

template <typename T>
class ABB_AVL {
private:
	No<T>* raiz;
	bool buscaABB(T&, No<T>*);
	void preOrdemABB(No<T>*);
	void ordemSimetricaABB(No<T>*);
	void posOrdemABB(No<T>*);
	void insereABB(T);
	//void removeABB(T&, No<T>*);

public:
	ABB_AVL() {
		criaABB();
	}

	void criaABB() {
		raiz = NULL;
	}
	bool busca(T& chave) {
		bool achado = buscaABB(chave, this->getRaiz());
		return achado;
	}
	void insere(T x) {
		insereABB(x);
	}

	//void remove(T&);
	void preOrdem() {
		preOrdemABB(raiz);
	}
	void ordemSimetrica() {
		ordemSimetricaABB(raiz);
	}
	void posOrdem() {
		posOrdemABB(raiz);
	}

	void processaItem(T x) {
		cout << x << "   ";
	}
	No<T>* getRaiz() {
		return raiz;
	}

};

template <typename T>
bool ABB_AVL<T>::buscaABB(T& x, No<T>* p) {
	/*if (p == NULL) {
		return false;
	} else if (x > p->getChave()) {
		buscaABB(x, p->getDir());
	} else if (x < p->getChave()) {
		buscaABB(x, p->getEsq());
	} else {
		x = p->getChave();
		return true;
	}
	//return 0;*/
	if(this->getRaiz() == NULL){
		return false;
	}
	No<T>* atual = this->getRaiz();
	while(atual != NULL){
		if(x == atual->getChave()){
			return true;
		}
		if(x > atual->getChave()){atual = atual->getDir();}
		else{atual = atual->getEsq();}
	}
	return false;
}

template <typename T>
void ABB_AVL<T>::preOrdemABB(No<T>* p) {
	if (p == NULL)
		return;
	else {
		processaItem(p->getChave());
		preOrdemABB(p->getEsq());
		preOrdemABB(p->getDir());
	}
}

template <typename T>
void ABB_AVL<T>::ordemSimetricaABB(No<T>* p) {
	if (p == NULL)
		return;
	else {
		ordemSimetricaABB(p->getEsq());
		processaItem(p->getChave());
		ordemSimetricaABB(p->getDir());
	}
}

template <typename T>
void ABB_AVL<T>::posOrdemABB(No<T>* p) {
	if (p == NULL)
		return;
	else {
		posOrdemABB(p->getEsq());
		posOrdemABB(p->getDir());
		processaItem(p->getChave());
	}
}

template <typename T>
void ABB_AVL<T>::insereABB(T x) {
	if (this->getRaiz() == NULL) {
		raiz = new No<T>(x);
	} else {
		No<T>* corrente = this->getRaiz();
		No<T>* anterior = NULL;
		while (corrente != NULL) {
			anterior = corrente;
			if (x > corrente->getChave()) {
				corrente = corrente->getDir();
			} else {
				corrente = corrente->getEsq();
			}
		}
		if (x > anterior->getChave()) {
			anterior->setDir(new No<T>(x));
		} else {
			anterior->setEsq(new No<T>(x));
		}
	}
}

template <typename T>
class Hash {
private:
	ABB_AVL<T>* abb;
public:
	Hash(int TAM) {
		abb = new ABB_AVL<T>[TAM];
	}
	int calculoHash(int num) {
		return num % tamHash;
	}
	void insere(T);
	void printTableHash();
};

template <typename T>
void Hash<T>::insere(T numero){
	int numeroConvertido = gerarIntString(numero);
	int posHash = calculoHash(numeroConvertido);

	if(!abb[posHash].busca(numero)){
		abb[posHash].insere(numero);
	}
}

template <typename T>
void Hash<T>::printTableHash(){
	int i;
	for(i = 0;i < tamHash;i++){
		cout << "[" << (i+1) << "]: ";
		abb[i].ordemSimetrica();
		cout << endl;
	}
}

void acrescentarZeros(string& num) {
	if (num.size() < 4) {
		while (num.size() < 4) {
			num = "0" + num;
		}
	}
}
int potencia(int base,int exp){
	if(base == 0){
		return 0;
	} else if(exp == 0){
		return 1;
	} else if(exp == 1){
		return base;
	} else if(exp > 1){
		return base * potencia(base,exp - 1);
	}
	return 0;
}
void verificarAscii(int& numero){
	if(numero == 0){numero = n0;}
	else if(numero == 1){numero = n1;}
	else if(numero == 2){numero = n2;}
	else if(numero == 3){numero = n3;}
	else if(numero == 4){numero = n4;}
	else if(numero == 5){numero = n5;}
	else if(numero == 6){numero = n6;}
	else if(numero == 7){numero = n7;}
	else if(numero == 8){numero = n8;}
	else if(numero == 9){numero = n9;}

}
int gerarIntString(string numeroStr) {
	int numeroInterpretado = 0;
	int exp = 3;
	int soma = 0;
	for (unsigned int i = 0; i < numeroStr.size(); i++) {
		int numero = int(numeroStr[i]);
		verificarAscii(numero);
		soma = numero*potencia(base,exp);
		numeroInterpretado += soma;
		exp--;
	}
	return numeroInterpretado;
}


int main(int argc, char** argv) {
	Hash<string> tableHash(tamHash);

	ifstream infile;
	infile.open("chaves.txt");

	string numero;
	while (!infile.eof()) {
		infile >> numero;
		acrescentarZeros(numero);
		tableHash.insere(numero);
	}

	tableHash.printTableHash();

	string entrada;
	cin >> entrada;

	return 0;
}
