def generate_sequence(n):
    """x1 = x2 = x3 = 1."""
    if n < 1:
        return []
    sequence = [1, 1, 1,  ]
    for i in range(3, n):
        sequence.append(sequence[i - 1] + sequence[i - 3])
    return sequence[:n]  # возврат первых n элементов

def is_palindrome(sequence):
    return sequence == sequence[::-1]


n = 3
seq = generate_sequence(n)
print("Сгенерированная последовательность:", seq)
print("Является ли палиндромом:", is_palindrome(seq))