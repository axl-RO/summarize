import argparse
from summarizer import summarize_text


def main():
    parser = argparse.ArgumentParser(description="Text Summarization using T5")
    parser.add_argument("--text", type=str, help="Text to summarize")
    parser.add_argument("--file", type=str, help="Text file to summarize")

    args = parser.parse_args()

    if args.text:
        text = args.text

    elif args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()

    else:
        print("Provide --text or --file")
        return

    summary = summarize_text(text)
    print("\nSummary:\n", summary)


if __name__ == "__main__":
    main()
