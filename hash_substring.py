# python3

def read_input():
    # this function needs to acquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    '''
    try:
        input_type = input().rstrip()
        
        if input_type == 'I':
            pattern = input().rstrip()
            text = input().rstrip()
            
        elif input_type == 'F':
            filename = "06"#input().rstrip()
            with open(filename) as f:
                pattern = f.readline().rstrip()
                text = f.readline().rstrip()
                
        return (pattern, text)
    
    except EOFError:
        return "Error: Input stream ended unexpectedly"
    '''
    text = input()
    if 'I' in text:
        pattern = input().rstrip()
        text = input().rstrip()
    elif 'F' in text:
        name = "06"#input()
        if not 'a' in name: 
            
            name = "tests/"+name
            f=open(name,"r")
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return (pattern, text)


def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurrences using Rabin Karp algorithm 
    occurrences = []
    
    if len(pattern) > len(text):
        return occurrences
    
    prime = 101
    d = 256
    q = 997
    p_hash = 0
    t_hash = 0
    h = 1
    
    for i in range(len(pattern) - 1):
        h = (h * d) % q
    
    for i in range(len(pattern)):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q
    
    for i in range(len(text) - len(pattern) + 1):
        if p_hash == t_hash:
            match = True
            for j in range(len(pattern)):
                if text[i+j] != pattern[j]:
                    match = False
                    break
            if match:
                occurrences.append(i)
        
        if i < len(text) - len(pattern):
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + len(pattern)])) % q
            if t_hash < 0:
                t_hash += q
    
    # return an iterable variable
    return occurrences

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
