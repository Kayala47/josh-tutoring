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
		
		Animal el = new Elephant("Sheila");
		
		System.out.println(el.getValue());
		
		
		System.out.println("Welcome!");
		
		//Josh's HW:
		//turn local variables in constructors to global
		//finish the follwoing steps:
		
		//feed all the animals
		/*
		 * 1. Check how much food we have - CEO
		 * 2. See how much animals eat - Animal
		 * 3. How much we have after each animal - Feeder
		 * 4. How much we have after the whole day - restock - CEO
		 * 
		 */
		
		Feeder feeder =  (Feeder) workerList[0];
		int food = feeder.getFood();
		
//		double ex1 = 10.0;
//		double ex2 = 5;
//		double result = (int) ex1 - ex2;
		
		System.out.println(food);
		
		
		//for loop
		for (int i = 0; i < animalList.length; i++) {
			
			Animal animal = animalList[i];
			
			int foodEaten = animal.howMuchFood();
			
			if (food < foodEaten) {
				System.out.println("Hey CEO, I bought more food!");
				feeder.restockFood();
				
			} 
			
			feeder.feed(animal);
		
			
		}
		
		
//		//while loop
//		int i = 0;
//		while (i < animalList.length) {
//			
//			
//			i++;
//		}
		
		
		
		
		//sell tickets
		
		Cashier cashier = (Cashier) workerList[1];
		double money = 0;
		
		for (int tickets = cashier.getTickets(); tickets > 0; tickets--) {
			
			money += cashier.TICKET_PRICE;
			
			
		}
		
		
		
		
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
		
		workerList[0] = new Feeder("Grover", 20.0, 100);
		
		workerList[1] = new Cashier("Luke", 22.0, 100);
		
		
		return workerList;
		// TODO Auto-generated method stub
		
		//return an array of workers
		
	}
	private static Animal[] createAnimals() {
		
		Animal[] animalList = new Animal[4];
		
		animalList[0] = new Owl("Greg");
		animalList[1] = new Eagle("Henry");
		animalList[2] = new Elephant("Sheila");
		animalList[3] = new Liger("Jack");
		
		
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
