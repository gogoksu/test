import random
import sys

# Daftar user-agent untuk berbagai browser dan perangkat
user_agents = [
    # User-Agent untuk browser modern
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.41 Safari/537.36",
    
    # User-Agent untuk perangkat mobile
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Android 10; Mobile; rv:90.0) Gecko/90.0 Firefox/90.0",
    
    # User-Agent untuk browser lama
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; AS; .NET CLR 4.0.30319; .NET4.0E; .NET4.0C; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729) like Gecko",
    
    # User-Agent palsu
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
]

def generate_fake_user_agents(count):
    return [random.choice(user_agents) for _ in range(count)]

def save_user_agents(user_agents, filename='ua.txt'):
    with open(filename, 'w') as file:
        for agent in user_agents:
            file.write(f"{agent}\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python fake_user_agent_generator.py <number_of_agents>")
        sys.exit(1)

    try:
        num_agents = int(sys.argv[1])
        if num_agents <= 0:
            raise ValueError("Number of agents must be a positive integer.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)

    # Bagi proses menjadi beberapa batch untuk efisiensi
    batch_size = 100000  # Misalnya, setiap batch menghasilkan 100,000 user-agent
    num_batches = num_agents // batch_size
    remainder = num_agents % batch_size

    # Menghasilkan user-agent dalam batch dan menyimpan ke file
    with open('ua.txt', 'w') as file:
        for _ in range(num_batches):
            agents = generate_fake_user_agents(batch_size)
            file.writelines(f"{agent}\n" for agent in agents)
        
        # Menangani sisa batch
        if remainder > 0:
            agents = generate_fake_user_agents(remainder)
            file.writelines(f"{agent}\n" for agent in agents)

    print(f"{num_agents} fake user-agents telah disimpan di ua.txt")

if __name__ == "__main__":
    main()
