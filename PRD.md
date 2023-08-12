# Product Requirement Document (PRD) for Handwriting Synthesis Program

## Overview:

The goal is to create a handwriting synthesis program that can take thousands of letters (uppercase, lowercase, numbers, symbols) all in SVG format and create different versions of handwriting that vary in style. The program will utilize existing SVGs to generate unique and distinguishable handwriting styles.

## Repository:

pywritesmooth

## Key Components:

### LSTM Handwriting Model Training:

**Class:** LSTMTrainer

**Description:** Main driver to train an LSTM handwriting model.

**Dependencies:** HandwritingSynthesisModel, LSTMDataInterface

[Code Link](https://github.com/shadowaxe99/pywritesmooth/blob/main/LSTMTrainer.py)

### Stroke Path Generation:

**Method:** get_stroke_path

**Description:** Generates the path of a stroke sample in SVG format.

**Parameters:** data, factor, offset_x, offset_y

[Code Link](https://github.com/shadowaxe99/pywritesmooth/blob/main/stroke_path_generator.py)

### Saving Generated Strokes:

**Methods:** save_generated_stroke, save_generated_stroke_biases

**Description:** Draws handwriting samples and saves them as SVG files.

**Parameters:** data, factor, show_save_loc, biases

[Code Link](https://github.com/shadowaxe99/pywritesmooth/blob/main/stroke_saver.py)

### One-Hot Encoding:

**Method:** one_hot

**Description:** Transforms a string sequence into a one-hot matrix.

**Parameters:** s (string sequence)

[Code Link](https://github.com/shadowaxe99/pywritesmooth/blob/main/one_hot_encoding.py)

## Requirements:

- Input: Thousands of SVGs representing different variations of characters.
- Output: At least 10+ different handwriting styles with distinguishable differences.
- Automation: Replace the manual handwriting process with an automated solution.

## Potential Enhancements:

- Cursive Writing: Explore ways to generate cursive style writing.
- Style Customization: Provide options to customize the generated handwriting styles.

## Conclusion:

The pywritesmooth repository provides a foundational framework for the handwriting synthesis program. It will require further development and customization to fully meet the project's specific requirements and objectives.