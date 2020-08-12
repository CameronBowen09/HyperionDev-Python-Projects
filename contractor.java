package level_two_capstone1;

public class contractor {
	
	// Initialize attributes below
	private String name;
	private String tellNumber;
	private String email;
	private String address;
	
	// Constructor method for the project class
	public contractor(String name, String tellNumber, String email, String address) {
		this.name = name;
		this.tellNumber = tellNumber;
		this.email = email;
		this.address = address;
	}
	
	public String getName() {
		return name;
	}
	
	public void setConName(String n) {
		name = n;
	}
	
	public String getTellNumber() {
		return tellNumber;
	}
	
	public void setTellNumber(String number) {
		tellNumber = number;
	}
	
	public String getEmail() {
		return email;
	}
	
	public void setEmail(String emailAddress) {
		email = emailAddress;
	}
	
	public String getAddress() {
		return address;
	}
	
	public void setConAddress(String roadAddress) {
		address = roadAddress;
	}
	
	// This method formats all the information into an easily readable format
	public String toString() {
		String output = "Name: " + name;
		output += "\nCellphone Number: " + tellNumber;
		output += "\nEmail Address: " + email;
		output += "\nPhysical Address: " + address;
		return output;
	}
}
