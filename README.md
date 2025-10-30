# Token Bucket Algorithm: Real-Time Bandwidth Monitoring and Rate Limiting in Python

## Overview

This project implements the **Token Bucket** algorithm for bandwidth monitoring and rate limiting. It features:

- Simulation of network packets
- Per-connection bandwidth control using a token bucket
- Real-time usage visualization with Matplotlib

## Features

- **Bandwidth Monitor:** Tracks and reports total allowed and denied data.
- **Rate Limiter:** Uses the Token Bucket algorithm to allow bursts of traffic within the configured rate and capacity.
- **Dashboard:** Visualizes the fill state of the bucket versus time.

## How It Works

- Randomly sized "packets" mimic incoming client data.
- Each packet is checked against the Token Bucket's current token and rate settings.
- Allowed packets consume tokens from the bucket; denied packets simulate bandwidth policing.
- All bucket token levels are recorded and plotted after the run.

## Usage

1. **Install dependencies:**

pip install matplotlib

text

2. **Run the script:**

python token_bucket_algorithm.py

text

3. **Interpret output:**

- Console shows allowed/denied packets.
- Graph displays bucket fill level over all events.
- Final totals summarize performance.

## Example Output

Packet of 38 bytes allowed.
:
:
Packet of 56 bytes denied. Insufficient tokens.
Packet of 7 bytes allowed.

Total allowed data: 798 bytes
Total denied data: 1058 bytes


![Token Bucket Live Usage Visualization](image.png.txt)

## Customization

- Change `token_capacity` and `token_rate` in the script to tune bandwidth and burst tolerance.
- Replace the simulation loop with real network data to enforce actual bandwidth limitations.

## References

- [GeeksforGeeks: Token Bucket Algorithm](https://www.geeksforgeeks.org/computer-networks/token-bucket-algorithm/)
- [Token Bucket Algorithm Example on GitHub](https://github.com/bbeck/token-bucket)

