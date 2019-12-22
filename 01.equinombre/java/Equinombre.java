/**
Dada una variable ristra la cual representa el nombre y los dos apellidos de una persona, 
realice una función llamada "Equinombre" que obtenga y devuelva un nombre equivalente, 
en la forma de segundo apellido seguido de las iniciales del nombre y primer apellido. 
*/
public class Equinombre {

    public static void main(String args[]) {
        String fullname = "Pepito Grillo Conejo";
        System.out.println(fullname);
        String nombreEquivalente = equinombre(fullname);
        System.out.println(nombreEquivalente);

    }

/**
 * Devuelve el nombre apellido en formato Apellido 2 y las iniciales de
 * nombre y apellido1
 *
 * @param fullname - Nombre, apellido1, apellido2
 * @return apellido2, inicial de nombre, inicial de apellido2
 */
    public static String equinombre(String fullname) {

        String nombreEquivalente = "";
        String[] arrFullname = fullname.split(" ");
        int contPalabras = arrFullname.length;

        if (contPalabras >= 3) {
            nombreEquivalente = arrFullname[2] + " " + arrFullname[0].charAt(0)
                    + " " + arrFullname[1].charAt(1);
        } else if (contPalabras == 2) {
            nombreEquivalente = arrFullname[1] + " " + arrFullname[0].charAt(0);
        } else if (contPalabras == 1) {
            nombreEquivalente = arrFullname[0];
        } else {
            nombreEquivalente = "";
        }

        return nombreEquivalente;

    }

}

