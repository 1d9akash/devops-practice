
---
### 3. `ECS & EKS`
---
### What are the core components of an EKS cluster?
- Control Plane - Managed by AWS
- Worker Nodes - EC2 or Fargate
- Node Groups - Managed or self-managed
- kubectl and IAM authentication
---
### How does EKS integrate with AWS networking?
- EKS cluster will be created in the subnets from VPC.
- We use subnets, security groups and routing tables.
- The Amazon VPC CNI plugin assigns VPC IPs to Pods.
---
### Difference between managed and self-managed node groups?
- Managed: AWS handles lifecycle, updates, scaling etc.
- Self-Managed: We launch EC2 instances manually and join them to the cluster.
---
### What role does IAM play in EKS?
- IAM controls access to the cluster.
- 'aws-auth' configmap maps the IAM users/roles to the K8S RBAC.
---
### How does EKS handle high-availability and scaling?
- Control plane across multiple AZs.
- Nodes can auto-scale using cluster Autoscaler.
---
### How do you expose services running in EKS to the internet?
- We have to use service type of Loadbalancer [ creates ALB/NLB ]
---
### What is Amazon VPC CNI Plugin?
- It allows pods to get IPs from the VPC CIDR.
---
### What is Kubernetes RBAC and how it is used in EKS?
- Role Based Access Control defines who can perform what action.
- We bind the roles to users/groups/service accounts, also works with aws-auth mapping.
---
### How do you enforce network policies in EKS?
- We can use Calico CNI for network policies in EKS.
---
### What is AWS ECR and how does it differ from docker hub?
- Elastic Container Registry is AWS managed docker image store.
- It is secure and integrated with IAM, Faster pull within AWS Infra.
---
### Difference between ECR public and ECR private?
- Public: Anyone can access the images.
- Private: Access controlled via IAM policies.
---