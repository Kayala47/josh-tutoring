package zoo;

public class Animal extends Zoo {
	
	public Animal animal;
	
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
	
	

}
