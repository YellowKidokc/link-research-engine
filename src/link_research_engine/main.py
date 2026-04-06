from link_research_engine.modules.intake import describe_questions


def main() -> None:
    print("Link Research Engine")
    print("====================")
    for line in describe_questions():
        print(f"- {line}")


if __name__ == "__main__":
    main()
