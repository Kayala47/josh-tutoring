package zoo;

public class Elephant extends Animal {

	
	//what do they eat?
	public static final String FOOD = "Grass or small plants";
	
	//how often do they eat per day?
	public static final int TIMES_A_DAY = 3;
	
	//how much are they worth?
	public static final int VALUE = 15;
	
	public static final String DEFAULT_NAME = "Shella";
	
	public static String name;
	
	
	public Elephant(String name){
		
		super("Elephant");
		
		name = DEFAULT_NAME;
		
	
		
	}
	
	public boolean amHungry() {
		
		
		return true;
	}
	
	

}
