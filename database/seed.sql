BEGIN;

INSERT OR IGNORE INTO products
(sku, name, category, description, price_cents, weight_grams, thumbnail_url, image_url, stock_qty)
VALUES
('KB-WAVE-PRO', 'Wavelength Pro Keyboard', 'Keyboards',
 'Mechanical gaming keyboard with Cherry MX switches, RGB backlighting, and programmable macros.',
 14999, 950, NULL, NULL, 25),

('MS-PRECISION', 'Precision Gaming Mouse', 'Mice',
 'High-DPI optical sensor, 7 programmable buttons, and ergonomic design for competitive gaming.',
 7999, 120, NULL, NULL, 40),

('HS-7-1', 'Surround Sound Headset', 'Audio',
 '7.1 surround sound gaming headset with noise-canceling microphone and comfortable padding.',
 12999, 320, NULL, NULL, 30),

('MON-4K-27-144', '4K Gaming Monitor', 'Monitors',
 '27\" 4K display with 144Hz refresh rate, HDR support, and ultra-low input lag.',
 39999, 5500, NULL, NULL, 12),

('CHR-ERGO', 'Ergonomic Gaming Chair', 'Chairs',
 'Premium gaming chair with lumbar support, adjustable armrests, and breathable mesh fabric.',
 29999, 15000, NULL, NULL, 18),

('GPU-RTX-4080', 'Graphics Card RTX 4080', 'PC Components',
 'Latest generation graphics card with ray tracing and DLSS 3.0 for ultimate gaming performance.',
 89999, 1800, NULL, NULL, 8);

INSERT INTO customers (email, password_hash, full_name, phone)
VALUES
('ayden@example.com', 'argon2id$hash1...', 'Ayden Tran', '+61 400 111 222'),
('kate@example.com',  'argon2id$hash2...', 'Kate Talbot-Smith', '+61 400 333 444'),
('alex@example.com',  'argon2id$hash3...', 'Alex Johnson', '+61 400 555 666');


INSERT INTO orders (customer_id, total_cents, status)
VALUES (2, 42998, 'PLACED');  -- 129.99 + 299.99 = 429.98


INSERT INTO order_items (order_id, product_id, unit_price_cents, qty)
VALUES
(1, 3, 12999, 1),  -- Headset
(1, 5, 29999, 1);  -- Gaming Chair



COMMIT;
