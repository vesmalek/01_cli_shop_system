## Phase 1 Consolidation Project: CLI Shop System

This is the right project for where you are. A command-line shopping system that mimics exactly what a web app backend does — manage products, handle a cart, validate input, apply logic, and produce a receipt. The only difference between this and a real FastAPI shop backend is that yours runs in the terminal instead of responding to HTTP requests. The logic is identical.

---

### What You're Building

A running program that gives the user a menu and lets them shop interactively:

```
============================
     ISMAIL'S SHOP
============================
1. View Products
2. Add Item to Cart
3. View Cart
4. Remove Item from Cart
5. Apply Discount Code
6. Checkout
7. Exit
============================
Enter your choice:
```

---

### Full Feature Requirements

**✅ Product Catalogue**
- ✅ Store at least 6 products in a dictionary with name, price, and stock quantity
- ✅ Displaying products should show a numbered list with prices formatted to 2 decimal places and stock status — show `"Out of Stock"` if quantity is 0

**Add to Cart**
- User enters a product number to add
- Validate that the choice is a valid product number — print an error if not
- Validate that the item is in stock — print an error if out of stock
- If already in cart, increase quantity instead of adding a duplicate
- Decrease the product's stock by 1 each time it's added

**View Cart**
- Show each item in the cart with quantity and subtotal per item
- Show the running total at the bottom
- If cart is empty, print a friendly message instead

**Remove Item from Cart**
- User picks an item to remove from the cart
- Return the stock back to the product catalogue when removed

**Discount Codes**
- Support at least 3 hardcoded discount codes: one for 10% off, one for 20% off, one for free shipping (you decide what free shipping means — maybe a flat $5 off)
- Only one discount can be applied at a time
- If an invalid code is entered, print an error
- If a code is already applied, tell the user

**Checkout**
- Cannot checkout with an empty cart — print an error
- Show a full receipt: each item, quantity, subtotal, discount applied, and grand total
- After checkout, clear the cart and reset to a fresh state

**Main Menu Loop**
- The whole program runs inside a `while` loop
- Invalid menu choices print an error and loop back — they don't crash the program
- Option 7 exits cleanly with a goodbye message

---

### Concepts You Will Use

Every single thing from Phase 1 appears here naturally — dictionaries and loops to manage products, `while` + `break` for the menu, `if/elif/else` for all validation, `continue` for invalid inputs, f-strings and `:.2f` for the receipt, string methods for discount code handling, casting for user input, and truthy/falsy checks for empty cart detection. Nothing from outside Phase 1 is needed.

---

### How to Approach It — Problem Decomposition

Don't try to build the whole thing at once. Build it in this exact order, testing each piece before moving to the next:

**Day 1:**
1. Set up your product dictionary and get the menu loop running with just `print` statements for each option
2. Build "View Products" fully
3. Build "Add to Cart" fully including all validation
4. Build "View Cart"

**Day 2:**
5. Build "Remove Item from Cart"
6. Build "Apply Discount Code"
7. Build "Checkout" with the full receipt
8. Test every edge case — empty cart checkout, invalid inputs, out of stock items, applying two discounts

---

### Rules

- No functions yet — everything runs as flat sequential code with loops and conditionals, the way you've been writing it. Functions are Phase 2. You'll feel the pain of not having them by the end of this project, and that's intentional — it'll make Phase 2 make perfect sense.
- No external libraries — only `input()`, `print()`, and everything you've already learned.
- Validate everything a user can type — assume the user will always try to break your program.

Start with the product dictionary and the menu loop, show me when you have those working, and we'll go from there.