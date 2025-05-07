
---
### 1. `Github`
---
### How do you build and push a python app that is in github to ECR using GitHub Actions?
- We'll use a Github actions workflow YAML file:
    - steps include:
        - Checkout code
        - Login to AWS ECR
        - Build Docker Image
        - Push to ECR
---
### How do GitHub actions enable CI/CD Automation?
- First, we'll have to define a workflow in '.github/workflows/'.
- When the code is pushed or a PR is created, Automated tests, builds, deploys the code.
---
### What are GitHub branches and how do they help?
- Branches allow parallel development.
- Dev's work on features in seperate branches without affecting the main branch.
---
### How do you use GitHub issues and PR for project management?
- Issues: These can be used to track bugs/features/
- PRs: These are to propose changes, enable code review and merge branches
- ex: Creating a PR for 'feature/login' to merge into 'dev' and linking it to issue #11.
--- 