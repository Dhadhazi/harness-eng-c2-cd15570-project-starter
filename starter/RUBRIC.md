# Project Rubric

This is the student-facing copy of the classroom rubric. Reviewers grade the behavior shown by your saved runs and artifacts; a prompt that describes a control is not evidence that the control ran.

## Run the Foundation

| Criteria | Meets Specifications |
|---|---|
| **Run the Default Loop Interactively** | - The run processes a free-form vehicle EDA question.<br>- The trace demonstrates more than one model cycle and at least one tool result returned to the model before the completed answer.<br>- **Evidence:** `outputs/non-production/interactive/answer.md` and `outputs/non-production/interactive/tool_trace.json`. |
| **Run the Non-Production Prompt** | - The run answers the shared EDA question.<br>- The trace records a skill load and a plan approval occurring before any planned data analysis.<br>- The trace includes registered EDA tool calls and their corresponding results.<br>- **Evidence:** `outputs/non-production/prompt/answer.md` and `outputs/non-production/prompt/tool_trace.json`. |

## Add Self-Evaluation and Hooks

| Criteria | Meets Specifications |
|---|---|
| **Show the Retrospective Evaluation** | - The primary task completes and generates an answer.<br>- A separate retrospective evaluation runs after the primary task.<br>- The evaluation JSON contains exactly five fields: `task_status` (SUCCESS, FAILED, or PARTIAL_SUCCESS), `efficiency_score` (0 to 1), `critique`, `systemic_failure_root_cause`, and `workflow_adjustments`.<br>- **Evidence:** `outputs/self-evaluation/prompt/answer.md`, `outputs/self-evaluation/prompt/tool_trace.json`, and `outputs/self-evaluation/prompt/retrospective_evaluation.json`. |
| **Show Hooks and Antidotes** | - The trace records a pre-tool hook decision.<br>- After a `plot_data` call, an ANTIDOTE is recorded containing numeric evidence.<br>- The final answer utilizes the numeric evidence provided by the antidote.<br>- **Evidence:** `outputs/hooks/prompt/answer.md`, `outputs/hooks/prompt/tool_trace.json`, and the corresponding chart file in `outputs/plots/`. |

## Add Permissions and Compare the Runs

| Criteria | Meets Specifications |
|---|---|
| **Show Scoped Permissions** | - The trace shows an allowed read-only tool call (a permission entry with `"decision": "allow"`).<br>- The trace records separate `require_approval` and `granted` entries for the protected `plot_data` and `rank_inventory` tools.<br>- Each approval request displays the exact tool name and arguments, and the grant applies only to that specific request (one approval equals one use).<br>- **Evidence:** `outputs/permissions/prompt/answer.md` and `outputs/permissions/prompt/tool_trace.json`. |
| **Compare the Four Runs** | - A short comparison document, saved as `outputs/comparison.md`, identifies the added component for each of the four loops.<br>- The comparison cites the exact terminal line or artifact proving the component ran and describes its observed effect on the shared EDA task.<br>- **Evidence:** `outputs/comparison.md`, the four `outputs/<loop>/prompt/` runs (answer + trace each), the Loop 02 `retrospective_evaluation.json`, and the charts in `outputs/plots/`. |

## Suggestions to Make Your Project Stand Out

1. **Ablation study and recommendation.** Compare the performance across all four loops and recommend a minimum-viable-harness configuration for Cedar Lane Motors.
2. **Failure log.** Implement a structured log that captures and categorizes agent failures across runs.
3. **Token and cost tracking.** Add a mechanism to track token usage and calculate the cost of each loop.
4. **Data quality analysis.** Run the `data_quality_report` tool on `vehicle_sales_reviews.csv` (which contains deliberate issues) before the agent analyzes it.
5. **Strict permission testing.** Write a custom test proving that if a protected argument changes, the agent cannot reuse an old approval grant.
