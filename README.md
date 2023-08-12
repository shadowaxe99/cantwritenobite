# Handwriting Synthesis Program

This repository contains a handwriting synthesis program that generates different versions of handwriting styles using existing SVGs. The program takes thousands of letters (uppercase, lowercase, numbers, symbols) in SVG format as input and produces handwriting samples with distinguishable differences.

## Repository Structure

- `main.py`: The main script to run the handwriting synthesis program.
- `pywritesmooth/`: Directory containing the key components of the program.

## Key Components

### LSTM Handwriting Model Training

- **Class**: `LSTMTrainer`
- **Description**: Main driver to train an LSTM handwriting model.
- **Dependencies**: `HandwritingSynthesisModel`, `LSTMDataInterface`

### Stroke Path Generation

- **Method**: `get_stroke_path`
- **Description**: Generates the path of a stroke sample in SVG format.
- **Parameters**: `data`, `factor`, `offset_x`, `offset_y`

### Saving Generated Strokes

- **Methods**: `save_generated_stroke`, `save_generated_stroke_biases`
- **Description**: Draws handwriting samples and saves them as SVG files.
- **Parameters**: `data`, `factor`, `show_save_loc`, `biases`

### One-Hot Encoding

- **Method**: `one_hot`
- **Description**: Transforms a string sequence into a one-hot matrix.
- **Parameters**: `s` (string sequence)
