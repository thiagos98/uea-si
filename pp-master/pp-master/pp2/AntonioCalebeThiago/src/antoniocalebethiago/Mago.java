package antoniocalebethiago;

public class Mago extends Personagem implements ComportamentoMagico{

    public Mago() {
    }

    public Mago(String nome) {
        super(nome);
        this.setNome(nome);
    }
    
    @Override
    public void andar() {
        System.out.println("Mago " + this.getNome() + " esta andando.");
    }

    @Override
    public void guardarItem() {
        System.out.println("Mago " + this.getNome() + " guardou o seu cajado mágico.");
    }

    @Override
    public void usarItem() {
        System.out.println("Mago " + this.getNome() + " usou o item de mana.");
    }

    @Override
    public void invisibilidade() {
        System.out.println("Mago " + this.getNome() + " vai ficar invisivel.");
    }

    @Override
    public void ultraRapidez() {
        System.out.println("Mago " + this.getNome() + " esta muito rápido.");
    }
    
}
