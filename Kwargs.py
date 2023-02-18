def order_pizza(name, address, **toppings):
    print(f"O nome e {name}")
    print(f"O endereco e {address}")
    preco = 22.00
    for key, value in toppings.items():
        preco = preco + 6.00
    print(f"O preco total e {preco}")
    return preco


total_price = order_pizza("Amanda", "Canada", jalapenos = True, extra_cheese = True, hum = True)


























