-- Day 4: meaning search. Finds the chunks whose embeddings are closest to the question's embedding.
create or replace function match_chunks(query_embedding extensions.vector(1536), match_count int)
returns table (id bigint, doc_url text, doc_title text, content text, similarity float)
language sql stable
as $$
  select id, doc_url, doc_title, content,
         1 - (embedding <=> query_embedding) as similarity
  from chunks
  order by embedding <=> query_embedding
  limit match_count;
$$;
