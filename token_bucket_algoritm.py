import time
import random
import matplotlib.pyplot as plt

class TokenBucket:
    def __init__(self, token_capacity, token_rate):
        self.token_capacity = token_capacity  # Maximum tokens in bucket
        self.token_rate = token_rate          # Tokens added per second
        self.tokens = token_capacity           # Start full for initial burst
        self.last_time = time.time()
        self.allowed_data = []
        self.denied_data = []
        self.bucket_fill = []

    def _update_tokens(self):
        now = time.time()
        elapsed_time = now - self.last_time
        new_tokens = elapsed_time * self.token_rate
        self.tokens = min(self.token_capacity, self.tokens + new_tokens)
        self.last_time = now

    def allow_request(self, data_bytes):
        self._update_tokens()
        if self.tokens >= data_bytes:
            self.tokens -= data_bytes
            self.allowed_data.append(data_bytes)
            self.bucket_fill.append(self.tokens)
            return True
        else:
            self.denied_data.append(data_bytes)
            self.bucket_fill.append(self.tokens)
            return False

# Configuration
bucket = TokenBucket(token_capacity=400, token_rate=100)  # 400 tokens max, refill at 100 tokens/sec
total_packets = 55
allowed_total = 0
denied_total = 0

for _ in range(total_packets):
    packet_size = random.randint(5, 70)
    if bucket.allow_request(packet_size):
        print(f"Packet of {packet_size} bytes allowed.")
        allowed_total += packet_size
    else:
        print(f"Packet of {packet_size} bytes denied. Insufficient tokens.")
        denied_total += packet_size
        time.sleep(0.2)

# Visualization
plt.figure(figsize=(10, 5))
plt.plot(bucket.bucket_fill, label="Bucket Fill Level (tokens)")
plt.xlabel("Packet Events")
plt.ylabel("Available Tokens")
plt.title("Token Bucket Live Usage Visualization")
plt.legend()
plt.grid(True)
plt.show()

print(f"\nTotal allowed data: {allowed_total} bytes")
print(f"Total denied data: {denied_total} bytes")
