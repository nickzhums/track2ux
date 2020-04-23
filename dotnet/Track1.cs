
using System;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.Azure.Management.ResourceManager;
using Microsoft.Azure.Management.ResourceManager.Fluent;
using Microsoft.Azure.Management.ResourceManager.Models;
using ResourceManagementClient = Microsoft.Azure.Management.ResourceManager.ResourceManagementClient;


namespace Track2UXCodeSample {
    static class Track1
    {
        public static async Task CreateResourceAsync(
            string subscriptionId,
            string resourceGroup,
            string location)
        {
            var credentials = SdkContext.AzureCredentialsFactory.FromFile("azureauth.properties");

            var resourceClient = new ResourceManagementClient(credentials);

            resourceClient.SubscriptionId = subscriptionId;

            Console.WriteLine(resourceClient);

            await resourceClient.ResourceGroups.CreateOrUpdateAsync("testname123", new ResourceGroup(location));

        }

    }
}