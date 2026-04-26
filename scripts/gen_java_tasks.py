import json
import os
import re


def load_indices_from_prompts(root: str) -> list[int]:
    path = os.path.join(root, "prompts.txt")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return [int(x) for x in re.findall(r"\d+", text)]


def main() -> None:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    indices = load_indices_from_prompts(root)
    jsonl_path = os.path.join(root, "humaneval_java.jsonl")
    base = os.path.join(root, "generated", "java")

    with open(jsonl_path, "r", encoding="utf-8") as f:
        rows = {json.loads(line)["task_id"]: json.loads(line) for line in f}

    os.makedirs(base, exist_ok=True)

    for i in indices:
        tid = f"Java/{i}"
        if tid not in rows:
            raise SystemExit(f"Missing {tid}")
        r = rows[tid]
        override_dir = os.path.join(os.path.dirname(__file__), "java8_solution_overrides")
        override_path = os.path.join(override_dir, f"{i}.java")
        if os.path.isfile(override_path):
            with open(override_path, "r", encoding="utf-8") as o:
                full_solution = o.read().rstrip()
        else:
            prompt = r["prompt"].rstrip()
            sol = r["canonical_solution"].strip()
            full_solution = prompt + sol
        test = r["test"].strip()
        d = os.path.join(base, f"task_{i}")
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "Solution.java"), "w", encoding="utf-8") as out:
            out.write(full_solution + "\n")
        main_src = "import java.util.*;\nimport java.lang.*;\n\n" + test
        with open(os.path.join(d, "Main.java"), "w", encoding="utf-8") as out:
            out.write(main_src + "\n")
        print("wrote", d)


if __name__ == "__main__":
    main()
