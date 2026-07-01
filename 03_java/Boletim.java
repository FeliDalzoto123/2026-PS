import java.util.Scanner;

public class AtvMedia {
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

    static int aprovacao(double[] notas){
        int aprovados = 0;
        for(int i = 0; i < notas.length; i++){
            if (notas[i] >= 6){
                aprovados ++;
            }
        }
        return aprovados;
    }

    static void exibirBoletim(double[] notas){
        double media = calcularMedia(notas);
        int aprovados = aprovacao(notas);

        String situacao;

        if (media >= 6.0){
            situacao = "APROVADO";
        }else{
            situacao = "EM RECUPERAÇÃO";
        }

        System.out.printf("Média: %.2f%n", media);
        System.out.println("Aprovados: " + aprovados);
        System.out.println("Situação: " + situacao);

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

        exibirBoletim(valores);

        scanner.close();
    }
    
}