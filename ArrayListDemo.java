import java.util.*;
class ArrayListDemo
{
	public static void main(String args[])
	{
		ArrayList a=new ArrayList();
		Scanner sc=new Scanner(System.in);
		String v;
		int i;
		System.out.println("Enter value to add :");
		v=sc.next();
		a.add(v);

		System.out.println("Enter index : ");
		i=sc.nextInt();
		System.out.println("Enter value to add :");
		v=sc.next();
		a.add(i,v);
		System.out.println(a);

		System.out.println("Enter value to remove : ");
		String rm=sc.next();
		a.remove(rm);
		System.out.println(a);
		System.out.println("Enter value to add :");
		v=sc.next();
		a.add(v);
		System.out.println(a);

		int i1;
		System.out.println("Enter index : ");
		i1=sc.nextInt();
		a.remove(i1);
		System.out.println(a);
		System.out.println("Enter value to add :");
		v=sc.next();
		a.add(v);
		System.out.println(a);

		Collections.sort(a);
		System.out.println(a);

		System.out.println("Enter value to add :");
		v=sc.next();
		int i2=a1.set(i,v)
		System.out.println(a);
	}
}