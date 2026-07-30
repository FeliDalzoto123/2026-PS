public class Alunos {
    private int matricula;
    private String nome;
    private String curso;
    private String situacao;
    
    public Alunos (int matricula, String nome, String curso, String situacao){
        
        if (matricula <= 0 ){
            throw new IllegalArgumentException("Matricula Invalida.");
        }

        if (nome == null || nome.isBlank()){
            throw new IllegalArgumentException("Nome Invalido.");
        }

        if (curso == null || curso.isBlank()){
            throw new IllegalArgumentException("curso Invalido.");

        }

        this.matricula = matricula;
        this.nome = nome;
        this.curso = curso;
        this.situacao = situacao;
    }

    public int getmatricula() {
        return matricula;    
    }

    public String getnome() {
        return nome;
    }

    public String getcurso() {
        return curso;
    }

    public String getsituacao(){
        return situacao;
    }

    public void setsituacao(String situacao){
        if (situacao.equals("Ativo") ||
            situacao.equals("Trancado") ||
            situacao.equals("Formado")){

                this.situacao = situacao;
            }else{
                System.out.println("Situação Invalida.");
        }
    }
    
    public void trancarCurso(){
        situacao = "Trancado";
    }

    public void formar(){
        situacao = "Formado";
    }

    public void exibirDados(){
        System.out.println("Matricula: " + matricula);
        System.out.println("Nome: " + nome);
        System.out.println("Curso: " + curso);
        System.out.println("Situação: " + situacao);
        System.out.println();
    }

    public static void main(String[] args) {
        Alunos alunos1 = new Alunos(1001, "Ana", "Engenharia", "Ativo");
        Alunos alunos2 = new Alunos(1002, "Bruno", "Direito", "Ativo");
        Alunos alunos3 = new Alunos(1003, "Carla", "Medicina", "Trancado");

        alunos1.setsituacao("Formado");

        alunos2.setsituacao("Cancelado");

        alunos2.trancarCurso();
        alunos3.formar();

        alunos1.exibirDados();
        alunos2.exibirDados();
        alunos3.exibirDados();   
    }
}