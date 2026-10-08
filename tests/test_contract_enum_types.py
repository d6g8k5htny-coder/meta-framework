"""Enum-shaped JSON must fail through ContractError, not hashing exceptions."""
from __future__ import annotations

import copy
import json
import unittest

from tools.contract_validation import (
    ContractError,
    validate_repository_role,
    validate_source_ref,
)

NONSTRING_JSON = ('[]', '["public"]', '{}', '{"value":"public"}',
                  'null', 'false', 'true', '0', '1.5')


def source_ref(kind="git"):
    row = {"schema_version": "1.0", "kind": kind, "role": "test-source",
           "visibility": "public", "sha256": "a" * 64, "size_bytes": 1}
    if kind == "git":
        row.update(repository="d6g8k5htny-coder/Math-", commit="b" * 40,
                   path="proof.txt", git_blob_sha1="c" * 40)
    else:
        row.update(provider="fixture", source_id="fixture-id",
                   monitorability="external-frozen")
    return row


def repository_role():
    return {"schema_version": "1.0", "repository": "d6g8k5htny-coder/Math-",
            "role_id": "math", "canonical_authority_for": ["proof-routing"],
            "derived_consumers": ["main"], "visibility": "public",
            "runtime_package": None, "scientific_status_authority": False}


class ContractEnumTypes(unittest.TestCase):
    def assert_refused(self, validator, row, message, **kwargs):
        before = copy.deepcopy(row)
        try:
            validator(row, **kwargs)
        except ContractError as exc:
            self.assertEqual(str(exc), message)
        except Exception as exc:
            self.fail("expected ContractError, got %s: %s" %
                      (type(exc).__name__, exc))
        else:
            self.fail("invalid enum value was accepted")
        finally:
            self.assertEqual(row, before, "validation must not mutate its input")

    def assert_accepted(self, validator, row, **kwargs):
        before = copy.deepcopy(row)
        result = validator(row, **kwargs)
        self.assertEqual(result, before)
        self.assertEqual(row, before)
        self.assertIsNot(result, row)

    def test_source_visibility_nonstring_json_is_handled(self):
        for kind in ("git", "external"):
            for raw in NONSTRING_JSON:
                with self.subTest(kind=kind, raw=raw):
                    row = source_ref(kind)
                    row["visibility"] = json.loads(raw)
                    self.assert_refused(validate_source_ref, row,
                                        "invalid visibility", public=False)

    def test_role_visibility_nonstring_json_is_handled(self):
        for raw in NONSTRING_JSON:
            with self.subTest(raw=raw):
                row = repository_role()
                row["visibility"] = json.loads(raw)
                self.assert_refused(validate_repository_role, row, "invalid visibility")

    def test_visibility_unknown_strings_still_refused(self):
        for bad in ("", "Public", " public", "private ", "external-live", "public\n"):
            for kind in ("git", "external", "role"):
                with self.subTest(kind=kind, value=bad):
                    row = repository_role() if kind == "role" else source_ref(kind)
                    row["visibility"] = bad
                    validator = validate_repository_role if kind == "role" else validate_source_ref
                    kwargs = {} if kind == "role" else {"public": False}
                    self.assert_refused(validator, row, "invalid visibility", **kwargs)

    def test_allowed_visibility_values_remain_unchanged(self):
        for visibility in ("public", "private"):
            for kind in ("git", "external", "role"):
                with self.subTest(kind=kind, visibility=visibility):
                    row = repository_role() if kind == "role" else source_ref(kind)
                    row["visibility"] = visibility
                    validator = validate_repository_role if kind == "role" else validate_source_ref
                    kwargs = {} if kind == "role" else {"public": False}
                    self.assert_accepted(validator, row, **kwargs)

    def test_public_source_policy_still_refuses_private(self):
        for kind in ("git", "external"):
            with self.subTest(kind=kind):
                row = source_ref(kind)
                row["visibility"] = "private"
                self.assert_refused(validate_source_ref, row,
                                    "public contract requires public visibility")

    def test_monitorability_nonstring_json_is_handled(self):
        for raw in NONSTRING_JSON:
            with self.subTest(raw=raw):
                row = source_ref("external")
                row["monitorability"] = json.loads(raw)
                self.assert_refused(validate_source_ref, row, "invalid monitorability")

    def test_monitorability_unknown_strings_still_refused(self):
        for bad in ("", "public", "External-live", " external-frozen", "external-live\n"):
            with self.subTest(value=bad):
                row = source_ref("external")
                row["monitorability"] = bad
                self.assert_refused(validate_source_ref, row, "invalid monitorability")

    def test_allowed_monitorability_values_remain_unchanged(self):
        for value in ("external-frozen", "external-live"):
            with self.subTest(value=value):
                row = source_ref("external")
                row["monitorability"] = value
                self.assert_accepted(validate_source_ref, row)

    def test_missing_enum_members_keep_existing_refusals(self):
        for kind in ("git", "external", "role"):
            with self.subTest(kind=kind):
                row = repository_role() if kind == "role" else source_ref(kind)
                del row["visibility"]
                validator = validate_repository_role if kind == "role" else validate_source_ref
                self.assert_refused(validator, row, "invalid visibility")
        row = source_ref("external")
        del row["monitorability"]
        self.assert_refused(validate_source_ref, row, "invalid monitorability")


if __name__ == "__main__":
    unittest.main()
