def find_runner_up_score():
    n = int(input("Enter the number of participants: "))

    scores = list(map(int, input("Enter the scores of the participants separated by spaces: ").split()))

    unique_scores = list(set(scores))

    unique_scores.sort(reverse=True)

    if len(unique_scores) > 1:
        runner_up_score = unique_scores[1]
    else:
        runner_up_score = "No runner-up, only one unique score."

    return runner_up_score

runner_up_score = find_runner_up_score()
print(f"Runner-up score: {runner_up_score}")
