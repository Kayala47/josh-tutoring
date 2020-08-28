package zoo;

public class Feeder extends Worker {
	
	public double salary;
	public int food;
	
	public int foodUsed;
	
	public Feeder(String name, double salary, int food) {
		
		super(name, salary);
		
		this.food = food;
		this.salary = salary;
		
	}
	
	public void restockFood() {
		
		food += 100;
		
		
	}
	
	public int getFood() {
		return food;
	}
	
	public void feed(Animal animal) {
		
		animal.getFed();
		
		foodUsed = animal.howMuchFood();
		
		
		food -= foodUsed; //food = food - foodUsed means exactly the same thing
		
		
	}
	
	
	
	

}
