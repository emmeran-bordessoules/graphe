
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
	
	Border blackline = BorderFactory.createLineBorder(Color.black,1);
	
	public Case(){
		this.setBorder(blackline);
	}


	public Case(int x, int y, Terrain tcase){
		this.x=x;
		this.y=y;
		this.tcase=tcase;
		this.setBorder(blackline);
		
	}
	
	public int getX() {
		return x;
	}


	public void setX(int x) {
		this.x = x;
	}


	public int getY() {
		return y;
	}


	public void setY(int y) {
		this.y = y;
	}


	public Terrain getTcase() {
		return tcase;
	}


	public void setTcase(Terrain tcase) {
		this.tcase = tcase;
	}
}
