/*
 * BEE 2453 - Língua do P - Level 4 - Ad-hoc
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bee2453 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(isr);

        System.out.println(desencripta(in.readLine()));

    }
    public static StringBuilder desencripta(String textoEmP){
        StringBuilder novoTexto = new StringBuilder();
        String[] palavras = textoEmP.trim().split(" +");//mais de um espaço em branco

        for(int i =0; i<palavras.length; i++){
            for(int j = 1; j<palavras[i].length(); j+=2){
                novoTexto.append(palavras[i].charAt(j));
            }
            if(i != palavras.length-1)
                novoTexto.append(" ");
        }

        return novoTexto;
    }
    public static StringBuilder encriptaEmP(String texto){
        StringBuilder textoEmP = new StringBuilder();

        for(int i = 0; i < texto.length(); i++){
            if(Character.isAlphabetic(texto.charAt(i)))
                textoEmP.append("p");
            textoEmP.append(texto.charAt(i));
        }
        return textoEmP;
    }  
}