"""Regression: arbitrarily long ASCII schema majors must not leak Python int limits.

Issue #15: the reader permits a decimal spelling of major 1 (including leading
zeroes), but every unsupported major must raise ContractError rather than an
interpreter-dependent ValueError. No external dependencies or schema changes.
"""
from __future__ import annotations

import json
import unittest
from pathlib import Path

from tools.contract_validation import (
    ContractError,
    parse_major,
    validate_repository_role,
    validate_source_manifest,
    validate_source_ref,
    validate_workspace_snapshot,
)

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"
VALIDATORS = (
    ("source_ref.git.json", validate_source_ref),
    ("source_ref.drive.json", validate_source_ref),
    ("repository_role.json", validate_repository_role),
    ("source_manifest.json", validate_source_manifest),
    ("workspace_snapshot.json", validate_workspace_snapshot),
)
# Above CPython 3.11+'s default 4,300-digit integer-conversion limit.
UNSUPPORTED_MAJORS = ("9" * 5000, "0" * 5000 + "2")
SUPPORTED_PADDED_ONE = "0" * 5000 + "1"


class LongSchemaMajorTests(unittest.TestCase):
    def test_oversized_unsupported_major_is_contract_error(self):
        for major in UNSUPPORTED_MAJORS:
            with self.subTest(major_length=len(major), suffix=major[-3:]):
                with self.assertRaisesRegex(ContractError, "^unsupported schema major$"):
                    parse_major(major + ".0")

    def test_oversized_leading_zero_major_one_is_still_supported(self):
        for minor in ("0", "15"):
            with self.subTest(minor=minor):
                self.assertEqual(parse_major(SUPPORTED_PADDED_ONE + "." + minor), 1)

    def test_all_reader_shapes_reject_oversized_unsupported_major(self):
        for name, validate in VALIDATORS:
            for major in UNSUPPORTED_MAJORS:
                with self.subTest(example=name, suffix=major[-3:]):
                    source = json.loads((EXAMPLES / name).read_text(encoding="utf-8"))
                    source["schema_version"] = major + ".7"
                    with self.assertRaisesRegex(ContractError, "^unsupported schema major$"):
                        validate(source)

    def test_all_reader_shapes_accept_oversized_leading_zero_one(self):
        for name, validate in VALIDATORS:
            with self.subTest(example=name):
                source = json.loads((EXAMPLES / name).read_text(encoding="utf-8"))
                source["schema_version"] = SUPPORTED_PADDED_ONE + ".7"
                output = validate(source)
                self.assertEqual(output["schema_version"], source["schema_version"])
                self.assertIsNot(output, source)
                self.assertEqual(source["schema_version"], SUPPORTED_PADDED_ONE + ".7")

    def test_short_version_contract_unchanged(self):
        for version in ("1.0", "01.0", "0001.123"):
            self.assertEqual(parse_major(version), 1)
        for version in ("0.0", "2.0", "02.1"):
            with self.subTest(version=version):
                with self.assertRaisesRegex(ContractError, "^unsupported schema major$"):
                    parse_major(version)
        for version in ("1", "+1.0", "1.0.0", "1.0\n"):
            with self.subTest(version=version):
                with self.assertRaisesRegex(ContractError, "^invalid schema_version$"):
                    parse_major(version)


if __name__ == "__main__":
    unittest.main()
