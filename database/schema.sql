PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;

BEGIN;

-- =============== USERS / ACCOUNTS =================
CREATE TABLE IF NOT EXISTS customers (
  id              INTEGER PRIMARY KEY,
  email           TEXT NOT NULL UNIQUE,
  password_hash   TEXT NOT NULL,               -- store a hash, not plain text
  full_name       TEXT,
  phone           TEXT,
  created_at      TEXT NOT NULL DEFAULT (datetime('now'))
);

-- =============== PRODUCTS =========================
-- Prices in cents (INTEGER) to avoid float rounding issues.
CREATE TABLE IF NOT EXISTS products (
  id             INTEGER PRIMARY KEY,
  sku            TEXT NOT NULL UNIQUE,
  name           TEXT NOT NULL,
  category       TEXT,                          -- e.g. "Keyboards", "Mice"
  description    TEXT,
  price_cents    INTEGER NOT NULL CHECK (price_cents >= 0),
  weight_grams   INTEGER CHECK (weight_grams >= 0),
  thumbnail_url  TEXT,
  image_url      TEXT,
  stock_qty      INTEGER NOT NULL DEFAULT 0 CHECK (stock_qty >= 0),
  created_at     TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at     TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Update timestamp trigger (your earlier “incomplete input” likely came from a missing END;)
CREATE TRIGGER IF NOT EXISTS trg_products_updated_at
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
  UPDATE products
  SET updated_at = datetime('now')
  WHERE id = NEW.id;
END;

-- Useful lookups
CREATE INDEX IF NOT EXISTS idx_products_category ON products(category);
CREATE INDEX IF NOT EXISTS idx_products_name ON products(name);

-- =============== CARTS ============================
-- A simple server-side cart per customer (or session).
CREATE TABLE IF NOT EXISTS carts (
  id            INTEGER PRIMARY KEY,
  customer_id   INTEGER REFERENCES customers(id) ON DELETE CASCADE,
  created_at    TEXT NOT NULL DEFAULT (datetime('now')),
  checked_out   INTEGER NOT NULL DEFAULT 0 CHECK (checked_out IN (0,1))
);

CREATE TABLE IF NOT EXISTS cart_items (
  id          INTEGER PRIMARY KEY,
  cart_id     INTEGER NOT NULL REFERENCES carts(id) ON DELETE CASCADE,
  product_id  INTEGER NOT NULL REFERENCES products(id),
  qty         INTEGER NOT NULL CHECK (qty > 0),
  UNIQUE(cart_id, product_id)
);

-- Optional: keep qty in sync with stock on checkout only (not while adding to cart).

-- =============== ORDERS ===========================
CREATE TABLE IF NOT EXISTS orders (
  id              INTEGER PRIMARY KEY,
  customer_id     INTEGER NOT NULL REFERENCES customers(id),
  total_cents     INTEGER NOT NULL CHECK (total_cents >= 0),
  created_at      TEXT NOT NULL DEFAULT (datetime('now')),
  status          TEXT NOT NULL DEFAULT 'PLACED' -- PLACED | PAID | SHIPPED | CANCELED
);

CREATE TABLE IF NOT EXISTS order_items (
  id           INTEGER PRIMARY KEY,
  order_id     INTEGER NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
  product_id   INTEGER NOT NULL REFERENCES products(id),
  unit_price_cents INTEGER NOT NULL CHECK (unit_price_cents >= 0),
  qty          INTEGER NOT NULL CHECK (qty > 0)
);

COMMIT;
