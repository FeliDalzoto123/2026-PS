import java.util.Scanner;

public class Metodos_resolucao {
    static double calcularDesconto(double valor, double percentual){
        return valor - (valor * percentual / 100);
    }

    static int maiorNumero(int a, int b){
        if (a > b){
            return a;
        }else{
            return b;
        }
    }
    
    static double calcularFrete(double peso){
       if (peso <= 1){
            return 10.0;
       }else if(peso <= 5){
            return 20.0;
       }else{
            return 35.0;
       }
    }

    static int somar(int a1, int b1) {
        return a1 + b1;
    }

    static double somar(double a1, double b1) {
        return a1 + b1;
    }

    static void exibirPodutos(String nomes){
        System.out.println("Produtos: " + nomes);
    }

    static void exibirProduto(String nome, double preco) {
        System.out.println("Produto: " + nome);
        System.out.printf("Preço: R$ %.2f%n", preco);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Problema 1: //
        System.out.println("Digite o valor do produto: ");
        double valor = scanner.nextDouble();
        
        System.out.print("Digite o percentual de desconto: ");
        double percentual = scanner.nextDouble();

        double desconto = calcularDesconto(valor, percentual);

        System.out.println("Valor do desconto: R$ " + desconto);

        // Problema 2: //
        System.out.print("Digite dois números inteiros: ");
        int a = scanner.nextInt();
        int b = scanner.nextInt();

        int maior = maiorNumero(a, b);
        System.out.println("Maior número: " + maior); 

        //Problema 3 //

        System.out.print("Digite o peso do produto (kg): ");
        double peso = scanner.nextDouble();

        double frete = calcularFrete(peso);

        System.out.println("Valor do frete: R$ " + frete);

        // Problem 4: //
        
        System.out.println("Digite dois números:");
        double a1 = scanner.nextDouble();
        double b1 = scanner.nextDouble();
        if (a1 % 1 == 0 && b1 % 1 == 0) {
            System.out.println("Soma: " + somar((int)a1, (int)b1));
        } else {
            System.out.println("Soma: " + somar(a1, b1));
        }

        //Problema 5 //

        System.out.print("Digite o nome do produto: ");
        String nome = scanner.next();

        System.out.print("Digite o preço do produto: ");
        double preco = scanner.nextDouble();

        if(preco == 0){
            exibirPodutos(nome);
        } else{
            exibirProduto(nome, preco);
        }



        
        scanner.close();

    }
    
}