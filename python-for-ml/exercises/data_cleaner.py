from typing import List, Dict, Any, Optional

def count_frequencies(values: List[Any]) -> Dict[Any, int]:
    freq: Dict[Any, int] = {}
    for x in values:
        freq[x] = freq.get(x, 0) + 1
    return freq

def convert_usd_to_vnd(
    prices_usd: List[float],
    threshold: float = 10.0,
    exchange_rate: float = 25000.0
) -> List[float]:
    return [ p * exchange_rate for p in prices_usd if p > threshold]

def clean_names(raw_names: List[Optional[str]]) -> List[str]:
    cleaned: List[str] = []
    for name in raw_names:
        if name is not None:
            formatted = name.strip().lower()
            if formatted and formatted not in cleaned:
                cleaned.append(formatted)
    return cleaned

def merge_names_and_scores(names: List[str], scores: List[float]) -> List[Dict[str, Any]]:
    if len(names) != len(scores):
        raise ValueError("Names and scores lists must have the same length")
    return [{"name": name, "score": score} for name, score in zip(names, scores)]

if __name__ == "__main__":
    print("Frequencies:", count_frequencies([12, 7, 9, 12, 15, 7, 21, 9, 12]))
    print("Converted VND:", convert_usd_to_vnd([10.5, 25.0, 5.0, 42.0, 8.5, 15.0]))
    print("Clean Names:", clean_names([" Alice", "BOB", "", " alice", None, "Charlie"]))
    print("Merged Data:", merge_names_and_scores(["An", "Bình", "Chi"], [8.5, 6.0, 9.0]))
                