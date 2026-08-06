public class CalcularMedia {

    static int Media(int[] numeros){
        int soma = 0;

        for(int i=0; i< numeros.length; i++){
            soma = soma + numeros[i];
        }
        return soma / numeros.length;
    }
    
    public static void main(String[] args) {
        int[] valores = {67, 42, 91};

        System.out.println(Media(valores));
    }
}