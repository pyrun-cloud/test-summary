2026-09-30 09:13:41,432 [INFO] config.py:146 -- Lithops v3.6.1.dev0 - Python3.12
2026-09-30 09:13:41,433 [DEBUG] config.py:107 -- Loading configuration from the cloud
2026-09-30 09:13:41,731 [DEBUG] config.py:186 -- Loading Serverless backend module: aws_lambda
2026-09-30 09:13:41,967 [DEBUG] config.py:226 -- Loading Storage backend module: aws_s3
2026-09-30 09:13:41,970 [DEBUG] aws_s3.py:36 -- Creating AWS S3 Client
2026-09-30 09:13:42,182 [INFO] aws_s3.py:59 -- S3 client created - Region: us-east-1
2026-09-30 09:13:42,221 [DEBUG] aws_lambda.py:53 -- Creating AWS Lambda client
2026-09-30 09:13:42,465 [INFO] aws_lambda.py:97 -- AWS Lambda client created - Region: us-east-1
2026-09-30 09:13:42,468 [DEBUG] invokers.py:105 -- ExecutorID da7ba6-0 - Invoker initialized. Max workers: 1000
2026-09-30 09:13:42,468 [DEBUG] invokers.py:309 -- ExecutorID da7ba6-0 - Serverless invoker created
2026-09-30 09:13:42,694 [DEBUG] executors.py:164 -- Function executor for aws_lambda created with ID: da7ba6-0
2026-09-30 09:13:42,695 [INFO] invokers.py:119 -- ExecutorID da7ba6-0 | JobID M000 - Selected Runtime: runtime-public-hello-pyrun-ai:c3e16251-amd64 - 256MB
2026-09-30 09:13:42,695 [DEBUG] storage.py:476 -- Runtime metadata found in local disk cache
2026-09-30 09:13:42,696 [DEBUG] job.py:242 -- ExecutorID da7ba6-0 | JobID M000 - Serializing function and data
2026-09-30 09:13:42,700 [DEBUG] serialize.py:75 -- Referenced Modules: __main__
2026-09-30 09:13:42,700 [DEBUG] serialize.py:120 -- Modules to transmit: None
2026-09-30 09:13:42,700 [DEBUG] job.py:276 -- ExecutorID da7ba6-0 | JobID M000 - Uploading function and modules to the storage backend
2026-09-30 09:13:42,745 [DEBUG] aws_s3.py:113 -- PUT Object lithops.jobs/da7ba6-0/d13592da0b2e99fefc9c284855a5b97d.func.pickle - Size: 525.0B - OK
2026-09-30 09:13:42,746 [DEBUG] job.py:316 -- ExecutorID da7ba6-0 | JobID M000 - Data per activation is < 8.0KiB. Passing data through invocation payload
2026-09-30 09:13:42,746 [INFO] invokers.py:188 -- ExecutorID da7ba6-0 | JobID M000 - Starting function invocation: sqrt_map() - Total: 5 activations
2026-09-30 09:13:42,746 [DEBUG] invokers.py:214 -- ExecutorID da7ba6-0 | JobID M000 - Worker processes: 1 - Chunksize: 1
2026-09-30 09:13:42,747 [DEBUG] invokers.py:318 -- ExecutorID da7ba6-0 - Async invoker 0 started
2026-09-30 09:13:42,747 [DEBUG] invokers.py:318 -- ExecutorID da7ba6-0 - Async invoker 1 started
2026-09-30 09:13:42,747 [DEBUG] invokers.py:458 -- ExecutorID da7ba6-0 | JobID M000 - Free workers: 1000 - Going to run 5 activations in 5 workers
2026-09-30 09:13:42,756 [INFO] invokers.py:227 -- ExecutorID da7ba6-0 | JobID M000 - View execution logs at /tmp/lithops-root/logs/da7ba6-0-M000.log
2026-09-30 09:13:42,756 [DEBUG] monitor.py:179 -- ExecutorID da7ba6-0 - Creating RabbitMQ queue lithops-da7ba6-0
2026-09-30 09:13:42,862 [DEBUG] monitor.py:247 -- ExecutorID da7ba6-0 | Starting RabbitMQ job monitor
2026-09-30 09:13:42,862 [INFO] executors.py:507 -- ExecutorID da7ba6-0 - Getting results from 5 function activations
2026-09-30 09:13:42,863 [INFO] wait.py:101 -- ExecutorID da7ba6-0 - Waiting for 5 function activations to complete
2026-09-30 09:13:42,864 [DEBUG] monitor.py:144 -- ExecutorID da7ba6-0 - Pending: 5 - Running: 0 - Done: 0
2026-09-30 09:13:42,884 [DEBUG] invokers.py:391 -- ExecutorID da7ba6-0 | JobID M000 - Calls 00001 invoked (0.134s) - Activation ID: 7aa8251f-47d3-4891-986b-dbc8370f765e
2026-09-30 09:13:42,885 [DEBUG] invokers.py:391 -- ExecutorID da7ba6-0 | JobID M000 - Calls 00004 invoked (0.131s) - Activation ID: e58d9acb-483b-4590-8788-d18e2674da12
2026-09-30 09:13:42,888 [DEBUG] invokers.py:391 -- ExecutorID da7ba6-0 | JobID M000 - Calls 00000 invoked (0.140s) - Activation ID: f1a01166-f2e6-4704-87cc-5d26a76ee5ef
2026-09-30 09:13:42,888 [DEBUG] invokers.py:391 -- ExecutorID da7ba6-0 | JobID M000 - Calls 00002 invoked (0.138s) - Activation ID: 02dc2503-8240-4294-8743-f0a201a48e75
2026-09-30 09:13:42,895 [DEBUG] invokers.py:391 -- ExecutorID da7ba6-0 | JobID M000 - Calls 00003 invoked (0.143s) - Activation ID: d48ad91b-554c-4b1e-9a34-f214195d7679
2026-09-30 09:13:50,865 [DEBUG] monitor.py:144 -- ExecutorID da7ba6-0 - Pending: 0 - Running: 5 - Done: 0
2026-09-30 09:13:51,788 [DEBUG] future.py:229 -- ExecutorID da7ba6-0 | JobID M000 - Got status from call 00002 - Activation ID: 02dc2503-8240-4294-8743-f0a201a48e75 - Time: 2.22 seconds
2026-09-30 09:13:51,789 [DEBUG] future.py:286 -- ExecutorID da7ba6-0 | JobID M000 - Got output from call 00002 - Activation ID: 02dc2503-8240-4294-8743-f0a201a48e75
2026-09-30 09:13:51,789 [DEBUG] future.py:229 -- ExecutorID da7ba6-0 | JobID M000 - Got status from call 00001 - Activation ID: 7aa8251f-47d3-4891-986b-dbc8370f765e - Time: 2.26 seconds
2026-09-30 09:13:51,789 [DEBUG] future.py:286 -- ExecutorID da7ba6-0 | JobID M000 - Got output from call 00001 - Activation ID: 7aa8251f-47d3-4891-986b-dbc8370f765e
2026-09-30 09:13:51,891 [DEBUG] future.py:229 -- ExecutorID da7ba6-0 | JobID M000 - Got status from call 00004 - Activation ID: e58d9acb-483b-4590-8788-d18e2674da12 - Time: 2.28 seconds
2026-09-30 09:13:51,891 [DEBUG] future.py:286 -- ExecutorID da7ba6-0 | JobID M000 - Got output from call 00004 - Activation ID: e58d9acb-483b-4590-8788-d18e2674da12
2026-09-30 09:13:51,993 [DEBUG] future.py:229 -- ExecutorID da7ba6-0 | JobID M000 - Got status from call 00003 - Activation ID: d48ad91b-554c-4b1e-9a34-f214195d7679 - Time: 2.25 seconds
2026-09-30 09:13:51,994 [DEBUG] future.py:286 -- ExecutorID da7ba6-0 | JobID M000 - Got output from call 00003 - Activation ID: d48ad91b-554c-4b1e-9a34-f214195d7679
2026-09-30 09:13:52,064 [DEBUG] monitor.py:144 -- ExecutorID da7ba6-0 - Pending: 0 - Running: 0 - Done: 5
2026-09-30 09:13:52,064 [DEBUG] monitor.py:282 -- ExecutorID da7ba6-0 | RabbitMQ job monitor finished
2026-09-30 09:13:52,096 [DEBUG] future.py:229 -- ExecutorID da7ba6-0 | JobID M000 - Got status from call 00000 - Activation ID: f1a01166-f2e6-4704-87cc-5d26a76ee5ef - Time: 2.30 seconds
2026-09-30 09:13:52,096 [DEBUG] future.py:286 -- ExecutorID da7ba6-0 | JobID M000 - Got output from call 00000 - Activation ID: f1a01166-f2e6-4704-87cc-5d26a76ee5ef
2026-09-30 09:13:52,096 [INFO] executors.py:631 -- ExecutorID da7ba6-0 - Cleaning temporary data
2026-09-30 09:13:52,098 [DEBUG] executors.py:532 -- ExecutorID da7ba6-0 - Finished getting results
[4, 16, 36, 64, 100]
