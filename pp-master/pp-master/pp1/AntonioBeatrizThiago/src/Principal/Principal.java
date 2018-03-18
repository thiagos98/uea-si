package Principal;

import Financeiro.ContaPagar;
import Financeiro.Divida;
import Pessoal.CadastroUser;
import Pessoal.Usuario;
import java.util.ArrayList;
import javax.swing.JOptionPane;

public class Principal {

    public static void main() {

        CadastroUser c = new CadastroUser();//Instância de um objeto da classe CadastroUser
        String operacao = "";

        int aux = 0;
        String vet[] = new String[1000];//Vetor auxiliar para o cadastro de usuarios

        do {
            operacao = JOptionPane.showInputDialog(null, "                                      CONTROLE DE DÍVIDAS\n\nCADASTRO\n"
                    + "             Cadastrar um novo usuário [ C ]  | "
                    + " Cadastrar Dívida de um Usuário [ D ]  \nCONSULTA DE DADOS\n"
                    + "             Consultar Contas de um Usuário [ CD ]  |"
                    + " Lista Contas de um Usuário[ LC ]  \nEXCLUIR\n"
                    + "             Exclusão de Contas de Usuário[ E ]\n"
                    + " SAIR [ S ]\n");
            /*
             * Menu Inicial do Programa
             */

            operacao = operacao.toUpperCase();

            if (operacao != null && operacao.equals("C")) {//Verificação se a entrada não é nula e se a operação foi a de cadastro
                String nome = "";
                nome = JOptionPane.showInputDialog(null, "Informe seu nome");
                nome = nome.toUpperCase();
                vet[aux] = nome;//Alocação dos nomes dentro do vetor vet
                aux++;
            } else if (operacao != null && operacao.equals("D")) {//Verificação se a entrada não é nula e se a operação foi a de cadastrar dividas
                String nome = "";
                nome = JOptionPane.showInputDialog(null, "Informe seu nome para consulta");
                for (int i = 0; i < vet.length; i++) {
                    if (nome.equalsIgnoreCase(vet[i])) {//Percorre o vetor para verificar se existe o nome informado
                        String op2 = "";
                        Usuario u = new Usuario(nome);//Cria uma instância de Usuario para o cadastro no ArrayList da classe CadastroUser
                        c.addUser(u);//Adiciona a instância de Usuário no ArrayList
                        //Porém, só é informado o nome. As dívidas e as contas serão informadas logo a seguir

                        int aux2 = 0;
                        do {
                            op2 = JOptionPane.showInputDialog(null, " Cadastrar Mês da Dívida[ M ]\n Sair[ S ]");
                            op2 = op2.toUpperCase();

                            if (op2.charAt(0) == 'M') {

                                String mes = "";
                                String nomeC = "";
                                double valor = 0;
                                int codigo = 0;

                                /*
                                 *Leitura das informações restantes que faltavam para compor a instância(u) da classe Usuário
                                 */
                                mes = JOptionPane.showInputDialog(null, "Mes da divida sr(a) " + vet[i]);
                                mes = mes.toUpperCase();
                                nomeC = JOptionPane.showInputDialog(null, "Mes: " + mes + "\n Nome da conta sr(a) " + vet[i]);
                                nomeC = nomeC.toUpperCase();
                                valor = Double.parseDouble(JOptionPane.showInputDialog(null, "Mes: " + mes + "\n Conta: " + nomeC + "\n Valor da conta sr(a) " + vet[i]));
                                codigo = Integer.parseInt(JOptionPane.showInputDialog(null, "Mes: " + mes + "\n Conta: " + nomeC + "\n Codigo da conta sr(a) " + vet[i]));

                                ContaPagar cp = new ContaPagar();//Instância da classe ContaPagar. Para compor a instância "u" da classe Usuário

                                cp.setNome(nomeC);
                                cp.setPreco(valor);
                                cp.setCodigo(codigo);

                                Divida d = new Divida();//Instância da classe Dívida para compor a instância "u" da classe Usuário
                                d.setMes(mes);
                                d.addConta(cp);//Neste momento, adicionamos no ArrayList de Contas na classe Dívida, a conta informada pelo usuário

                                u.addDividas(d);//Adicionamos na ArrayList de dívidas na classe Usuario, uma nova divida
                            }
                        } while (op2.charAt(0) != 'S');
                        aux++;
                    }
                }
            } else if (operacao != null && operacao.equals("CD")) {
                String nome = "";
                String op3 = "";
                do {
                    op3 = JOptionPane.showInputDialog(null, "Informar seu nome[ N ]\nSair[ S ]");
                    op3 = op3.toUpperCase();
                    if (op3.charAt(0) == 'N') {
                        nome = JOptionPane.showInputDialog(null, "Informe seu nome para listar sua contas");
                        nome = nome.toUpperCase();

                        c.verificarNome2(nome);
                        break;
                    }

                } while (op3.charAt(0) != 'S');

            } else if (operacao != null && operacao.equals("LC")) {
                String nome = "";
                nome = JOptionPane.showInputDialog(null, "Informe seu nome: ");
                nome = nome.toUpperCase();

                int index = c.verificarNome3(nome);//A busca do indice que o nome informado está armazenado na ArrayList de usuarios
                c.mostrarUsuarios3(nome, index);//chamada da função mostrarUsuarios3 passando como parâmetro o nome e o indice
            } else if (operacao != null && operacao.equals("E")) {
                String nome = "";
                String mes = "";
                nome = JOptionPane.showInputDialog(null, "Exclusão de Contas\nInforme seu nome para consulta");
                nome = nome.toUpperCase();

                int k = 0;
                boolean validador = true;
                //if (c.verificarNome(nome)) {
                while (k < vet.length && validador) {
                    if (nome.equalsIgnoreCase(vet[k])) {//testa se o nome informado esta contido no vetor de nomes
                        mes = JOptionPane.showInputDialog(null, "Exclusão de Contas\nInforme o mes para consulta");
                        mes = mes.toUpperCase();
                        int index = c.verificarNome3(nome);//caso ele tenha sido cadastrado, buscamos o índice com qual o mesmo esta cadastrado na ArrayList
                        if (c.verificarMes(mes, index)) {//verifica se existe o mês informado atraves do indice resgatado do método verificarNome3
                            int codigo = 0;
                            codigo = Integer.parseInt(JOptionPane.showInputDialog(null, "Nome: " + nome
                                    + "\nMes: " + mes
                                    + "\nInforme o codigo para consulta"));//Leitura do código para a consulta
                            validador = c.excluirConta(codigo, index);//o método retorna "true", caso a conta nao tenha sido encontrada. E false caso ela seja encontrada
                        } else {
                            JOptionPane.showConfirmDialog(null, "Mes nao encontrado");
                        }
                    }
                    k++;
                }
                //}

            }

        } while (operacao.charAt(0) != 'S');

        JOptionPane.showConfirmDialog(null, "Muito Obrigado por Usar nosso Software");
        JOptionPane.showConfirmDialog(null, "Developers ->\n Thiago S. Borges\nAntônio Neto Rodrigues\nAna Beatriz");

    }
}
