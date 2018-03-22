package Problems;

public class Problem05 {
    
    public static void main(String[] args) {
        
       /* 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
        without any remainder.
        What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? */
        int numero = 2520;
        int resultado = 0;
        boolean eh_divisivel = false;
        do{
            for(int i = 2; i <= 20; i++){
                if(numero%i == 0)
                    eh_divisivel = true;
                else{
                    eh_divisivel = false;
                    break;
                }
            }
            if(eh_divisivel == true){
                resultado = numero;
                numero = 0;
            }
            else
                numero += 2;
        } while(numero != 0);
        
        System.out.println("O menor numero é: " + resultado);
    }
    
}
