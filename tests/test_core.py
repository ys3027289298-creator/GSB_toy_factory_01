import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_no_duplicate_feed(self):
        state = core.new_game()
        self.assertTrue(core.feed(state, 1, 10))
        self.assertFalse(core.feed(state, 1, 10))

    def test_02_line_capacity(self):
        state = core.new_game()
        state["line_load"] = 2
        result = core.produce_line(state, 1)
        self.assertFalse(result)

    def test_03_fee_exact(self):
        state = core.new_game()
        self.assertEqual(core.fee(state, 1, 3), 2)

    def test_04_cancel_refunds_material(self):
        state = core.new_game()
        core.feed(state, 1, 5)
        core.cancel(state, 1)
        self.assertEqual(state["material"], 100)

    def test_05_no_produce_on_fault(self):
        state = core.new_game()
        state["detect_fault"] = True
        result = core.produce(state, 5)
        self.assertFalse(result)

    def test_06_defect_once(self):
        state = core.new_game()
        core.defect(state)
        self.assertEqual(state["yield_rate"], 95)

    def test_07_no_ship_without_parts(self):
        state = core.new_game()
        state["parts"] = 0
        result = core.ship(state, 1)
        self.assertFalse(result)

    def test_08_load_preserves_order(self):
        state = core.new_game()
        state["order_id"] = 4
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["order_id"], 4)


if __name__ == "__main__":
    unittest.main()
