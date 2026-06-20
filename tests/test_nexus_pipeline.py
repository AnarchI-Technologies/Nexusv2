import unittest

from nexus_orchestration_core import NexusEvent, run_pipeline


class NexusPipelineTests(unittest.TestCase):
    def test_executes_low_risk_high_confidence_event(self):
        decision = run_pipeline(NexusEvent("tenant", "message", {"body": "ok"}, 0.9, 0.2))

        self.assertEqual(decision.action, "execute")
        self.assertFalse(decision.requires_ai)

    def test_holds_high_risk_event(self):
        decision = run_pipeline(NexusEvent("tenant", "deploy", {}, 0.95, 0.9))

        self.assertEqual(decision.action, "hold")

    def test_reviews_risky_write_event(self):
        decision = run_pipeline(NexusEvent("tenant", "payment", {"amount": 7500}, 0.8, 0.5))

        self.assertEqual(decision.action, "review")

    def test_escalates_low_confidence_event(self):
        decision = run_pipeline(NexusEvent("tenant", "market_signal", {}, 0.3, 0.2))

        self.assertEqual(decision.action, "escalate")
        self.assertTrue(decision.requires_ai)


if __name__ == "__main__":
    unittest.main()
