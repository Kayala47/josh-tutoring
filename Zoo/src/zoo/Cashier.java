package zoo;

public class Cashier extends Worker {
	
	public int money;
	public String name;
	public double salary;
	public int tickets;
	
	public static int TICKET_PRICE = 12;
	
	
	public Cashier(String name, double salary, int tickets) {
		
		super(name, salary);
		this.name = name;
		this.salary = salary;
		this.tickets = tickets;
		
	
		
		
	}
	
	public int getTickets() {
		return tickets;
	}
	

	

}
