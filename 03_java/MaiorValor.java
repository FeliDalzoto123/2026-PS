public class MaiorValor {
    
    static int maior(int[] valores){
        int maiorAteAgora = valores[0];
        for (int v : valores){
            if (v > maiorAteAgora){
                maiorAteAgora = v;

            }
        }
        return maiorAteAgora;
    }

    public static void main(String[] args) {
        int[] idades = {17, 23, 15, 31};
        System.out.println(maior(idades));
    }
    
}