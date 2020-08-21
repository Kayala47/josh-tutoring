package zoo;

public class Cashier extends Worker {
	
	public int food;
	
	public Cashier(int strength, String name, float salary, int speed) {
		
		super(name, salary);
		
		
		
		
	}
	
	public void getFood() {
		
		food += 3;
		
		
	}
	
	

}
