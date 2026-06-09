
public class teste {

    public static void main(String[] args) {
        int idade = 18;

        if (idade >= 18){
            System.out.println("Maior de idade");
        }

        int estoque = 5;
        if (estoque > 0){
            System.out.println("Produto Disponivel");
        } else {
            System.out.println("Produto esgotado");
        }

        int opcao = 2;
        switch (opcao) {
            case 1:
                System.out.println("X-Burguer");
                break;
            case 2:
                System.out.println("Pizza");
                break;    

            default:
                break;
        }

        int contador = 1;

        while(contador <= 5 ){
            System.out.println(contador);
            contador++;
        }

        for(int i=1; i <= 5; i++){
            System.out.println(i);
        }
    }
    
}
