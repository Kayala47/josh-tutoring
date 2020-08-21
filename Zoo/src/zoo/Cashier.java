package zoo;

public class Cashier extends Worker {
	
	public int Money;
	
	public Cashier(int strength, String name, float salary, int speed) {
		
		super(name, salary);
		
		
		
		
	}
	
	public void getFood() {
		
		Money += 3;
		
		
	}
	
	

}
