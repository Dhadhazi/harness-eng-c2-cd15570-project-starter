"""Loop 02 component: make a separate model call that reviews finished evidence."""

from __future__ import annotations

from typing import Any


REQUIRED_KEYS = {
    "task_status",
    "efficiency_score",
    "critique",
    "systemic_failure_root_cause",
    "workflow_adjustments",
}

# TODO: Replace this empty placeholder with real evaluator instructions.
# Tell the evaluator to judge goal fulfillment, loop or stall behavior, tool
# efficiency, and log sufficiency using only the supplied evidence. Require
# JSON with exactly the keys in REQUIRED_KEYS. task_status must be SUCCESS,
# FAILED, or PARTIAL_SUCCESS; efficiency_score must be a number from 0 to 1.
# Do not ask for private model reasoning.
#
# Also tell it how to read task_result. An "iteration_limit" run was stopped by
# the harness at its cap, so final_output arrives empty; that is truncation,
# not the model refusing to answer, and must not be critiqued as though the
# model produced nothing.
EVALUATION_INSTRUCTIONS = ""


def _evaluation_error(message: str) -> dict[str, Any]:
    """Return a schema-valid result explaining why evaluation could not finish."""
    # TODO: Return a dict carrying every key in REQUIRED_KEYS so callers always
    # receive the same shape. Use a FAILED task_status, a 0.0 efficiency_score,
    # and place `message` in the critique so the saved artifact stays diagnosable.
    raise NotImplementedError("Return a structured evaluation error.")


def _parse_evaluation(raw_output: str) -> dict[str, Any]:
    """Validate raw evaluator text and coerce it into the required schema."""
    # TODO 1: The model may wrap its JSON in a ``` fence. Strip that before parsing.
    # TODO 2: json.loads the text, but return _evaluation_error on a decode
    # failure rather than raising. A malformed review must not crash the harness.
    # TODO 3: Reject anything whose keys are not exactly REQUIRED_KEYS, whose
    # task_status is outside SUCCESS/FAILED/PARTIAL_SUCCESS, or whose
    # efficiency_score is non-numeric or outside 0 to 1.
    raise NotImplementedError("Parse and validate the evaluator response.")


def run_retrospective_evaluation(
    client: Any,
    deployment: str,
    original_prompt: str,
    execution_trace: list[dict[str, Any]],
    tool_run_log: list[dict[str, Any]],
    final_output: str,
    task_result: str,
) -> dict[str, Any]:
    """Return validated retrospective JSON for one finished task."""
    # TODO 1: Build an evidence object containing original_prompt,
    # execution_trace, tool_run_log, final_output, and task_result.
    # TODO 2: Call client.responses.create with deployment, these evaluator
    # instructions, and the serialized evidence. This must be a NEW call,
    # separate from the primary EDA conversation.
    # TODO 3: Pass review.output_text through _parse_evaluation. Guard the API
    # call too, so a transport failure returns _evaluation_error instead of
    # propagating out of the harness.
    raise NotImplementedError("Implement retrospective evaluation.")
