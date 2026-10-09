def check_budget(purchases, budget):
    for purchase in purchases:
        if purchase > budget:
            print("This purchase is over budget!")
        else:
            print("This purchase is within budget!")


# Test case 1
check_budget([20, 30, 40], 50)

# Test case 2
check_budget([60, 25, 75], 50)