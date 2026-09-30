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
