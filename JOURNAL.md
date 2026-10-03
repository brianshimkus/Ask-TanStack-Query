## Day 1: "before" examples
Q: How do I run code after a query succeeds in TanStack Query v5? Show code.
A:
onSuccess: (data) => {
    // Code to run after the query succeeds
    doSomethingWithTodos(data);
}

Q: How do I share query options between useQuery and prefetchQuery?
A:
const sharedQueryOptions = {
    staleTime: 5 * 60 * 1000,    // 5 minutes
    cacheTime: 60 * 60 * 1000,   // 1 hour
    refetchOnWindowFocus: false
}

What I did: I made a Python program that sends a question to gpt-5-nano that prints the answer. I asked it 5 questions about TanStack Query v5 and saved two bad answers found above.

What broke: The program ran fine. The answers were wrong. One to me to use onSuccess inside useQuery, and v5 removed that. Another to me to set cacheTime, and v5 renamed that to gcTime. The code looked real.

What I learned: A model can sound sure and still describe an older version of a library. Nothing in the answer warns me. This is why this project looks the answer up in the current docs instead of trusting the model's memory.
