---
title: "Floci – A free, open-source local AWS emulator"
url: https://github.com/hectorvent/floci
clipped: 2026-06-17 01:29:31
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Floci – A free, open-source local AWS emulator](https://github.com/hectorvent/floci)

## Digest Summary
Floci is a free, open‑source local AWS emulator that runs via `docker compose up`. It provides over 20 AWS services on `http://localhost:4566`, with all services reachable using any AWS region and arbitrary credentials. The Docker image (`hectorvent/floci:latest`) maps port 4566 and mounts `./data` for persistent storage. Floci replaces LocalStack’s community edition, which will require auth tokens and lose CI support after March 2026. It passes all 408 SDK compliance tests.

Typical usage examples:  
- AWS CLI: `aws s3 mb s3://my-bucket` or `aws sqs create-queue --queue-name my-queue`.  
- Java SDK v2: configure `DynamoDbClient` with `endpointOverride("http://localhost:4566")` and static test credentials.  
- Python boto3: `boto3.client("s3", endpoint_url="http://localhost:4566", ...)`.  
- Node.js SDK v3: instantiate `S3Client` with `endpoint`, `region`, and test credentials, enabling `forcePathStyle`.

Configuration is driven by environment variables prefixed with `FLOCI_` (e.g., `FLOCI_DEFAULT_REGION`, `FLOCI_STORAGE_MODE`, `FLOCI_STORAGE_PERSISTENT_PATH`). Storage modes include memory, persistent, hybrid, and wal. Floci is released under the MIT license.

## Discussion Summary
The comments express strong support for cloud providers offering official local emulators, viewing them as essential for reliable integration testing and broader adoption. Existing solutions like LocalStack are praised for usefulness but criticized for limited future support, compatibility gaps, and licensing constraints, prompting calls for transparent API coverage matrices. An open, community‑driven emulator is seen as desirable, with interest extending to GCP equivalents. Concerns focus on maintaining accurate behavior across services to avoid production discrepancies, while overall enthusiasm for such tooling remains high.

---

## Full Article

[![Floci](https://github.com/floci-io/floci/raw/main/docs/assets/floci-black.svg#gh-light-mode-only)](https://github.com/floci-io/floci/blob/main/docs/assets/floci-black.svg#gh-light-mode-only)
[![Floci](https://github.com/floci-io/floci/raw/main/docs/assets/floci-white.svg#gh-dark-mode-only)](https://github.com/floci-io/floci/blob/main/docs/assets/floci-white.svg#gh-dark-mode-only)

**Light, fluffy, and always free**  
No account. No auth token. No feature gates. Just `docker compose up`.

[![Latest Release](https://camo.githubusercontent.com/c892d7fecb7988b7b3deada1dce66fb04a5ce604f44c24d0bfef71588414b734/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f666c6f63692d696f2f666c6f63693f6c6162656c3d6c617465737425323072656c6561736526636f6c6f723d626c7565)](https://github.com/floci-io/floci/releases/latest)
[![Build Status](https://camo.githubusercontent.com/fe80e691bbc394ea1a41482161b9db7e89905b9f1af7d3eadf66e7bdaa756152/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f666c6f63692d696f2f666c6f63692f72656c656173652e796d6c3f6c6162656c3d6275696c64)](https://github.com/floci-io/floci/actions/workflows/release.yml)
[![Docker Pulls](https://camo.githubusercontent.com/a0baf22d81171625a19cba372e88169c313366f0397beb44693d4f1c3fc333de/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f70756c6c732f666c6f63692f666c6f63693f6c6162656c3d646f636b657225323070756c6c73)](https://hub.docker.com/r/floci/floci)
[![Docker Image Size](https://camo.githubusercontent.com/ed3a09325423d2d937e42a307261285f40d1d7d4d446977fb683fb039c157ca1/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f696d6167652d73697a652f666c6f63692f666c6f63692f6c61746573743f6c6162656c3d696d61676525323073697a65)](https://hub.docker.com/r/floci/floci)
[![License: MIT](https://camo.githubusercontent.com/f8df3091bbe1149f398a5369b2c39e896766f9f6efba3477c63e9b4aa940ef14/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d677265656e)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://camo.githubusercontent.com/02cf08877e8fc8049ece2824ec2b956cec1fe0b330cfc3b0b8354f8f1e0c29b4/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f666c6f63692d696f2f666c6f63693f7374796c653d666c6174)](https://github.com/floci-io/floci/stargazers)

[Quick Start](https://github.com/hectorvent/floci#quick-start) ·
[Features](https://github.com/hectorvent/floci#features) ·
[Services](https://github.com/hectorvent/floci#supported-services) ·
[SDKs](https://github.com/hectorvent/floci#sdk-integration) ·
[Testcontainers](https://github.com/hectorvent/floci#testcontainers) ·
[Migration](https://github.com/hectorvent/floci#migrating-from-localstack) ·
[Docs](https://floci.io/floci/)

---

Floci is a free, open-source local AWS emulator for development, testing, and CI.

It gives you AWS-shaped services on your machine without requiring a cloud account, an auth token, or paid feature gates. Point your AWS SDK, CLI, Terraform, CDK, OpenTofu, or test suite at `http://localhost:4566` and keep your existing workflows.

Floci is named after [floccus](https://en.wikipedia.org/wiki/Cirrocumulus_floccus), the cloud formation that looks like popcorn.

The fastest way to run Floci is with the official [CLI](https://github.com/floci-io/floci-cli)

Export the AWS environment variables:

Use your existing AWS tools normally:

```
aws s3 mb s3://my-bucket

aws dynamodb create-table \
  --table-name demo-table \
  --attribute-definitions AttributeName=pk,AttributeType=S \
  --key-schema AttributeName=pk,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST

aws dynamodb list-tables
```

This short demo shows the CLI flow: start Floci, export the local AWS environment, run standard AWS CLI commands, and stop the emulator.

floci-cli-demo.mp4

[
](https://private-user-images.githubusercontent.com/182702325/593771979-b55714dc-ef36-40ae-a734-cd2cadc288a8.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDAyNzAsIm5iZiI6MTc4MTYzOTk3MCwicGF0aCI6Ii8xODI3MDIzMjUvNTkzNzcxOTc5LWI1NTcxNGRjLWVmMzYtNDBhZS1hNzM0LWNkMmNhZGMyODhhOC5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQxOTU5MzBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xYTllMjMzOTBlMjRkYTgyM2Y1MzNmMjVmM2JjNzQ0NzE3MjUyYzEyMTE5NTMwOGVkNjYzOGE1YWFjOWExNDJkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9dmlkZW8lMkZtcDQifQ.MXTgl44DYsUJ7YxgeLlbNPnd8pnPvBJevwd9A_4rCoA)

All AWS services are available at `http://localhost:4566`. Any region works. Credentials can be any non-empty values.

Prefer Docker Compose?

Create a `compose.yaml` file:

```
services:
  floci:
    image: floci/floci:latest
    ports:
      - "4566:4566"
```

Start Floci:

Then configure your AWS environment manually:

```
export AWS_ENDPOINT_URL=http://localhost:4566
export AWS_DEFAULT_REGION=us-east-1
export AWS_ACCESS_KEY_ID=test
export AWS_SECRET_ACCESS_KEY=test
```


Using the old `hectorvent/floci` image?

Update your image name:

```
# Before
image: hectorvent/floci:latest

# After
image: floci/floci:latest
```

The old `hectorvent/floci` repository no longer receives updates.


**Local AWS without the cloud account**

Run AWS-compatible services locally without an AWS account, auth token, or paid feature gates.


**Real Docker where fidelity matters**

Lambda, RDS, Neptune, ElastiCache, MSK, ECS, EC2, EKS, OpenSearch, and CodeBuild use real Docker-backed execution instead of shallow mocks.


**Drop-in AWS compatibility**

Point standard AWS clients at `http://localhost:4566`. Existing credentials, regions, SDKs, CLI commands, and IaC workflows stay familiar.


**Fast enough for CI**

The native image starts in milliseconds and keeps idle memory low, making it practical for local development and test pipelines.


**Configurable persistence**

Choose from in-memory, persistent, hybrid, and write-ahead log storage depending on the durability profile you need.

LocalStack's community edition [sunset in March 2026](https://blog.localstack.cloud/the-road-ahead-for-localstack/), requiring auth tokens and freezing security updates. Floci is the no-strings-attached alternative.

| Capability | Floci | LocalStack Community |
| --- | --- | --- |
| Auth token required | No | Yes |
| Security updates | Yes | Frozen |
| Startup time | ~24 ms | ~3.3 s |
| Idle memory | ~13 MiB | ~143 MiB |
| Docker image size | ~90 MB | ~1.0 GB |
| License | MIT | Restricted |
| API Gateway v2 / HTTP API | Yes | No |
| Cognito | Yes | No |
| RDS, ElastiCache, MSK | Real Docker | No |
| Neptune (graph DB + Gremlin WebSocket) | Real Docker | No |
| ECS, EC2, EKS | Real Docker | No |
| CodeBuild | Real Docker execution | No |
| Native binary | ~40 MB | No |

**54 AWS services. Broad coverage. Free forever.**

```
flowchart LR
    Client["AWS SDK / CLI"]

    subgraph Floci ["Floci, port 4566"]
        Router["HTTP Router\nJAX-RS / Vert.x"]

        subgraph Stateless ["Stateless Services"]
            A["SSM · SQS · SNS\nIAM · STS · KMS\nSecrets Manager · SES\nCognito · Kinesis\nEventBridge · Scheduler · AppConfig\nCloudWatch · Step Functions\nCloudFormation · ACM · Config\nAPI Gateway · AppSync · ELB v2 · Auto Scaling\nCodeDeploy · Backup · Bedrock Runtime · Route53 · Transfer"]
        end

        subgraph Stateful ["Stateful Services"]
            B["S3 · DynamoDB\nDynamoDB Streams"]
        end

        subgraph Containers ["Container Services"]
            C["Lambda\nElastiCache\nRDS\nNeptune\nECS\nEC2\nMSK\nEKS\nOpenSearch\nCodeBuild"]
            D["Athena -> floci-duck\nDuckDB sidecar"]
        end

        Router --> Stateless
        Router --> Stateful
        Router --> Containers
        Stateless & Stateful --> Store[("StorageBackend\nmemory · hybrid · persistent · wal")]
    end

    Docker["Docker Engine"]
    Client -->|"HTTP :4566\nAWS wire protocol"| Router
    Containers -->|"Docker API\nIAM / SigV4 auth"| Docker
```

 Loading

Floci supports local emulation for application services, data services, eventing, identity, infrastructure, billing, and container-backed workloads.

| Category | Services |
| --- | --- |
| Core app services | S3, SQS, SNS, DynamoDB, Lambda, IAM, STS, KMS, Secrets Manager |
| Events and workflows | EventBridge, EventBridge Pipes, EventBridge Scheduler, Step Functions, CloudWatch Logs, CloudWatch Metrics |
| API and identity | API Gateway REST, API Gateway v2, AppSync, Cognito, ACM, Route53, Cloud Map |
| Containers and compute | ECS, EC2, EKS, CodeBuild, CodeDeploy, Auto Scaling, ELB v2 |
| Data and analytics | Athena, Glue, Firehose, OpenSearch, Textract, Transcribe |
| Databases | RDS, RDS Data API, Neptune |
| Messaging and transfer | SES, SES v2, Kinesis, Transfer Family |
| Cost and billing | Pricing, Cost Explorer, Cost and Usage Reports, BCM Data Exports |
| Backup and config | AWS Backup, AWS Config, AppConfig, AppConfigData, CloudFormation |

For operation-level compatibility, see the [Services Overview](https://floci.io/floci/services/).

Detailed service notes


| Service | How it works | Notable features |
| --- | --- | --- |
| SSM Parameter Store | In-process | Version history, labels, SecureString, tagging |
| SSM Run Command | In-process | SendCommand, GetCommandInvocation, ListCommands, CancelCommand, agent polling via ec2messages |
| SQS | In-process | Standard and FIFO queues, DLQ, visibility timeout, batch operations, tagging |
| SNS | In-process | Topics, subscriptions, SQS, Lambda and HTTP delivery, tagging |
| S3 | In-process | Versioning, multipart upload, pre-signed URLs, Object Lock, event notifications |
| DynamoDB | In-process | GSI, LSI, Query, Scan, TTL, transactions, batch operations |
| DynamoDB Streams | In-process | Shard iterators, records, Lambda event source mapping trigger |
| Lambda | Real Docker | Runtime environment, execution model, warm container pool, aliases, Function URLs |
| API Gateway REST | In-process | Resources, methods, stages, Lambda proxy, MOCK integrations, AWS integrations |
| API Gateway v2 | In-process | HTTP APIs, routes, integrations, JWT authorizers, stages |
| AppSync | In-process | GraphQL API management API, schema registry, AWS scalars, domain names, channel namespaces |
| IAM | In-process | Users, roles, groups, policies, instance profiles, access keys |
| STS | In-process | AssumeRole, WebIdentity, SAML, GetFederationToken, GetSessionToken |
| Cognito | In-process | User pools, app clients, auth flows, JWKS and OpenID well-known endpoints |
| KMS | In-process | Encrypt, decrypt, sign, verify, data keys, aliases |
| Kinesis | In-process | Streams, shards, enhanced fan-out, split and merge |
| Secrets Manager | In-process | Versioning, resource policies, tagging |
| Step Functions | In-process | ASL execution, task tokens, execution history |
| CloudFormation | In-process | Stacks, change sets, resource provisioning |
| EventBridge | In-process | Custom buses, rules, SQS, SNS and Lambda targets |
| EventBridge Pipes | In-process | Poller-based integration connecting SQS, Kinesis, DynamoDB, and MSK sources to targets with optional filtering |
| EventBridge Scheduler | In-process | Schedule groups, schedules, flexible time windows, retry policies, DLQs |
| CloudWatch Logs | In-process | Log groups, streams, ingestion, filtering |
| CloudWatch Metrics | In-process | Custom metrics, statistics, alarms |
| ElastiCache | Real Docker | Redis / Valkey protocol, IAM auth, SigV4 validation |
| RDS | Real Docker | PostgreSQL, MySQL, MariaDB, IAM auth, JDBC-compatible engines |
| RDS Data API | REST JSON over real RDS containers | Raw SQL execution and transactions for local MySQL / MariaDB RDS resources |
| Neptune | Real Docker | Graph DB via TinkerPop Gremlin Server; RDS-shaped control plane; Gremlin WebSocket on port 8182 with SigV4 proxy |
| MSK | Real Docker | Kafka-compatible broker via Redpanda |
| Athena | In-process with DuckDB sidecar | Real SQL execution over S3 and Glue-backed views |
| Glue | In-process | Data Catalog, Schema Registry, tables consumed by Athena |
| Data Firehose | In-process | Streaming delivery, NDJSON flush to S3 |
| ECS | Real Docker | Clusters, task definitions, tasks, services, capacity providers, task sets |
| EC2 | Real Docker | RunInstances launches containers, SSH key injection, UserData, IMDS, VPC resources |
| ACM | In-process | Certificate issuance and validation lifecycle |
| ECR | In-process with real registry | Repositories, docker push / pull, image-backed Lambda functions |
| Resource Groups Tagging API | In-process | GetResources, tag and untag resources, tag key and value discovery across services |
| SES | In-process | Send email, raw email, identity verification, DKIM, templates |
| SES v2 | In-process | REST JSON API, identities, DKIM, account sending, templates |
| OpenSearch | Real Docker | Domain CRUD, tags, versions, instance types, upgrade stubs |
| AppConfig | In-process | Applications, environments, profiles, hosted versions, deployments |
| AppConfigData | In-process | Configuration sessions and dynamic configuration retrieval |
| Bedrock Runtime | In-process stub | Dummy Converse and InvokeModel responses for local development |
| EKS | Real Docker, mock mode available | k3s clusters with live Kubernetes API server |
| ELB v2 | In-process | ALB, NLB, target groups, listeners, routing rules, Lambda targets, tags |
| CodeBuild | In-process with real Docker | Real buildspec execution, CloudWatch logs, S3 artifacts |
| CodeDeploy | In-process with Lambda traffic shifting | Deployment groups, configs, lifecycle hooks, auto-rollback |
| Auto Scaling | In-process with reconciler | Launch configs, ASGs, desired capacity reconciliation, lifecycle hooks |
| AWS Backup | In-process | Vaults, backup plans, selections, simulated job lifecycle, recovery points |
| AWS Config | In-process | Config rules, configuration recorders, delivery channels, conformance packs, tagging |
| Route53 | In-process | Hosted zones, SOA and NS records, resource record sets, change tracking, tagging |
| Cloud Map | In-process | HTTP and DNS namespaces, services, instance registration, discovery queries, operations, tagging |
| Transfer Family | In-process | Server lifecycle, user management, SSH key import, tagging |
| Textract | In-process stub | API-compatible stubs, dummy block data, async job simulation |
| Transcribe | In-process stub | Transcription jobs and custom vocabularies; jobs complete immediately, no real audio processing |
| Pricing | In-process with static snapshot | Product discovery, attributes, price list files, pagination |
| Cost Explorer | In-process | Cost synthesized from Floci resource state and pricing snapshots |
| Cost and Usage Reports | In-process with floci-duck sidecar | CUR 2.0 and FOCUS 1.2 columns, account-scoped storage, Parquet emission |
| BCM Data Exports | In-process | Export lifecycle, executions, update and delete operations |

Floci uses real Docker containers when in-process emulation would reduce fidelity. This applies to stateful databases, connection-heavy protocols, runtimes, and build systems.

| Service | Default image | What is real |
| --- | --- | --- |
| Lambda | `public.ecr.aws/lambda/<runtime>` | AWS runtime environment, execution model, warm container pool |
| ElastiCache | `valkey/valkey:8` | Redis / Valkey protocol, ACL-based IAM auth, SigV4 validation |
| RDS PostgreSQL | `postgres:16-alpine` | PostgreSQL engine, IAM auth, JDBC-compatible access |
| RDS MySQL / Aurora | `mysql:8.0` | MySQL engine, IAM auth, JDBC-compatible access |
| RDS MariaDB | `mariadb:11` | MariaDB engine, IAM auth, JDBC-compatible access |
| Neptune | `tinkerpop/gremlin-server:3.7.3` | TinkerPop Gremlin Server; Gremlin WebSocket on port 8182; SigV4 auth proxy |
| MSK | `redpandadata/redpanda:latest` | Kafka-compatible broker via Redpanda |
| EC2 | AMI-mapped Linux images | Linux containers, SSH key injection, UserData, IMDS, IAM credentials |
| ECS | User-specified task image | Container lifecycle, start, stop, health checks |
| EKS | `rancher/k3s:latest` | Kubernetes API server via k3s |
| CodeBuild | User-specified environment image | Buildspec execution, log streaming, S3 artifact upload |
| OpenSearch | `opensearchproject/opensearch:2` | Full OpenSearch engine with REST API |
| ECR | `registry:2` | OCI-compatible registry for docker push and docker pull |

Docker-backed services require the Docker socket:

```
docker run -d --name floci \
  -p 4566:4566 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -u root \
  floci/floci:latest
```

### Overriding default images

| Variable | Default |
| --- | --- |
| `FLOCI_SERVICES_ELASTICACHE_DEFAULT_IMAGE` | `valkey/valkey:8` |
| `FLOCI_SERVICES_RDS_DEFAULT_POSTGRES_IMAGE` | `postgres:16-alpine` |
| `FLOCI_SERVICES_RDS_DEFAULT_MYSQL_IMAGE` | `mysql:8.0` |
| `FLOCI_SERVICES_RDS_DEFAULT_MARIADB_IMAGE` | `mariadb:11` |
| `FLOCI_SERVICES_MSK_DEFAULT_IMAGE` | `redpandadata/redpanda:latest` |
| `FLOCI_SERVICES_OPENSEARCH_DEFAULT_IMAGE` | `opensearchproject/opensearch:2` |
| `FLOCI_SERVICES_NEPTUNE_DEFAULT_IMAGE` | `tinkerpop/gremlin-server:3.7.3` |
| `FLOCI_SERVICES_EKS_DEFAULT_IMAGE` | `rancher/k3s:latest` |
| `FLOCI_SERVICES_ECR_REGISTRY_IMAGE` | `registry:2` |
| `FLOCI_ECR_BASE_URI` | `public.ecr.aws` |

Persistence and Storage Modes
-----------------------------

Floci can trade speed for durability depending on the workflow. Configure the default mode with `FLOCI_STORAGE_MODE`, or override storage per service.

| Mode | Behavior | Best for | Durability |
| --- | --- | --- | --- |
| `memory` | Entirely in RAM. Data is lost when the container stops. | CI and ephemeral tests | None |
| `persistent` | Loaded at startup and flushed to disk immediately on every write operation. | Simple local state preservation with immediate persistence | Medium |
| `hybrid` | In-memory performance with periodic async flushing every 5 seconds. | Local development | Good |
| `wal` | Write-ahead log. Every mutation is logged before responding. | Maximum durability | Highest |

Use `memory` for fast test runs. Use `hybrid` when you want state preserved across container restarts without much overhead.

For more detail, see the [Storage Configuration documentation](https://floci.io/floci/configuration/storage/).

Floci supports per-account resource isolation with no extra setup. If `AWS_ACCESS_KEY_ID` is exactly 12 digits, Floci uses it as the account ID. Resources created by one account are invisible to another.

```
AWS_ACCESS_KEY_ID=111111111111 aws sqs create-queue --queue-name orders
AWS_ACCESS_KEY_ID=222222222222 aws sqs create-queue --queue-name orders
```

Any other key format, such as `test` or `AKIA...`, causes Floci to fall back to `FLOCI_DEFAULT_ACCOUNT_ID`, which defaults to `000000000000`.

See the [Multi-Account Isolation docs](https://floci.io/floci/configuration/multi-account/).

Point your existing AWS SDK at `http://localhost:4566`.

**Java, AWS SDK v2**

```
var client = DynamoDbClient.builder()
    .endpointOverride(URI.create("http://localhost:4566"))
    .region(Region.US_EAST_1)
    .credentialsProvider(StaticCredentialsProvider.create(
        AwsBasicCredentials.create("test", "test")))
    .build();

client.createTable(b -> b
    .tableName("demo-table")
    .billingMode(BillingMode.PAY_PER_REQUEST)
    .attributeDefinitions(
        AttributeDefinition.builder().attributeName("pk").attributeType(ScalarAttributeType.S).build())
    .keySchema(
        KeySchemaElement.builder().attributeName("pk").keyType(KeyType.HASH).build()));

System.out.println(client.listTables().tableNames());
```


**Python, boto3**

```
import boto3

client = boto3.client(
    "ssm",
    endpoint_url="http://localhost:4566",
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test",
)

client.put_parameter(
    Name="/demo/app/message",
    Value="hello from floci",
    Type="String",
    Overwrite=True,
)

response = client.get_parameter(Name="/demo/app/message")
print(response["Parameter"]["Value"])
```


**Node.js, AWS SDK v3**

```
import { SQSClient, SendMessageCommand } from "@aws-sdk/client-sqs";

const client = new SQSClient({
  endpoint: "http://localhost:4566",
  region: "us-east-1",
  credentials: { accessKeyId: "test", secretAccessKey: "test" },
});

await client.send(
  new SendMessageCommand({
    QueueUrl: "http://localhost:4566/000000000000/demo-queue",
    MessageBody: "hello from floci",
  }),
);
```


**Go, AWS SDK v2**

```
package main

import (
    "context"
    "fmt"
    "log"

    "github.com/aws/aws-sdk-go-v2/config"
    "github.com/aws/aws-sdk-go-v2/credentials"
    "github.com/aws/aws-sdk-go-v2/service/s3"
)

func main() {
    cfg, err := config.LoadDefaultConfig(context.TODO(),
        config.WithRegion("us-east-1"),
        config.WithCredentialsProvider(
            credentials.NewStaticCredentialsProvider("test", "test", ""),
        ),
        config.WithBaseEndpoint("http://localhost:4566"),
    )
    if err != nil {
        log.Fatal(err)
    }

    client := s3.NewFromConfig(cfg, func(o *s3.Options) {
        o.UsePathStyle = true
    })

    out, err := client.ListBuckets(context.TODO(), nil)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(out.Buckets)
}
```


**Rust, AWS SDK**

```
use aws_sdk_secretsmanager::config::{Credentials, Region};
use aws_sdk_secretsmanager::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = aws_config::defaults(aws_config::BehaviorVersion::latest())
        .region(Region::new("us-east-1"))
        .credentials_provider(Credentials::new("test", "test", None, None, "floci"))
        .endpoint_url("http://localhost:4566")
        .load()
        .await;

    let client = Client::new(&config);

    client
        .create_secret()
        .name("demo/secret")
        .secret_string("hello from floci")
        .send()
        .await?;

    Ok(())
}
```


**Bash, AWS CLI**

```
export AWS_ACCESS_KEY_ID=test
export AWS_SECRET_ACCESS_KEY=test
export AWS_DEFAULT_REGION=us-east-1

aws --endpoint-url http://localhost:4566 s3 mb s3://my-bucket
aws --endpoint-url http://localhost:4566 s3 ls
```

Floci has Testcontainers modules for starting isolated Floci instances directly from tests. This avoids shared state, manual daemon setup, and port conflicts.

| Language | Package | Latest | Registry | Source |
| --- | --- | --- | --- | --- |
| Java | `io.floci:testcontainers-floci` | `1.4.0` | [Maven Central](https://mvnrepository.com/artifact/io.floci/testcontainers-floci) | [GitHub](https://github.com/floci-io/testcontainers-floci) |
| Node.js | `@floci/testcontainers` | `0.1.0` | [npm](https://www.npmjs.com/package/@floci/testcontainers) | [GitHub](https://github.com/floci-io/testcontainers-floci-node) |
| Python | `testcontainers-floci` | `0.1.1` | [PyPI](https://pypi.org/project/testcontainers-floci/) | [GitHub](https://github.com/floci-io/testcontainers-floci-python) |
| Go | In progress | In progress | N/A | [GitHub](https://github.com/floci-io/testcontainers-floci-go) |


**Java**

```
<dependency>
    <groupId>io.floci</groupId>
    <artifactId>testcontainers-floci</artifactId>
    <version>1.4.0</version>
    <scope>test</scope>
</dependency>
```

```
@Testcontainers
class S3IntegrationTest {

    @Container
    static FlociContainer floci = new FlociContainer();

    @Test
    void shouldCreateBucket() {
        S3Client s3 = S3Client.builder()
                .endpointOverride(URI.create(floci.getEndpoint()))
                .region(Region.of(floci.getRegion()))
                .credentialsProvider(StaticCredentialsProvider.create(
                        AwsBasicCredentials.create(floci.getAccessKey(), floci.getSecretKey())))
                .forcePathStyle(true)
                .build();

        s3.createBucket(b -> b.bucket("my-bucket"));
    }
}
```

For Testcontainers 2.x / Spring Boot 4.x, use version `2.5.0`.


**Node.js / TypeScript**

```
npm install --save-dev @floci/testcontainers
```

```
import { FlociContainer } from "@floci/testcontainers";
import { S3Client, CreateBucketCommand } from "@aws-sdk/client-s3";

describe("S3", () => {
  let floci: FlociContainer;

  beforeAll(async () => {
    floci = await new FlociContainer().start();
  });

  afterAll(async () => {
    await floci.stop();
  });

  it("creates a bucket", async () => {
    const s3 = new S3Client({
      endpoint: floci.getEndpoint(),
      region: floci.getRegion(),
      credentials: {
        accessKeyId: floci.getAccessKey(),
        secretAccessKey: floci.getSecretKey(),
      },
      forcePathStyle: true,
    });

    await s3.send(new CreateBucketCommand({ Bucket: "my-bucket" }));
  });
});
```


**Python**

```
pip install testcontainers-floci
```

```
import boto3
from testcontainers_floci import FlociContainer


def test_s3_create_bucket():
    with FlociContainer() as floci:
        s3 = boto3.client(
            "s3",
            endpoint_url=floci.get_endpoint(),
            region_name=floci.get_region(),
            aws_access_key_id=floci.get_access_key(),
            aws_secret_access_key=floci.get_secret_key(),
        )
        s3.create_bucket(Bucket="my-bucket")
```

The [`compatibility-tests`](https://github.com/floci-io/floci/blob/main/compatibility-tests) directory validates Floci across SDKs and tooling workflows.

| Module | Language / Tool | SDK / Client | Tests |
| --- | --- | --- | --- |
| `sdk-test-java` | Java 17 | AWS SDK for Java v2 | 899 |
| `sdk-test-node` | Node.js | AWS SDK for JavaScript v3 | 366 |
| `sdk-test-python` | Python 3 | boto3 | 272 |
| `sdk-test-go` | Go | AWS SDK for Go v2 + RDS Data API SDK v1 | 145 |
| `sdk-test-awscli` | Bash | AWS CLI v2 | 152 |
| `sdk-test-rust` | Rust | AWS SDK for Rust | 90 |
| `compat-terraform` | Terraform | v1.10+ | 14 |
| `compat-opentofu` | OpenTofu | v1.9+ | 14 |
| `compat-cdk` | AWS CDK | v2+ | 17 |

**1,969 automated compatibility tests across 6 SDKs and 3 IaC tools.**

Migrating from LocalStack
-------------------------

Floci is a drop-in replacement for LocalStack Community. The port, credentials, SDK configuration, and CLI endpoint pattern work the same way. Swap the image and keep going.

```
# Before
image: localstack/localstack

# After, standard image
image: floci/floci:latest

# After, if init scripts need AWS CLI or boto3
image: floci/floci:latest-compat
```

LocalStack environment variables are translated automatically:

| LocalStack | Floci equivalent |
| --- | --- |
| `LOCALSTACK_HOST` | `FLOCI_HOSTNAME` |
| `PERSISTENCE=1` | `FLOCI_STORAGE_MODE=persistent` |
| `LAMBDA_DOCKER_NETWORK` | `FLOCI_SERVICES_LAMBDA_DOCKER_NETWORK` |
| `LAMBDA_REMOVE_CONTAINERS=1` | `FLOCI_SERVICES_LAMBDA_EPHEMERAL=true` |
| `DEBUG=1` | `QUARKUS_LOG_LEVEL=DEBUG` |

Init scripts mounted under `/etc/localstack/init/` run unchanged. The `/_localstack/init` and `/_localstack/health` endpoints are still served. Once the emulator is up, the log also ends with a LocalStack-style `Ready.` line, so tooling that watches the log for it — such as the default wait strategy of Testcontainers' `LocalStackContainer` — works unchanged. Set `LOCALSTACK_PARITY=false` to opt out of automatic translation.

See the [full migration guide](https://floci.io/floci/getting-started/migrate-from-localstack/).

Every tag combines a variant and a channel.

| Channel | Standard | Compat with AWS CLI and boto3 |
| --- | --- | --- |
| Release, floating | `latest` | `latest-compat` |
| Release, pinned | `x.y.z` | `x.y.z-compat` |
| Nightly, floating | `nightly` | `nightly-compat` |
| Nightly, dated | `nightly-mmddyyyy` | `nightly-mmddyyyy-compat` |

Use `latest` for stable releases, a pinned version for reproducible builds, and `nightly` to track `main`.

```
# Recommended
image: floci/floci:latest

# Includes AWS CLI and boto3
image: floci/floci:latest-compat

# Pinned release
image: floci/floci:1.5.11

# Track main
image: floci/floci:nightly
```

All settings are overridable through environment variables with the `FLOCI_` prefix.

| Variable | Default | Description |
| --- | --- | --- |
| `FLOCI_PORT` | `4566` | Port exposed by the Floci API |
| `FLOCI_DEFAULT_REGION` | `us-east-1` | Default AWS region |
| `FLOCI_DEFAULT_ACCOUNT_ID` | `000000000000` | Default AWS account ID |
| `FLOCI_BASE_URL` | `http://localhost:4566` | Base URL used when Floci returns service URLs |
| `FLOCI_HOSTNAME` | Unset | Hostname used in returned URLs when Floci runs inside Docker Compose |
| `FLOCI_STORAGE_MODE` | `memory` | Storage mode: `memory`, `persistent`, `hybrid`, or `wal` |
| `FLOCI_STORAGE_PERSISTENT_PATH` | `./data` | Directory used for persisted state |
| `FLOCI_ECR_BASE_URI` | `public.ecr.aws` | ECR base URI used when pulling container images |

Full reference: [configuration docs](https://floci.io/floci/configuration/advanced/application-yml)

### Multi-container Docker Compose

When your application runs in a different container, set `FLOCI_HOSTNAME` to the Floci service name so returned URLs, such as SQS `QueueUrl` values, resolve correctly.

```
services:
  floci:
    image: floci/floci:latest
    ports:
      - "4566:4566"
    environment:
      - FLOCI_HOSTNAME=floci

  my-app:
    environment:
      - AWS_ENDPOINT_URL=http://floci:4566
    depends_on:
      - floci
```

Without this, services may return URLs using `localhost`, which points to the wrong container from the application container.

Community
---------

Join the Floci community on [Slack](https://join.slack.com/t/floci/shared_invite/zt-3tjn02s3q-A00kEjJ1cZxsg_imTfy6Cw) or [GitHub Discussions](https://github.com/orgs/floci-io/discussions). Feature ideas, compatibility questions, design tradeoffs, and rough proposals are welcome.

[![Star History Chart](https://camo.githubusercontent.com/ba905122e930e3f522fcd999f11250cb13a62b5decc15befefb9a18a7acc9ba9/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f63686172743f7265706f733d666c6f63692d696f2f666c6f636926747970653d64617465266c6567656e643d746f702d6c656674)](https://www.star-history.com/?repos=floci-io%2Ffloci&type=date&legend=top-left)

[![](https://camo.githubusercontent.com/1ed0fdc36d4bbe6a2b1b3dacb3cbf5cc77cb063a3bd29591d398c49495991259/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d666c6f63692d696f2f666c6f6369266d61783d31303026636f6c756d6e733d3230)](https://github.com/floci-io/floci/graphs/contributors)

MIT. Use it however you want.