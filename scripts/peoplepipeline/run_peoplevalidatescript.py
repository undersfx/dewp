"""
This is a basic generated Great Expectations script that runs a checkpoint.

Internally, a Checkpoint is a list of one or more batches paired with one or more
Expectation Suites and a configurable Validation Operator.

Checkpoints can be run directly without this script using the
`great_expectations checkpoint run` command. This script is provided for those
who wish to run checkpoints via python.

Data that is validated is controlled by BatchKwargs, which can be adjusted in
the checkpoint file: great_expectations/checkpoints/peoplevalidatescript.yml.

Data are validated by use of the `ActionListValidationOperator` which is
configured by default. The default configuration of this Validation Operator
saves validation results to your results store and then updates Data Docs.

This makes viewing validation results easy for you and your team.

Usage:
- Run this file: `python great_expectations/uncommitted/run_peoplevalidatescript.py`.
- This can be run manually or via a scheduler such as cron.
- If your pipeline runner supports python snippets you can paste this into your
pipeline.
"""
import sys

from great_expectations import DataContext

# checkpoint configuration
context = DataContext("great_expectations")
checkpoint = context.get_checkpoint("peoplevalidatescript")

# run the Checkpoint
results = checkpoint.run()

# take action based on results
if not results["success"]:
    print('{"result":"fail"}')
    sys.exit(0)

print('{"result":"pass"}')
sys.exit(0)
