# ============================================================
#  PROJECT 1 — Set Operations Visualiser
#  IITM BS Math 1  |  Beginner Python
# ============================================================
#
#  HOW TO RUN:
#    python set_operations.py
#
#  WHAT YOU WILL PRACTISE:
#    - Python sets (they ARE math sets)
#    - Functions  (def)
#    - Loops      (for)
#    - Conditions (if / else)
#    - f-strings  (printing results neatly)
# ============================================================


# ------------------------------------------------------------
# STEP 1 — define your sets  (same as writing A = {1,3,5,7})
# ------------------------------------------------------------

A = {1, 3, 5}
B = {2, 4, 6}
U = {1, 2, 3, 4, 5, 6,}   # Universal set


# ------------------------------------------------------------
# STEP 2 — a tiny helper so results print nicely
# ------------------------------------------------------------

def show(label, result):
    """Print a labelled set result."""
    print(f"  {label:<30} {sorted(result)}")
    #       ^ left-align label in 30 chars  ^ sort so order is predictable


# ------------------------------------------------------------
# STEP 3 — the six operations you know from class
# ------------------------------------------------------------

def set_operations(A, B, U):
    print("\n========== SET OPERATIONS ==========")
    print(f"  A = {sorted(A)}")
    print(f"  B = {sorted(B)}")
    print(f"  U = {sorted(U)}")
    print("-------------------------------------")

    show("A ∪ B  (union)",          A | B)
    show("A ∩ B  (intersection)",   A & B)
    show("A - B  (difference)",     A - B)
    show("B - A  (difference)",     B - A)
    show("A'     (complement of A)", U - A)
    show("B'     (complement of B)", U - B)

    print()
    print("  Verify De Morgan's 1st law:")
    left  = U - (A | B)          # (A ∪ B)'
    right = (U - A) & (U - B)    # A' ∩ B'
    print(f"    (A ∪ B)'  = {sorted(left)}")
    print(f"    A' ∩ B'   = {sorted(right)}")
    print(f"    Equal?    {left == right}")   # should always be True

    print()
    print("  Verify De Morgan's 2nd law:")
    left2  = U - (A & B)         # (A ∩ B)'
    right2 = (U - A) | (U - B)   # A' ∪ B'
    print(f"    (A ∩ B)'  = {sorted(left2)}")
    print(f"    A' ∪ B'   = {sorted(right2)}")
    print(f"    Equal?    {left2 == right2}")


# ------------------------------------------------------------
# STEP 4 — Cartesian product  (A × B)
#           This is where relation R lives!
# ------------------------------------------------------------

def cartesian_product(A, B):
    print("\n========== CARTESIAN PRODUCT A×B ==========")
    product = set()
    for a in A:
        for b in B:            # nested loop = every (a,b) pair
            product.add((a, b))

    print(f"  Total pairs: {len(product)}   (should be {len(A)} × {len(B)} = {len(A)*len(B)})")
    for pair in sorted(product):
        print(f"    {pair}")
    return product


# ------------------------------------------------------------
# STEP 5 — Build relation R  where  a < b
#           (the exact relation from your problem!)
# ------------------------------------------------------------

def build_relation(A, B):
    print("\n========== RELATION  R : a < b ==========")

    R = set()
    for a in A:
        for b in B:
            if a < b:          # the condition that defines R
                R.add((a, b))

    print(f"  Pairs in R:  {sorted(R)}")
    print(f"  |R| = {len(R)}   (cardinality)")

    # Domain  = all first elements
    domain = {a for a, b in R}     # set comprehension — new concept!
    print(f"  Domain of R:       {sorted(domain)}")

    # Range (image) = all second elements
    range_ = {b for a, b in R}
    print(f"  Range of R:        {sorted(range_)}")

    return R


# ------------------------------------------------------------
# STEP 6 — Inverse relation  R⁻¹
#           just flip every pair (a,b) → (b,a)
# ------------------------------------------------------------

def inverse_relation(R):
    print("\n========== INVERSE RELATION  R⁻¹ ==========")

    R_inv = set()
    for a, b in R:
        R_inv.add((b, a))      # swap the two elements

    print(f"  Pairs in R⁻¹: {sorted(R_inv)}")

    domain_inv = {x for x, y in R_inv}
    range_inv  = {y for x, y in R_inv}

    print(f"  Domain of R⁻¹:  {sorted(domain_inv)}")
    print(f"  Range  of R⁻¹:  {sorted(range_inv)}")

    # Verify option (a) from your problem
    domain_R = {a for a, b in R}
    print()
    print("  Verify: Domain(R) == Range(R⁻¹) ?")
    print(f"    Domain(R)    = {sorted(domain_R)}")
    print(f"    Range(R⁻¹)  = {sorted(range_inv)}")
    print(f"    Equal?       {domain_R == range_inv}")   # True ✓


# ------------------------------------------------------------
# STEP 7 — Power set  P(A)
#           all possible subsets of A
# ------------------------------------------------------------

def power_set(A):
    print("\n========== POWER SET  P(A) ==========")

    A_list = list(A)           # sets can't be indexed, lists can
    n      = len(A_list)
    result = []

    # Trick: a set with n elements → 2^n subsets
    # Each number from 0 to 2^n - 1 in binary tells us which elements to pick
    for i in range(2 ** n):
        subset = set()
        for j in range(n):
            if i & (1 << j):   # bitwise: is the j-th bit of i set?
                subset.add(A_list[j])
        result.append(subset)

    print(f"  |A| = {n}  →  |P(A)| = 2^{n} = {2**n}")
    print(f"  All subsets:")
    for s in result:
        print(f"    {sorted(s)}")

    return result


# ------------------------------------------------------------
# STEP 8 — run everything
# ------------------------------------------------------------
hello please work bro ffo