---
title: "The development pipeline is a production system"
url: https://sundry.jerryorr.com/2026/07/31/development-pipeline-is-a-production-system
clipped: 2026-08-31 12:17:56
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [The development pipeline is a production system](https://sundry.jerryorr.com/2026/07/31/development-pipeline-is-a-production-system)

## Digest Summary
The article argues that a software development pipeline—comprising issue trackers, IDEs, build tools, package repositories, CI/CD systems, test suites, and QA environments—should be treated as a production system. When any component fails (e.g., code cannot compile, QA server is down, tests fail), developers and testers are unable to work, constituting a production‑grade outage that must be prioritized for immediate resolution. The author notes that while many organizations have extensive downtime‑prevention processes for customer‑facing services, similar rigor is often lacking for internal tooling. By recognizing each step from “customer request” to “delivery” as critical infrastructure, teams can apply the same urgency, monitoring, and incident‑response practices to maintain pipeline reliability and ensure continuous software delivery.

---

## Full Article

# The development pipeline is a production system

    
    
      
          by [Jerry Orr](https://sundry.jerryorr.com/about)
      
    
    Jul 31, 2026
    
    
      
        [programming](https://sundry.jerryorr.com/topics/programming)
      
        [technology](https://sundry.jerryorr.com/topics/technology)
      
      
    
    
    
      2 minute read
    
    
  
  

Software developers learn early in their careers that nothing is more urgent than fixing a production outage. Drop everything! All hands on deck!

However, the same level of urgency is not often given to problems with our development tools, build systems, QA environments, and other parts of the software development pipeline. But for the development team, the development pipeline is a production system.

A software developer’s job is to deliver value for the company. Sometimes that means building new features, sometimes that means fixing critical bugs for the customers’ production systems. But none of this can happen when something is broken in the software development pipeline.

If the code can’t compile, the developers are unable to do their jobs, and the team isn’t producing software. For the development team, this is a production outage. Fixing this should be a top priority.

If the QA server is down, the testers are unable to do their jobs, and the team isn’t producing working software. For the QA team, this is a production outage. Fixing it should be a top priority.

  
  You will not be shocked to learn that I drew this myself.

In manufacturing, there are [extensive processes and procedures](https://emshandbook.com/vol-12/4/escalation-slas/) on how to prevent and minimize downtime on the assembly line.[1](https://sundry.jerryorr.com/2026/07/31/development-pipeline-is-a-production-system#fn1)
 And similar processes exist for [IT service outages](https://sre.google/resources/practices-and-processes/incident-management-guide). But I’ve found that most of those focus on outages in the service provided to customers, not for the people responsible for building and supporting the services.

I recommend thinking about all the components that take you from “customer wants something” to “that something is delivered to customers”:

  
- Issue reporting and change request systems, like GitHub Issues, Jira, etc
  
- Tools developers use to directly build software, like IDEs, build tools (Gradle, Maven, etc), package repositories (npm, Maven Central, internal repositories, etc), local databases, containers, etc
  
- CI/CD tools (Jenkins, GitHub Actions, etc).
  
- A failing test suite (surely you don’t deploy to production if the tests are failing?)
  
- QA server outage (surely you don’t deploy to production if QA hasn’t tested it?)
  
- Literally any step in your process that prevents you from making changes and deploying them to production

A team with a broken development pipeline can’t produce software, and must treat this as a production outage.

	1 Interestingly, they often call it the "production line". Is the usage of the term "production" in the software world related to its history in the manufacturing world?
	[↩](https://sundry.jerryorr.com/2026/07/31/development-pipeline-is-a-production-system#top1)
