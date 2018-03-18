package Pessoal;

import Financeiro.Divida;
import java.util.ArrayList;
import javax.swing.JOptionPane;

public class CadastroUser {

    private ArrayList<Usuario> users;

    public CadastroUser() {
        this.users = new ArrayList<Usuario>();
    }

    public ArrayList<Usuario> getUsers() {
        return users;
    }

    public void setUsers(ArrayList<Usuario> users) {
        this.users = users;
    }

    public void addUser(Usuario s) {
        this.users.add(s);
    }

    public void mostrarUsuarios(String nome) {
        for (int i = 0; i < this.users.size(); i++) {
            this.users.get(i).mostrarUsuario(nome);
        }
    }

    public void mostrarUsuarios2(String nome, int index) {
        double var = this.users.get(index).mostrarUsuario2();//chamada do método mostarUsuario2 da classe Usuario
                                                            //resgata o valor total de todas as dívidas do usuario informado
        JOptionPane.showConfirmDialog(null, "Nome: " + nome + "\nTotal: " + var);//informa o nome e o total a pagar
    }

    public void mostrarUsuarios3(String nome, int index) {
        this.users.get(index).mostrarUsuario(nome);//chama o método mostrarUsuario atráves da ArrayList users, indexando no índice "index"
    }

    public boolean verificarNome(String nomeTeste) {//verifica se o nome foi cadastrado na ArrayList
        for (int i = 0; i < users.size(); i++) {
            if (nomeTeste.equals(users.get(i).getNome())) {
                return true;
            }
        }
        return false;
    }

    public void verificarNome2(String nomeTeste) {//método verifica se nome informado existe, caso existe chama outro método desta classe
                                                  //mostrarUsuarios2, passando como parâmetro o nome e o índice com o qual o nome foi encontrado
        for (int i = 0; i < this.users.size(); i++) {
            if (nomeTeste.equalsIgnoreCase(this.users.get(i).getNome())) {
                //System.out.println(i);
                this.mostrarUsuarios2(nomeTeste, i);
            }

        }
    }

    public int verificarNome3(String nomeTeste) {//Verifica em qual índice o nome informado esta cadastrado na ArrayList
        for (int i = 0; i < this.users.size(); i++) {
            if (nomeTeste.equalsIgnoreCase(this.users.get(i).getNome())) {
                return i;
            }

        }
        return -1;
    }

    public boolean verificarMes(String mes, int index) {//verifica se o mes informado no índice "index" existe, se existir retorna "true"
                                                        //senão, retorna false
        for (int j = 0; j < users.get(index).getDividas().size(); j++) {
            if (mes.equalsIgnoreCase(users.get(index).getDividas().get(j).getMes())) {
                return true;
            }
        }

        return false;
    }

    public boolean excluirConta(int codigo, int index) {//percorremos através de duas estruturas de repetição "for" os indices da ArrayList
                                                        //e a cada iteração é feito um teste para verificar se o codigo informado é válido
        boolean teste = true;

        for (int j = 0; j < users.get(index).getDividas().size(); j++) {
            for (int k = 0; k < users.get(index).getDividas().get(j).getContas().size(); k++) {
                if (codigo == users.get(index).getDividas().get(j).getContas().get(k).getCodigo()) {
                    users.get(index).getDividas().get(j).getContas().remove(k);
                    JOptionPane.showConfirmDialog(null, "Conta Excluida com Sucesso");
                    teste = false;
                }
            }
        }

        return teste;
    }

    public boolean listarContas(String nome) {
        for (int i = 0; i < users.size(); i++) {
            if (nome.equalsIgnoreCase(users.get(i).getNome())) {
                for (int j = 0; j < users.get(i).getDividas().size(); j++) {
                    JOptionPane.showConfirmDialog(null, users.get(i).getDividas().get(j).getMes());
                    for (int k = 0; k < users.get(i).getDividas().get(j).getContas().size(); k++) {
                        if (nome.equalsIgnoreCase(users.get(i).getNome())) {
                            return true;
                        }

                    }
                }
            }
        }
        return false;
    }
}
