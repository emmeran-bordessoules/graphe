
import java.awt.Color;
import java.awt.GridLayout;

import javax.swing.BorderFactory;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.Border;

public class Case extends JPanel{
	private int x;
	private int y;
	private Terrain tcase;
	
	
	public Case(int x, int y, Terrain tcase){
		x=x;
		y=y;
		tcase=tcase;
		
	}
}
