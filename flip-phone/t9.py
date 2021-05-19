with open('dictionary.txt', 'r') as f:
    dictionary = f.read().splitlines()

results = list()
sequence = input('Enter sequence: ')
num_pad = {2:['a', 'b', 'c'], 3:['d', 'e', 'f'], 4:['g', 'h', 'i'], 5:['j', 'k', 'l'], 6:['m', 'n', 'o'], 
           7:['p', 'q', 'r', 's'], 8:['t', 'u', 'v'], 9:['w', 'x', 'y', 'z']}

for word in dictionary:
    if len(word) == len(sequence):
        for idx, num in enumerate(sequence):
            if word[idx] in num_pad[int(num)]: 
                if idx == len(sequence) - 1:
                    results.append(word)
            else:
                break
print(results[:10])
