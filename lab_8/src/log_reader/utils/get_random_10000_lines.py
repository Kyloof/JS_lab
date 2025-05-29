import random

def get_random_lines(input_file, output_file, num_lines=10000):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    if num_lines > len(lines):
        sampled_lines = lines
    else:
        sampled_lines = random.sample(lines, num_lines)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(sampled_lines)

if __name__ == "__main__":
    input_file = "http.log"  
    output_file = "random_http.log"
    get_random_lines(input_file, output_file)
