"""Hex identity types must be checked before format, never converted to strings.

Issue #15 reader-defect regression.  A decimal integer with forty or sixty-four
digits can satisfy the former str(value) + regex path even though every declared
identity is a JSON string.  Scientific effect: none.
"""
from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from tools.contract_validation import (
    ContractError,
    validate_source_manifest,
    validate_source_ref,
    validate_workspace_snapshot,
)

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"

# Seven separately enforced hash fields across both source-ref variants, the
# source-manifest root and entries, and nested workspace-snapshot repositories.
CASES = (
    ("source_ref.git.json", validate_source_ref, ("commit",), 40, "exact commit required"),
    ("source_ref.git.json", validate_source_ref, ("git_blob_sha1",), 40, "exact blob required"),
    ("source_ref.git.json", validate_source_ref, ("sha256",), 64, "exact sha256 required"),
    ("source_ref.drive.json", validate_source_ref, ("sha256",), 64, "exact sha256 required"),
    ("source_manifest.json", validate_source_manifest, ("commit",), 40, "exact commit required"),
    ("source_manifest.json", validate_source_manifest, ("files", 0, "sha256"), 64, "exact sha256 required"),
    ("workspace_snapshot.json", validate_workspace_snapshot, ("repositories", 0, "commit"), 40, "exact commit required"),
)


def sample(name):
    return json.loads((EXAMPLES / name).read_text(encoding="utf-8"))


def set_field(document, path, value):
    target = document
    for component in path[:-1]:
        target = target[component]
    target[path[-1]] = value


class ExactHexFieldTypes(unittest.TestCase):
    def test_integer_digit_lookalikes_refused_in_every_field(self):
        # A 40- or 64-digit integer is an actual JSON-compatible numeric value.
        # All seven were previously accepted after implicit str(...) coercion.
        self.assertEqual(len(CASES), 7)
        for name, validator, path, width, message in CASES:
            with self.subTest(example=name, field=path):
                document = sample(name)
                set_field(document, path, int("1" * width))
                original = copy.deepcopy(document)
                with self.assertRaises(ContractError) as raised:
                    validator(document)
                self.assertEqual(str(raised.exception), message)
                self.assertEqual(document, original)

    def test_string_digit_lookalikes_still_valid(self):
        for name, validator, path, width, _ in CASES:
            with self.subTest(example=name, field=path):
                document = sample(name)
                set_field(document, path, "1" * width)
                original = copy.deepcopy(document)
                result = validator(document)
                self.assertIsNot(result, document)
                self.assertEqual(result, original)
                self.assertEqual(document, original)

    def test_invalid_hex_strings_still_refused_with_same_diagnostic(self):
        for name, validator, path, width, message in CASES:
            with self.subTest(example=name, field=path):
                document = sample(name)
                set_field(document, path, "g" * width)
                with self.assertRaises(ContractError) as raised:
                    validator(document)
                self.assertEqual(str(raised.exception), message)

    def test_documented_minor_version_allowances_still_accepted(self):
        examples = {name: validator for name, validator, _, _, _ in CASES}
        for name, validator in examples.items():
            for version in ("1.0", "1.1", "01.0", "1.10", "1.00"):
                with self.subTest(example=name, version=version):
                    document = sample(name)
                    document["schema_version"] = version
                    self.assertEqual(validator(document), document)


if __name__ == "__main__":
    unittest.main()
