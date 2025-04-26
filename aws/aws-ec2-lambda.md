
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