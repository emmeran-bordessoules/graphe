

import javax.swing.JPanel;

public class Grille extends JPanel{

	private Case[][] tab;
	private Agent[] listeAgent;
	
	public Grille(int x,int y){
		this.tab= new Case[x][y];		
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
