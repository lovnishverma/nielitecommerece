import sqlite3

conn = sqlite3.connect('database.db')

# conn.execute('''CREATE TABLE users 
# 		(userId INTEGER PRIMARY KEY, 
# 		password TEXT,
# 		email TEXT,
# 		firstName TEXT,
# 		lastName TEXT,
# 		address1 TEXT,
# 		address2 TEXT,
# 		zipcode TEXT,
# 		city TEXT,
# 		state TEXT,
# 		country TEXT, 
# 		phone TEXT
# 		)''')

# conn.execute('''CREATE TABLE products
# 		(productId INTEGER PRIMARY KEY,
# 		name TEXT,
# 		price REAL,
# 		description TEXT,
# 		image TEXT,
# 		stock INTEGER,
# 		categoryId INTEGER,
# 		FOREIGN KEY(categoryId) REFERENCES categories(categoryId)
# 		)''')

# conn.execute('''CREATE TABLE kart
# 		(userId INTEGER,
# 		productId INTEGER,
# 		FOREIGN KEY(userId) REFERENCES users(userId),
# 		FOREIGN KEY(productId) REFERENCES products(productId)
# 		)''')

# conn.execute('''CREATE TABLE categories
# 		(categoryId INTEGER PRIMARY KEY,
# 		name TEXT
# 		)''')




conn.execute('''CREATE TABLE allorders (
    orderId INTEGER PRIMARY KEY AUTOINCREMENT,
    userId INTEGER,
    productId INTEGER,
    quantity INTEGER,
    total_price REAL,
    order_date TEXT,
    FOREIGN KEY(userId) REFERENCES users(userId),
    FOREIGN KEY(productId) REFERENCES products(productId)
)''')
# Execute SQL command to create the wishlist table
conn.execute('''CREATE TABLE wishlist (
    wishlistId INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique ID for each wishlist entry
    userId INTEGER,  -- User who added the product
    productId INTEGER,  -- Product that is added to the wishlist
    FOREIGN KEY(userId) REFERENCES users(userId),  -- Link to the users table
    FOREIGN KEY(productId) REFERENCES products(productId)  -- Link to the products table
)''')

conn.close()

