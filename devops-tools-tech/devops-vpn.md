
---
### 3. `VPN`
---
### What is a VPN, and how does it enhance network security and privacy?
- VPN: Virtual Private Network
- It encrypts trafffice, hides the IPs and secures public networks.
- ex: To connect to AWS VPC securely, we can use VPN.
---
### Difference between site-to-site and client VPN?
- site-to-site: Connects two networks ( ex: Connecting On-Prem to AWS )
- client: Individual user connects to network (ex: me using a VPN to connect to AWS )
---
### How does AWS VPN provide secure access?
- It uses IPSec protocol.
- AWS VPN is configured with Virtual Gateway or AWS Client VPN endpoints.
---
### Common VPN Protocols and differences?
- IPSec: Secure, Complex, Common
- OpenVPN: Flexible, based on SSL
- WireGuard: Lighweight, Fast
---
### How to troubleshoot VPN issues?
- Latency: Check routes, network hops.
- Auth failures: Verfiy credentials.
- Packet drops: Firewall blocks.
- Also, using logs and diagnostics from client/server.
---
