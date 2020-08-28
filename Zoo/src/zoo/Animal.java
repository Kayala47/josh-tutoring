package zoo;

public class Animal extends Zoo {
	
	public Animal animal;
	
	public boolean alreadyFed;
	
	public static final int VALUE = 1;
	
	public Animal(String type) {
		
		if (type == "penguin") {
			
			animal = new Penguin("Tyler");
			
		}
		
		
		
	}
	
	public boolean amHungry() {
		
		return animal.amHungry();
		
		
//		return true;
		
	}
	
	public boolean amDirty() {
		
		
		return true;
	}
	
	public void getFed() {
		
		alreadyFed = true;
		
	}
	
	public int howMuchFood() {
		return 0;
	}
	
	public int getValue() {
		return this.VALUE;
	}
	
	

}
