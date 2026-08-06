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
        int [] nota = {35, 40, 67, 34};
        System.out.println(contarAcima(nota, 50));
    }
}