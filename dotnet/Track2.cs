
using System;
using System.Linq;
using System.Threading.Tasks;
using System.Collections;

using Azure.Identity;
using Azure.Management.Compute;
using Azure.Management.Network;
using Azure.Management.Resources;

namespace Track2UXCodeSample {
    static class Track2
    {
        public static async Task CreateResourceAsync(
            string subscriptionId,
            string resourceGroup,
            string location)
        {
            Console.WriteLine("test");
            var resourceClient = new ResourcesClient(subscriptionId, new DefaultAzureCredential(true));
        }

    }
}