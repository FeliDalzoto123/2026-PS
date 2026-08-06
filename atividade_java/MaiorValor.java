public class MaiorValor {

    static int Maior(int [] numeros){

        int m = numeros[0];

        for(int i=1; i < numeros.length; i++){
            
            if(m < numeros[i]){
                m = numeros[i];
            }
        }
        return m;

    }
    
    public static void main(String[] args) {
        int[] valores = {67, 42, 21};

        System.out.println(Maior(valores));

    }
}