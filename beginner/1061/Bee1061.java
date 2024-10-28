/*
* BEE 1061 - Event Time - Level 3 - Beginner
*/

// Submission: 01/11/17, 3:04 PM 

import java.util.Scanner;

public class Bee1061 {

	public static void main(String[] args) {
//		Solução:
//		1: pegar dias completos: diaFinal - diaInicial - 1;
//		somar o restante do dia inicial com as horas do dia final em segundos
//		encontras dias(2 no máximo), horas, min, seg;
		Scanner entrada = new Scanner(System.in);
		String dia1, dia2, horaInicial, horaFinal;
		String [] dia1Split = new String[2], dia2Split = new String[2], horaInicialSplit = new String[2], horaFinalSplit = new String[2];
		
		dia1 = entrada.nextLine();
		dia1Split = dia1.split(" ");
		horaInicial = entrada.nextLine();
		horaInicialSplit = horaInicial.split(" : ");
//		
		dia2 = entrada.nextLine();
		dia2Split = dia2.split(" ");
		horaFinal = entrada.nextLine();
        entrada.close();
		horaFinalSplit = horaFinal.split(" : ");
		
		
		int entre = Integer.parseInt(dia2Split[1])-Integer.parseInt(dia1Split[1]) - 1;//dias completos
		
//		quantidade de horas até terminar o dia: a partir do inicio; 24:00:00 - horaIni
		int restoDia1EmSeg = 86400 - (Integer.parseInt(horaInicialSplit[0])*3600 + Integer.parseInt(horaInicialSplit[1])*60+ Integer.parseInt(horaInicialSplit[2]));
		int horasDia2EmSeg = Integer.parseInt(horaFinalSplit[0])*3600 + Integer.parseInt(horaFinalSplit[1])*60+ Integer.parseInt(horaFinalSplit[2]);
		
		int horasRestantesDias = restoDia1EmSeg+horasDia2EmSeg;
		int dias = (horasRestantesDias/86400)+ entre;//dias completos+dias, se for o caso (máximo 2d)
		int horas = (horasRestantesDias%86400)/3600;
		int min = (((horasRestantesDias%86400))%3600)/60;
		int seg = (((horasRestantesDias%86400))%3600)%60;		
		
		System.out.println(dias+" dia(s)\n"+horas+" hora(s)\n"+min+" minuto(s)\n"+seg+" segundo(s)");
		
		
	}

}
