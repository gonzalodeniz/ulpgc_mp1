/*
Desarrolle una función que calcule el producto escalar de dos vectores.
*/
public class productoEscalar {
    public static void main(String[] args) {
        Vector u = new Vector(3, 0, 0);
        Vector v = new Vector(5, 5, 0);
        int resultado = u.productoEscalar(v);
        System.out.println("Resultado: " + resultado);
                
    }
        
}

/*
Clase vector
*/
class Vector {
    int x = 0;
    int y = 0;
    int z = 0;
    
    Vector(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
    
    /* Cálculo del producto escalar */
    public int productoEscalar(Vector u) {
        int r = this.x * u.x + this.y * u.y + this.z * u.z;
        return r;
    }
    
}
