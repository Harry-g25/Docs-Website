import unittest

from examples.heat_loss_app.calc import Room, Surface, conduction_heat_loss_w, room_heat_loss_w, ventilation_heat_loss_w


class TestCalc(unittest.TestCase):
    def test_conduction(self) -> None:
        surfaces = [Surface(name="Wall", kind="wall", area_m2=10.0, u_value_w_m2k=0.3)]
        self.assertAlmostEqual(conduction_heat_loss_w(surfaces, 20), 60.0)

    def test_ventilation(self) -> None:
        self.assertAlmostEqual(ventilation_heat_loss_w(50, 0.5, 20), 165.0)

    def test_room_total(self) -> None:
        room = Room(name="Room", volume_m3=50, ach=0.5)
        surfaces = [Surface(name="Wall", kind="wall", area_m2=10.0, u_value_w_m2k=0.3)]
        q_cond, q_vent, q_total = room_heat_loss_w(room, surfaces, 20)
        self.assertAlmostEqual(q_cond, 60.0)
        self.assertAlmostEqual(q_vent, 165.0)
        self.assertAlmostEqual(q_total, 225.0)


if __name__ == "__main__":
    unittest.main()
