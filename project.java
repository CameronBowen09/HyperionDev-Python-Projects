package level_two_capstone1;

public class project {
	
	// Initialize attributes below
	private architect architect;
	private contractor contractor;
	private customer customer;
	private int projNum;
	private String projName;
	private String buildType;
	private String projAddress;
	private int erfNumber;
	private int projFee;
	private int amountPaid;
	private String projDeadline;
	
	// Constructor method for the project class
	public project(int projNum, String projName, String buildType, String projAddress, int erfNumber, int projFee, int amountPaid, String projDeadline,architect arch, contractor con, customer cust) {
		this.projNum = projNum;
		this.projName = projName;
		this.buildType = buildType;
		this.projAddress = projAddress;
		this.erfNumber = erfNumber;
		this.projFee = projFee;
		this.amountPaid = amountPaid;
		this.projDeadline = projDeadline;
		architect = arch;
		contractor = con;
		customer = cust;
		
	}
	
	public architect getArchitect() {
		return architect;
	}
	
	public void setArchitect(architect arch) {
		architect = arch;
	}
	
	public contractor getContractor(){
		return contractor;
	}
	
	public void setContractor(contractor con) {
		contractor = con;
	}
	
	public customer getCustomer() {
		return customer;
	}
	
	public void setCustomer(customer cust) {
		customer = cust;
	}
	
	public int getProjNum() {
		return projNum;
	}
	
	public void setNumber(int number) {
		projNum = number;
	}
	
	public String getProjName() {
		return projName;
	}
	
	public void setProjName(String name) {
		projName = name;
	}
	
	public String getBuildType() {
		return buildType;
	}
	
	public void setBuildType(String build) {
		buildType = build;
	}
	
	public String getProjAddress() {
		return projAddress;
	}
	
	public void setAddress(String address) {
		projAddress = address;
	}
	
	public int getErfNumber() {
		return erfNumber;
	}
	
	public void setEFRNumber(int erfnum) {
		erfNumber = erfnum;
	}
	
	public int getProjFee() {
		return projFee;
	}
	
	public void setFee(int fee) {
		projFee = fee;
	}
	
	public int getAmountPaid() {
		return amountPaid;
	}
	
	public void setAmount(int amount) {
		amountPaid = amount;
	}
	
	public String getProjDeadline() {
		return projDeadline;
	}
	
	public void setDeadline(String deadline) {
		projDeadline = deadline;
	}
	
	// This method formats all the information into an easily readable format
	public String toString() {
		String output = "Project Number: " + projNum;
		output += "\nProject Name: " + projName;
		output += "\nBuilding Type: " + buildType;
		output += "\nProject Address: " + projAddress;
		output += "\nERF Number: " + erfNumber;
		output += "\nProject Fee: " + projFee;
		output += "\nAmount paid: " + amountPaid;
		output += "\nProject Deadline: " + projDeadline;
		return output;
	}
}
