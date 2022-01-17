nums = []

for i in range(0, 10):
    nums.append(int(input('Digite um número: ')))

soma = 0

for i in range(0, 10):
    soma += nums[i]

print(soma)