-- Everything is built with: python database.py

CREATE TABLE IF NOT EXISTS vehicles (
    id  INTEGER PRIMARY KEY,    --unique, auto-assigned
    make    TEXT NOT NULL,
    model   TEXT NOT NULL,
    year    INTEGER,
    nickname    TEXT,
    registration    TEXT,
    purchase_date   TEXT,
    purchase_price  REAL,
    odometer_at_purchase    INTEGER,
    fuel_type   TEXT,
    notes   TEXT

);

CREATE TABLE IF NOT EXISTS fuel_ups (
    id INTEGER PRIMARY KEY,
    vehicle_id INTEGER NOT NULL REFERENCES vehicles(id),
    date TEXT,
    odometer    INTEGER,
    litres  REAL,
    price_per_litre REAL,
    total_cost  REAL,
    is_full_tank BOOLEAN,
    notes   TEXT

);

CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY,
    vehicle_id INTEGER NOT NULL REFERENCES vehicles(id),
    date TEXT,
    category    TEXT,
    description TEXT,
    cost    REAL,
    odometer    INTEGER,
    vendor  TEXT,
    notes   TEXT
);

CREATE TABLE IF NOT EXISTS service_records (
    id INTEGER PRIMARY KEY,
    vehicle_id INTEGER NOT NULL REFERENCES vehicles(id),
    date TEXT,
    odometer    INTEGER,
    service_type TEXT,
    description TEXT,
    cost    REAL,
    provider    TEXT,
    next_due_miles INTEGER,
    next_due_date TEXT
);