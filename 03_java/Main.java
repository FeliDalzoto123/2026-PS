public class Produto {
    private String nome;
    private double preco;
    private int quantidade;
    
    public Produto (String nome, double preco, int quantidade) {
        this.nome = nome;
        this.preco = preco;
        this.quantidade = quantidade;
    }

    public String getNome(){
        return nome;
    }

    public double getPreco(){
        return preco;
    }

    public int getQuantidade(){
        return quantidade;
    }

    public void setNome(String nome){
        if (nome != null && !nome.isBlank()){
            this.nome = nome;
        }
    }

    public void setPreco(double preco){
        if(preco >= 0){
            this.preco = preco;
        }
    }

    public void setQuantidade(int quantidade){
        if (quantidade >= 0){
            this.quantidade = quantidade;
        }
    }

    public void adicionarEstoque(int quantidadeAdicionar){
        if (quantidadeAdicionar > 0){
            quantidade += quantidadeAdicionar;
        }
    }
    public boolean removerEstoque(int quantidadeRemover){
        if (quantidadeRemover > 0 && quantidadeRemover <= quantidade){
            quantidade -= quantidadeRemover;
                return true;
        } 
      return false;  
    }
    
    public double calcularValorEmEstoque(){
        return preco * quantidade;
    }
}

public class Main{
    public static void main(String[] args) {
        Produto produto = new Produto("Mouse", 80.00, 10);

        produto.adicionarEstoque(5);
        boolean removido = produto.removerEstoque(3);


        System.out.println("Produto: " + produto.getNome());
        System.out.println("Preço: " + produto.getPreco());
        System.out.println("Quantidade: " + produto.getQuantidade());
        System.out.println("Remoção realizada: " + removido);
        System.out.println("Valor em Estoque: R$ " + produto.calcularValorEmEstoque());

    }
}
