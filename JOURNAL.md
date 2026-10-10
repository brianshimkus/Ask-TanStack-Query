# Journal

## Day 1: "before" examples

**How do I run code after a query succeeds in TanStack Query v5?**

```tsx
onSuccess: (data) => {
  // Code to run after the query succeeds
  doSomethingWithTodos(data);
}
```

**How do I share query options between `useQuery` and `prefetchQuery`?**

```tsx
const sharedQueryOptions = {
  staleTime: 5 * 60 * 1000, // 5 minutes
  cacheTime: 60 * 60 * 1000, // 1 hour
  refetchOnWindowFocus: false,
}
```

> [!TIP]
> **What I did.** I made a Python program that sends a question to gpt-5-nano and prints the answer. I asked it 5 questions about TanStack Query v5 and saved two bad answers.

> [!WARNING]
> **What broke.** The program ran fine. The answers were wrong. One told me to use `onSuccess` inside `useQuery`, and v5 removed that. Another told me to set `cacheTime`, and v5 renamed that to `gcTime`. The code looked real.

> [!IMPORTANT]
> **What I learned.** A model can sound sure and still describe an older version of a library. Nothing in the answer warns me. This is why this project looks the answer up in the current docs instead of trusting the model's memory.

## Day 2: Downloading answered questions

A lot of the accepted answers are old, and a lot of them point at a docs page.

> [!TIP]
> **What I did.** Downloaded two piles onto my computer. One is the TanStack Query docs. The other is GitHub questions that have an accepted answer.

> [!WARNING]
> **What broke.** The scripts ran, but the pile is messy. Some accepted answers are from older versions.

> [!IMPORTANT]
> **What I learned.** A lot of the answers are old, and a lot of them link to a docs page.

## Day 3: bad chunks

**InfiniteQueryObserverOptions**

```text
ether errors should be thrown...
```

**TimeoutManager**

```text
meoutManager } from '@tanstack/query-core'...
```
