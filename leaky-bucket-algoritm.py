import time
import random
import matplotlib.pyplot as plt

class LeakyBucket:
    def __init__(self, capacity, rate):
        self.capacity = capacity  # bucket capacity (bytes)
        self.rate = rate          # leak rate (bytes/sec)
        self.tokens = 0           # current fill (bytes)
        self.last_time = time.time()
        self.allowed_data = []
        self.denied_data = []
        self.bucket_fill = []

    def _update_tokens(self):
        now = time.time()
        elapsed_time = now - self.last_time
        self.tokens = min(self.capacity, self.tokens + elapsed_time * self.rate)
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
bucket = LeakyBucket(capacity=400, rate=100)  # bytes bursting,  bytes/sec leak
total_packets = 55
allowed_total = 0
denied_total = 0

for _ in range(total_packets):
    # Simulate incoming network packets 
    packet_size = random.randint(5, 70)
    if bucket.allow_request(packet_size):
        print(f"Packet of {packet_size} bytes allowed.")
        allowed_total += packet_size
    else:
        print(f"Packet of {packet_size} bytes denied. Wait for bucket to drain.")
        denied_total += packet_size
        time.sleep(0.2)  # Wait for some tokens to refill

# Visualization
plt.figure(figsize=(10,5))
plt.plot(bucket.bucket_fill, label="Bucket Fill Level (bytes)")
plt.xlabel("Packet Events")
plt.ylabel("Bucket Fill Level")
plt.title("Leaky Bucket Live Usage Visualization")
plt.legend()
plt.grid(True)
plt.show()

print(f"\nTotal allowed data: {allowed_total} bytes")
print(f"Total denied data: {denied_total} bytes")
