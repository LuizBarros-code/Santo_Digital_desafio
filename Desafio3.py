def subconjuntos(nums):
    subcon = [[]] 

    for num in nums:
        subcon += [subset + [num] for subset in subcon]

    return subcon

nums = [1, 2, 3, 4]
resultado = subconjuntos(nums)
print(resultado)
