package Pessoal;

import java.util.ArrayList;
import Financeiro.Divida;
import javax.swing.JOptionPane;

public class Usuario {
    private String nome;
    private ArrayList<Divida> dividas;

    public Usuario() {
        this.dividas = new ArrayList<Divida>();
    }

    public Usuario(String nome) {
        this.nome = nome;
        this.dividas = new ArrayList<Divida>();
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public ArrayList<Divida> getDividas() {
        return dividas;
    }

    public void setDividas(ArrayList<Divida> dividas) {
        this.dividas = dividas;
    }
    
    public void addDividas(Divida d){
        this.dividas.add(d);
    }
    
    public void mostrarUsuario(String nome){
        for(int i = 0;i < this.getDividas().size();i++){
            dividas.get(i).mostrarDivida(this.getNome());
        }
    }    
    
    public double mostrarUsuario2(){
        double var = 0;
        for(int i = 0;i < this.getDividas().size();i++){
            var += dividas.get(i).mostrarDivida2(this.getNome());
        }
        return var;
    }
    
}
