import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);

        System.out.println("=============================");
        System.out.println("   CARDÁPIO ELETRÔNICO");
        System.out.println("=============================");
        System.out.println("1 - X-Burguer ..........R$ 18,00");
        System.out.println("2 - Pizza .............R$ 35,00");
        System.out.println("3 - Suco Natural...........R$ 8,00");
        System.out.println("4 - Café .............R$ 5,00");
        System.out.println("=============================");


        System.out.print("Escolha uma opção: ");
        int opcao = entrada.nextInt();

        if (opcao == 1 ){
            System.out.println("Você escolheu X-Burguer.");
        }else if (opcao == 2 ){
            System.out.println("Você escolheu Pizza.");
        }else if (opcao == 3 ){
            System.out.println("Você escolheu Suco Natural.");
        }else if (opcao == 4 ){
            System.out.println("Você escolheu Café.");
        } else {
            System.out.println("Opção inválida.");
        }

        entrada.close();

    }
}