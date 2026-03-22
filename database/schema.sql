-- ============================================================
-- CODY Bot — Database Schema
-- Jalankan sekali saat pertama kali setup:
--   psql -U postgres -d cody_bot -f database/schema.sql
-- ============================================================

-- Enum types
CREATE TYPE currency_type AS ENUM ('coin');
CREATE TYPE coworking_type AS ENUM ('focus', 'break');
CREATE TYPE transaction_type AS ENUM ('earn', 'spend');

-- ---------------------------------------------------------------
-- users
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS users (
    id              SERIAL PRIMARY KEY,
    discord_user_id VARCHAR(32) NOT NULL UNIQUE,
    created_at      TIMESTAMP   NOT NULL DEFAULT NOW(),
    modified_at     TIMESTAMP   NOT NULL DEFAULT NOW()
);

-- ---------------------------------------------------------------
-- project
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS project (
    id               SERIAL PRIMARY KEY,
    user_id          INT         NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name             VARCHAR(100) NOT NULL,
    description      TEXT,
    due_date         DATE,
    min_session_time INT         NOT NULL DEFAULT 25, -- dalam menit
    created_at       TIMESTAMP   NOT NULL DEFAULT NOW(),
    modified_at      TIMESTAMP   NOT NULL DEFAULT NOW()
);

-- ---------------------------------------------------------------
-- coworking
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS coworking (
    id          SERIAL PRIMARY KEY,
    user_id     INT             NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    start_time  TIMESTAMP       NOT NULL DEFAULT NOW(),
    end_time    TIMESTAMP,
    type        coworking_type  NOT NULL DEFAULT 'focus',
    created_at  TIMESTAMP       NOT NULL DEFAULT NOW(),
    modified_at TIMESTAMP       NOT NULL DEFAULT NOW()
);

-- ---------------------------------------------------------------
-- streak
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS streak (
    id                 SERIAL PRIMARY KEY,
    user_id            INT       NOT NULL REFERENCES users(id) ON DELETE CASCADE UNIQUE,
    current_streak     INT       NOT NULL DEFAULT 0,
    last_activity_date DATE,
    longest_streak     INT       NOT NULL DEFAULT 0,
    created_at         TIMESTAMP NOT NULL DEFAULT NOW(),
    modified_at        TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ---------------------------------------------------------------
-- currencies
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS currencies (
    id          SERIAL PRIMARY KEY,
    user_id     INT           NOT NULL REFERENCES users(id) ON DELETE CASCADE UNIQUE,
    amount      INT           NOT NULL DEFAULT 0,
    type        currency_type NOT NULL DEFAULT 'coin',
    created_at  TIMESTAMP     NOT NULL DEFAULT NOW(),
    modified_at TIMESTAMP     NOT NULL DEFAULT NOW()
);

-- ---------------------------------------------------------------
-- item
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS item (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    created_at  TIMESTAMP    NOT NULL DEFAULT NOW(),
    modified_at TIMESTAMP    NOT NULL DEFAULT NOW()
);

-- ---------------------------------------------------------------
-- inventory
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS inventory (
    id          SERIAL PRIMARY KEY,
    user_id     INT       NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    item_id     INT       NOT NULL REFERENCES item(id) ON DELETE CASCADE,
    qty         INT       NOT NULL DEFAULT 0,
    created_at  TIMESTAMP NOT NULL DEFAULT NOW(),
    modified_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ---------------------------------------------------------------
-- transaction
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS transaction (
    id          SERIAL PRIMARY KEY,
    user_id     INT              NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    item_id     INT              REFERENCES item(id) ON DELETE SET NULL,
    type        transaction_type NOT NULL,
    amount      INT              NOT NULL,
    created_at  TIMESTAMP        NOT NULL DEFAULT NOW(),
    modified_at TIMESTAMP        NOT NULL DEFAULT NOW()
);
