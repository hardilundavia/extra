using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp5
{
    class Program
    {
        static void Main(string[] args)
        {
            int i;
            string[] str = new string[100];
            Console.WriteLine(" Enter how many strings you want to store : ");
            int no = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("strings you entered : " + no);

            for (i = 0; i < no; i++)
            {
                Console.Write("\nEnter string" +i+" : ");
                str[i] = Console.ReadLine();
            }
            Console.WriteLine("strings in array \n");
            for (i = 0; i < no; i++)
            {
                Console.WriteLine("\n string : " +str[i]);
                
            }
         

                Console.ReadKey();
        }
    }
}
