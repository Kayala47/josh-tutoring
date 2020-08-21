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
	
	public void getFood() {
		
		food += 10;
		
		
	}
	
	public void feed(Animal animal) {
		
		animal.getFed();
		
		foodUsed = animal.howMuchFood();
		
		
		food -= foodUsed; //food = food - foodUsed means exactly the same thing
		
		
	}
	
	
	
	

}
