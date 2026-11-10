---
title: "Atomicity! How? A Deep Dive into Data Integrity Across Systems"
source: "https://medium.com/@karim.albakry/atomicity-how-ffa5107b9293"
author:
  - "[[Karim Albakry]]"
published: 2024-08-24
created: 2026-06-29
description: "Atomicity is a critical aspect of programming, especially when dealing with shared data across multiple scopes. In this article, we will exp"
tags:
  - "clippings"
---
![](https://miro.medium.com/v2/resize:fit:1260/format:webp/1*ZKfsvDtbDn0TX60tKSAEQA@2x.jpeg)

Atomicity is a critical aspect of programming, especially when dealing with shared data across multiple scopes. In this article, we will explore what atomicity means, where it can be applied, and how it ensures the integrity of operations.

## What is Atomicity?

Atomicity means that an operation cannot be divided into smaller parts.  
When an operation is atomic, it either finishes or doesn’t happen at all.  
This ensures that if several steps are combined into one atomic operation, they all must succeed, or none of them will.  
This consistency is vital for maintaining data integrity.

Imagine you have a task with 100 small steps. If 99 of these steps succeed but the last one fails, the whole task is canceled, and everything reverts to the state it was in before the task began. This keeps the system stable and correct.

For an operation to be considered atomic, it should be:

- **Indivisible:** The operation cannot be split into smaller parts.
- **Uninterruptible:** The operation must either finish entirely without interruption or be canceled entirely if something goes wrong.

## Where Can Atomicity Be Used?

The effectiveness of atomicity depends on the scope in which it is applied. An operation might be atomic within a specific scope, but that doesn’t necessarily mean it remains atomic across other scopes. For example, an operation could be atomic within a small part of a program but not across the entire program or system. To understand this more clearly, we will explore how atomicity is applied in three different scopes: concurrency, databases, and distributed systems.

## 1\. Atomicity in Concurrency

Concurrency introduces challenges in ensuring atomicity because operations may be interdependent. Consider the famous i++ example in programming:

```c
let exit = false;
for (let i = 0; !exit; i++) {
  // ...
}
```

Here, `i++` might seem like a single operation that increments the value of `i`.

However, `i++` actually involves three steps:

1. Retrieve the value of `i`.
2. Increment the value of `i`.
3. Store the updated value of `i`.

If these steps are not handled atomically, issues can arise inside the `for` loop, leading to inconsistent data.

To better understand this, let’s consider an example where `i` is shared between two different functions, and each function processes `i` in a different way. In this case, `i` is not guaranteed to be handled atomically due to the operation being divided between two functions in different scopes. Additionally, since they run concurrently, each function may execute in an unexpected sequence:

```c
let i = 0;

async function add() {
  for (let j = 0; j < 100; j++) {
    i++;
    await new Promise(resolve => setTimeout(resolve, Math.random() * 10));
  }
  console.log('Add completed:', i);
}

async function square() {
  for (let j = 0; j < 10; j++) {
    i = (i - 10) * 2;
    await new Promise(resolve => setTimeout(resolve, Math.random() * 10));
  }
  console.log('Square completed:', i);
}

add();
square();
```

In this example, the functions `add` and `square` are both modifying `i` asynchronously. Since `i` is not handled atomically, the operations may interleave, leading to unpredictable and inconsistent results. For instance, `add` might retrieve the value of `i` before `square` has completed its operation, causing data inconsistencies.

Different outputs will be produced each time:

```c
$ node index.js 
Square completed: -18783
Add completed: -18694

$ node index.js 
Square completed: -17838
Add completed: -17752

$ node index.js 
Square completed: -18382
Add completed: -18292she
```

**Note:** The previous example violates the two conditions of atomicity:

1. **Indivisibility:** Each function runs individually rather than acting as one operation.
2. **Uninterruptibility:** If an error occurs in one function, the other may continue to execute normally, breaking the atomic nature of the operation.

To solve this problem, it’s crucial to understand the concurrency model used in your programming language and apply the appropriate mechanism to ensure atomicity.

For example, you can use a mutex to lock and unlock the shared resource, which in our case is `i`:

```c
let i = 0;

// Create a simple mutex lock
class Mutex {
  constructor() {
    this.queue = [];
    this.locked = false;
  }

  lock() {
    return new Promise((resolve) => {
      if (this.locked) {
        this.queue.push(resolve);
      } else {
        this.locked = true;
        resolve();
      }
    });
  }

  unlock() {
    if (this.queue.length > 0) {
      const resolve = this.queue.shift();
      resolve();
    } else {
      this.locked = false;
    }
  }
}

const mutex = new Mutex();

async function add() {
  await mutex.lock();
  for (let j = 0; j < 100; j++) {
    i++;
    await new Promise(resolve => setTimeout(resolve, Math.random() * 10));
  }

  console.log('Add completed:', i);
  mutex.unlock();
}

async function square() {
  await mutex.lock();
  for (let j = 0; j < 10; j++) {
    i = (i - 10) * 2;
    await new Promise(resolve => setTimeout(resolve, Math.random() * 10));
  }
  console.log('Square completed:', i);
  mutex.unlock();
}

(async function execute() {
  await add(); // Runs in a controlled manner
  await square(); // Runs in a controlled manner
})();
```

With this approach, the output will produce the same result no matter how many times you run the code:

```c
Add completed: 100
Square completed: 81940
```

## 2\. Atomicity in Database

In databases, atomicity is often managed through transactions, where all included operations must succeed for the transaction to commit; otherwise, all changes are rolled back to maintain the database’s previous state.

## Get Karim Albakry’s stories in your inbox

Join Medium for free to get updates from this writer.

Consider a transaction in an e-commerce or inventory management system, where atomicity ensures that orders are only placed when there are enough stocks, preventing situations where an order is processed without the necessary inventory.

**Example: Transaction to Check Stock and Create an Order**

```c
BEGIN TRANSACTION;

-- Step 1: Check if there is sufficient stock
DECLARE @stock INT;
SELECT @stock = stock FROM Products WHERE product_id = 101;

IF @stock < 1
BEGIN
    PRINT 'Insufficient stock for the product';
    ROLLBACK;
END
ELSE
BEGIN
    -- Step 2: Decrease inventory for the product
    UPDATE Products
    SET stock = stock - 1
    WHERE product_id = 101;

    -- Step 3: Create a new order record
    INSERT INTO Orders (order_id, product_id, customer_id, quantity, order_date)
    VALUES (2002, 101, 302, 1, CURRENT_TIMESTAMP);

    COMMIT;
END
```
- **BEGIN TRANSACTION:** Starts a transaction that ensures all later operations are treated as a single unit of work.
- **SELECT:** Check if there are enough stocks for the product.
- **ROLLBACK:** If there is insufficient stock, the transaction is rolled back, undoing any changes made within the transaction.
- **UPDATE:** If there are enough stocks, the inventory is decreased.
- **INSERT:** A new order record is created.
- **COMMIT:** Finalizes the transaction, making all changes permanent.

## 3\. Atomicity in Distributed Systems

Ensuring atomicity across nodes in distributed systems is complex because these systems require external mechanisms to ensure atomic operations across multiple nodes. The distributed nature of the data in these systems makes them susceptible to network failures, node crashes, and other issues that can interrupt processes. However, there are various techniques to achieve atomicity:

- Two-Phase Commit (2PC).
- Consensus Protocols.

## 3.1 Two-Phase Commit (2PC)

Two-Phase Commit (2PC) is a protocol used to ensure that a distributed transaction either commits or rolls back on all involved microservices, maintaining data consistency across the system.

As the name suggests, it consists of two phases:

- Phase 1: Prepare
- Phase 2: Commit/Rollback

### \# Phase 1: Prepare

1. Transaction Initiation: The Transaction Coordinator (TC) sends a “prepare” request to all participants (nodes) involved in the transaction.
2. Participants prepare: Each participant performs all necessary actions to ensure they can commit the transaction and write these changes to a temporary storage (e.g., a transaction log). If a participant can commit, it replies with a “yes” to the TC. If it cannot commit, it replies with a “no.”

### \# Phase 2: Commit/Rollback

1. **Commit:** If all participants replied “yes” in the prepare phase, the TC sends a “commit” request to all participants, instructing them to make the changes permanent.
2. **Rollback:** If any participant replied “no” in the prepare phase, the TC sends a “rollback” request to all participants, instructing them to undo any changes made during the prepare phase.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*_czDEI1I2fchocCQaSMOJA.jpeg)

