import sys
input = sys.stdin.readline


def sort_books():
    # 가장큰 번호
    max_num = N

    # 가장 큰 번호의 책부터 시작해서 아래로 내려가는 책 정렬 필요 X
    max_num_idx = books.index(max_num)
    answer = N - max_num_idx - 1

    # 가장 큰 번호의 책 위에 있는 책들을 역으로 순회
    for book in books[:max_num_idx][::-1]:
        if book == max_num - 1:
            max_num = book
        else:
            answer += 1

    return answer


N = int(input())  # 책의 개수N
# 책 순서
books = [int(input()) for _ in range(N)]

print(sort_books())