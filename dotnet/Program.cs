using System;
using System.Threading.Tasks;

namespace Track2UXCodeSample
{
    class Program
    {
        static async Task Main(string[] args)
        {
            //https://intellipaat.com/community/7050/the-client-with-object-id-does-not-have-authorization-to-perform-action-microsoft-datafactory-datafactories-datapipelines-read-over-scope
            var subscripionId = "6f341b56-77fd-41d5-b8df-7229d50461b6";
            
            Console.WriteLine("Hello World!");

            await Track2.CreateResourceAsync(subscripionId, "", "westus2");
        }
    }
}
