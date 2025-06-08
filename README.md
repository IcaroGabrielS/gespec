# GESPEC

GESPEC is a simple tool to display hardware specifications on Windows and Linux operating systems. The program collects and displays information about CPU, GPU, memory, and monitors connected to the system.

## Features

- Displays detailed CPU information (model, cores, frequency)
- Detects and lists GPUs installed on the system
- Shows RAM and Swap memory amounts
- Displays data about connected monitors and their resolutions

## Requirements

- Python 3.6+
- Libraries:
  - psutil
  - py-cpuinfo
  - GPUtil (optional, for GPU detection)
  - WMI (optional, for Windows systems)
  - screeninfo
  - colorama

## Installation

1. Clone the repository:
```
git clone https://github.com/IcaroGabrielS/gespec.git
cd gespec
```

2. Install dependencies:
```
pip install psutil py-cpuinfo GPUtil screeninfo colorama
```

3. On Windows systems, also install:
```
pip install WMI
```

## Usage

Run the main file:
```
python main.py
```

## Project Structure

- `main.py`: Main file that coordinates the display of information
- `cpuGetter.py`: Collects processor information
- `gpuGetter.py`: Identifies and retrieves data about graphics cards
- `ramGetter.py`: Obtains system memory information
- `videoGetter.py`: Collects data about connected monitors

## Compatibility

The program was developed to work on Windows and Linux systems, adapting collection methods according to the detected operating system.