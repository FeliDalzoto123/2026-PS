import java.util.Scanner;

public class AtvAprovados {
    static double calcularMedia(double[] notas){
        double total = somar(notas);
        return (double) total / notas.length;
    }

    static double somar(double[] notas){
        double total = 0;
        for (int i = 0; i < notas.length; i++){
            total = total + notas[i];

        }
        return total;
    }

    static int verificacao(double[] notas){
        int aprovados = 0;
        for(int i = 0; i < notas.length; i++){
            if (notas[i] >= 6){
                aprovados ++;
            }
        }
        return aprovados;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Digite a quantidade de notas: ");
        int quantidade = scanner.nextInt();
    
        double[] valores = new double[quantidade];
        
        for(int i = 0; i < quantidade; i++){
            System.out.print("Digite as notas " + (i + 1) + ": ");
            valores[i] = scanner.nextDouble();
        }
        System.out.println(verificacao(valores));


        scanner.close();
    }
    
}