# Quickstart Tutorial - Resource Management using Azure .NET SDK

In this basic quickstart guide, we will walk you through how to authenticate to Azure using our .NET SDK and start interacting with Azure resources.  There are several possible approaches to authentication. This document illustrates the most common scenario

## Prerequisites
You will need the following values to authenticate to Azure
- **Client ID**
- **Client Secret**
- **Tenant ID**
- **Subscription ID**

These values can be obtained from the portal, here's the instructions:

#### Get Subscription ID
1. Login into your azure account
2. Select Subscriptions in the left sidebar
3. Select whichever subscription is needed, for our UX Study purpose, please use "Visual Studio Enterprise"
4. Click on overview
5. Copy the Subscription ID

#### Get Client ID
1. Login into your azure account
2. Select azure active directory in the left sidebar
3. Click "App Registrations"
4. Select the application which you have created, in our case, this refers to "sdk"
5. Copy "Application (client) ID"

#### Get Client Secret
1. Login into your azure account
2. Select azure active directory in the left sidebar
3. Click "App Registrations" in the left sidebar
4. Click "Certificates & Secrets"
5. Click "+ New client secret"
6. Type description and click "Add"
7. Copy and store the key value. You won’t be able to retrieve it after you leave this page.

#### Get Tenant ID
1. Login into your azure account
2. Select azure active directory in the left sidebar
3. Click "App Registrations" in the left sidebar
4. Select the application which you have created, in our case, this refers to "sdk"
5. Copy "Directory (tenant) ID"

#### Setting Environment Variables
After you obtained the values, you need to set the following values as your environment variables

-   `AZURE_CLIENT_ID`
-   `AZURE_CLIENT_SECRET`
-   `AZURE_TENANT_ID`

To set the following environment variables on your development system:

```
export AZURE_CLIENT_ID="__CLIENT_ID__"
export AZURE_CLIENT_SECRET="__CLIENT_SECRET__"
export AZURE_TENANT_ID="__TENANT_ID__"
```

## Authentication and Creating REST Client

Now that the environment is setup, all you need to do is to create an authenticated client. Our default option is to use **DefaultAzureCredentials** and in this guide we have picked **Resource** as our target service. To authenticate to Azure and create a REST client, simply do the following:
```
using  Azure.Identity;
using  Azure.Management.Resource;
using  Azure.Management.Resource.Models;
...
var subscriptionId = "yourSubscriptionId"
var resourceClient = new ResourceClient(subscriptionId, new DefaultAzureCredential(true));
```

More information regarding .NET SDK authentication can be found at 
[here](https://docs.microsoft.com/en-us/dotnet/api/overview/azure/identity-readme?view=azure-dotnet) 

## Managing Resources

Now that we are authenticated, we can use our REST client to make API calls. Let's create a resource group and demostrate REST client's usage

**Create a resource group**

```
var location = "westus2";
var resourceGroupName = "myResourceGroupName";
var result = await resourceClient.ResourceGroups.CreateOrUpdateAsync(resourceGroupName, new ResourceGroup(location));
```

**Update a resource group**

```
var resourceGroupName = "myResourceGroupName";
// Create tags
var tags = new Dictionary<string, string>();
tags.Add("environment","dev");
tags.Add("business","education");
group.setTags(tags);
// Update resource group
var result = await resourceClient.ResourceGroup.CreateOrUpdateAsync(resourceGroupName, group)

```
 
**List all resource groups**

```
// List all resource groups
var result = await resourceClient.ResourceGroups.ListAsync();
foreach (var resourceGroup in result) {
    Console.WriteLine("Resouce group: " + resourceGroup.Name);
}
```

**Delete**

```
// Delete a resource group
await resourceClient.ResourceGroups.DeleteAsync(resourceGroupName)
```