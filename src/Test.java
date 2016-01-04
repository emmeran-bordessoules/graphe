

import java.awt.Color;
import java.awt.GridLayout;

import javax.swing.BorderFactory;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.Border;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Terrain terrain1 = new Terrain('h',5,new Color(0,100,0));
		Terrain terrain2 = new Terrain('c',1,new Color(0,100,100));
		
		JFrame t = new JFrame();
		t.setSize(1000, 1000);
		Grille pan = new Grille ();
		Border blackline = BorderFactory.createLineBorder(Color.black,1); 
		
		   Case ptest = new Case(1,1,terrain1);
		   ptest.setBorder(blackline);
		   ptest.setBackground(terrain1.getCouleur());
		  
		   Case case2 = new Case(1,2,terrain2);
		   case2.setBorder(blackline);
		   case2.setBackground(terrain2.getCouleur());
		   
		   pan.add(ptest);
		   pan.add(case2);
		
		pan.setBorder(blackline);
		t.add(pan);
		t.setVisible(true);
		
		System.out.println("yolo");
	}

}
