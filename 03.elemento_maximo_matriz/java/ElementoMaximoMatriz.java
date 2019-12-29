/*
 * Desarrolle un procedimiento para obtener el elemento máximo de una matriz de ristras y su posición.
 */

package main;

import java.util.Random;

public class ElementoMaximoMatriz {
    
    public static void main(String[] args) {
        Matriz m = new Matriz(10,10);
        int[][] mran = m.random(10);
        Matriz.print(mran);
        elementoMaximo(mran);
                
    }
    
    public static void elementoMaximo(int [][]m) {
        /* Muestra en consola el elemento máximo de la matriz y su posición */
        int max = 0;
        int x=0;
        int y=0;
        
        for(int i=0; i<m.length; i++) {
            for(int j=0; j<m[i].length; j++){
                if(m[i][j] > max) {
                    max = m[i][j];
                    x = i + 1;
                    y = j + 1;
                }
            }
        }
        System.out.println("Valor maximo: " + max);
        System.out.println("Posicion: " + x + "," + y);
    }
                    
}

class Matriz {
    int[][] m;
       
    public Matriz(int filas, int columnas) {
        /* Inicializa una matriz de 'filas' x 'columnas' */
        this.m = new int[filas][columnas];
    }
    public Matriz(int filas, int columnas, int value) {
        /* Inicializa una matriz de 'filas' x 'columnas' con el valor 'value' */
        this.m = new int[filas][columnas];
        for(int i=0; i<filas;i++)
            for(int j=0;j<columnas;j++)
                this.m[i][j]=value;
    }
    
    public int[][] random(int maxValue) {
        /* Sustituye el contenido de la matriz por valores aleatorios desde 0 hasta
           'maxValue'
        */
        Random r = new Random();
        for(int i=0; i<this.m.length;i++)
            for(int j=0; j<this.m[i].length;j++)
                this.m[i][j] = r.nextInt(maxValue);
        
        return this.m;
               
    }
    
    public void print(){
        /* Muestra la matriz en la consola */
        for(int i=0; i<this.m.length;i++){
            for(int j=0; j<this.m[i].length;j++) {
                System.out.print(" " + this.m[i][j] + " ");
            }
            System.out.print("\n");
        }        
    }
    
    public static void print(int[][] m){
        /* Muestra la matriz en la consola */
        
        for(int i=0; i<m.length;i++){
            for(int j=0; j<m[i].length;j++) {
                System.out.print(" " + m[i][j] + " ");
            }
            System.out.print("\n");
        }  
    }
    
}
