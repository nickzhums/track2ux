
using System;
using System.Linq;
using System.Threading.Tasks;
using System.Collections;

using Azure.Identity;
using Azure.Management.Compute;
using Azure.Management.Network;
using Azure.Management.Resources;
using Azure.Management.Resources.Models;

namespace Track2UXCodeSample {
    static class Track2
    {
        public static async Task CreateResourceAsync(
            string subscriptionId,
            string resourceGroup,
            string location)
        {
            Console.WriteLine("test");
            var credentials = new DefaultAzureCredential(true);
            var resourceGroupClient = new ResourcesManagementClient(subscriptionId, credentials).GetResourceGroupsClient();
            var createdResourceGroup = await resourceGroupClient.CreateOrUpdateAsync("test_rng_name", new ResourceGroup(location));

            Console.WriteLine(createdResourceGroup.Value.Name);


        }

    }
}