// Создание запроса и ответа NET для доступа к данным из Интернета
using System;
using System.IO;
using System.Net;
using System.Text;

namespace Khasaev
{
    public class RequestGet
    {
        public static void Main()
        {
         	
            WebRequest request = WebRequest.Create("https://github.com/warhogz");
            request.Credentials = CredentialCache.DefaultCredentials;
            HttpWebResponse response = (HttpWebResponse)request.GetResponse();
            Console.WriteLine(response.StatusDescription);

                
            Stream dataStream = response.GetResponseStream();
            StreamReader reader = new StreamReader(dataStream);
            string responseFromServer = reader.ReadToEnd();
            Console.WriteLine(responseFromServer);

            if (response == null || response.StatusCode != HttpStatusCode.OK)
            {
                // failed
            }
            else
            {
                Console.WriteLine("\n========================================================================================================================");
                Console.WriteLine("\n                                                   САЙТ ДОСТУПЕН...\n");
                Console.WriteLine("========================================================================================================================\n");
            }
            
            reader.Close();
            dataStream.Close();
            response.Close();
            Console.ReadLine();
        }
    }
}