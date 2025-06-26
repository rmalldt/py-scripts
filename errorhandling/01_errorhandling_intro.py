def read_and_sum_integers(filepath):
    try:
        with open(filepath, mode="r", encoding="utf-8") as f:
            sum = 0
            for line in f:
                try:
                    num = int(line.strip())
                    sum += num
                except ValueError as e:
                    raise ValueError(f"Invalid content in file: {line.strip()}") from e
            return sum
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {filepath}") from e
    except Exception as e:
        raise RuntimeError(f"An unexpected error occured: {e}") from e


def main():
    filepath = "../data/texts/numbers.txt"

    try:
        total = read_and_sum_integers(filepath)
        print(f"Sum of the integers: {total}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# ------------------ Test

if __name__ == "__main__":
    main()
