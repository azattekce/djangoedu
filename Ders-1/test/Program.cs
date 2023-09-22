// See https://aka.ms/new-console-template for more information




class Program
{
    static void Main()
    {
        Console.WriteLine("Hesap Makinesi");

        var dizi = new int { 1, 2, 5, 6, 8, 9, 10, 3, 4 };
        for (int i = 0; i < dizi.Length; i++)
        {
        Console.WriteLine("{0} . eleman",dizi[i]);
        }

        Console.ReadKey();
    }
}