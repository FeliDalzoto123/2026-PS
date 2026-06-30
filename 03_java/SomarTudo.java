public class SomarTudo {

    static int somarTudo(int[] numeros){
        int total = 0;
        for(int i = 0; i < numeros.length; i++){
            total = total + numeros[i];

        }
        return total;
    }

    public static void main(String[] args) {

     // Uso:
        int[] valores = {10, 20,30};
        System.out.println(somarTudo(valores));
    
    }
}


