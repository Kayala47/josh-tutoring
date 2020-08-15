package zoo;

import java.awt.*;


public class Zoo {
	
	//make an array in Java
	static Animal[] animalList;
	static Worker[] workerList; 
	
	
	
	public static void main(String[] args) {
		
		//TODO: Create Animals
		/*
		 * Animals:
		 * 4
		 * Liger (Tiger & Lion cross)
		 * Owl
		 * Elephant
		 * Penguin
		 * Eagle
		 * 
		 * 
		 */
	/*
	 * 
	 * HW: make three new animals and one new worker	
	 */
		
		
		System.out.println("Zoo");
		
		
		
		animalList = createAnimals();
		
		
		//TODO: Create Workers
		/*
		 * Workers:
		 * 5 people everyday
		 * 
		 * Name, phone, salary
		 * 
		 * 
		 */
		
		workerList = createWorkers();
		
		//TODO: Find out what animals need
		
		
		
		//TODO: Make the workers do what's needed
		
		//TODO: Open for business
		
		
		
		// one line comment
		
		/*Functions
		 * 
		 * feedAnimal() - worker
		 * amHungry() - animal
		 * 
		 * amDirty() - animal
		 * cleanAnimal() - worker
		 * 
		 * buyFod() - zoo
		 * openZoo() - zoo
		 * 
		 * chargeMoney() - workers
		 * 
		 * variables:
		 * - how much food we have: zoo
		 * - how much money we have: zoo
		 * - how much to pay workers: zoo
		 * - how much is each animal worth: animal 
		 * - how much does each animal eat: animal
		 * - how much to charge customers: zoo
		 * 
		 * 
		 */
		
		
		
		
	}
	private static Worker[] createWorkers() {
		
		Worker[] workerList = new Worker[4];
		
		return workerList;
		// TODO Auto-generated method stub
		
		//return an array of workers
		
	}
	private static Animal[] createAnimals() {
		
		Animal[] animalList = new Animal[4];
		
		
		return animalList;
		// automatically create all animals
		
		//return an array of animals
		
		
		
	}
	/**
	 * This function does blah blah
	 * 
	 * 
	 */
	public static String getHello() {
		return "hello";
	}

}
