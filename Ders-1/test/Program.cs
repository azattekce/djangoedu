// See https://aka.ms/new-console-template for more information




class Program
{
    static void Main()
    {
        Console.WriteLine("Hesap Makinesi");

        var dizi = new int[]{ 1, 2, 5, 6, 8, 9, 10, 3, 4 };
        var dizi2=new int[dizi.Length];

        Array.Copy(dizi,dizi2,dizi.Length);

        dizi2[6]=dizi2[6]*2;
        foreach(var i in dizi)
        {
        Console.WriteLine("{0} . eleman",i);
        }


     Console.WriteLine("**************");
        foreach(var i in dizi2)
                {
                Console.WriteLine("{0} . eleman",i);
                }

        Console.ReadKey();
    }
}