import java.util.*;
class Exception1
{
	public static void main(String args[])
	{
		int sem;
		String name;
		Scanner sc=new Scanner(System.in);
		try
		{
		 	System.out.println("Enter Username : ");
			name=sc.next();
			System.out.println("Enter Semester : ");
			sem=sc.nextInt();

	   }
		catch(InputMismatchException e)
		{
			System.out.println(e);
		}
		finally
		{
			System.out.println("good bye");
		}
	}
}