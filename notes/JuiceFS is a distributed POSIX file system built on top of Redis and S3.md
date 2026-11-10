---
title: "JuiceFS is a distributed POSIX file system built on top of Redis and S3"
url: https://github.com/juicedata/juicefs
clipped: 2026-06-17 01:58:16
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [JuiceFS is a distributed POSIX file system built on top of Redis and S3](https://github.com/juicedata/juicefs)

## Digest Summary
JuiceFS is a distributed POSIX‑compatible file system that leverages Redis for metadata management and object storage services such as S3 for data persistence. The project provides a stable release, continuous‑integration workflow status, and Go code quality metrics. Documentation is available in English, and community support is offered via a Slack channel. Architectural diagrams illustrate the system’s design, data‑structure layout, and file storage methodology. Benchmark results are presented for sequential read/write performance and metadata operation latency, demonstrating scalability. Contribution activity is highlighted by a star‑history chart and a list of active maintainers and developers.

## Discussion Summary
Comments express mixed views on JuiceFS. Many raise concerns about relying on Redis or other volatile metadata stores, demanding stronger durability guarantees and benchmark comparisons with alternatives such as PostgreSQL or database‑free solutions. Experiences of limited performance and data‑loss risk when metadata fails are cited, prompting some teams to abandon the system. Critics note incomplete POSIX semantics and suggest native S3‑compatible designs for large‑scale workloads, while a few acknowledge JuiceFS’s innovation but see it suited mainly for smaller or experimental projects.

---

## Full Article

[![JuiceFS Logo](https://github.com/juicedata/juicefs/raw/main/docs/en/images/juicefs-logo-new.svg)](https://github.com/juicedata/juicefs)

[![Latest Stable Release](https://camo.githubusercontent.com/cec0bf624db538d949f984c369863000bc44cd310780dd4f675274db55f0169d/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f6a75696365646174612f6a756963656673)](https://github.com/juicedata/juicefs/releases/latest)
[![GitHub Workflow Status](https://camo.githubusercontent.com/2e766deb7a59d61ca1a9ba15ccc06885e81f4fa898c34d3ed6a5935bf9c6d5b8/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f6a75696365646174612f6a7569636566732f756e697474657374732e796d6c3f6272616e63683d6d61696e266c6162656c3d556e697425323054657374696e67)](https://github.com/juicedata/juicefs/actions/workflows/unittests.yml)
[![GitHub Workflow Status](https://camo.githubusercontent.com/466bcc5ec53e4102d5182089e73006eb0d91bc4e552292db8c2ce5017c7f3cdc/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f6a75696365646174612f6a7569636566732f696e746567726174696f6e74657374732e796d6c3f6272616e63683d6d61696e266c6162656c3d496e746567726174696f6e25323054657374696e67)](https://github.com/juicedata/juicefs/actions/workflows/integrationtests.yml)
[![Go Report](https://camo.githubusercontent.com/b5fae9aa1aa50391e5b08ee7f89dc43071ba9686fc03aee762460176ed3aa772/68747470733a2f2f676f7265706f7274636172642e636f6d2f62616467652f6769746875622e636f6d2f6a75696365646174612f6a756963656673)](https://goreportcard.com/report/github.com/juicedata/juicefs)
[![English doc](https://camo.githubusercontent.com/4c7edbd33f4fb971a378441dac037365bc1696779b2b317d0a4f0fc822c0b247/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f63732d446f6325323043656e7465722d627269676874677265656e)](https://juicefs.com/docs/community/introduction)
[![Join Discord](https://camo.githubusercontent.com/d7224b78869ad45eeaf4923733ba58a5d156acc704d909fda909dc3316f3fcbc/68747470733a2f2f62616467656e2e6e65742f62616467652f446973636f72642f4a6f696e2532304a7569636546532f3061626435393f69636f6e3d646973636f7264)](https://go.juicefs.com/discord)

**JuiceFS** is a high-performance [POSIX](https://en.wikipedia.org/wiki/POSIX) file system released under Apache License 2.0, particularly designed for the cloud-native environment. The data, stored via JuiceFS, will be persisted in Object Storage *(e.g. Amazon S3)*, and the corresponding metadata can be persisted in various compatible database engines such as Redis, MySQL, and TiKV based on the scenarios and requirements.

With JuiceFS, massive cloud storage can be directly connected to big data, machine learning, artificial intelligence, and various application platforms in production environments. Without modifying code, the massive cloud storage can be used as efficiently as local storage.

📖 **Document**: [Quick Start Guide](https://juicefs.com/docs/community/quick_start_guide)

1. **Fully POSIX-compatible**: Use as a local file system, seamlessly docking with existing applications without breaking business workflow.
2. **Fully Hadoop-compatible**: JuiceFS' [Hadoop Java SDK](https://juicefs.com/docs/community/hadoop_java_sdk) is compatible with Hadoop 2.x and Hadoop 3.x as well as a variety of components in the Hadoop ecosystems.
3. **S3-compatible**: JuiceFS' [S3 Gateway](https://juicefs.com/docs/community/s3_gateway) provides an S3-compatible interface.
4. **Cloud Native**: A [Kubernetes CSI Driver](https://juicefs.com/docs/community/how_to_use_on_kubernetes) is provided for easily using JuiceFS in Kubernetes.
5. **Shareable**: JuiceFS is a shared file storage that can be read and written by thousands of clients.
6. **Strong Consistency**: The confirmed modification will be immediately visible on all the servers mounted with the same file system.
7. **Outstanding Performance**: The latency can be as low as a few milliseconds, and the throughput can be expanded nearly unlimitedly *(depending on the size of the Object Storage)*. [Test results](https://juicefs.com/docs/community/benchmark)
8. **Data Encryption**: Supports data encryption in transit and at rest (please refer to [the guide](https://juicefs.com/docs/community/security/encrypt) for more information).
9. **Global File Locks**: JuiceFS supports both BSD locks (flock) and POSIX record locks (fcntl).
10. **Data Compression**: JuiceFS supports [LZ4](https://lz4.github.io/lz4) or [Zstandard](https://facebook.github.io/zstd) to compress all your data.

---

[Architecture](https://github.com/juicedata/juicefs#architecture) | [Getting Started](https://github.com/juicedata/juicefs#getting-started) | [Advanced Topics](https://github.com/juicedata/juicefs#advanced-topics) | [POSIX Compatibility](https://github.com/juicedata/juicefs#posix-compatibility) | [Performance Benchmark](https://github.com/juicedata/juicefs#performance-benchmark) | [Supported Object Storage](https://github.com/juicedata/juicefs#supported-object-storage) | [Who is using](https://github.com/juicedata/juicefs#who-is-using) | [Roadmap](https://github.com/juicedata/juicefs#roadmap) | [Reporting Issues](https://github.com/juicedata/juicefs#reporting-issues) | [Contributing](https://github.com/juicedata/juicefs#contributing) | [Community](https://github.com/juicedata/juicefs#community) | [Usage Tracking](https://github.com/juicedata/juicefs#usage-tracking) | [License](https://github.com/juicedata/juicefs#license) | [Credits](https://github.com/juicedata/juicefs#credits) | [FAQ](https://github.com/juicedata/juicefs#faq)

---

JuiceFS consists of three parts:

1. **JuiceFS Client**: Coordinates Object Storage and metadata storage engine as well as implementation of file system interfaces such as POSIX, Hadoop, Kubernetes, and S3 gateway.
2. **Data Storage**: Stores data, with supports of a variety of data storage media, e.g., local disk, public or private cloud Object Storage, and HDFS.
3. **Metadata Engine**: Stores the corresponding metadata that contains information of file name, file size, permission group, creation and modification time and directory structure, etc., with supports of different metadata engines, e.g., Redis, MySQL, SQLite and TiKV.

[![JuiceFS Architecture](https://github.com/juicedata/juicefs/raw/main/docs/en/images/juicefs-arch-new.png)](https://github.com/juicedata/juicefs/blob/main/docs/en/images/juicefs-arch-new.png)

JuiceFS can store the metadata of file system on different metadata engines, like Redis, which is a fast, open-source, in-memory key-value data storage, particularly suitable for storing metadata; meanwhile, all the data will be stored in Object Storage through JuiceFS client. [Learn more](https://juicefs.com/docs/community/architecture)

[![data-structure-diagram](https://github.com/juicedata/juicefs/raw/main/docs/en/images/data-structure-diagram.svg)](https://github.com/juicedata/juicefs/blob/main/docs/en/images/data-structure-diagram.svg)

Each file stored in JuiceFS is split into **"Chunk"** s at a fixed size with the default upper limit of 64 MiB. Each Chunk is composed of one or more **"Slice"**(s), and the length of the slice varies depending on how the file is written. Each slice is composed of size-fixed **"Block"** s, which are 4 MiB by default. These blocks will be stored in Object Storage in the end; at the same time, the metadata information of the file and its Chunks, Slices, and Blocks will be stored in metadata engines via JuiceFS. [Learn more](https://juicefs.com/docs/community/architecture/#how-juicefs-store-files)

[![How JuiceFS stores your files](https://github.com/juicedata/juicefs/raw/main/docs/en/images/how-juicefs-stores-files.svg)](https://github.com/juicedata/juicefs/blob/main/docs/en/images/how-juicefs-stores-files.svg)

When using JuiceFS, files will eventually be split into Chunks, Slices and Blocks and stored in Object Storage. Therefore, the source files stored in JuiceFS cannot be found in the file browser of the Object Storage platform; instead, there are only a chunks directory and a bunch of digitally numbered directories and files in the bucket. Don't panic! This is just the secret of the high-performance operation of JuiceFS!

Before you begin, make sure you have:

1. One supported metadata engine, see [How to Set Up Metadata Engine](https://juicefs.com/docs/community/databases_for_metadata)
2. One supported Object Storage for storing data blocks, see [Supported Object Storage](https://juicefs.com/docs/community/how_to_setup_object_storage)
3. [JuiceFS Client](https://juicefs.com/docs/community/installation) downloaded and installed

Please refer to [Quick Start Guide](https://juicefs.com/docs/community/quick_start_guide) to start using JuiceFS right away!

Check out all the command line options in [command reference](https://juicefs.com/docs/community/command_reference).

JuiceFS can be used as a persistent volume for Docker and Podman, please check [here](https://juicefs.com/docs/community/juicefs_on_docker) for details.

It is also very easy to use JuiceFS on Kubernetes. Please find more information [here](https://juicefs.com/docs/community/how_to_use_on_kubernetes).

If you wanna use JuiceFS in Hadoop, check [Hadoop Java SDK](https://juicefs.com/docs/community/hadoop_java_sdk).

Please refer to [JuiceFS Document Center](https://juicefs.com/docs/community/introduction) for more information.

JuiceFS has passed all of the compatibility tests (8813 in total) in the latest [pjdfstest](https://github.com/pjd/pjdfstest) .

```
All tests successful.

Test Summary Report
-------------------
/root/soft/pjdfstest/tests/chown/00.t          (Wstat: 0 Tests: 1323 Failed: 0)
  TODO passed:   693, 697, 708-709, 714-715, 729, 733
Files=235, Tests=8813, 233 wallclock secs ( 2.77 usr  0.38 sys +  2.57 cusr  3.93 csys =  9.65 CPU)
Result: PASS
```

Aside from the POSIX features covered by pjdfstest, JuiceFS also provides:

* **Close-to-open consistency**. Once a file is written *and* closed, it is guaranteed to view the written data in the following opens and reads from any client. Within the same mount point, all the written data can be read immediately.
* Rename and all other metadata operations are atomic, which are guaranteed by supported metadata engine transaction.
* Opened files remain accessible after unlink from same mount point.
* Mmap (tested with FSx).
* Fallocate with punch hole support.
* Extended attributes (xattr).
* BSD locks (flock).
* POSIX record locks (fcntl).

JuiceFS provides a subcommand that can run a few basic benchmarks to help you understand how it works in your environment:

[![JuiceFS Bench](https://github.com/juicedata/juicefs/raw/main/docs/en/images/juicefs-bench.png)](https://github.com/juicedata/juicefs/blob/main/docs/en/images/juicefs-bench.png)

A sequential read/write benchmark has also been performed on JuiceFS, [EFS](https://aws.amazon.com/efs) and [S3FS](https://github.com/s3fs-fuse/s3fs-fuse) by [fio](https://github.com/axboe/fio).

[![Sequential Read Write Benchmark](https://github.com/juicedata/juicefs/raw/main/docs/en/images/sequential-read-write-benchmark.svg)](https://github.com/juicedata/juicefs/blob/main/docs/en/images/sequential-read-write-benchmark.svg)

Above result figure shows that JuiceFS can provide 10X more throughput than the other two (see [more details](https://juicefs.com/docs/community/fio)).

A simple mdtest benchmark has been performed on JuiceFS, [EFS](https://aws.amazon.com/efs) and [S3FS](https://github.com/s3fs-fuse/s3fs-fuse) by [mdtest](https://github.com/hpc/ior).

[![Metadata Benchmark](https://github.com/juicedata/juicefs/raw/main/docs/en/images/metadata-benchmark.svg)](https://github.com/juicedata/juicefs/blob/main/docs/en/images/metadata-benchmark.svg)

The result shows that JuiceFS can provide significantly more metadata IOPS than the other two (see [more details](https://juicefs.com/docs/community/mdtest)).

See [Real-Time Performance Monitoring](https://juicefs.com/docs/community/fault_diagnosis_and_analysis#performance-monitor) if you encountered performance issues.

* Amazon S3 *(and other S3 compatible Object Storage services)*
* Google Cloud Storage
* Azure Blob Storage
* Alibaba Cloud Object Storage Service (OSS)
* Tencent Cloud Object Storage (COS)
* Qiniu Cloud Object Storage (Kodo)
* QingStor Object Storage
* Ceph RGW
* MinIO
* Local disk
* Redis
* ...

JuiceFS supports numerous Object Storage services. [Learn more](https://juicefs.com/docs/community/how_to_setup_object_storage#supported-object-storage).

JuiceFS is production ready and used by thousands of machines in production. A list of users has been assembled and documented [here](https://juicefs.com/docs/community/adopters). In addition JuiceFS has several collaborative projects that integrate with other open source projects, which we have documented [here](https://juicefs.com/docs/community/integrations). If you are also using JuiceFS, please feel free to let us know, and you are welcome to share your specific experience with everyone.

The storage format is stable, and will be supported by all future releases.

* Gateway Optimization
* Resumable Sync
* Read-ahead Optimization
* Optimization for Large-scale Scenarios
* Snapshots

We use [GitHub Issues](https://github.com/juicedata/juicefs/issues) to track community reported issues. You can also [contact](https://github.com/juicedata/juicefs#community) the community for any questions.

Thank you for your contribution! Please refer to the [JuiceFS Contributing Guide](https://juicefs.com/docs/community/development/contributing_guide) for more information.

Community
---------

Welcome to join the [Discussions](https://github.com/juicedata/juicefs/discussions) and the [Discord channel](https://go.juicefs.com/discord) to connect with JuiceFS team members and other users.

JuiceFS collects **anonymous** usage data by default to help us better understand how the community is using JuiceFS. Only core metrics (e.g. version number) will be reported, and user data and any other sensitive data will not be included. The related code can be viewed [here](https://github.com/juicedata/juicefs/blob/main/pkg/usage/usage.go).

You could also disable reporting easily by command line option `--no-usage-report`:

```
juicefs mount --no-usage-report
```

JuiceFS is open-sourced under Apache License 2.0, see [LICENSE](https://github.com/juicedata/juicefs/blob/main/LICENSE).

The design of JuiceFS was inspired by [Google File System](https://research.google/pubs/pub51), [HDFS](https://hadoop.apache.org) and [MooseFS](https://moosefs.com). Thanks for their great work!

### Why doesn't JuiceFS support XXX Object Storage?

JuiceFS supports many Object Storage services. Please check out [this list](https://juicefs.com/docs/community/how_to_setup_object_storage#supported-object-storage) first. If the Object Storage you want to use is compatible with S3, you could treat it as S3. Otherwise, try reporting any issue.

### Can I use Redis Cluster as metadata engine?

Yes. Since [v1.0.0 Beta3](https://github.com/juicedata/juicefs/releases/tag/v1.0.0-beta3) JuiceFS supports the use of [Redis Cluster](https://redis.io/docs/manual/scaling) as the metadata engine, but it should be noted that Redis Cluster requires that the keys of all operations in a transaction must be in the same hash slot, so a JuiceFS file system can only use one hash slot.

See ["Redis Best Practices"](https://juicefs.com/docs/community/redis_best_practices) for more information.

### What's the difference between JuiceFS and XXX?

See ["Comparison with Others"](https://juicefs.com/docs/community/comparison/juicefs_vs_alluxio) for more information.

For more FAQs, please see the [full list](https://juicefs.com/docs/community/faq).

[![Star History Chart](https://camo.githubusercontent.com/4b0bfc7a450e88b5992d8be47e970b03dbe4b31e94319ce3fac064b7027d4873/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d6a75696365646174612f6a75696365667326747970653d44617465)](https://star-history.com/#juicedata/juicefs&Date)