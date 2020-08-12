package level_two_capstone1;

import java.util.*;

public class Poised_Engineering {
	
	// This method gathers all the information on the project
	public static project getData() {
		
		System.out.print("Enter Project Number: ");
		Scanner n = new Scanner(System.in);
		int projNum = n.nextInt();
		
		System.out.print("Enter Project Name: ");
		n = new Scanner(System.in);
		String projName = n.nextLine();
		
		System.out.print("Enter Type of Building: ");
		n = new Scanner(System.in);
		String buildType = n.nextLine();
		
		System.out.print("Enter Project Address: ");
		n = new Scanner(System.in);
		String projAddress = n.nextLine();
		
		System.out.print("Enter ERF Number: ");
		n = new Scanner(System.in);
		int erfNumber = n.nextInt();
		
		System.out.print("Enter Project Fee: ");
		n = new Scanner(System.in);
		int projFee = n.nextInt();
		
		System.out.print("Enter Amout Paid: ");
		n = new Scanner(System.in);
		int amountPaid = n.nextInt();
		
		System.out.print("Enter Deadline of Project: ");
		n = new Scanner(System.in);
		String projDeadline = n.nextLine();
		
		architect arch = getDataArch();
		contractor con = getDataCon();
		customer cust = getDataCust();
		
		return new project(projNum, projName, buildType, projAddress, erfNumber, projFee, amountPaid, projDeadline, arch, con, cust);
	}
	
	// This method gathers all the information on the architect an returns the object of the architect
	public static architect getDataArch() {
		
		System.out.print("Enter Architect Name: ");
		Scanner n = new Scanner(System.in);
		String archName = n.nextLine();
		
		System.out.print("Enter Architect tell Number: ");
		n = new Scanner(System.in);
		String archNum = n.nextLine();
		
		System.out.print("Enter Architect email address: ");
		n = new Scanner(System.in);
		String archEmail = n.nextLine();
		
		System.out.print("Enter Architect address: ");
		n = new Scanner(System.in);
		String archAddress = n.nextLine();
		
		return new architect(archName, archNum, archEmail, archAddress);
	}
	
	// This method gathers information on the constructor and returns the object of the constructor
	public static contractor getDataCon() {
		
		System.out.print("Enter Contractor Name: ");
		Scanner n = new Scanner(System.in);
		String conName = n.nextLine();
		
		System.out.print("Enter Contractor tell Number: ");
		n = new Scanner(System.in);
		String conNum = n.nextLine();
		
		System.out.print("Enter Contractor email address: ");
		n = new Scanner(System.in);
		String conEmail = n.nextLine();
		
		System.out.print("Enter Contractor address: ");
		n = new Scanner(System.in);
		String conAddress = n.nextLine();
		
		return new contractor(conName, conNum, conEmail, conAddress);
	}
	
	// This method gathers information on the customer and returns the object of the customer
	public static customer getDataCust() {
		
		System.out.print("Enter Customer Name: ");
		Scanner n = new Scanner(System.in);
		String custName = n.nextLine();
		
		System.out.print("Enter Customer tell Number: ");
		n = new Scanner(System.in);
		String custNum = n.nextLine();
		
		System.out.print("Enter Customer email address: ");
		n = new Scanner(System.in);
		String custEmail = n.nextLine();
		
		System.out.print("Enter Customer address: ");
		n = new Scanner(System.in);
		String custAddress = n.nextLine();
		
		return new customer(custName, custNum, custEmail, custAddress);
	}
    
	// Main method where everything is executed
	public static void main(String[] args) {
		
		// Call the method to run the information gathering process 
		project p1 = getData();
		
		// Print a menu for the user to make choices on what to do
		System.out.println("Main Menu:\n" + "To change project due date enter - d: \n" + "To change the amount paid enter - p: \n" + "To change the constructors name enter - c: \n" + "To finalize the project enter - f: ");
		Scanner n = new Scanner(System.in);
		String menuSelect = n.nextLine();
		
		// If user selects d, allow user to change the due date
		if (menuSelect.equalsIgnoreCase("d")) {
			System.out.println("Enter a new due date: ");
			n = new Scanner(System.in);
			String newDate = n.nextLine();
			p1.setDeadline(newDate);
			System.out.println("Due date successfully changed!");
		}
		// If user selects p, allow the user to change the new paid amount
		if (menuSelect.equalsIgnoreCase("p")) {
			System.out.println("Enter the new paid amount: ");
			n = new Scanner(System.in);
			int newAmount = n.nextInt();
			p1.setAmount(newAmount);
			System.out.println("Amount already paid successfully changed!");
		}
		// If the user selects c, allow the user to change tell number and email address
		if (menuSelect.equalsIgnoreCase("c")) {
			System.out.println("Enter the contractors new tell number: ");
			n = new Scanner(System.in);
			String newNum = n.nextLine();
			p1.getContractor().setTellNumber(newNum);
			System.out.println("Tell number successfully changed!");
			
			System.out.println("Enter the contractors new email: ");
			n = new Scanner(System.in);
			String newEmail = n.nextLine();
			p1.getContractor().setEmail(newEmail);
			System.out.println("Email successfully changed!");
		}
		// If user selects f, finalize the project and print an invoice
		if (menuSelect.equalsIgnoreCase("f")) {
			System.out.println("\nCustomer Invoice: \n" + "------------------------");
			System.out.println("Name: " + p1.getCustomer().getName() + "\n" + "Tell Number: " + p1.getCustomer().getTellNumber() + "\n" + "Email: " + p1.getCustomer().getEmail() + "\n" + "Address: " + p1.getCustomer().getAddress());
			int amountOwed = p1.getProjFee() - p1.getAmountPaid();
			System.out.println("Amount still owing: " + amountOwed);
		}
	}

}
