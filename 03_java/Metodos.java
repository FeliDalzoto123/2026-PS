public class Metodos {
    public static void saudacao() {
        System.out.println("Olá Turma!");        
    }

    public static void main(String[] args) {
        
        saudacao();
        
         exibirNome("Maria");
        
         int resultado = somar(10,20);
        System.out.println(resultado);

        double resultado1 = somar(20,10);
        System.out.println(resultado1);
    }


    static void exibirNome(String nome){
        System.out.println(nome);

    }

    static int somar(int a, int b) {
    return a + b;
    }


    static double somar(double a, double b){
    return a+b;
    }

   
}