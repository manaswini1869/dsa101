# metrics api
# input ("log: 123, fps:123, temp:45, iter_val:1", model_name="gpt-4", "run_num:1")
# input ("log: 123, fps:123, temp:45, iter_val:2", model_name="gpt-4", "run_num:1")
# input ("log: 123, fps:123, temp:45, iter_val:3", model_name="gpt-4", "run_num:1")

# output for model name gpt-4: [
# {log: 123,
#  fps:123,
#  temp:45,
#  iter_val:1},
# {log: 123,
#  fps:123,
#     temp:45,
#     iter_val:2},
# {log: 123,
#     fps:123,
#     temp:45,
#     iter_val:3}

# ]


import threading
from collections import defaultdict
from typing import Dict, List


class MetricsAPI:
    def __init__(self):
        # model -> run -> list of metric dicts
        self._store = defaultdict(lambda: defaultdict(list))
        self._lock = threading.Lock()

    def push(self, log_line: str, model: str, run: int) -> None:
        """
        log_line example:
        "log: 123, fps:123, temp:45, iter_val:1"
        """
        metrics = self._parse_log_line(log_line)

        if "iter_val" not in metrics:
            raise ValueError("log_line must contain iter_val")

        with self._lock:
            self._store[model][run].append(metrics)

    def get(self, model: str, run: int) -> List[Dict]:
        """
        Returns metrics ordered by iter_val
        """
        with self._lock:
            runs = self._store.get(model, {})
            metrics = runs.get(run, [])

            return sorted(metrics, key=lambda x: x["iter_val"])

    def _parse_log_line(self, log_line: str) -> Dict:
        """
        Converts:
        'log: 123, fps:123, temp:45, iter_val:1'
        into:
        {'log': 123, 'fps': 123, 'temp': 45, 'iter_val': 1}
        """
        result = {}
        for part in log_line.split(","):
            key, value = part.split(":")
            key = key.strip()
            value = value.strip()

            # convert numeric values
            if value.isdigit():
                value = int(value)
            else:
                try:
                    value = float(value)
                except ValueError:
                    pass

            result[key] = value

        return result



