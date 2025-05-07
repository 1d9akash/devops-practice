
---
### 5. `S3 & CloudFront`
---
### How does Amazon CloudFront work with S3 to deliver content efficiently?
- S3 stores content, CloudFront caches it globally for faster delivery.
---
### What is an S3 bucket policy, and how can it be used to allow CloudFront access to private S3 content?
- It allows access to S3 content from CloudFront Origin Identity.
---
### What is the difference between a CloudFront distribution and an S3 static website hosting setup?
- S3 static website hosting setup is good for simple websites.
- CloudFront: CDN with caching, security, SSL.
---
### How does CloudFront caching work, and how can you invalidate cached objects when updating S3 content?
- It caches content in edge locations.
- We have to use Invalidations to refresh content with either of the ways (CLI/API/Console).
---
### What are signed URLs and signed cookies in CloudFront, and how do they secure private S3 content?
- These restrict access to private content.
- Signed URL: Valid for specific user/time.
- Signed Cookie: For multiple files under a path.
---