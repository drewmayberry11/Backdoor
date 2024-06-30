# Backdoor 

This repository contains the server and backdoor scripts for creating a reverse shell setup. The server script listens for incoming connections, while the backdoor script connects to the server and waits for commands. The setup allows for file upload/download, command execution, and file deletion on the target machine.

## Setup Instructions

### Prerequisites

- Python 3.x installed on both the server and target machines.
- Basic understanding of networking and Python programming.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/drewmayberry11/Backdoor.git
    cd Backdoor
    ```

### Server Script

The server script listens for incoming connections from the backdoor script and allows for various operations like command execution, file upload/download, and file deletion.



### Backdoor Script

The backdoor script connects to the server and waits for commands. It retries connecting if the initial connection fails.



### Usage

1. **Start the Server Script**:
    - On your server machine, run the server script:
      ```bash
      python3 server.py
      ```
    - The server will listen for incoming connections on port 4444.

2. **Start the Backdoor Script**:
    - On the target machine, run the backdoor script:
      ```bash
      python3 backdoor.py
      ```
    - The backdoor script will attempt to connect to the server and wait for commands.

### Features

- **Command Execution**: Execute system commands on the target machine.
- **File Upload**: Upload files from the server to the target machine.
- **File Download**: Download files from the target machine to the server.
- **File Deletion**: Delete files on the target machine.

### Security Disclaimer

This project is intended for educational purposes only. Unauthorized use of these scripts on systems you do not own or have explicit permission to test is illegal and unethical. Use responsibly and within the bounds of the law.


---

Feel free to clone this repository and customize the scripts as per your requirements. For any issues or contributions, please create a pull request or raise an issue on GitHub.

---


