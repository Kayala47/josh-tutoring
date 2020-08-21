package zoo;

public class Penguin extends Animal {
	
	//what do they eat?
	public static final String FOOD = "fish";
	
	//how often do they eat per day?
	public static final int TIMES_A_DAY = 3;
	
	//how much are they worth?
	public static final int VALUE = 8;
	
	public static final String DEFAULT_NAME = "Bob";
	
	public static String name;
	
	public static boolean alreadyFed;
	
	
	public Penguin(String name){
		
		super("Penguin");
		
		name = DEFAULT_NAME;
		
	
		
	}
	
	public boolean amHungry() {
		
		
		return !alreadyFed;
	}
	
	

}
