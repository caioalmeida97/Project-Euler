package Problems;

public class Problem06 {

    public static void main(String[] args) {
        /* Find the difference between the sum of the squares of the first one hundred natural numbers
        and the square of the sum. */
        
        double soma_quadrados = 0;
        double quadrado_soma;
        double resultado;
        int a = 0;
        
        for (int i = 1; i <= 100; i++) {
            a += i;
        }
        quadrado_soma = Math.pow(a, 2);
        
        for (int i = 1; i <= 100; i++) {
            soma_quadrados += Math.pow(i, 2);
        }
        
        resultado = quadrado_soma - soma_quadrados;
        System.out.println(quadrado_soma + " - " + soma_quadrados + " = " + resultado);
        System.out.println("O resultado é 25164150");
    }
    
}
