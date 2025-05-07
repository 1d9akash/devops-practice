
---
### 7. `Cloudwatch ( Metrics & Logs )`
---
### What are cloudwatch metrics, logs and alarms, and how do they help in monitoring AWS resources?
- Metrics: Key Performance Indicators / Numerical values over time ( CPU, Memory etc. )
- Logs: Application's / System's output.
- Alarms: Trigger on a pre-defined thresholds.
---
### How can you setup a cloudwatch alarm to trigger an action when EC2 instance CPU usage exceeds a threshold?
- We have to create a Metric Alarm on 'CPUUtilization > 75%'.
- Action: Notify via SNS or AutoScale the instances.
---
### What is CloudWatch Logs Insights, and how can it be used to analyze log data efficiently?
- We can query logs using SQL like syntax.
- It helps filter, aggregate, and find patterns fast.
---