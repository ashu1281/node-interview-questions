import re

FILE_PATH = "node-js-interview-questions.md"


def parse_and_update_tables(lines):
    """
    STEP 1

    Update:
    - serial numbers
    - anchor numbers
    - collect questions + stars

    Example:
    #72-question
    ->
    #113-question
    """

    updated_lines = []

    questions = []

    inside_table = False

    counter = 1

    for line in lines:

        # detect question table
        if line.strip().startswith("| No. | Question |"):

            inside_table = True

            updated_lines.append(line)

            continue

        # separator row
        if inside_table and line.strip().startswith("|---"):

            updated_lines.append(line)

            continue

        if inside_table:

            match = re.match(
                r'^\|\s*(\d+)\s*\|\s*\[(.*?)\]\((#\d+-(.*?))\)\s*\|\s*(.*?)\s*\|$',
                line
            )

            if match:

                question = match.group(2).strip()

                old_slug = match.group(4).strip()

                stars = match.group(5).strip()

                # update only number
                new_anchor = f"#{counter}-{old_slug}"

                # save question + stars
                questions.append({
                    "number": counter,
                    "question": question,
                    "stars": stars
                })

                updated_line = (
                    f"| {counter} | "
                    f"[{question}]({new_anchor}) | "
                    f"{stars} |"
                )

                updated_lines.append(updated_line)

                counter += 1

                continue

            # table ended
            if not line.startswith("|"):

                inside_table = False

        updated_lines.append(line)

    return updated_lines, questions


def update_question_headings(lines, questions):
    """
    STEP 2

    Update:
    # 72. Question
    ->
    # 72. Question ⭐⭐⭐

    ONLY matching questions
    """

    updated_lines = []

    for line in lines:

        updated = False

        for item in questions:

            number = item["number"]

            question = item["question"]

            stars = item["stars"]

            pattern = (
                rf'^#\s+\d+\.\s+'
                rf'{re.escape(question)}'
                rf'(?:\s+⭐+)?\s*$'
            )

            if re.match(pattern, line):

                updated_lines.append(
                    f"# {number}. {question} {stars}"
                )

                updated = True

                break

        if not updated:
            updated_lines.append(line)

    return updated_lines


def main():

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        content = file.read()

    lines = content.split("\n")

    # STEP 1
    lines, questions = parse_and_update_tables(lines)

    # STEP 2
    lines = update_question_headings(
        lines,
        questions
    )

    updated_content = "\n".join(lines)

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        file.write(updated_content)

    print("✅ Table serial numbers updated")
    print("✅ Anchor numbers updated")
    print("✅ Question headings updated")
    print("✅ Stars added to headings")
    print("✅ Slug text preserved")


if __name__ == "__main__":
    main()