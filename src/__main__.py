import argparse
import game


def main():
    parser = argparse.ArgumentParser(
        prog="Ball Game",
        description="Ball game for entertaining purposes",
    )

    # Add an argument for the number of balls
    parser.add_argument(
        "-n", "--num-balls",
        type=int,
        default=1,  # Default number of balls
        help="Number of balls to spawn in the game (default: 50)"
    )

    args = parser.parse_args()

    # Pass the number of balls to the game.run() function
    game.run(num_balls=args.num_balls)


if __name__ == "__main__":
    main()