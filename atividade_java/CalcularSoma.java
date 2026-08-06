public class CalcularSoma {

    static int Somar(int[] numeros){
        int somar = 0;

        for(int i=0; i<numeros.length; i++){
            somar = somar + numeros[i];
        }
        return somar;
    }

    public static void main(String[] args) {
        int[] valores = {23, 34, 65};

        System.out.println(Somar(valores));
    }
}