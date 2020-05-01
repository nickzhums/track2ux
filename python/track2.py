import os
import azure.mgmt.compute  # use track2
import azure.mgmt.network  # use track1, network track2 does not ready.
import azure.mgmt.resource  # use track2
import uuid
from azure.identity import ClientSecretCredential
from azure.identity import DefaultAzureCredential
# from azure.common.credentials import ServicePrincipalCredentials

class createVMSample(object):

    def __init__(self, group_name, location):
        self.location = "westus2"

        #tenant_id = os.environ.get("AZURE_TENANT_ID")
        #client_id = os.environ.get("AZURE_CLIENT_ID")
        #client_secret = os.environ.get("AZURE_CLIENT_SECRET")
        subscription_id = "6f341b56-77fd-41d5-b8df-7229d50461b6"
        self.subscription_id = subscription_id

        #client_credentials = ClientSecretCredential(
        #    client_id=client_id,
        #    client_secret=client_secret,
        #    tenant_id=tenant_id
        #)

        # service_credentials = ServicePrincipalCredentials(
        #     client_id=client_id,
        #     secret=client_secret,
        #     tenant=tenant_id
        # )
        credentials = DefaultAzureCredential()

        self.compute_client = azure.mgmt.compute.ComputeManagementClient(credential=credentials, subscription_id=self.subscription_id)
        self.network_client = azure.mgmt.network.NetworkManagementClient(credential=credentials, subscription_id=self.subscription_id)
        self.resource_client = azure.mgmt.resource.ResourceManagementClient(credential=credentials, subscription_id=self.subscription_id)

        #self.compute_client = azure.mgmt.compute.ComputeManagementClient(credential=client_credentials, subscription_id=self.subscription_id)
        #self.network_client = azure.mgmt.network.NetworkManagementClient(credential=client_credentials, subscription_id=self.subscription_id)
        #self.resource_client = azure.mgmt.resource.ResourceManagementClient(credential=client_credentials, subscription_id=self.subscription_id)

        group_name = "pythonsdk-test-" + str(uuid.uuid1())
        self.group = self.resource_client.resource_groups.create_or_update(
            group_name,
            {'location': self.location}
        )

        self.group.tags = {
          "environment":"test",
          "department":"tech"
        }
        self.updated_group = self.resource_client.resource_groups.create_or_update(group_name, self.group)

        self.group_list = self.resource_client.resource_groups.list()
        for g in self.group_list:
          print(g.name)

        async_op = self.resource_client.resource_groups.begin_delete(group_name)
        async_op.wait()

        print('finished')
    # TODO: need change to track2 after network track2 ready.
    def create_virtual_network(self, group_name, location, network_name, subnet_name):
      
        result = self.network_client.virtual_networks.begin_create_or_update(
            group_name,
            network_name,
            {
                'location': location,
                'address_space': {
                    'address_prefixes': ['10.0.0.0/16']
                }
            },
        )
        result_create = result.result()

        async_subnet_creation = self.network_client.subnets.begin_create_or_update(
            group_name,
            network_name,
            subnet_name,
            {'address_prefix': '10.0.0.0/24'}
        )
        subnet_info = async_subnet_creation.result()
          
        return subnet_info

    # TODO: need change to track2 after network track2 ready.
    def create_network_interface(self, group_name, location, nic_name, subnet):

        async_nic_creation = self.network_client.network_interfaces.begin_create_or_update(
            group_name,
            nic_name,
            {
                'location': location,
                'ip_configurations': [{
                    'name': 'MyIpConfig',
                    'subnet': {
                        'id': subnet.id
                    }
                }]
            }
        )
        nic_info = async_nic_creation.result()

        return nic_info.id

    def create_vm(self, vm_name, network_name, subnet_name, interface_name):
        group_name = self.group.name
        location = self.location

        # create network
        subnet = self.create_virtual_network(group_name, location, network_name, subnet_name)
        nic_id = self.create_network_interface(group_name, location, interface_name, subnet)

        # Create a vm with empty data disks.
        BODY = {
          "location": "eastus",
          "hardware_profile": {
            "vm_size": "Standard_D2_v2"
          },
          "storage_profile": {
            "image_reference": {
              "sku": "2016-Datacenter",
              "publisher": "MicrosoftWindowsServer",
              "version": "latest",
              "offer": "WindowsServer"
            },
            "os_disk": {
              "caching": "ReadWrite",
              "managed_disk": {
                "storage_account_type": "Standard_LRS"
              },
              "name": "myVMosdisk",
              "create_option": "FromImage"
            },
            "data_disks": [
              {
                "disk_size_gb": "1023",
                "create_option": "Empty",
                "lun": "0"
              },
              {
                "disk_size_gb": "1023",
                "create_option": "Empty",
                "lun": "1"
              }
            ]
          },
          "os_profile": {
            "admin_username": "testuser",
            "computer_name": "myVM",
            "admin_password": "Aa1!zyx_",
            "windows_configuration": {
              "enable_automatic_updates": True  # need automatic update for reimage
            }
          },
          "network_profile": {
            "network_interfaces": [
              {
                "id": nic_id,
                "properties": {
                  "primary": True
                }
              }
            ]
          }
        }
        result = self.compute_client.virtual_machines.begin_create_or_update(group_name, vm_name, BODY)
        result = result.result()


def main():
    print("init sample.")
    sample = createVMSample('testgroupvm', 'eastus')

    print("create vm ...")
    sample.create_vm('testvm', 'testnetwork', 'testsubnet', 'testinterface')

    print("finish.")


if __name__ == '__main__':
    main()
