import time
#1
class HashTableArray:   # separate chaining class
    class Entry:    # bucket entry type
        def __init__(self, key, value):
            self.key = key  # unique identifier
            self.value = value  # stored data

    def __init__(self, capacity=10):  # Initialize hash table with capacity
        self.capacity = capacity  # Number of buckets/slots
        self.table = [[] for _ in range(capacity)]  # Array of empty lists (chains)
        self.size = 0  # Counter for total items stored

    def _hash(self, key):  # Hash function to compute bucket index
        return hash(key) % self.capacity  # Use modulo to get array index
    
    def insert(self, key, value):  # Insert/update key-value pair
        index = self._hash(key)  # Get bucket index using hash function
        bucket = self.table[index]  # Access the bucket (linked list)

        for entry in bucket:  # Check if key already exists
            if entry.key == key:  # Key found
                entry.value = value  # Update existing value
                return  # Exit early

        bucket.append(self.Entry(key, value))  # New key: add to bucket
        self.size += 1  # Increment item count
    
    def search(self, key):  # Search for value by key (returns None if not found)
        index = self._hash(key)  # Compute bucket index
        bucket = self.table[index]  # Get the bucket

        for entry in bucket:  # Linear search within bucket
            if entry.key == key:  # Key found
                return entry.value  # Return the associated value
            
        return None  # Key not found in hash table

    def delete(self, key):  # delete method 
        index = self._hash(key)
        bucket = self.table[index]
        for i, e in enumerate(bucket):
            if e.key == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def __len__(self):  # length method for size of hash table
        return self.size
    
    def print_table(self):  # print method (for debugging)
        for i, bucket in enumerate(self.table):
            print(f'{i}: ', end='')
            for entry in bucket:
                print(f'\n[{entry.key}, {entry.value}]', end=' ')
            print()


# Entity class for baby shop products
class BabyProduct:
    def __init__(self, productId, name, price, stock, category):
        self.productId = productId
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def __repr__(self):
        return f"{self.productId} - {self.name} | RM{self.price:.2f} | Stock: {self.stock} | Category: {self.category}"


