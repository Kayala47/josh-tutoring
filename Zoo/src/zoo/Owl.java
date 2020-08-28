package zoo;

public class Owl extends Animal {

	
	//what do they eat?
	public static final String FOOD = "Insects";
	
	//how often do they eat per day?
	public static final int TIMES_A_DAY = 3;
	
	public static final int LBS_FOOD = 1;
	
	//how much are they worth?
	public static final int VALUE = 11;
	
	public static final String DEFAULT_NAME = "Greg";
	
	public static String name;
	
	public static boolean alreadyFed;
	
	
	public Owl(String name){
		
		super("Owl");
		
		name = DEFAULT_NAME;
		
	
		
	}
	
	public boolean amHungry() {
		
		
		return !alreadyFed;
	}
	
	public int howMuchFood() {
		return LBS_FOOD * TIMES_A_DAY;
	}
	
	

}