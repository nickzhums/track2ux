# Welcome to Python SDK UX Study

In this basic quickstart guide, we will walk you through how to authenticate to Azure using our Python SDK and start interacting with Azure resources. There are several possible approaches to authentication. This document illustrates the most common scenario

## Prerequisites
You will need the following values to authenticate to Azure
- Client ID
- Client Secret
- Tenant ID
- Subscription ID

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

To set environment variables, you can refer to these documentation
[Windows](https://www.computerhope.com/issues/ch000549.htm) / [Linux](https://www.serverlab.ca/tutorials/linux/administration-linux/how-to-set-environment-variables-in-linux/)

## Authentication and Creating REST Client

Now that the environment is setup, all you need to do is to create an authenticated client. Our default option is to use **DefaultAzureCredentials** and in this guide we have picked **Resource** as our target service. To authenticate to Azure and create a REST client, simply do the following:
```
import azure.mgmt.resource
import azure.mgmt.network
import azure.mgmt.compute
from azure.identity import DefaultAzureCredential;
...
subscription_id = "your_subscription_id"
credentials = DefaultAzureCredential()
resource_client = azure.mgmt.resource.ResourceManagementClient(credential=credentials, subscription_id=self.subscription_id)
```

More information regarding Python SDK authentication using Azure Identity can be found at 
[here](https://docs.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python) 

## Managing Resources

Now that we are authenticated, we can use our REST client to make API calls. Let's create a resource group and demostrate REST client's usage

**Create a resouce group**

```
location = "westus2"
group = resource_client.resource_groups.create_or_update(
    group_name,
    {'location': location}
)
```

**Update**
group.tags = {
    "environment":"test",
    "department":"tech"
}
updated_group = resource_client.resource_groups.create_or_update(group_name, group)

**List all resouce groups**
```
group_list = self.resource_client.resource_groups.list()
for g in group_list:
    print_resource_group(g)

```
**Delete**
delete_async_op = self.resource_client.resource_groups.begin_delete(group_name)
delete_async_op.wait()


```