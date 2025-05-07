
---
### 2. `ArgoCD`
---
### What is ArgoCD, and how does it enable GitOps for Kubernetes?
- ArgoCD is a GitOps based CD tool for k8s that automates the application deployments by syncing changes from git repositories to our K8s cluster.
- Git is the source of truth.
---
### How does ArgoCD manage sync and drift detection?
- It continuously monitors live cluster vs git repo.
- It flags as drift and shows as status ex: outofsync, healthy.
---
### What are ArgoCD sync waves?
- It controls deployment order using annotations.
- like 'argocd.argoproj.io/sync-wave: 0', 'argocd.argoproj.io/sync-wave: 1' etc.
---
### How to deploy apps to EKS using ArgoCD and GitHub?
- We have to push the app manifest to Github.
- Confiure the git repo in the ArgoCD and Create an application in it pointing to the specific directory.
- ArgoCD watches the repo, If any changes are made then it syncs the changes to the EKS cluster.
---