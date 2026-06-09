import java.util.Scanner;

public class Cardapio_Eletronico {

    public static void mostrarCardapio() {
        System.out.println("\n========Cardapio Eletronico=========");
        System.out.println("1- X-Burguer R$ 15,00");
        System.out.println("2- X-Salada  R$ 18,00");
        System.out.println("3- Sorvete   R$ 10,00");
        System.out.println("4- Refrigerante R$ 6,00");
        System.out.println("5- Batata Frita R$ 10,00");
        System.out.println("6- Nuggets R$ 28,00");
        System.out.println("0- Finalizar Pedido");
    }

    public static double preco(int opcao) {
        switch (opcao) {
            case 1:
                return 15.00;
            case 2:
                return 18.00;
            case 3:
                return 10.00;
            case 4:
                return 6.00;
            case 5:
                return 10.00;
            case 6:
                return 28.00;

            default:
                return 0.00;
        }
    }

    public static String nomeProduto(int opcao){
        switch (opcao) {
            case 1:
                return "X-Burguer";
            case 2:
                return "X-Salada";
            case 3:
                return "Sorvete";
            case 4:
                return "Refigerante";
            case 5:
                return "Batata Frita";
            case 6:
                return "Nugget";
        
            default:
                return "Produto Invalido";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int opcao;
        double total = 0;

        do {
            mostrarCardapio();

            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();

            if (opcao >= 1 && opcao <= 6) {
                total += preco(opcao);
                System.out.println(nomeProduto(opcao) + " adicionado ao pedido!");
            } else if (opcao != 0) {
                System.out.println("Opção inválida!");
            }

        } while (opcao != 0);
            System.out.println("Deseja Finalizar o Pedido?");
            System.out.println("1 - Finalizar");
            System.out.println("2- Voltar para o Cardapio");

            
            
            
        }

        System.out.printf("\nTotal do pedido: R$ %.2f%n", total);

        scanner.close();
    }
}