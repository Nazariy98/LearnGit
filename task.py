
def my_test_fn(my_laptop_price: dict, value_type: type) -> str:
    price_str = ''
    for key, value in my_laptop_price.items():
        if type(value) == value_type:
            value += value * 0.05
            value = round(value, 2)
        if type(value) == str:
            value = value.capitalize()
        
        price_str += f"[{key.upper()}]: {value}$\n"
        # price_str = price_str.upper()
    return price_str

my_price_laptop_dict = {
    'asus': 24_787.0,
    'dell': 34_787.0,
    'hp': 44_787.55,
    'aser': 'ended',
}

print(my_test_fn(my_laptop_price=my_price_laptop_dict, value_type=float))






if __name__ == "__main__":
    print()

