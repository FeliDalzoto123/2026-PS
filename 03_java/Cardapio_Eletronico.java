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

    public static String nomeProduto(int opcao) {
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

    public static String mostrarResumoPedido(int[] quantidades, double total) {
    String resumo = "\n======= RESUMO DO PEDIDO =======\n";

    for (int i = 1; i <= 6; i++) {
        if (quantidades[i] > 0) {
            resumo += quantidades[i] + "x "
                    + nomeProduto(i)
                    + " - R$ "
                    + String.format("%.2f", preco(i))
                    + "\n";
        }
    }

    resumo += "\nTOTAL DO PEDIDO: R$ "
            + String.format("%.2f", total);

    return resumo;
}

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int opcao;
        double total = 0;
        int[] quantidades = new int[7];

        boolean finalizarPedido = false;

while (!finalizarPedido) {

    mostrarCardapio();

    System.out.print("Escolha uma opção: ");
    opcao = scanner.nextInt();

    if (opcao >= 1 && opcao <= 6) {

        total += preco(opcao);
        quantidades[opcao]++;

        System.out.println(nomeProduto(opcao) + " adicionado ao pedido!");

    } else if (opcao == 0) {

        System.out.println("\n===== FINALIZAR PEDIDO =====");
        System.out.println("1 - Continuar comprando");
        System.out.println("2 - Finalizar pedido");
        System.out.print("Escolha uma opção: ");

        int escolha = scanner.nextInt();

        if (escolha == 1) {

            System.out.println("\nVoltando ao cardápio...");

        } else if (escolha == 2) {

            finalizarPedido = true;

        } else {

            System.out.println("Opção inválida!");
        }

    } else {

        System.out.println("Opção inválida!");
    }
}
System.out.println(mostrarResumoPedido(quantidades, total));

System.out.println("\n======= PAGAMENTO =======");
System.out.println("1 - Pix");
System.out.println("2 - Cartão");
System.out.println("3 - Dinheiro");
System.out.print("Escolha a forma de pagamento: ");

int pagamento = scanner.nextInt();

switch (pagamento) {
    case 1:
        System.out.println("Pagamento via Pix realizado com sucesso!");
        break;

    case 2:
        System.out.println("Pagamento via Cartão realizado com sucesso!");
        break;

    case 3:
        System.out.println("Pagamento em Dinheiro selecionado!");
        break;

    default:
        System.out.println("Forma de pagamento inválida!");
}
scanner.close();
    }
}
