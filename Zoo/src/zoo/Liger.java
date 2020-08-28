package zoo;

public class Liger extends Animal {

	
	//what do they eat?
	public static final String FOOD = "Beef or chicken";
	
	//how often do they eat per day?
	public static final int TIMES_A_DAY = 3;
	
	public static final int LBS_DAY = 5;
	
	//how much are they worth?
	public static final int VALUE = 20;
	
	public static final String DEFAULT_NAME = "jack";
	
	public static String name;
	
	public static boolean alreadyFed;
	
	
	public Liger(String name){
		
		super("Liger");
		
		name = DEFAULT_NAME;
		
		this.name = name;
		
	
		
	}
	
	public boolean amHungry() {
		
		
		return !alreadyFed;
	}
	
	public int howMuchFood() {
		return LBS_DAY * TIMES_A_DAY;
	}
	
	

}