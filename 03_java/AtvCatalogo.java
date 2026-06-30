import java.util.ArrayList;
import java.util.Scanner;

public class AtvCatalogo {

    static void adicionar(ArrayList<String> lista, String item){
        lista.add(item);

    }

    static void listar(ArrayList<String> lista){
        for (String item: lista){
            System.out.println("- " + item);
        }
    }
    public static void main(String[] args) {
        ArrayList<String> produtos = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        while (true){
        
            System.out.println("Digite o nome do item (ou 'fim' para parar): ");
            String item = scanner.nextLine();
            

            if (item.equalsIgnoreCase("fim")) {
                break;
            }
            adicionar(produtos, item);
        }

        System.out.println("\nLista de Produtos: ");
        listar(produtos);

        scanner.close();
    }

}