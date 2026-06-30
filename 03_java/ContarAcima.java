public class ContarAcima {

    static int contarAcima(int[] valores, int limite) {
        int quantidade = 0;
        for (int v: valores){
            if(v > limite){
                quantidade = quantidade + 1;
            }
        }
        return quantidade;
    }

    public static void main(String[] args) {
        // Uso:
        int[] notas = {40, 75, 90, 30};
        System.out.println(contarAcima(notas, 50));
    }

}