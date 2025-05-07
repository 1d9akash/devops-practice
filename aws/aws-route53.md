
---
### 4. `Route 53`
---
### What is Amazon Route 53 and its key features?
- It is an AWS DNS service. Helps ous to map domain names to AWS resources.
- Features: domain registration, health checks, traffic policies.
---
### What are the different types of DNS records supported by Route 53 ( A, CNAME, ALIAS, etc .. )?
- A: Maps to IP address
- CNAME: Maps to another domain name
- ALIAS: Like CNAME but for AWS resources
- MX, TXT, NS, AAAA, PTR, SRV and more
---
### What is the difference between public and a private hosted zone in Route 53?
- Public: Resolves domains on the internet.
- Private: Works only inside a VPC (internal DNS).
---
### How does Route 53 handle routing policies ( Simple, Weighted, Latency-based, Geolocation, Failover, Multi-value )?
- Simple: One record per name.
- Weighted: Distribute % of traffic.
- Latency-based: Routes based on lowest latency.
- Geo/Geolocation: Based on user's location.
- Failover: Route to healthy endpoints.
- Multi-value: Return multiple healthy records.
---
### What is an Alias record, and how does it differ from a CNAME record in Route 53?
- CNAME: Cannot be used for root domain.
- Alias: Works for root domain, integrates with AWS services like ALB/S3.
---
### How does Route 53 integrate with AWS services like ALB, Cloudfront, and S3?
- We can create ALIAS records to ALB, S3 static sites, or CloudFront.
---
### How can Route 53 help in setting up a Multi-Region DR with Route 53?
- We can use failover routing between primary and secondary regions and health checks decide traffic redirection.
---