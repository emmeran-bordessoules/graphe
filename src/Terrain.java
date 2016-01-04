
import java.awt.Color;

public class Terrain {

	private char nom;
	private int temps;
	private Color couleur; 


public Terrain(char lenom, int letemps, Color lacouleur ){
	this.nom = lenom;
	this.temps = letemps;
	this.couleur = lacouleur;
}


public char getNom() {
	return nom;
}


public void setNom(char nom) {
	this.nom = nom;
}


public int getTemps() {
	return temps;
}


public void setTemps(int temps) {
	this.temps = temps;
}


public Color getCouleur() {
	return couleur;
}


public void setCouleur(Color couleur) {
	this.couleur = couleur;
}




}