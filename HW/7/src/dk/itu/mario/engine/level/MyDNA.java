package dk.itu.mario.engine.level;

import java.util.Random;
import java.util.*;

public class MyDNA extends DNA {
	public int numGenes = 0;

	// Return a new DNA that differs from this one in a small way.
	// Do not change this DNA by side effect; copy it, change the copy, and return the copy.
	public MyDNA mutate () {
		MyDNA copy = new MyDNA();
		String characters = "abcdefghijklmnopqrstuvwxyz";
		Random random = new Random();
		int change = random.nextInt(this.getChromosome().length());
		copy.setChromosome(this.getChromosome().substring(0, change) + characters.charAt(random.nextInt(characters.length())) + this.getChromosome().substring(change + 1));
		return copy;
	}

	// Do not change this DNA by side effect
	public ArrayList<MyDNA> crossover (MyDNA mate) {
		ArrayList<MyDNA> offspring = new ArrayList<MyDNA>();

		Random random = new Random();
		int split = random.nextInt(this.getChromosome().length());

		MyDNA child1 = new MyDNA();
		MyDNA child2 = new MyDNA();
		child1.setChromosome(this.getChromosome().substring(0, split) + mate.getChromosome().substring(split, mate.getChromosome().length()));
		child2.setChromosome(mate.getChromosome().substring(0, split) + this.getChromosome().substring(split, this.getChromosome().length()));
		offspring.add(child1);
		offspring.add(child2);
		return offspring;
	}

	public int compareTo(MyDNA other) { return super.compareTo(other); }

	public String toString () { return super.toString(); }

	public void setNumGenes (int n)
	{
		numGenes = n;
	}
}