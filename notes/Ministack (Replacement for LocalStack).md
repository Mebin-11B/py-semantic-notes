---
title: "Ministack (Replacement for LocalStack)"
url: https://ministack.org/
clipped: 2026-06-17 01:24:36
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Ministack (Replacement for LocalStack)](https://ministack.org/)

## Digest Summary
MiniStack is an open‑source local AWS emulator that implements a wide range of core services, many with real‑infrastructure back‑ends. Key capabilities include:

- **Storage & Messaging**: S3 (buckets, versioning, encryption, lifecycle, replication), SQS (standard/FIFO, DLQ, batch), SNS (topics, subscriptions, fan‑out), Kinesis (streams, shards, consumers), EventBridge (buses, rules, targets), and Firehose (delivery streams to S3).
- **Databases**: DynamoDB (CRUD, queries, transactions, TTL, GSIs) and RDS (containerized PostgreSQL/MySQL). ElastiCache runs actual Redis/Memcached containers.
- **Compute**: Lambda (Python execution, warm workers, SQS event mapping, layers), ECS (run‑task with real Docker containers), EC2 (instances, VPC components, networking), EMR (clusters, steps – Pro only), and Step Functions (full ASL engine).
- **Security & Identity**: IAM (users, roles, policies, OIDC), STS, Secrets Manager, ACM, Cognito (user pools, MFA, identity pools), WAF v2 (Pro only).
- **Monitoring & Management**: CloudWatch Logs, Metrics, Alarms, Dashboards, Insights, SSM Parameter Store.
- **Additional services**: API Gateway v1/v2, Glue (catalog, crawlers), Athena (SQL via DuckDB), Route 53, SES/SES v2, ALB/ELBv2 (Pro only), EBS/EFS (Pro only).

The emulator supports both API‑level simulation and real‑backend execution for many services, providing a comprehensive local development environment.

## Discussion Summary
Comments express skepticism toward the new project, questioning its documentation quality and overall reliability, while noting concerns that its README appears unreviewed. Many acknowledge past positive experiences with LocalStack but highlight persistent problems such as drift between local emulation and production behavior, which led some teams to adopt short‑lived real AWS environments despite higher costs. The recent licensing changes to LocalStack generate frustration, prompting interest in alternatives like the community‑archive tag or other clones, though doubts remain about whether these can maintain broad AWS compatibility without similar issues. Overall sentiment is cautious and critical, emphasizing the need for proven stability.

---

## Full Article

Core AWS services plus real infrastructure â RDS runs actual databases, ElastiCache runs real
Redis, ECS starts real Docker containers, Athena executes real SQL via DuckDB (when installed).

* ðª£

  S3

  Buckets, objects, versioning, encryption, lifecycle, CORS, Object Lock, replication

  REST/XML
* ð¨

  SQS

  Queues, FIFO, DLQ, batch, visibility

  JSON+Query
* ð¢

  SNS

  Topics, subscriptions, fanout to SQS, batch publish

  Query/XML
* ðï¸

  DynamoDB

  Tables, CRUD, query, scan, transactions, TTL, GSI

  JSON
* â¡

  Lambda

  Real Python execution, warm workers, SQS event source mapping, Layers

  REST/JSON
* ð

  IAM

  Users, roles, policies, groups, instance profiles, OIDC

  Query/XML
* ð«

  STS

  CallerIdentity, AssumeRole, GetSessionToken

  Query/XML
* ð

  Secrets Manager

  CRUD, versioning, rotation, resource policies

  JSON
* ð

  CW Logs

  Groups, streams, retention, subscription filters, metric filters, Insights

  JSON
* ð

  SSM Params

  String, SecureString, paths, labels, tags

  JSON
* ð

  EventBridge

  Buses, rules, targets, Lambda dispatch, archives, permissions

  JSON
* ð

  Kinesis

  Streams, split/merge shards, consumers, encryption, monitoring

  JSON
* ð

  CW Metrics

  Metrics, alarms, composite alarms, dashboards, alarm history

  Query/CBOR
* âï¸

  SES

  Send email/raw/templated, identities, configuration sets

  Query/XML
* ð

  Step Functions

  Full ASL engine, sync execution, task tokens, all state types

  JSON
* ð

  API Gateway v2

  HTTP APIs, Lambda proxy, path params, execute-api data plane

  REST/JSON
* ð

  API Gateway v1

  REST APIs, resources, methods, integrations, stages, MOCK, Lambda proxy format 1.0

  REST/JSON
* ð

  RDS

  Real Postgres/MySQL containers

  Real Docker
* ð´

  ElastiCache

  Real Redis/Memcached containers, users, user groups

  Real
  Docker
* ð³

  ECS

  RunTask starts real containers, capacity providers

  Real Docker
* ð§ª

  Glue

  Catalog, crawlers, jobs, triggers, workflows

  Real Exec
* ð

  Athena

  Real SQL via DuckDB (optional), data catalogs, prepared statements

  DuckDB
* ð

  Firehose

  Delivery streams, PutRecord/PutRecordBatch, S3 delivery, encryption, tags

  REST/JSON
* ð

  Route53

  Hosted zones, record sets (CREATE/UPSERT/DELETE), health checks, tags, alias records

  REST/XML
* ð

  Cognito

  User pools, auth flows, TOTP MFA, identity pools, federated credentials

  JSON
* ð¥ï¸

  EC2

  Instances, VPCs, subnets, security groups, route tables, ENIs, elastic IPs, NAT gateways, NACLs,
  flow logs, VPC peering, DHCP options, egress-only IGWs

  Query/XML
* â¡

  EMR

  Clusters, steps, instance groups/fleets, bootstrap actions, tags â Pro-only on LocalStack

  JSON
* ð¾

  EBS

  Volumes, snapshots, attach/detach, modify, copy â Pro-only on LocalStack

  Query/XML
* ð

  EFS

  File systems, mount targets, access points, lifecycle, backup policy â Pro-only on LocalStack

  REST/JSON
* âï¸

  ALB / ELBv2

  Load balancers, target groups, listeners, rules, Lambda targets + live data-plane routing â
  Pro-only on LocalStack

  Query/XML
* ð

  ACM

  Request, import, describe certificates; DNS validation records; SANs; tags

  JSON
* âï¸

  SES v2

  SendEmail, identities, configuration sets, account suppression â REST API

  REST/JSON
* ð¡ï¸

  WAF v2

  WebACLs, IP sets, rule groups, resource associations, LockToken enforcement â Pro-only on
  LocalStack

  JSON
* âï¸

  CloudFormation

  Stack lifecycle, change sets, 68 resource types, YAML/JSON templates, intrinsic functions,
  rollback, cross-stack exports

  XML
* ð

  KMS

  RSA & symmetric envelope encryption for internal cryptographic signatures

  JSON
* ð¦

  ECR

  In-memory container registry providing Docker V2 manifests and full lifecycle rules

  JSON
* â¡

  AppSync

  Serverless GraphQL architecture mocking local DataSources and complex Resolvers

  REST/JSON
* ð

  CloudFront

  High-throughput edge location edge server emulation targeting origins natively

  XML
* ð

  AutoScaling

  ASGs, launch configs, scaling policies, lifecycle hooks, scheduled actions, tags

  Query/XML
* ð¨

  CodeBuild

  Projects, builds, start/stop, batch operations, metadata stored in-memory

  JSON
* ðºï¸

  Cloud Map

  HTTP/DNS namespaces, services, instance registration, discovery, Route53 integration

  JSON
* ð

  S3 Files

  File systems, mount targets, access points, policies â new April 2026 S3 service

  REST
* ðï¸

  RDS Data API

  ExecuteStatement, BatchExecute, transactions â routes SQL to real RDS containers

  REST
* ð

  OpenSearch

  Domains, versions, change progress, tags â optional real `opensearchproject/opensearch` cluster + Dashboards sidecar via `OPENSEARCH_DATAPLANE=1`

  Real Docker
* ðï¸

  Organizations

  DescribeOrganization, ListRoots, accounts, OUs with the new `Path` field

  REST/JSON
* ðªª

  Account

  GetAccountInformation (with `AccountState`), GetContactInformation, ListRegions opt-in matrix

  REST/JSON
* âï¸

  Batch

  Compute environments, job queues, job definitions (auto-revisioning), SubmitJob â Pro-only on LocalStack

  REST/JSON
* ð¡ï¸

  WAF Classic

  v1 + Regional stub for legacy Terraform / CFN â empty `List*`, valid `GetChangeToken`, `WAFNonexistentItemException`

  JSON
* ð¡

  IMDS

  EC2 Instance Metadata Service v1 + v2 â SDK credential chains resolve via `AWS_EC2_METADATA_SERVICE_ENDPOINT`

  HTTP
* â°

  EventBridge Scheduler

  Schedules, schedule groups, rate/cron expressions, target dispatch

  REST/JSON
* ð¾

  Backup

  Vaults, plans, recovery points, tags â control plane stub

  REST/JSON
* ð©

  AppConfig

  Applications, environments, profiles, deployments, hosted versions, configuration sessions data plane

  REST/JSON
* ð¤

  Transfer

  SFTP servers, users, public-key auth, tags

  JSON
* â¸ï¸

  EKS

  Clusters, node groups, Fargate profiles, addons â Pro-only on LocalStack

  REST/JSON
* ð·ï¸

  Resource Groups Tagging

  GetResources, GetTagKeys/Values, TagResources across S3, Lambda, SQS, SNS, DDB, KMS, ECR, ECS, EFS, AppSync, scheduler, more

  JSON
* ðª

  MWAA

  Managed Workflows for Apache Airflow â real `apache/airflow:<version>` containers (2.x and 3.x), DAG sync from S3, `InvokeRestApi` proxy

  REST/JSON
* ð¡

  IoT Core

  Things / certificates / policies, MQTT 3.1.1 over WebSocket on the gateway port, HTTP `iot-data Publish`, Local CA, persistent sessions + QoS 1 + LWT

  REST + MQTT/WS
* ð¡ï¸

  Inspector2

  14 ops â `Enable`, `Disable`, `ListFindings` with filtering/sorting/pagination, coverage and aggregation queries, filter and tag CRUD; deterministic stub vulnerability findings for ECR images, Lambda functions, and EC2 instances

  JSON
* ð§

  S3 Tables

  Table buckets, namespaces, Iceberg-format tables; control plane covers Create/List/Get/Delete for buckets, namespaces, and tables plus `GetTableMetadataLocation` / `UpdateTableMetadataLocation`; embedded Iceberg REST catalog at `/iceberg` so Spark jobs commit Iceberg tables without an external catalog

  REST/JSON
* â¡

  AppSync Events

  Realtime WebSocket + HTTP publish on `/event`, `aws-appsync-event-ws` subprotocol, connection-scoped authorization, strict mode via `APPSYNC_EVENTS_ENFORCE_AUTH=1`

  WS/JSON
* ðï¸

  CloudFront KeyValueStore

  Create / Describe / Delete stores, key CRUD via the cloudfront-keyvaluestore data plane (`/key-value-stores/`)

  REST/JSON
* ð

  CloudTrail

  Trail CRUD (stub) â sufficient for IaC stacks that declare trails alongside other resources

  JSON
* ð¸

  Cost & Usage Reports

  CUR report definitions (stub) â control plane only, no real billing data emitted

  Query
* ð

  DynamoDB Streams

  Stream records emitted by DynamoDB writes; `GetShardIterator` / `GetRecords` honoring `StreamViewType`

  JSON
* ð

  EventBridge Pipes

  Pipe CRUD with source â enrichment â target wiring (SQS, Kinesis, DDB Streams sources; Lambda, SQS, SFN targets)

  REST/JSON