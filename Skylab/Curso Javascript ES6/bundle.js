/*
class List{
    constructor(){
        this.data = []
    }
    add(data){
        this.data.push(data);
        console.log(this.data);
    }
}

class TodoList  extends List{
    constructor(){
        this.todos = [];
    }
    addTodo(){
        this.todos.push('novo todo');
        console.log(this.todos);
    }

    constructor(){
        super();

        this.usuario = 'thiago';
    }

    mostraUsuario(){
        console.log(this.usuario);
    }
}

var minhaLista = new TodoList();

document.getElementById('novotodo').onclick = function(){
    minhaLista.add('novo todo');
}

minhaLista.mostraUsuario();



//metodos estaticos
class Matematica{
    static soma(a, b){
        return a + b;
    }
}

console.log(Matematica.soma(1,2));
console.log(Matematica.soma(2,3));
console.log(Matematica.soma(3,4));
console.log(Matematica.soma(4,5));


const arr = [1,2,3,5,6,7,8];
console.log(arr);

const newArr = arr.map(function(item, index) {
    return item + index;
});
console.log(newArr);

const sum = arr.reduce(function(total, next){
    return total + next;
});
console.log(sum);

const filter = arr.filter(function(item){
    return item % 2 === 0;
});
console.log(filter);

const find = arr.find(function(item){
    return item === 6;
});
console.log(find);


//Arrow Functions
const arr = [1,2,3,5,6,7,8];

const newArr = arr.map(item => item * 2);

console.log(newArr);

const teste = () => ({nome: 'thiago', altura:1.81});

console.log(teste());


//Valores Padrão

function soma(a = 3, b = 5){
    return a + b;
}

console.log(soma(4));
console.log(soma());

const sum = (a=6, b=10) => a + b;

console.log(sum(2));



//Desestruturação de objetos

const usuario = {
    nome: 'thiago',
    idade: 21,
    endereco :{
        cidade: 'manaus',
        estado: 'AM'
    }
};

const carro = {
    marca: 'chevrolet',
    modelo: 'onix',
    ano: 2019,
    cor: 'vermelho vinho'
}
const { nome, idade,endereco: {cidade} } = usuario;

//console.log(nome);
//console.log(idade);
//console.log(cidade);

function mostraNome({nome},{modelo}){
    console.log(nome);
    console.log(modelo);
}

mostraNome(usuario,carro);

*/
//Operadores Rest/Spread
"use strict";
