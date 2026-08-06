from typing import List, Dict, Any

def process_scores(score_list: List[float]) -> Dict[str, Any]:
    if not score_list:
        raise ValueError("Score list must not be empty.")

    avg_score = sum(score_list) / len(score_list)
    return {
        "mean": round(avg_score, 2),
        "max": max(score_list),
        "min": min(score_list),
        "high_scores_count": sum(1 for s in score_list if s >= 8.0),
        "passed_scores": [s for s in score_list if s >= 5.0],
    }


def classify_scores(score_list: List[float]) -> List[Dict[str, Any]]:
    if not score_list:
        raise ValueError("Score list must not be empty.")

    results = []
    for s in score_list:
        if s >= 8.0:
            grade = "Excellent"
        elif s >= 6.5:
            grade = "Good"
        elif s >= 5.0:
            grade = "Average"
        else:
            grade = "Fail"
        results.append({"score": s, "grade": grade})
    return results


if __name__ == "__main__":
    # Test cases
    sample_scores = [7.5, 8.0, 5.5, 9.0, 6.5, 8.5, 4.0]
    print("--- Statistical Results ---")
    print(process_scores(sample_scores))
    print("\n--- Classification Results ---")
    print(classify_scores(sample_scores))
    