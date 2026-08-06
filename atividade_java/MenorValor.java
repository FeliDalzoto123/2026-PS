public class MenorValor {

    static int Menor(int[] numeros){
        int m = numeros[0];
        
        for(int i=1; i<numeros.length; i++){
            if(m > numeros[i]){
                m = numeros[i];
            }
        }
        return m;
    }

    public static void main(String[] args) {
        int[] valores = {10, 5, 20};

        System.out.println(Menor(valores));
    }

}