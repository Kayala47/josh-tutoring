package zoo;

public class Worker extends Zoo{
	
	public static final String DEFAULT_NAME = "Josh";
	public static final double DEFAULT_SALARY = 12.0;
	
	public double salary;
	public String name;
	
	
	public double ex1;
	public int ex2;
	public boolean ex5;
	
	public String ex3;
	public Animal ex4;


	
	public Worker(String name, double salary) {
		
		this.name = name;
		this.salary = salary;
		
		
		
		
		
		
	}
	
	public double getSalary() {
		return salary;
	}
	
	public int getFood() {
		return 0;
	}
	
	

}
