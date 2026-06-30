public class Media {
    static double media(int[] numeros){
        int total = somarTudo(numeros);
        return (double) total / numeros.length;
    }

    static int somarTudo(int[] numeros){
    int total = 0;
    for(int i = 0; i < numeros.length; i++){
        total = total + numeros[i];

    }
    return total;
}

    public static void main(String[] args) {
        int[] valores = {10,20,30};
        System.out.println(media(valores));
    }
    
    
}