#2
def local_storage_system():
    hashTable = HashTableArray(capacity=10)
    arrayStorage = []  # 1D array #4

    # Pre-defined products (ALL UPPERCASE)
    p1  = BabyProduct("D001", "DRYPERS WEE WEE DIAPERS", 29.90, 100, "DIAPERS")
    p2  = BabyProduct("B002", "PIGEON BABY BOTTLE 240ML", 24.50, 50, "FEEDING")
    p3  = BabyProduct("W003", "PUREEN BABY WIPES 80S", 9.90, 200, "CARE")
    p4  = BabyProduct("L004", "JOHNSON’S BABY LOTION 200ML", 16.90, 80, "SKINCARE")
    p5  = BabyProduct("D005", "MAMYPOKO EXTRA DRY DIAPERS M SIZE 60PCS", 45.90, 120, "DIAPERS")
    p6  = BabyProduct("D006", "HUGGIES DRY PANTS L SIZE 50PCS", 39.90, 90, "DIAPERS")
    p7  = BabyProduct("F007", "AVENT NATURAL FEEDING BOTTLE 260ML", 34.90, 40, "FEEDING")
    p8  = BabyProduct("S013", "SEBAMED BABY LOTION 200ML", 29.90, 70, "SKINCARE")
    p9  = BabyProduct("F008", "TOMMEE TIPPEE CLOSER TO NATURE BOTTLE 150ML", 29.90, 30, "FEEDING")
    p10 = BabyProduct("C009", "DR BROWN’S BABY PACIFIER 2PCS", 18.90, 60, "CARE")
    p11 = BabyProduct("C010", "PUKU BABY COMB AND BRUSH SET", 12.50, 80, "CARE")
    p12 = BabyProduct("W011", "HUGGIES BABY WIPES 80S", 11.90, 150, "CARE")
    p13 = BabyProduct("W012", "MAMYPOKO BABY WIPES 100S", 13.90, 140, "CARE")
    p14 = BabyProduct("S014", "BUDS ORGANICS BABY SHAMPOO 230ML", 32.90, 50, "SKINCARE")
    p15 = BabyProduct("H015", "PANADOL CHILDREN SUSPENSION 100ML", 14.90, 60, "HEALTH")
    p16 = BabyProduct("H016", "NUBY BABY NASAL ASPIRATOR", 19.90, 40, "HEALTH")
    p17 = BabyProduct("T017", "FISHER-PRICE BABY RATTLE SET", 22.90, 35, "TOYS")
    p18 = BabyProduct("T018", "FISHER-PRICE TEETHING RING", 15.90, 55, "TOYS")
    p19 = BabyProduct("B019", "BABY COTTON BIB 3PCS PACK", 9.90, 120, "CLOTHING")
    p20 = BabyProduct("B020", "BABY MITTENS AND BOOTIES SET", 7.90, 200, "CLOTHING")
    p21 = BabyProduct("C021", "PUREEN BABY HEAD-TO-TOE WASH 750ML", 18.50, 90, "CARE")
    p22 = BabyProduct("C022", "JOHNSON’S BABY POWDER 500G", 12.90, 110, "CARE")
    p23 = BabyProduct("S023", "BEPANTHEN BABY DIAPER CREAM 30G", 17.90, 70, "SKINCARE")
    p24 = BabyProduct("S024", "SUDOCREM DIAPER RASH CREAM 60G", 24.90, 65, "SKINCARE")
    p25 = BabyProduct("D025", "DRYPERS DRY PANTS XL SIZE 42PCS", 46.90, 80, "DIAPERS")
    p26 = BabyProduct("D026", "PETPET TAPE DIAPERS S SIZE 72PCS", 28.90, 140, "DIAPERS")
    p27 = BabyProduct("D027", "PETPET DAYPANTS XL SIZE 52PCS", 39.90, 90, "DIAPERS")
    p28 = BabyProduct("F028", "PIGEON WIDE NECK TEAT SIZE M", 16.90, 60, "FEEDING")
    p29 = BabyProduct("F029", "PIGEON BREAST PUMP MANUAL", 89.90, 25, "FEEDING")
    p30 = BabyProduct("F030", "TOMMEE TIPPEE MILK POWDER DISPENSER", 19.90, 75, "FEEDING")
    p31 = BabyProduct("C031", "PIGEON BABY NAIL CLIPPER", 15.50, 85, "CARE")
    p32 = BabyProduct("C032", "SAFERCARE BABY NASAL DROPS 28ML", 8.90, 55, "CARE")
    p33 = BabyProduct("H033", "APOLLO BABY FEVER COOLING PATCH 6PCS", 12.90, 90, "HEALTH")
    p34 = BabyProduct("H034", "PUREEN ANTIBACTERIAL WIPES 40S", 6.90, 130, "HEALTH")
    p35 = BabyProduct("T035", "LAMAZE BABY SOFT BOOK", 29.90, 40, "TOYS")
    p36 = BabyProduct("T036", "BABY PLAY MAT FOLDABLE 180CM", 79.90, 20, "TOYS")
    p37 = BabyProduct("C037", "BABY COTTON SWABS 200PCS", 5.90, 160, "CARE")
    p38 = BabyProduct("C038", "PUREEN BABY LAUNDRY DETERGENT 1L", 18.90, 45, "CARE")
    p39 = BabyProduct("B039", "BABY ROMPER SHORT SLEEVE 3PCS", 25.90, 70, "CLOTHING")
    p40 = BabyProduct("B040", "BABY BLANKET 100% COTTON", 18.90, 50, "CLOTHING")
    p41 = BabyProduct("S041", "CALIFORNIA BABY SHAMPOO & BODYWASH 251ML", 49.90, 30, "SKINCARE")
    p42 = BabyProduct("S042", "MUSTELA NO-RINSE CLEANSING WATER 300ML", 44.90, 35, "SKINCARE")
    p43 = BabyProduct("F043", "NAN OPTIPRO INFANT FORMULA 800G", 75.90, 45, "FEEDING")
    p44 = BabyProduct("F044", "ENFAGROW A+ Step 3 FORMULA 1.3KG", 89.90, 55, "FEEDING")
    p45 = BabyProduct("D045", "GENKI TAPE MEGA PACK M SIZE 96PCS", 54.90, 100, "DIAPERS")
    p46 = BabyProduct("D046", "MERRIES TAPE DIAPERS L SIZE 56PCS", 77.90, 45, "DIAPERS")
    p47 = BabyProduct("T047", "STACKING CUPS BABY TOY SET", 14.90, 85, "TOYS")
    p48 = BabyProduct("T048", "BABY TEETHING TOY BANANA SILICONE", 12.90, 95, "TOYS")
    p49 = BabyProduct("C049", "PUREEN BABY OIL 250ML", 10.90, 60, "CARE")
    p50 = BabyProduct("C050", "JOHNSON’S BABY OIL 300ML", 12.90, 70, "CARE")



    products = [
        p1, p2, p3, p4, p5, p6, p7, p8,
        p9, p10, p11, p12, p13, p14, p15, p16,
        p17, p18, p19, p20, p21, p22, p23, p24,
        p25, p26, p27, p28, p29, p30, p31, p32,
        p33, p34, p35, p36, p37, p38, p39, p40,
        p41, p42, p43, p44, p45, p46, p47, p48,
        p49, p50]


    # Insert into hash table and array for dual storage #4
    for product in products:  # Loop through all products
        hashTable.insert(product.productId, product)  # Add to hash table
        arrayStorage.append(product)  # Add to array

    return hashTable, arrayStorage  # Return both data structures


#3
def menu():
    print("\n=== BABY PRODUCTS RETAIL SHOP ===")
    print("1. Insert new product")
    print("2. Search product by Product ID")
    print("3. Show all products")
    print("4. Delete product by Product ID (optional)")
    print("5. Performance comparison: Hash Table vs Array (search)")
    print("0. Exit")
    return input("Enter your choice: ")
    
