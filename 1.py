import timeit
from Crypto.Cipher import DES, DES3, AES
from Crypto.Random import get_random_bytes
from Crypto.Util. Padding import pad
from tabulate import tabulate

def generate_large_data(size_in_bytes):
    return b'A' * size_in_bytes

def measure execution_time(data):
    execution_times = []
    
    def measure_des_time (data, key): 
        cipher = DES.new(key, DES.MODE_ECB) 
        start_time = timeit.default_timer() 
        ct = cipher.encrypt(pad(data, DES.block_size)) 
        end_time = timeit.default_timer() 
        return end_time - start_time
    
    def measure_3des_time (data, key): 
        cipher = DES3.new(key, DES3.MODE_ECB) 
        start_time = timeit.default_timer() 
        ct = cipher.encrypt(pad(data, DES3.block_size)) 
        end_time = timeit.default_timer() 
        return end_time - start_time
    
    def measure_aes_128_time(data, key): 
        cipher AES.new(key, AES.MODE_ECB) 
        start_time = timeit.default_timer() 
        ct = cipher.encrypt(pad(data, AES.block_size)) 
        end_time = timeit.default_timer() 
        return end_time - start_time
    
    def measure_aes_256_time (data, key):
        cipher = AES.new(key, AES.MODE_ECB)
        start_time = timeit.default_timer()
        ct = cipher.encrypt (pad (data, AES.block_size))
        end_time = timeit.default_timer()
        return end_time - start_time
    
    des_key = get_random_bytes(8)
    execution_times.append(("DES", measure_des_time(data, des_key)))
    
    triple_des_key = get_random_bytes (24) #Triple DES = 24 bytes
    execution_times.append(("Triple DES", measure_3des_time(data, triple_des_key)))
    
    aes_128_key = get_random_bytes (16) #AES-128 = 16 bytes
    execution_times.append(("AES-128", measure_aes_128_time(data, aes_128_key)))
    
    aes_256_key = get_random_bytes (32) #AES-256 = 32 bytes
    execution_times.append(("AES-256"; measure_aes_256_time(data, aes_256_key)))
    
    return execution_times

def generate_table(execution times):
    execution_times.sort(key=lambda x: x[1]) # Sort by execution time in ascending order
    table = []
    for i, (algorithm, time) in enumerate (execution_times):
        table.append([
            i + 1,
            algorithm,
            "Python",
            len(data) * 8,
            {
                "DES": 64,
                "Triple DES": 64,
                "AES-128": 128,
                "AES-256": 256
            }.get(algorithm, ""),
            round(time, 7),
            i + 1 # Priority based on sorted order
        ])
    return table

if __name__ == "__main__":
    data = generate_large_data(1000)
    execution_times = measure_execution_time (data)
    table = generate_table (execution_times)
    
    sorted_table = sorted(table, key=lambda x: x[6])
    headers = ["Serial No.", "Encryption Algorithm", "Programming Language", "Input Size (bits)", "Output Size(bits)", "Total Time Tsken(seconds)", "Priority"]
    print(tabulate(sorted_table, headers=headers, tablefmt="grid"))