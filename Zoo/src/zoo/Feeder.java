package zoo;

public class Feeder extends Worker {
	
	public int Money;
	
	public Feeder(int strength, String name, float salary, int speed) {
		
		super(name, salary);
		
		
		
		
	}
	
	public void getFood() {
		
		Money += 3;
		
		
	}
	
	

}
