# AWS
---
### 1. `IAM - Identity and Access Management`
---
### What are users, groups, roles and policies?
- Users: These are real people or applications that need AWS access.
- Groups: A Collection of users with common permissions.
- Roles: These are permissions that AWS Services or Users can assume.
- Policies: These are JSON documents that define permissions.
---
### What is the principle of least privilege, and why should it be followed?
- Principle of least privilege gives users and systems a minimum permissions that they need. So, that It reduces security risk. Less access = Less damage if something goes wrong.
---
### What is the difference between an identity-based policy and a resource-based policy?
- Identity-based policy: It is attached to users, groups and roles. This defines what they can access.
- Resource-based policy: Instead of attaching the policy to a user/group/role, here the policy is directly attached to the resource ( ex: S3, Lambda ). It defines who can access the resource.
---
### What are AWS-managed policies and customer-managed policies?
- AWS-managed policies: These are in-built policies made and mainatained by AWS. ( ex: S3FullAccess )
- Customer-managed policies: These are created and managed by the user for custom needs. ( ex: A custom policy that provides access to specific bucket )
---
### What is multi-factor authentication (MFA), and how does it enhance security?
- MFA: It adds a second layer of security. After entering the password, we must also enter a code from our device. ( ex: Authy, Google Authenticator etc.)
- Even if the account login credentials are compromised, the hacker can't login without a code from MFA device.
---
### What is a service-linked role, and how is it different from a standard IAM role?
- Service-linked role: It is an IAM role that automatically gets created and managed by AWS services on our behalf. (ex: upon creating an AWS ELB, AWS auto-creates a service-linked role. So, ELB can manage the instances.)
- Standard IAM role: We create and assign manually.
---
### How do you audit IAM activity using AWS CloudTrail?
- CloudTrail: It records who did what in our AWS account, including all IAM activities.
- ex: In the CloudTrail console, we can find out that a user: Akash had created an new IAM role yesterday at 10:00 PM from a XXX.XX.228.6 IP address.
---