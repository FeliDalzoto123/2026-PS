import java.util.Scanner;


public class AtvMaiorValor {

    static int maiorValor(int[] valores){
        int maior = valores[0];
        for(int i = 1; i < valores.length; i++){
            if(valores[i] > maior){
                maior = valores[i];
            }
        }
        return maior;
    }

    static int maiorValor(int a, int b){
        return(a > b) ? a : b ;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite a quantidade de numeros que você quer verificar: ");
        int n = scanner.nextInt();
        int[] valores = new int[n];

        System.out.println("Digite os números: ");
        for(int i = 0; i < n; i++){
            valores[i] = scanner.nextInt();
        }
        System.out.println(maiorValor(valores));
    }

}