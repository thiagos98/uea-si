/* class List{
    constructor(){
        this.data = [];
    }

    add(data){
        this.data.push(data);
        console.log(this.data);
    }
}

class TodoList extends List{
    constructor(usuario){
        super(); //import no constructor da classe pai

        this.usuario = usuario;
    }

    mostraUsuario(){
        console.log(this.usuario);
    }
}
//comentar em bloco: shift+alt+A

const MinhaLista = new TodoList(); // instancia objeto da classe Todolist

document.getElementById('addTodo').onclick = function(){ // evento de click do botao foi acionado, pegando botao atraves do id
    const nome = document.getElementById('addNome').value; // pega o valor digitado no campo input
    MinhaLista.add(nome);
}

MinhaLista.mostraUsuario(); */