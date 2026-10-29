/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package repasojava;

/**
 *
 * @author DAM2-06
 */
import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Random;

public class RepasoJava {

    public static class ListaInteligente extends ArrayList<Integer> {

        public Integer moda() {
            int maxApar = 0;
            Integer numMasRep = null;
            Map<Integer, Integer> apariciones = new HashMap<>();
            for (int i = 0; i < this.size(); i++) {
                if (apariciones.containsKey(this.get(i))) {
                    apariciones.put(this.get(i), apariciones.get(this.get(i)) + 1);
                } else {
                    apariciones.put(this.get(i), 1);
                }
                
                if(apariciones.get(this.get(i)) > maxApar){
                    numMasRep = this.get(i);
                    maxApar = apariciones.get(this.get(i));
                }
            }
            return numMasRep;
        }
        public void ordenar(){
            
        }
    }

    public static void main(String[] args) {
        Random rn = new Random();
        rn.setSeed(0);

        Map<String, Integer> precios = new HashMap<>();
        precios.put("coche", 30000);
        precios.put("moto", 8000);
        System.out.println(precios.containsKey("coche"));
        System.out.println("El tamaño de mapa es: " + precios.size());

        Integer precioBarco = precios.get("barco");
        if (precioBarco == null) {
            precioBarco = 10000;
        }
        System.out.println("El precio del coche es: " + precioBarco);
        
        ListaInteligente li = new ListaInteligente();
        for (int i = 0; i < 10; i++) {
            li.add(rn.nextInt(0, 10));
        }
        System.out.println(li);
        System.out.println("La moda es: " + li.moda());
        System.out.println(li.sort());
    }

}
