#include <iostream>
#include <fstream>

/*
	Equipe:
	Thiago Santos Borges - 1615310023
	Antonio Rodrigues de Souza Neto - 1615310028
	Bruno de Oliveira Freite - 1615310030

*/

using namespace std;
//   n0...n9 estão com seus respectivos valores conforme a tabela ASCII.
int const TAMHASH = 787;
int const BASE = 128;
int const N0 = 48;
int const N1 = 49;
int const N2 = 50;
int const N3 = 51;
int const N4 = 52;
int const N5 = 53;
int const N6 = 54;
int const N7 = 55;
int const N8 = 56;
int const N9 = 57;

int interpretarString(string numeroStr);
template <typename T>
class No {
private:
	T chave;
	int fe;//fator de equilibrio
	No* esq;
	No* dir;
	No* pai;
public:
	No() {
		this->fe = 0;
		this->esq = NULL;
		this->dir = NULL;
		this->pai = NULL;
	}
	No(T chave) {
		this->chave = chave;
		this->fe = 0;
		this->esq = NULL;
		this->dir = NULL;
		this->pai = NULL;
	}
	T getChave();
	int getFe();
	No* getEsq();
	No* getDir();
	No* getPai();
	void setChave(T);
	void setFe(int);
	void setEsq(No<T>*);
	void setDir(No<T>*);
	void setPai(No<T>*);

};
template <typename T>
int No<T>::getFe(){ return fe; }

template <typename T>
void No<T>::setFe(int fe){ this->fe = fe; }

template <typename T>
T No<T>::getChave() { return chave; }

template <typename T>
No<T>* No<T>::getEsq() { return esq; }

template <typename T>
No<T>* No<T>::getDir() { return dir; }

template <typename T>
No<T>* No<T>::getPai() { return pai; }

template <typename T>
void No<T>::setChave(T x) { this->chave = x; }

template <typename T>
void No<T>::setEsq(No<T>* esq) { this->esq = esq; }

template <typename T>
void No<T>::setDir(No<T>* dir) { this->dir = dir; }

template <typename T>
void No<T>::setPai(No<T>* pai) { this->pai = pai; }
///////////////////////////////////////////////////////////////////////////////

template <typename T>
class ABB_AVL {
private:
	No<T>* raiz;
	bool buscaABB(T&, No<T>*);
	void ordemSimetricaABB(No<T>*);
	bool insereABB(T);
	void balanceandoAVL(No<T>*);
public:
	ABB_AVL() { criaABB(); }

	No<T>* RSE(No<T>*);
	No<T>* RSD(No<T>*);
	No<T>* RDE(No<T>*);
	No<T>* RDD(No<T>*);
	int obterFE(No<T>*);
	int maior(int,int);
	void atualizarFE(No<T>*);
	
	bool busca(T& chave) {
		bool achado = buscaABB(chave, this->getRaiz());
		return achado;
	}
	void criaABB() { raiz = NULL; }
	void insere(T x) { insereABB(x); }
	void ordemSimetrica() { ordemSimetricaABB(raiz); }
	
	void processaItem(T x) { cout << x << " "; }
	No<T>* getRaiz() { return raiz; }
	void setRaiz(No<T>* raiz){ this->raiz = raiz; }
};

template <typename T>
void ABB_AVL<T>::atualizarFE(No<T>* p){
	p->setFe(obterFE(p->getDir()) - (obterFE(p->getEsq())));
}
template <typename T>
int ABB_AVL<T>::maior(int n1,int n2){
	if(n1 > n2){return n1;}
	else{return n2;}
}
template <typename T>
int ABB_AVL<T>::obterFE(No<T>* p){
	if(p == NULL){
		return -1;
	} 
	else {
		return maior(obterFE(p->getEsq()),obterFE(p->getDir())) + 1;
	}
}

template <typename T>
No<T>* ABB_AVL<T>::RSE(No<T>* p){
	No<T> *aux = p->getDir();
    aux->setPai(p->getPai());
    p->setDir(aux->getEsq());
    if(p->getDir() != NULL){
        p->getDir()->setPai(p);
	}
	aux->setEsq(p);
    p->setPai(aux);
    
    if(aux->getPai() != NULL) {
        if (aux->getPai()->getDir() == p) {
            aux->getPai()->setDir(aux);
        } 
		else {
            aux->getPai()->setEsq(aux);
        }
    }
    atualizarFE(p);
    atualizarFE(aux);
	return aux;
}

template <typename T>
No<T>* ABB_AVL<T>::RSD(No<T>* p){
	No<T>* aux = p->getEsq();
    aux->setPai(p->getPai());
    p->setEsq(aux->getDir());
    if(p->getEsq() != NULL){
        p->getEsq()->setPai(p);
	}
    aux->setDir(p);
    p->setPai(aux);
    
	if(aux->getPai() != NULL) {
        if(aux->getPai()->getDir() == p) { 
			aux->getPai()->setDir(aux); 
		} 
		else { 
			aux->getPai()->setEsq(aux); 
		}
    }
    atualizarFE(p);
    atualizarFE(aux);
    return aux;
}

template <typename T>
No<T>* ABB_AVL<T>::RDE(No<T>* p){
	p->setDir(RSD(p->getDir()));
    return RSE(p);
}

template <typename T>
No<T>* ABB_AVL<T>::RDD(No<T>* p){
	p->setEsq(RSE(p->getEsq()));
    return RSD(p);
}

