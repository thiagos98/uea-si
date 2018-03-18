package Financeiro;


import Financeiro.ContaPagar;
import java.util.ArrayList;
import javax.swing.JOptionPane;

public class Divida {
    private String mes;
    private ArrayList<ContaPagar> contas;

    public Divida(String mes) {
        this.mes = mes;
        this.contas = new ArrayList<ContaPagar>();
    }
    public Divida(){
        this.contas = new ArrayList<ContaPagar>();
    }

    public String getMes() {
        return mes;
    }

    public void setMes(String mes) {
        this.mes = mes;
    }

    public ArrayList<ContaPagar> getContas() {
        return contas;
    }

    public void setContas(ArrayList<ContaPagar> contas) {
        this.contas = contas;
    }
    
    public void addConta(ContaPagar c){
        this.contas.add(c);
    }
    
    public void mostrarDivida(String nome){
        for(int i = 0;i<this.contas.size();i++){
            this.contas.get(i).mostrarConta(nome,this.getMes());
        }
    }
    public double mostrarDivida2(String nome){
       double var = 0 ;
        int i = 0;
        var += this.contas.get(i).getPreco();
        i++;
        return var;
    }
}