def inventory_system():  # Main system - handles user interactions
    hashTable, arrayStorage = local_storage_system()  # Load initial data
    print("Welcome to Baby Shop Inventory System (Hash Table + Array)")  # Welcome message

    while True:  # Main loop - keep running until exit
        choice = menu()  # Display menu and get choice

        if choice == "1":  # INSERT NEW PRODUCT
            productId = input("Enter Product ID (e.g., D001): ").upper()  # Get ID
            name = input("Enter Full Product Name (e.g., Drypers Wee Wee Diapers): ").upper()  # Get name
            price = float(input("Enter Product Price in RM (e.g., 29.90): "))  # Get price
            stock = int(input("Enter Quantity in Stock (e.g., 100): "))  # Get quantity
            category = input("Enter Product Category (e.g., Diapers / Feeding / Care / Skincare): ").upper()  # Get category

            new_product = BabyProduct(productId, name, price, stock, category)  # Create product object
            hashTable.insert(productId, new_product)  # Add to hash table
            arrayStorage.append(new_product)  # Add to array
            print("Product inserted successfully.")  

        elif choice == "2":  # SEARCH PRODUCT
            productId = input("Enter Product ID to search: ").upper()  # Get ID to search
            result = hashTable.search(productId)  # Search in hash table
            if result:  # If found
                print("Product found in hash table:")  # Confirmation
                print(result)  # Display product details
            else:  # If not found
                print("Product NOT found.")  # Error message

        elif choice == "3":  # DISPLAY ALL PRODUCTS
            print("\nAll products in hash table:")  # Header
            hashTable.print_table()  # Print table structure

        elif choice == "4":  # DELETE PRODUCT
            productId = input("Enter Product ID to delete: ").upper()  # Get ID
            deleted = hashTable.delete(productId)  # Delete from hash table

            if deleted:  # If deletion successful
                # Remove from array as well (for consistency)
                arrayStorage[:] = [p for p in arrayStorage if p.productId != productId]  # Filter array
                print("Product deleted from hash table and array.")  # Confirm deletion
            else:  # If product not found
                print("Product not found; nothing deleted.")  # Error message

        elif choice == "5":  # PERFORMANCE TEST
            run_performance_test(hashTable, arrayStorage)  # Run comparison test

        elif choice == "0":  # EXIT PROGRAM
            print("Exiting system...")  # Goodbye message
            break  # Exit while loop

        else:  # Invalid choice
            print("Invalid choice, please try again.")  # Error message

#4
def run_performance_test(hashTable, arrayStorage):  # Compare hash table vs array search performance
    if not arrayStorage:  # Check if data exists
        print("No data available for performance test.")  # Error if no data
        return  # Exit function

    # User chooses the Product ID to test performance
    targetProductId = input("Enter Product ID to test performance search: ").upper()  # Get search target

    # Check if the product exists at least once in the array
    exists = any(product.productId == targetProductId for product in arrayStorage)  # Verify existence
    if not exists:  # If not found
        print("Product ID not found in the system. Cannot run performance test.")  # Error message
        return  # Exit function
    
    iterations = 100000  # Repeat searches to measure clearer timing differences

    # Hash table search timing
    startHash = time.perf_counter()  # Start timer
    for _ in range(iterations):  # Repeat search
        hashTable.search(targetProductId)  # Hash table lookup
    endHash = time.perf_counter()  # End timer
    hashTime = endHash - startHash  # Calculate elapsed time

    # Array search timing
    startArray = time.perf_counter()  # Start timer
    for _ in range(iterations):  # Repeat search
        for product in arrayStorage:  # Linear search through array
            if product.productId == targetProductId:  # Find match
                break  # Exit inner loop when found
    endArray = time.perf_counter()  # End timer
    arrayTime = endArray - startArray  # Calculate elapsed time


    # Single search to OUTPUT the dataset for this Product ID
    hashResult = hashTable.search(targetProductId)  # Get product from hash table
    arrayResult = None  # Initialize
    for product in arrayStorage:  # Search array
        if product.productId == targetProductId:  # Match found
            arrayResult = product  # Store result
            break  # Exit loop

    print("\n=== Performance Test Result ===")  # Header
    print(f"Search key: {targetProductId}\n")  # Show search target
    print("Hash table search result:")  # Label
    print(hashResult)  # Display product
    print(f"Hash table search time: {hashTime:.6f} seconds")  # Show hash table time
    print("\nArray search result:")  # Label
    print(arrayResult)  # Display product
    print(f"Array search time:      {arrayTime:.6f} seconds")  # Show array time

    if hashTime < arrayTime:  # HashTime is faster
        print("=> Hash table is faster for searching in this test.(it jumps straight to where the product is stored)")
    else:  # Array is faster
        print("=> Array is faster in this specific run (variable is in the earlier/front part of the array).")

if __name__ == "__main__":  # Entry point
    inventory_system()  # Start the program