def word_frequency(text):
    
    text = text.lower()
    
    words = text.split()
    
    freq = {}
    
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
            
    return freq

sentence = "I Love My Mother and I love My Dadu"
print(word_frequency(sentence))