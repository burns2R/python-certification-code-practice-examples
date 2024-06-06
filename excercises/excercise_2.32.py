product_ids = [101, 102, 103, 104, 105]

for id in product_ids:
    if id % 2 == 0:
        # Note: Correct is “continue”. “continue” goes on with the next loop iteration. 
        # Proof: https://docs.python.org/3/reference/simple_stmts.html#the-continue-statement 
        # Assertion: https://builtin.com/software-engineering-perspectives/pass-vs-continue-python 
        continue
    print('Product ID is', id)