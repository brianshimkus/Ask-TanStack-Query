-- Day 3: the "library" table. Run this once in the Supabase SQL Editor.

-- Turn on pgvector, the add-on that lets Postgres store and search embeddings.
create extension if not exists vector with schema extensions;

-- One row = one chunk (index card).
create table chunks (
  id bigint primary key generated always as identity,
  doc_url text not null,          -- the docs page this chunk came from
  doc_title text,                 -- that page's title
  content text not null,          -- the chunk's text
  -- A keyword-search version of the text that Postgres keeps up to date by itself (used on Day 9).
  fts tsvector generated always as (to_tsvector('english', content)) stored,
  -- The chunk's 1,536 "meaning numbers" from text-embedding-3-small.
  embedding extensions.vector(1536)
);

-- Indexes make both kinds of search fast.
create index on chunks using gin (fts);
create index on chunks using hnsw (embedding vector_cosine_ops);

-- Lock the table so only your server (which uses the secret key) can read or write it.
alter table chunks enable row level security;
