package antoniocalebethiago;

import java.util.ArrayList;

public class AntonioCalebeThiago {
    public static void main(String[] args) {
        //3a Questao -> Letra a
        ArrayList<Personagem> personagens = new ArrayList();
        personagens.add(new Cavaleiro("Ragnar Lodbrok"));
        personagens.add(new Cavaleiro("Bjorn Ironside"));
        personagens.add(new Mago("O Vidente"));
        personagens.add(new Mago("Gandoulf"));
        personagens.add(new Dragao("Dragao de gelo"));
        personagens.add(new Dragao("Dragao de fogo"));
        
        //3a Questao -> Letra b
        int i;
        Jogo j = new Jogo();
        for(i = 0;i < personagens.size();i++){
            j.executaAcoesComuns(personagens.get(i));
        }
        
        //3a Questao -> Letra c
        Personagem p = new Mago("Raure Porco");
        
    }    
}
