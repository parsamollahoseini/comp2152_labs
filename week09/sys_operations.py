

#!/usr/bin/env python3
import os
import socket
import platform
import sys

# ------------------------------
# System Information and Operations
# ------------------------------
print("Machine type:", platform.machine())
print("Processor type:", platform.processor())

# Set default timeout for sockets to 50 seconds
socket.setdefaulttimeout(50)
print("Default socket timeout:", socket.getdefaulttimeout())

print("Operating system name:", os.name)
print("Current process ID:", os.getpid())

# Fork a new process (Unix-based systems only)
if hasattr(os, 'fork'):
    pid = os.fork()
    if pid == 0:
        # Child process
        print("Forked child process. PID:", os.getpid())
        sys.exit(0)
    else:
        os.wait()  # Wait for child process to exit
        print("Parent process after fork. PID:", os.getpid())
else:
    print("Fork not available on this operating system.")

print("\n--- File Operations using os module (lower level) ---")
print("Using os module for file operations is a lower-level approach compared to 'with open'.")
print("It provides more granular control over file descriptors, but requires manual management.")

# Print current process id before file operations
print("Current process ID (before file operations):", os.getpid())

# Open (or create) a file named fdpractice.txt for reading and writing
# The os.open method is a lower-level alternative to the built-in open() function.
fd = os.open("fdpractice.txt", os.O_RDWR | os.O_CREAT, 0o666)

# Write text to the file
text = "Some string to write to the file"
os.write(fd, text.encode())

# Fork a new process to demonstrate file descriptor sharing
fork_fd_pid = os.fork()
if fork_fd_pid == 0:
    # Child process
    print("Child process (file operation) PID:", os.getpid())
    # Move file pointer back to the beginning of the file
    os.lseek(fd, 0, os.SEEK_SET)
    # Read up to 100 bytes from the file
    file_content = os.read(fd, 100)
    print("Content read from file:", file_content.decode())
    # Close the file in the child process
    os.close(fd)
    os._exit(0)
else:
    # Parent process
    print("Parent process (file operation) PID:", os.getpid())
    os.wait()  # Wait for the child process to finish
    os.close(fd)