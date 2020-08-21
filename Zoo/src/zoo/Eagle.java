package zoo;

public class Eagle extends Animal {

	
	//what do they eat?
	public static final String FOOD = "Small mammals";
	
	//how often do they eat per day?
	public static final int TIMES_A_DAY = 3;
	
	//how much are they worth?
	public static final int VALUE = 16;
	
	public static final String DEFAULT_NAME = "Hank";
	
	public static String name;
	
	
	public Eagle(String name){
		
		super("Eagle");
		
		name = DEFAULT_NAME;
		
	
		
	}
	
	public boolean amHungry() {
		
		
		return true;
	}
	
	

}