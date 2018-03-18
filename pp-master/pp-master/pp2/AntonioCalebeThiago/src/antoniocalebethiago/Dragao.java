package antoniocalebethiago;

public class Dragao extends Personagem {
    public Dragao() {
    }

    public Dragao(String nome) {
        super(nome);
        this.setNome(nome);
    }
    
    @Override
    public void andar() {
        System.out.println("O temível Dragão " + this.getNome() + " esta andando.");
    }

    @Override
    public void guardarItem() {
        System.out.println("O temível Dragão " + this.getNome() + " esta guardando algum item.");
    }

    @Override
    public void usarItem() {
        System.out.println("O temível Dragão " + this.getNome() + " esta usando algum item.");
    }
    
    public void atirarFogo(){
        System.out.println("O temível Dragão " + this.getNome() + " esta atirando fogo em um vilarejo!!!\nCOOORRAAMMMM PARA AS COLINAAAAS");
    }
    
    public void voar(){
        System.out.println("O temível Dragão " + this.getNome() + " esta voando.");
    }
    
    public void morder(){
        System.out.println("O temível Dragão " + this.getNome() + " esta mordendo um grande inimigo.");
    }
}
