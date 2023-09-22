using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hesap Makinesi");
        Console.WriteLine("----------------");

        Console.Write("Birinci sayıyı girin: ");
        double sayi1 = Convert.ToDouble(Console.ReadLine());

        Console.Write("İkinci sayıyı girin: ");
        double sayi2 = Convert.ToDouble(Console.ReadLine());

        double toplam = sayi1 + sayi2;

        Console.WriteLine($"Sonuç: {sayi1} + {sayi2} = {toplam}");

        Console.WriteLine("----------------");

        // Konsolu açık tutmak için bekleme
        Console.ReadKey();
    }
}