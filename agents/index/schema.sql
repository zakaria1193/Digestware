-- Pulse index schema. Rebuilt from web/src/content/**.md — never authoritative.
--
-- Design notes:
--  * `docs_fts` is a plain (non-external-content) FTS5 table keyed by doc_id.
--    External-content tables need delete-triggers carrying the *old* row value;
--    getting that wrong silently corrupts the index. At ~3k docs the duplicated
--    text costs a few MB, which buys a re-index path that is just
--    DELETE-then-INSERT and cannot drift.
--  * The tokenizer is the highest-leverage line in this file. Default unicode61
--    splits on `_`, `-` and `.`, which shreds exactly the tokens this corpus is
--    searched by: bfd_elf_final_link, -fipa-sra, tc-z80.c, R_AARCH64_TLSDESC.
--    Adding them to tokenchars keeps each identifier a single searchable term.

CREATE TABLE IF NOT EXISTS docs (
    id             INTEGER PRIMARY KEY,
    path           TEXT    NOT NULL UNIQUE,   -- repo-relative, stable id across rebuilds
    content_hash   TEXT    NOT NULL,          -- sha256 of file text; drives incremental work
    kind           TEXT    NOT NULL,          -- landing | discussion
    project        TEXT    NOT NULL DEFAULT '',
    subsystem      TEXT    NOT NULL DEFAULT '',
    commit_hash    TEXT,
    discussion_id  TEXT,
    series_id      TEXT,
    outcome        TEXT,
    impact_score   INTEGER,
    sentiment_score INTEGER,
    breaking_change INTEGER NOT NULL DEFAULT 0,
    performance_win INTEGER NOT NULL DEFAULT 0,
    is_stub        INTEGER NOT NULL DEFAULT 0,
    tags           TEXT    NOT NULL DEFAULT '[]',   -- JSON array
    authors        TEXT    NOT NULL DEFAULT '[]',   -- JSON array (proposer/author/exchanges)
    headline       TEXT    NOT NULL DEFAULT '',
    tldr           TEXT    NOT NULL DEFAULT '',
    body           TEXT    NOT NULL DEFAULT '',
    search_text    TEXT    NOT NULL DEFAULT '',     -- what actually gets indexed
    url            TEXT    NOT NULL DEFAULT '',
    date           TEXT    NOT NULL DEFAULT ''      -- ISO YYYY-MM-DD, lexically sortable
);

CREATE INDEX IF NOT EXISTS idx_docs_date       ON docs(date);
CREATE INDEX IF NOT EXISTS idx_docs_project    ON docs(project);
CREATE INDEX IF NOT EXISTS idx_docs_subsystem  ON docs(subsystem);
CREATE INDEX IF NOT EXISTS idx_docs_series     ON docs(series_id);
CREATE INDEX IF NOT EXISTS idx_docs_commit     ON docs(commit_hash);
CREATE INDEX IF NOT EXISTS idx_docs_discussion ON docs(discussion_id);

CREATE VIRTUAL TABLE IF NOT EXISTS docs_fts USING fts5(
    doc_id UNINDEXED,
    search_text,
    tokenize = "unicode61 tokenchars '_-.+'"
);

CREATE TABLE IF NOT EXISTS symbols (
    doc_id  INTEGER NOT NULL REFERENCES docs(id) ON DELETE CASCADE,
    symbol  TEXT    NOT NULL,   -- normalised (casefolded) lookup key
    display TEXT    NOT NULL,   -- as it appears in the article
    kind    TEXT    NOT NULL,   -- file | flag | reloc | bug | macro | ident | test
    PRIMARY KEY (doc_id, symbol, kind)
) WITHOUT ROWID;

CREATE INDEX IF NOT EXISTS idx_symbols_symbol ON symbols(symbol);
CREATE INDEX IF NOT EXISTS idx_symbols_kind   ON symbols(kind);

CREATE TABLE IF NOT EXISTS embeddings (
    doc_id INTEGER PRIMARY KEY REFERENCES docs(id) ON DELETE CASCADE,
    model  TEXT NOT NULL,
    dim    INTEGER NOT NULL,
    vector BLOB NOT NULL          -- little-endian float32, L2-normalised
);

CREATE TABLE IF NOT EXISTS meta (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
