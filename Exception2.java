import java.util.*;
class InvalidUsernameException extends Exception
{
	String msg;
	public InvalidUsernameException(String msg)
	{
		this.msg=msg;
	}
	public void getMsg()
	{
		System.out.println(msg);
	}
}
class Exception2
{
	public static void main(String args[])
	{
		String name;
		Scanner sc=new Scanner(System.in);
		try
		{
			System.out.println("Enter user name : ");
			name=sc.next();
			if(name.length()<4 || name.length()>10 || !name.matches("^[a-zA-Z0-9]*$"))
				throw new InvalidUsernameException("You have entered ivalid username : "+name);
		}
		catch(InvalidUsernameException e)
		{
			e.getMsg();
		}
	}
}