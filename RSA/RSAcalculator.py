import math

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def get_prime_input(prompt):
    while True:
        try:
            num = int(input(prompt))

            if is_prime(num):
                return num
            else:
                print(f"{num} is not a prime number. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# Step 1: Get prime numbers
p = get_prime_input("Enter the first prime number: ")
q = get_prime_input("Enter the second prime number: ")

print(f"Successfully received primes: {p} and {q}")


# Step 2: Calculate N
N = p * q
print("N =", N)


# Step 3: Calculate Euler's Totient
r = (p - 1) * (q - 1)
print("r =", r)


# Step 4: Choose e
while True:
    try:
        e = int(input("Enter e: "))

        if 1 < e < r and math.gcd(e, r) == 1:
            print("e is valid and coprime with r.")
            break
        else:
            print(f"{e} is not a valid value for e.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


# Step 5: Calculate d
d = 1

while True:
    if (d * e) % r == 1:
        break
    d += 1

print("d =", d)


# Step 6: Encryption
m = int(input("Enter a message number: "))

c = pow(m, e, N)

print("Original message:", m)
print("Encrypted message:", c)

# Step 8: Decryption
decrypted_message = pow(c, d, N)

print("Decrypted message:", decrypted_message)