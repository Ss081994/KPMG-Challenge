Solution Overview

This Azure Quick Start template deploys a 3 Tier Red Hat Solution on Azure.The Solution includes Web tier Servers, Application tier Servers and Database Tier Servers running Red Hat Enterprise Linux 7.3. Template follows Standard best practices for running a 3 tier Red Hat Linux IaaS workload on Azure. This template will deploy specified number of VMs in each tier as per requirement.

Template Solution Architecture

This template will deploy:

1. Four storage accounts: 3 for storing VM's disks of each tier, 1 for storing diagnostics data.
2.  One Virtual Network with four subnets.
3. 4 Network Security Group, one for each subnet.
4. External Load Balancer to load balance Web Traffic(HTTP & HTTPS) to web servers.
5. Internal Load Balancer to load balance traffic for app VM's.
6. 2 Public IP’s, one for external Load balancer and other for Jump VM.
7. 3 Virtual Machine Availability sets for Web Tier, Application Tier and Database tier.
8. One Jump VM to faclitate ssh access to all other tier VMs.
9. Multiple Red Hat Enterprise Linux VMs for each tier as per parameter value specified during deployment.
