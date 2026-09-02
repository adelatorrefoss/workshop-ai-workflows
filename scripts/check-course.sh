#!/usr/bin/env bash
set -u

root_dir="$(cd "$(dirname "$0")/.." && pwd)"
output_file="$(mktemp)"
trap 'rm -f "$output_file"' EXIT

fail() { echo "scaffold failure: $*" >&2; exit 1; }
green() {
  local exercise="$1" command="$2"
  (cd "$root_dir/$exercise" && make "$command") >"$output_file" 2>&1 || { cat "$output_file"; fail "$exercise make $command should pass"; }
  echo "$exercise: green (make $command)"
}
red() {
  local exercise="$1" command="$2" marker="$3"
  if (cd "$root_dir/$exercise" && make "$command") >"$output_file" 2>&1; then cat "$output_file"; fail "$exercise make $command should fail initially"; fi
  grep -q "$marker" "$output_file" || { cat "$output_file"; fail "$exercise missing expected diagnostic: $marker"; }
  echo "$exercise: expected red (make $command)"
}

exercises=(exercise-01-workflow exercise-02-crystallized-workflow exercise-03-executable-feedback exercise-04-autonomous-loop exercise-05-protected-validation exercise-06-github-issue-to-pr exercise-07-ci-feedback-loop)
for exercise in "${exercises[@]}"; do
  for required in README.md AGENTS.md Makefile prompts; do
    [[ -e "$root_dir/$exercise/$required" ]] || fail "$exercise is missing $required"
  done
  find "$root_dir/$exercise" -name '*.csproj' -print -quit | grep -q . || fail "$exercise has no .NET project"
  grep -q '## Learning goal' "$root_dir/$exercise/README.md" || fail "$exercise README lacks a learning goal"
  grep -q '## Success and reflection' "$root_dir/$exercise/README.md" || fail "$exercise README lacks success and reflection guidance"
done

grep -q 'Module 7 — Workflows' "$root_dir/README.md" || fail "README lacks module identity"
grep -q 'Codesai Training: Advanced AI-Assisted Development' "$root_dir/README.md" || fail "README lacks course identity"
grep -q 'net10.0' "$root_dir/exercise-01-workflow/InterestApi/InterestApi.csproj" || fail "exercise baseline is not .NET 10"

green exercise-01-workflow validate
green exercise-02-crystallized-workflow validate
green exercise-03-executable-feedback build
red exercise-03-executable-feedback architecture-test 'ARCHITECTURE FAILURE'
red exercise-04-autonomous-loop validate 'VALIDATION FAILURE'
green exercise-05-protected-validation test
red exercise-05-protected-validation mutation-test 'MUTATION FAILURE'
green exercise-06-github-issue-to-pr validate
green exercise-07-ci-feedback-loop validate
red exercise-07-ci-feedback-loop ci-validate 'CI CONTRACT FAILURE'

echo "course scaffold: all .NET checks passed"
