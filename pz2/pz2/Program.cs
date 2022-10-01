using System;
using System.IO;

namespace ReadWriteFiles
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Для записи введите 1/Для чтения 2");
            int a = int.Parse(Console.ReadLine());
            switch (a)
            {

                case 1:
                    {
                        string path = @"MyTest.txt";
                        if (!File.Exists(path))
                        {
                            File.Create(path).Close();
                        }
                        Console.WriteLine("Введите \"stop\" для прекращения записи в файл.");
                        Console.WriteLine();
                        {
                            using (var file = new StreamWriter(@"MyTest.txt"))
                            {
                                while (true)
                                {
                                    Console.Write("Введите текст для записи: ");

                                    // Читаем введёный текст 
                                    var line = Console.ReadLine();

                                    // Если ввели stop прерываем цикл 
                                    if (line == "stop")
                                        break;

                                    // Пишем в файл.
                                    file.WriteLine(line);
                                    
                                }
                            }
                           
                        }
                        break;
                    }
                case 2:
                    String liney;
                    try
                    {
                        
                        StreamReader sr = new StreamReader(@"MyTest.txt");
                        //Читаем первую линию текста
                        liney = sr.ReadLine();
                        //Продолжаем читать до конца
                        while (liney != null)
                        {
                            
                            Console.WriteLine(liney);
                           
                            liney = sr.ReadLine();
                        }
                        //close the file
                        sr.Close();
                        Console.ReadLine();
                    }
                    catch (Exception)
                    {

                    }
                   
                    break;
            }
        }
    }
}