---
title: "Google copybara: moving code between repositories"
url: https://github.com/google/copybara
clipped: 2026-08-31 12:17:39
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Google copybara: moving code between repositories](https://github.com/google/copybara)

## Digest Summary
Copybara is a Google‑internal tool for transforming and syncing code between repositories, primarily supporting Git (with experimental Mercurial read support). It designates one repository as authoritative while allowing contributions from any repository and enabling releases from any of them. Core capabilities include:  

- Importing sections of code between confidential and public repos, and vice‑versa.  
- Propagating changes from non‑authoritative to authoritative repos with automatic conflict handling.  
- Stateless operation: state is stored as a label in destination commit messages, ensuring consistent results across users.  

Configuration uses a Skylark‑style workflow (e.g., `core.workflow`) specifying origins, destinations, file globs, authoring, and transformations (replace, move).  

Installation options:  

- Use weekly snapshot binaries (requires Java 21+, add `--java_runtime_version=remotejdk_21` to `.bazelrc`).  
- Build from source with JDK 11 and Bazel (`bazel build //java/com/google/copybara:copybara_deploy.jar`).  
- Add as an external Bazel repository via `http_archive` in `WORKSPACE`.  
- Run via Docker (experimental) with environment variables to set subcommand, config, workflow, etc.  

Documentation is evolving; contact the mailing list for queries.

---

## Full Article

[Skip to content](https://github.com/google/copybara#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      
    

      
  
  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

  

  

      

        
            
  
      
    
    
      [google](https://github.com/google)    
    /
    
      [copybara](https://github.com/google/copybara)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2Fgoogle%2Fcopybara)    You must be signed in to change notification settings

  

  
- 
          [Fork
    344](https://github.com/login?return_to=%2Fgoogle%2Fcopybara)
  

  
- 
        
        [Star
          3.8k](https://github.com/login?return_to=%2Fgoogle%2Fcopybara)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     master[Branches](https://github.com/google/copybara/branches)[Tags](https://github.com/google/copybara/tags)Go to fileCodeOpen more actions menu

## Latest commit

 

## History

[3,697 Commits](https://github.com/google/copybara/commits/master/)3,697 Commits

## Folders and files

NameNameLast commit messageLast commit date[.docker](https://github.com/google/copybara/tree/master/.docker)[.docker](https://github.com/google/copybara/tree/master/.docker)  [.github/workflows](https://github.com/google/copybara/tree/master/.github/workflows)[.github/workflows](https://github.com/google/copybara/tree/master/.github/workflows)  [ci/ubuntu](https://github.com/google/copybara/tree/master/ci/ubuntu)[ci/ubuntu](https://github.com/google/copybara/tree/master/ci/ubuntu)  [copybara/integration](https://github.com/google/copybara/tree/master/copybara/integration)[copybara/integration](https://github.com/google/copybara/tree/master/copybara/integration)  [docs](https://github.com/google/copybara/tree/master/docs)[docs](https://github.com/google/copybara/tree/master/docs)  [external/third_party](https://github.com/google/copybara/tree/master/external/third_party)[external/third_party](https://github.com/google/copybara/tree/master/external/third_party)  [java/com/google/copybara](https://github.com/google/copybara/tree/master/java/com/google/copybara)[java/com/google/copybara](https://github.com/google/copybara/tree/master/java/com/google/copybara)  [javatests/com/google/copybara](https://github.com/google/copybara/tree/master/javatests/com/google/copybara)[javatests/com/google/copybara](https://github.com/google/copybara/tree/master/javatests/com/google/copybara)  [scripts](https://github.com/google/copybara/tree/master/scripts)[scripts](https://github.com/google/copybara/tree/master/scripts)  [third_party](https://github.com/google/copybara/tree/master/third_party)[third_party](https://github.com/google/copybara/tree/master/third_party)  [.bazelproject](https://github.com/google/copybara/blob/master/.bazelproject)[.bazelproject](https://github.com/google/copybara/blob/master/.bazelproject)  [.bazelrc](https://github.com/google/copybara/blob/master/.bazelrc)[.bazelrc](https://github.com/google/copybara/blob/master/.bazelrc)  [.dockerignore](https://github.com/google/copybara/blob/master/.dockerignore)[.dockerignore](https://github.com/google/copybara/blob/master/.dockerignore)  [.gitignore](https://github.com/google/copybara/blob/master/.gitignore)[.gitignore](https://github.com/google/copybara/blob/master/.gitignore)  [AUTHORS](https://github.com/google/copybara/blob/master/AUTHORS)[AUTHORS](https://github.com/google/copybara/blob/master/AUTHORS)  [BUILD](https://github.com/google/copybara/blob/master/BUILD)[BUILD](https://github.com/google/copybara/blob/master/BUILD)  [CONTRIBUTING.md](https://github.com/google/copybara/blob/master/CONTRIBUTING.md)[CONTRIBUTING.md](https://github.com/google/copybara/blob/master/CONTRIBUTING.md)  [Dockerfile](https://github.com/google/copybara/blob/master/Dockerfile)[Dockerfile](https://github.com/google/copybara/blob/master/Dockerfile)  [LICENSE](https://github.com/google/copybara/blob/master/LICENSE)[LICENSE](https://github.com/google/copybara/blob/master/LICENSE)  [MODULE.bazel](https://github.com/google/copybara/blob/master/MODULE.bazel)[MODULE.bazel](https://github.com/google/copybara/blob/master/MODULE.bazel)  [README.md](https://github.com/google/copybara/blob/master/README.md)[README.md](https://github.com/google/copybara/blob/master/README.md)  [ci.Dockerfile](https://github.com/google/copybara/blob/master/ci.Dockerfile)[ci.Dockerfile](https://github.com/google/copybara/blob/master/ci.Dockerfile)  [cloudbuild.sh](https://github.com/google/copybara/blob/master/cloudbuild.sh)[cloudbuild.sh](https://github.com/google/copybara/blob/master/cloudbuild.sh)  [cloudbuild.yaml](https://github.com/google/copybara/blob/master/cloudbuild.yaml)[cloudbuild.yaml](https://github.com/google/copybara/blob/master/cloudbuild.yaml)  [cloudbuild_setup.sh](https://github.com/google/copybara/blob/master/cloudbuild_setup.sh)[cloudbuild_setup.sh](https://github.com/google/copybara/blob/master/cloudbuild_setup.sh)  [repositories.bzl](https://github.com/google/copybara/blob/master/repositories.bzl)[repositories.bzl](https://github.com/google/copybara/blob/master/repositories.bzl)  View all files

## Repository files navigation

# Copybara

A tool for transforming and moving code between repositories.

Copybara is a tool used internally at Google. It transforms and moves code between repositories.

Often, source code needs to exist in multiple repositories, and Copybara allows you to transform
and move source code between these repositories. A common case is a project that involves
maintaining a confidential repository and a public repository in sync.

Copybara requires you to choose one of the repositories to be the authoritative repository, so that
there is always one source of truth. However, the tool allows contributions to any repository, and
any repository can be used to cut a release.

The most common use case involves repetitive movement of code from one repository to another.
Copybara can also be used for moving code once to a new repository.

Examples uses of Copybara include:

- 

Importing sections of code from a confidential repository to a public repository.

- 

Importing code from a public repository to a confidential repository.

- 

Importing a change from a non-authoritative repository into the authoritative repository. When
a change is made in the non-authoritative repository (for example, a contributor in the public
repository), Copybara transforms and moves that change into the appropriate place in the
authoritative repository. Any merge conflicts are dealt with in the same way as an out-of-date
change within the authoritative repository.

One of the main features of Copybara is that it is stateless, or more specifically, that it stores
the state in the destination repository (As a label in the commit message). This allows several
users (or a service) to use Copybara for the same config/repositories and get the same result.

Currently, the only supported type of repository is Git. Copybara is also able
to read from Mercurial repositories, but the feature is still experimental.
The extensible architecture allows adding bespoke origins and destinations
for almost any use case.
Official support for other repositories types will be added in the future.

## Example

 `core.workflow(
    name = "default",
    origin = git.github_origin(
      url = "https://github.com/google/copybara.git",
      ref = "master",
    ),
    destination = git.destination(
        url = "file:///tmp/foo",
    ),

    # Copy everything but don't remove a README_INTERNAL.txt file if it exists.
    destination_files = glob(["third_party/copybara/**"], exclude = ["README_INTERNAL.txt"]),

    authoring = authoring.pass_thru("Default email <default@default.com>"),
    transformations = [
        core.replace(
                before = "//third_party/bazel/bashunit",
                after = "//another/path:bashunit",
                paths = glob(["**/BUILD"])),
        core.move("", "third_party/copybara")
    ],
)` 

Run:
 `$ (mkdir /tmp/foo ; cd /tmp/foo ; git init --bare)
$ copybara copy.bara.sky` 

## Getting Started using Copybara

The easiest way to start is with weekly "snapshot" releases, that include pre-built a binary.
Note that these are released automatically without any manual testing, version compatibility or correctness guarantees.

Choose a release from [https://github.com/google/copybara/releases](https://github.com/google/copybara/releases).

### Building from Source

To use an unreleased version of copybara, so you need to compile from HEAD.
In order to do that, you need to do the following:

- [Install JDK 11](https://www.oracle.com/java/technologies/downloads/#java11).

- [Install Bazel](https://bazel.build/install).

- Clone the copybara source locally:

-  `git clone https://github.com/google/copybara.git` 

- Build:

-  `bazel build //java/com/google/copybara` 

-  `bazel build //java/com/google/copybara:copybara_deploy.jar`  to create an executable uberjar.

- Tests:  `bazel test //...`  if you want to ensure you are not using a broken version. Note that
certain tests require the underlying tool to be installed(e.g. Mercurial, Quilt, etc.). It is
fine to skip those tests if your Pull Request is unrelated to those modules (And our CI will
run all the tests anyway).

### System packages

These packages can be installed using the appropriate package manager for your
system.

#### Arch Linux

-  `` [aur/copybara-git](https://aur.archlinux.org/packages/copybara-git)

### Using Intellij with Bazel plugin

If you use Intellij and the Bazel plugin, use this project configuration:
 ` `directories:
  copybara/integration
  java/com/google/copybara
  javatests/com/google/copybara
  third_party

targets:
  //copybara/integration/...
  //java/com/google/copybara/...
  //javatests/com/google/copybara/...
  //third_party/...
` ` 

Note: configuration files can be stored in any place, even in a local folder.
We recommend using a VCS (like git) to store them; treat them as source code.

### Using pre-built Copybara in Bazel

If using a weekly snapshot release, install Copybara as follows:

- Copybara ships with class files with version 65.0, so it must be run with Java Runtime 21 or greater. Add to your  `.bazelrc`  file:  `run --java_runtime_version=remotejdk_21` 

- Use  `http_jar`  to download the release artifact.

- In WORKSPACE:  `load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_jar")` 

- In MODULE.bazel:  `http_jar = use_repo_rule("@bazel_tools//tools/build_defs/repo:http.bzl", "http_jar")` 

- In WORKSPACE or MODULE.bazel, fill in the  `[version]`  placeholder:
 `http_jar(
    name = "com_github_google_copybara",
    # Fill in from https://github.com/google/copybara/releases/download/[version]/copybara_deploy.jar.sha256
    # sha256 = "",
    urls = ["https://github.com/google/copybara/releases/download/[version]/copybara_deploy.jar"],
)` 

- In any BUILD file (perhaps  `/tools/BUILD.bazel` ) declare the  `java_binary` :
 `load("@rules_java//java:java_binary.bzl", "java_binary")
java_binary(
   name = "copybara",
   main_class = "com.google.copybara.Main",
   runtime_deps = ["@com_github_google_copybara//jar"],
)` 

- Use that target with  `bazel run` , for example  `bazel run //tools:copybara -- migrate copy.bara.sky` 

### Building Copybara from Source as an external Bazel repository

There are convenience macros defined for all of Copybara's dependencies. Add the
following code to your  `WORKSPACE`  file, replacing  `{{ sha256sum }}`  and
 `{{ commit }}`  as necessary.
 `http_archive(
  name = "com_github_google_copybara",
  sha256 = "{{ sha256sum }}",
  strip_prefix = "copybara-{{ commit }}",
  url = "https://github.com/google/copybara/archive/{{ commit }}.zip",
)

load("@com_github_google_copybara//:repositories.bzl", "copybara_repositories")

copybara_repositories()

load("@com_github_google_copybara//:repositories.maven.bzl", "copybara_maven_repositories")

copybara_maven_repositories()

load("@com_github_google_copybara//:repositories.go.bzl", "copybara_go_repositories")

copybara_go_repositories()` 

You can then build and run the Copybara tool from within your workspace:
 `bazel run @com_github_google_copybara//java/com/google/copybara -- <args...>` 

### Using Docker to build and run Copybara

NOTE: Docker use is currently experimental, and we encourage feedback or contributions.

You can build copybara using Docker like so
 `docker build --rm -t copybara .` 

Once this has finished building, you can run the image like so from the root of
the code you are trying to use Copybara on:
 `docker run -it -v "$(pwd)":/usr/src/app copybara help` 

#### Environment variables

In addition to passing cmd args to the container, you can also set the following
environment variables as an alternative:

-  `COPYBARA_SUBCOMMAND=migrate` 

- allows you to change the command run, defaults to  `migrate` 

-  `COPYBARA_CONFIG=copy.bara.sky` 

- allows you to specify a path to a config file, defaults to root  `copy.bara.sky` 

-  `COPYBARA_WORKFLOW=default` 

- allows you to specify the workflow to run, defaults to  `default` 

-  `COPYBARA_SOURCEREF=''` 

- allows you to specify the sourceref, defaults to none

-  `COPYBARA_OPTIONS=''` 

- allows you to specify options for copybara, defaults to none

 `docker run \
    -e COPYBARA_SUBCOMMAND='validate' \
    -e COPYBARA_CONFIG='other.config.sky' \
    -v "$(pwd)":/usr/src/app \
    -it copybara` 

#### Git Config and Credentials

There are a number of ways by which to share your git config and ssh credentials
with the Docker container, an example is below:
 `docker run \
    -v ~/.gitconfig:/root/.gitconfig:ro \
    -v ~/.ssh:/root/.ssh \
    -v ${SSH_AUTH_SOCK}:${SSH_AUTH_SOCK} -e SSH_AUTH_SOCK
    -v "$(pwd)":/usr/src/app \
    -it copybara` 

## Documentation

We are still working on the documentation. Here are some resources:

- [Reference documentation](https://github.com/google/copybara/blob/master/docs/reference.md)

- [Examples](https://github.com/google/copybara/blob/master/docs/examples.md)

- [Tutorial on how to get started](https://blog.kubesimplify.com/moving-code-between-git-repositories-with-copybara)

## Contact us

If you have any questions about how Copybara works, please contact us at our
[mailing list](https://groups.google.com/forum/#!forum/copybara-discuss).

## Optional tips

- 

If you want to see the test errors in Bazel, instead of having to  `cat`  the
logs, add this line to your  `~/.bazelrc` :
 ` `test --test_output=streamed
` ` 

## About

Copybara: A tool for transforming and moving code between repositories.

### Resources

[Readme](https://github.com/google/copybara#readme-ov-file)[Apache-2.0 license](https://github.com/google/copybara#Apache-2.0-1-ov-file)

### Code of conduct

[Code of conduct](https://github.com/google/copybara#coc-ov-file)

### Contributing

[Contributing](https://github.com/google/copybara#contributing-ov-file)

### Security policy

[Security policy](https://github.com/google/copybara#security-ov-file)[Activity](https://github.com/google/copybara/activity)[Custom properties](https://github.com/google/copybara/custom-properties)

### Stars

3.8k stars

### Watchers

51 watching

### Forks

[344 forks](https://github.com/google/copybara/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fgoogle%2Fcopybara&report=google+%28user%29)

## Releases

## Packages

## Used by

## Contributors

## Languages

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
