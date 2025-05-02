
---
### 2. `EC2 & Lambda`
---
### What are the different EC2 instance types, and how do they differ?
- General Purpose: t3, t4g, m5 - Balanced CPU, Memory, Networking.
- Compute Optimzied: c5, c6g - High CPU performance.
- Memory Optimized: r5, r6g - Larger RAM for in-memory Apps.
- Storage Optimized: i3, d3 - High speed storage for DBs.
- Accelerated Computing: p4, inf1 - GPUs for AI/ML workloads.
---
### What are the key components of an ASG?
- Launch Template
- Scaling Policies
- Health Checks
- Min, Max, Desired Capacity
---
### How do scaling policies work in ASG, and what are the different types?
- Dynamic Scaling:
    - Target Tracking: Maintain a metric at specific threshold ( ex: I want the Avg. ASG CPU to stay around 50% )
    - Simple/Step Scaling: Scale based on metric thresholds.
- Scheduled Scaling: Scale at specific time ( cron like )
- Predictive Scaling: Analyzes historical load data and uses it to forecast future capacity needs.
---
### What are the different types of AWS load balancers, and when should you use each?
- Classic Load Balancer ( CLB ): Older generation, Layer 4/7, Health checks are TCP or HTTP based, Fixed hostname
- Application Load Balancer ( ALB ): Layer 7 - HTTP/HTTPS, smart routing
- Netowork Load Balancer ( NLB ): Layer 4 - TCP/UDP, High performance, 1 static IP per AZ
- Gateway Load Balancer ( GWLB ): Layer 3 - GENEVE Protocol, single entry/exit for all traffic.
- ALB for web-apps, NLB for game servers, GWLB for security-focused industries.
---
### How does an ALB distribute traffic across multiple EC2 instances?
- ALB checks instances health and distribute requests to healthy targets.
- It uses Round-Robin/Least-Outstanding requests algorithms.
---
### What are target groups, and how do they work with ALB?
- A target group is a set of EC2 Instances, IPs or Lambda functions that receive traffic from ALB.
- ALB forwards requests to one or more registered targets based on listener rules.
---
### How can you configure host-based and path-based routing in ALB?
- Host-based: Forward the requests based on domain names ( ex: api.example.com or app.example.com ).
- Path-based: Forward the requests based on the URL paths ( ex: /login, /orders ).
- We need to setup target groups and then configure the ALB listener rules to route traffic either of the above ways.
---
### What are AWS Security Groups, and how do they function?
- These acts as virtual firewalls to the EC2 instances.
- To Allow specific inbound and outbound traffic based on ports, protocols, IPs.
- These are stateful, means return traffic is automatically allowed.
---
### How do Security Groups differ from Network ACLs?
- Security Groups: applies to Instances, stateful, contains only allow rules, All rules are evaluated.
- Network ACLs: applies to subnets, stateless, contains both the allow and deny rules, Rules are evaluated from top-down.
---
### How do you allow only SSH traffic from a specific IP range?
- By addding an inbound rule in the security group with port: 22, protocol: TCP, source: < specific-ip-range >
---
### What is the impact of deleting a security group associated with an active EC2 instance?
- We cannot delete a security group attacehd to an active instance, We must first detach it or replace it.
---
### What are the different types of EBS volumes, and when should you use each?
- General Purpose SSD - gp2/gp3 - Balanced performance, default choice.
- Provisioned IOPS SSD - io2/io1 - High Performance Databases, etc.
- Throughput Optimized HDD - st1 - Big data, logs, etc.
- Cold HDD - sc1 - Archival, less frequently accessed data.
---
### How do you resize an EBS volume without downtime?
- Modify volume size via AWS console or CLI.
- Then extend the filesystem inside the EC2 Instance.
---
### What is an EBS snapshot and how can it be used for backup and recovery?
- EBS snapshot = Backup of an EBS volume.
- We can restore a new EBS volume from a snapshot in any region.
---
### How do you encrypt an EBS volume, and what are the benefits?
- We have to enable encryption when creating a volume.
- Uses AWS KMS keys: data at rest, in-transit encryption, easier compliance.
---
### What is the difference between EBS & EFS?
- EBS: Block storage, can be attachable to one EC2 at a time, can be used for Databases/OS disks.
- EFS: File storage, Can be attachable to multiple instances at a time, shared filesystem.
---