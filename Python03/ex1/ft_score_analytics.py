import sys


def score_player() -> None:
    print("=== Player Score Analytics ===")

    scores = []
    total_args = len(sys.argv)

    if total_args == 1:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        i = 1
        while i < total_args:

            try:
                score = int(sys.argv[i])
                scores.append(score)
            except ValueError:
                print(f"Invalid parameter: '{sys.argv[i]}'")
            i += 1

        if scores:
            print(f"Scores processed: {scores}")
            total_scores = len(scores)
            print(f"Total players: {total_scores}")
            sum_scores = sum(scores)
            print(f"Total score: {sum_scores}")
            print(f"Average score: {sum_scores / total_scores}")
            max_score = max(scores)
            print(f"High score: {max_score}")
            min_score = min(scores)
            print(f"Low score: {min_score}")
            print(f"Score range: {max_score - min_score}")
        else:
            print(
                "No scores provided. "
                "Usage: python3 ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    score_player()
