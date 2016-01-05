

import java.awt.Color;
import java.util.Random;

import javax.swing.BorderFactory;
import javax.swing.JPanel;
import javax.swing.border.Border;

public class Grille extends JPanel{

	private Case[][] tab;
	private Agent[] listeAgent;
	
	Case case1 = new Case();
	Random rand = new Random();
	Border blackline = BorderFactory.createLineBorder(Color.black,1);
	
	public Grille(int x,int y){
		this.tab= new Case[x][y];
		
		for(int i=0;i<x;i++){
			for (int j=0;j<y;j++){
				JPanel case1 = new JPanel();
				this.setBorder(blackline);
				float r = rand.nextFloat();
				float g = rand.nextFloat();
				float b = rand.nextFloat();
				Color randomColor = new Color(r, g, b);
				case1.setBackground(randomColor);
				this.add(case1);
				this.setVisible(true);
			}
		}
		
	}
	
	public Case[][] getTab() {
		return tab;
	}
	public void setTab(Case[][] tab) {
		this.tab = tab;
	}
	public Agent[] getListeAgent() {
		return listeAgent;
	}
	public void setListeAgent(Agent[] listeAgent) {
		this.listeAgent = listeAgent;
	}

	
}
