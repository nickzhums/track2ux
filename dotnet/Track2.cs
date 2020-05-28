
using System;
using System.Linq;
using System.Threading.Tasks;
using System.Collections;
using System.Collections.Generic;

using Azure.Core.Pipeline;
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
            string resourceGroupName,
            string location)
        {
            Console.WriteLine("test");
            var credentials = new DefaultAzureCredential(true);
            
            //create
            var resourceGroupClient = new ResourcesManagementClient(subscriptionId, credentials).GetResourceGroupsClient();
            var resourceGroup = new ResourceGroup(location);
            resourceGroup = await resourceGroupClient.CreateOrUpdateAsync("test_rng_name", resourceGroup);
            //var createdResourceGroup = res.Value;

            Console.WriteLine(resourceGroup.Name);

            //update
            var tags = new Dictionary<string, string>();
            tags.Add("env","prod");
            tags.Add("scenario","test");
            resourceGroup.Tags = tags;
            var updatedResourceGroup = await resourceGroupClient.CreateOrUpdateAsync("test_rng_name", resourceGroup);


            //get
            AsyncPageable<ResourceGroup> response = await resourceGroupClient.ListAsync();
            await foreach (ResourceGroupPatchable resourceGroup in response) {
                Console.WriteLine(resourceGroup.Name);
            }



        }

    }
}