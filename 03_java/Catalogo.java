import java.util.ArrayList;

public class Catalogo {

    static void adicionar(ArrayList<String> lista, String item){
        lista.add(item);
    }
    
    static void listar(ArrayList<String> lista){
        for (String item : lista){
            System.out.println("- " + item);
        }
    }
    public static void main(String[] args) {
        ArrayList<String> produtos = new ArrayList<>();
        adicionar(produtos, "Pizza");
        adicionar(produtos, "Suco");
        listar(produtos);
    }
}