using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Area_cal a = new Area_cal();
            Console.WriteLine("Enter radious : ");
            double ra = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Area of circle : "+a.Area(ra));

            Console.WriteLine("Enter base  : ");
            double base1 = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter height  : ");
            double height = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Area of circle : " + a.Area(base1 , height));

            Console.WriteLine("Enter length  : ");
            int length = Convert.ToInt16(Console.ReadLine());
            Console.WriteLine("Enter width  : ");
            int width = Convert.ToInt16(Console.ReadLine());
            Console.WriteLine("Area of circle : " + a.Area(length, width));

            Console.WriteLine("Enter side : ");
            int side = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Area of circle : " + a.Area(side));
        }
    }
    class Area_cal
    {
        public const double PI = 3.14;
        public double Area(double r)
        {
            return PI * r *  r;
        }
        public double Area(double b, double h)
        {
            return 0.5 * b * h;
        }
        public int Area(int l, int w)
        {
            return l * w;
        }
        public int Area(int a)
        {
            return a * a;
        }
    }

}

