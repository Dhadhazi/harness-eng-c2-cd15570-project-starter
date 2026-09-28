"""Loop 03 scaffold: call deterministic checks around registered tools."""

from __future__ import annotations

from typing import Any

from .loop_01_non_production import HarnessLoop
from harness.stage_05_antidotes import AntidoteRegistry


class HooksLoop(HarnessLoop):
    """A hook detects a lifecycle event; an antidote checks or enriches it."""

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.antidotes = AntidoteRegistry()

    def before_tool_execution(
        self, tool_name: str, tool_input: dict[str, Any]
    ) -> str | None:
        # TODO: Call self.antidotes.pre_tool. Log and print the decision even
        # when it allows the call. Return a BLOCKED message with the reason
        # when validation fails; HarnessLoop then skips the tool handler.
        # tests/test_hook_visibility.py asserts the terminal wording and the
        # tool_run_log keys verbatim, so match the strings it expects exactly
        # rather than inventing your own phrasing.
        raise NotImplementedError("Implement the Loop 03 pre-tool hook.")

    def after_tool_execution(
        self, tool_name: str, tool_input: dict[str, Any], output: str
    ) -> list[str]:
        # TODO: Call self.antidotes.post_tool. Print and log every result, and
        # return its text so HarnessLoop adds it to --- HOOK EVIDENCE --- in
        # the observation sent back to the model. Do not create chart evidence
        # for a blocked or failed chart call. Say so on the terminal when a
        # tool produced no antidote at all, and note that the same test file
        # pins this wording and the log keys verbatim.
        raise NotImplementedError("Implement the Loop 03 post-tool hook.")
