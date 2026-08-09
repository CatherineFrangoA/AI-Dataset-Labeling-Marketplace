import logging
from datetime import datetime

logging.basicConfig(
    filename="agent.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def perceive(data):
    logging.info("PERCEIVE: Received dataset information")
    return data


def plan(data):
    logging.info("PLAN: Creating labeling plan")

    if isinstance(data, list):
        return {
            "action": "analyze_dataset",
            "rows": len(data)
        }

    return {
        "action": "analyze_dataset"
    }


def tool_count_rows(data):
    logging.info("TOOL 1: Counting dataset rows")

    if isinstance(data, list):
        return len(data)

    return 0


def tool_generate_labels(data):
    logging.info("TOOL 2: Generating label suggestions")

    if isinstance(data, list):
        return ["label_suggestion"]

    return ["label_suggestion"]


def act(data, plan_result):
    logging.info("ACT: Executing planned action")

    row_count = tool_count_rows(data)
    labels = tool_generate_labels(data)

    return {
        "row_count": row_count,
        "suggested_labels": labels
    }


def observe(result):
    logging.info("OBSERVE: Checking action result")
    return result


def run_agent(data):
    logging.info("AGENT LOOP STARTED")

    perceived_data = perceive(data)

    plan_result = plan(perceived_data)

    action_result = act(
        perceived_data,
        plan_result
    )

    final_result = observe(action_result)

    logging.info("AGENT LOOP COMPLETED")

    return {
        "perceive": perceived_data,
        "plan": plan_result,
        "act": action_result,
        "observe": final_result
    }