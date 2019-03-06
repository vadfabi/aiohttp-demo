CREATE EXTENSION IF NOT EXISTS pgcrypto;
CREATE EXTENSION IF NOT EXISTS citext;

CREATE TABLE IF NOT EXISTS accounts_user (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    email CITEXT NOT NULL,
    profile JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    deleted_at TIMESTAMP WITH TIME ZONE
);

CREATE INDEX CONCURRENTLY IF NOT EXISTS accounts_user_email ON accounts_user (email);
CREATE INDEX CONCURRENTLY IF NOT EXISTS accounts_user_updated ON accounts_user (updated_at);
CREATE INDEX CONCURRENTLY IF NOT EXISTS accounts_user_deleted ON accounts_user (deleted_at);

ALTER TABLE accounts_user OWNER TO aiodemo;

COPY accounts_user
    (id, name, email, profile, created_at, updated_at, deleted_at)
FROM stdin;

INSERT INTO accounts_user VALUES
    ('60e3bcbff6c1464b8aed5be0fce86052', 'Lucas', 'test@example.com');