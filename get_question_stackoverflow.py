__doc__ = """
Viết script lấy top **N** câu hỏi được vote cao nhất của tag **LABEL** trên stackoverflow.com.
In ra màn hình: Title câu hỏi, link đến câu trả lời được vote cao nhất

Link API: https://api.stackexchange.com/docs

Dạng của câu lệnh:

python3 so.py N LABEL
"""


def get_top_questions(N, LABEL):
    import requests

    list_questions = []
    url = "https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=votes&tagged={}&site=stackoverflow".format(
        LABEL
    )
    r = requests.get(url)
    questions = r.json()

    for question in questions["items"]:
        list_questions.append((question["score"], question["title"], question["link"]))
    list_questions.sort(key=lambda x: int(x[0]), reverse=True)

    return list_questions[: int(N)]


def main():
    import sys

    N, LABEL = sys.argv[1], sys.argv[2]

    for (idx, (vote, title, link)) in enumerate(get_top_questions(N, LABEL), start=1):
        print("{}: {} votes - {} - Answer: {}".format(idx, vote, title, link))


if __name__ == "__main__":
    main()