Two-Phase Commit (2PC)

## 3\. Consensus Protocols

Distributed transactions can also use consensus protocols like Paxos or Raft, which are designed to reach agreement among distributed nodes. Unlike 2PC, which requires all nodes to agree, consensus protocols only need a majority to agree on the transaction’s outcome. This method is often better at handling network issues and node failures, allowing the system to keep running even if some nodes go down.

Example: Consensus Protocols Imagine a group of nodes trying to choose a leader. In a consensus protocol like Raft, the nodes communicate and vote on which one should be the leader. If a majority agrees, a leader is elected, even if some nodes don’t participate. This process ensures that the system can continue to work properly, even if some nodes fail.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yaLBuIG_RAvCFRIWa23uGQ.png)

For more information on Raft, visit the [Raft website](https://raft.github.io/)

### Technical Depth:

- **Two-Phase Commit** (2PC): While 2PC ensures consistency, it has significant drawbacks, especially in distributed environments. If one of the participating nodes fails during the commit process, the entire transaction can become stuck. This happens because 2PC requires all nodes to agree on either committing or aborting the transaction. If a node fails, the coordinator might be unable to decide, leaving the system in a blocked state, which can lead to indefinite retries if the failure isn’t resolved quickly.
- **Consensus Protocols**: In contrast, consensus protocols like Paxos or Raft are designed to handle failures more effectively in distributed environments. They can tolerate the failure of some nodes while still reaching an agreement on the system’s state. These protocols are more fault-tolerant because they allow the system to continue operating even when some nodes are unavailable, avoiding the indefinite blocking issue seen with 2PC. This makes consensus protocols more suitable for environments where high availability and fault tolerance are crucial.

## Conclusion

Atomicity is a fundamental concept in ensuring the reliability and consistency of operations across various scopes, from individual program operations to complex distributed systems. While techniques like Two-Phase Commit (2PC) and consensus protocols offer robust solutions, each comes with its own trade-offs. Understanding these trade-offs and applying the appropriate mechanism is key to maintaining system integrity, particularly in environments where failures are expected.