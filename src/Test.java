

import java.awt.Color;
import java.awt.GridLayout;

import javax.swing.BorderFactory;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.Border;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Terrain chemin = new Terrain('c',5,Color.orange);
		Terrain pont = new Terrain('p',5,Color.black);
		Terrain herbe = new Terrain('h',20,Color.green);
		Terrain foret = new Terrain('f',70,Color.green.darker());
		Terrain eau = new Terrain('e',70,Color.blue);
		Terrain mur = new Terrain('m',70,Color.gray);
		
				
		
		JFrame t = new JFrame();
		t.setSize(1000, 500);
		Grille pan = new Grille(43,37);
		pan.setLayout(new GridLayout(43, 37));
		t.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 
		Border blackline = BorderFactory.createLineBorder(Color.black,1); 
		
		   Case ptest = new Case(1,1,chemin);
		   ptest.setBorder(blackline);
		   ptest.setBackground(chemin.getCouleur());
		  
		   Case case2 = new Case(1,2,pont);
		   case2.setBorder(blackline);
		   case2.setBackground(pont.getCouleur());
		   
		   Case case3 = new Case(1,3,herbe);
		   case3.setBorder(blackline);
		   case3.setBackground(herbe.getCouleur());
		   
		   Case case4 = new Case(1,4,foret);
		   case4.setBorder(blackline);
		   case4.setBackground(foret.getCouleur());
		   
		   System.out.println(case3.getY());
		   
		   pan.getTab()[ptest.getX()][ptest.getY()]=ptest;
		   pan.getTab()[case2.getX()][case2.getY()]=case2;
		   pan.getTab()[case3.getX()][case3.getY()]=case3;
		   pan.getTab()[case4.getX()][case4.getY()]=case4;
		   
		   /*pan.add(case4);
		   pan.add(case2);
		   pan.add(case3);
		   pan.add(ptest);*/
		
		pan.setBorder(blackline);
		t.add(pan);
		t.setVisible(true);
		
		System.out.println("yolo");
	}

}
