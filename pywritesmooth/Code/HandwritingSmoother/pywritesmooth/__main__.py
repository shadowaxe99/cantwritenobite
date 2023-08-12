from pywritesmooth.Code.HandwritingSmoother.pywritesmooth.TrainSmoother.LSTMTrainer import LSTMTrainer
from pywritesmooth.Code.HandwritingSmoother.pywritesmooth.data import save_generated_stroke, save_generated_stroke_biases, load_svg_data


def main():
    # Initialize LSTMTrainer
    trainer = LSTMTrainer()

    # Load data
    data = load_svg_data('path_to_svg_directory')

    # Train the network
    trainer.train_network(data)

    # Generate handwriting
    handwriting = trainer.generate_handwriting(data)

    # Smooth the handwriting
    smoothed_handwriting = trainer.smooth_handwriting(handwriting)

    # Save the generated handwriting
    save_generated_stroke(smoothed_handwriting)


if __name__ == '__main__':
    main()