
---
### 6. `VPC & Networking`
---
### What is the difference between a public and private subnet in a VPC?
- Public has route to Internet Gateway.
- Private has no direct route to internet, via Nat Gateway.
---
### How does a route table work in AWS VPC, and how do you associate it with subnets?
- Route table maps traffic to destination (CIDR) via target (IGW/NAT).
- Associate route tables to subnets.
---
### What is the purpose of an Internet Gateway (IGW), and how does it enable internet access for VPC resources?
- It enables internet access for public subnets.
---
### What is a NAT Gateway, and how does it differ from an Internet Gateway?
- It allows outbound-only internet access for private subnets. Where as IGW is for inbound + outbound ( public )
---
### How does VPC Peering work, and when should you use it instead of a Transit Gateway?
- VPC Peering: Point-to-point, simple
- Transit Gateway: Hub-and-spoke, scalable
---
### Can VPC Peering be established between different AWS accounts and regions? How?
- Yes, we have to accept manually, but it needs non-overlapping CIDRs
---
### How can you ensure high availability and fault tolerance when using NAT Gateway?
- Deploy in multiple AZs.
- Each AZ needs its own NAT Gateway for full HA.
---
### What are the security best practices when configuring route tables, NAT Gateways, and Internet Gateways?
- By following the least privilege.
- No 0.0.0.0/0 in private routes unless behind a NAT.
---
### How can you troubleshoot connectivity issues in a VPC using VPC Flow Logs?
- It captures network traffic logs. we can analyze to debug denied traffic or bottlenecks.
---