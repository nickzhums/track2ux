# Welcome to .NET SDK UX Study

In this basic quickstart guide, we will walk you through how to authenticate to Azure using our .NET SDK and start interacting with Azure resources.  There are several possible approaches to authentication. This document illustrates the most common scenario

## Prerequisites
You will need to set the following values as environment variables 

-   `AZURE_CLIENT_ID`
-   `AZURE_CLIENT_SECRET`
-   `AZURE_TENANT_ID`

The information can be obtained from the portal, here's the instructions:
[How to get Azure credentials from portal](https://www.inkoop.io/blog/how-to-get-azure-api-credentials/](https://www.inkoop.io/blog/how-to-get-azure-api-credentials/)

To set these values as environment variables, you can follow these documentation
[Windows](https://www.computerhope.com/issues/ch000549.htm)
[Linux](https://www.serverlab.ca/tutorials/linux/administration-linux/how-to-set-environment-variables-in-linux/)

## Authentication

Now that the environment is setup, all you need to do is to create an authenticated client. Our default option is to use **DefaultAzureCredentials** and in this guide we have picked **Compute** as our target service. To authenticate to Azure and create a REST client, simply do the following:
```
using  Azure.Identity;
using  Azure.Management.Compute;
...

var  computeClient = new  ComputeClient(subscriptionId, new  DefaultAzureCredential(true));
```

More information regarding Azure SDK authentication can be found [here](https://azure.github.io/azure-sdk/posts/2020-02-25/defaultazurecredentials.html)


## Managing Resources

Now that we are authenticated, we can use our REST client to make API calls. Take compute for example, let's play around with xxx

**Create**

**Update**

**Get**

**Delete**



```