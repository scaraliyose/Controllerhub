# Sample Python code for testing  linting and type checking

def add(a, b) -> int:
    """Return the sum of a and b."""
    return a + b


def main() -> None:
    result: int = add(2, 3)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
