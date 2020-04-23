using System;
using System.Threading.Tasks;

namespace Track2UXCodeSample
{
    class Program
    {
        static async Task Main(string[] args)
        {
            var subscripionId = "6f341b56-77fd-41d5-b8df-7229d50461b6";
            
            Console.WriteLine("Hello World!");

            await Track1.CreateResourceAsync(subscripionId, "", "westus2");
        }
    }
}