template <typename T>
bool ABB_AVL<T>::insereABB(T chave){
	if (raiz == NULL){
        raiz = new No<T>(chave);
        raiz->setPai(NULL);
    } else{
        No<T>* p;
		No<T>* aux;
        p = raiz;
        do{
			aux = p;
			if(p->getChave() == chave){ return false; }
			bool teste;
			if(chave < p->getChave()){ 
				teste = true; 
			}
			else{ 
				teste = false; 
			}
			
			if(teste == true){ 
				p = p->getEsq(); 
			} 
			else{ 
				p = p->getDir(); 
			}
            
			if(p == NULL){
                if(teste == true){
                	No<T>* novo = new No<T>(chave);
                	novo->setPai(aux);
                    aux->setEsq(novo);
                } 
				else{
                	No<T>* novo = new No<T>(chave);
                	novo->setPai(aux);
                    aux->setDir(novo);
                }
                balanceandoAVL(aux);
                
            }
		}while(p!=NULL);
        	
    }

    return true;
}
template <typename T>
void ABB_AVL<T>::balanceandoAVL(No<T>* p){
	atualizarFE(p);
    if(p->getFe() == 2){
        if(obterFE(p->getDir()->getDir()) >= obterFE(p->getDir()->getEsq())){ 
			p = RSE(p); 
		}
		else{ 
			p = RDE(p);
		}
    } else if(p->getFe() == -2) {
        if(obterFE(p->getEsq()->getEsq()) >= obterFE(p->getEsq()->getDir())){
			p = RSD(p);
		} 
		else{
			p = RDD(p);
		}
    } 
    if(p->getPai() == NULL){
		raiz = p;
	} 
	else{
		balanceandoAVL(p->getPai());
	}
}
template <typename T>
bool ABB_AVL<T>::buscaABB(T& x, No<T>* p) {
	if(this->getRaiz() == NULL){
		return false;
	}
	No<T>* atual = this->getRaiz();
    while(atual != NULL){
		if(x == atual->getChave()){
			return true;
		}
		if(x > atual->getChave()) {
			atual = atual->getDir();
		}
		else{
			atual = atual->getEsq();
		}
	}
	return false;
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
class Hash {
private:
	ABB_AVL<T>* abb;
public:
	Hash(int TAM) {
		abb = new ABB_AVL<T>[TAM];
	}
	int calculoHash(int num) {
		return num % TAMHASH;
	}
	void insere(T);
	void printTableHash();
	void printPosHash(int);
	void buscarChave(int,T);
};

template <typename T>
void Hash<T>::insere(T numero){
	int numeroConvertido = interpretarString(numero);
	int posHash = calculoHash(numeroConvertido);
	abb[posHash].insere(numero);
}

template <typename T>
void Hash<T>::printTableHash(){
	int i;
	for(i = 0;i < TAMHASH;i++){
		cout << "[" << (i) << "]: ";
		abb[i].ordemSimetrica();
		cout << endl;
	}
}
template <typename T>
void Hash<T>::printPosHash(int posHash){
	abb[posHash].ordemSimetrica();
}
template <typename T>
void Hash<T>::buscarChave(int posHash,T chave){
	if(abb[posHash].busca(chave)){
		this->printPosHash(posHash);
	} 
	else {
		cout<<"Chave nÃ£o encontrada.";
	}
}

void acrescentarZeros(string& num) {
	if (num.size() < 4) {
		while(num.size() < 4) {
			num = "0" + num;
		}
	}
}
int potencia(int base,int exp){
	if(base == 0){
		return 0;
	} 
	else if(exp == 0){
		return 1;
	} 
	else if(exp == 1){
		return base;
	} 
	else if(exp > 1){
		return base * potencia(base,exp - 1);
	}
	return 0;
}
//Verifica o numero e modifica seu valor,conforme a sua correspondencia na ASCII.
void verificarAscii(int& numero){
	if(numero == 0){numero = N0;}
	else if(numero == 1){numero = N1;}
	else if(numero == 2){numero = N2;}
	else if(numero == 3){numero = N3;}
	else if(numero == 4){numero = N4;}
	else if(numero == 5){numero = N5;}
	else if(numero == 6){numero = N6;}
	else if(numero == 7){numero = N7;}
	else if(numero == 8){numero = N8;}
	else if(numero == 9){numero = N9;}

}

//interpretarString -> interpreta uma string e gera seu correspondente nos números naturais
//foi usado a base 128 para os cálculos
int interpretarString(string numeroStr) {
	int numeroInterpretado = 0;
	int expoente = 3;
	int soma = 0;
	for (unsigned int i = 0; i < numeroStr.size(); i++) {
		int numero = int(numeroStr[i]);
		verificarAscii(numero);
		soma = numero*potencia(BASE,expoente);
		numeroInterpretado += soma;
		expoente--;
	}
	return numeroInterpretado;
}
//Gera uma posição na hash conforme a entrada da chave.
int gerarPosEntrada(string numeroEntrada){
	int variavel = interpretarString(numeroEntrada);
	int calculo = variavel % TAMHASH;
	return calculo;

}

int main(int argc, char** argv) {
    Hash<string> hash(TAMHASH);

	ifstream infile;
	infile.open("chaves.txt");

	string numero;
	while (!infile.eof()) {
		infile >> numero;
		acrescentarZeros(numero);
		hash.insere(numero);
	}
	
	string entradaPrograma;
	cin >> entradaPrograma;
	acrescentarZeros(entradaPrograma);
	int posHash = gerarPosEntrada(entradaPrograma);
	hash.buscarChave(posHash,entradaPrograma);

	return 0;
}
