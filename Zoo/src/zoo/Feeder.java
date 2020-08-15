package zoo;

public class Feeder extends Worker {
	
	public int food;
	
	public Feeder(int strength, String name, float salary, int speed) {
		
		super(name, salary);
		
		
		
		
	}
	
	public void getFood() {
		
		food += 3;
		
		
	}
	
	

}
