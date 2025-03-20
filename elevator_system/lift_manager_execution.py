from elevator_system.lift_manager import LiftManager

if __name__ == "__main__":
    lift_manager = LiftManager()
    lift_manager.init(floors=6, lifts=2, lifts_capacity=2, helper=None)
    print(lift_manager.request_lift(floor=0, direction='U'))
    print(lift_manager.request_lift(floor=5, direction='D'))
    lift_manager.press_floor_button_in_lift(lift_index=0, floor=4)
    lift_manager.tick()
    print(lift_manager.get_lift_state(lift_index=0))
    print(lift_manager.get_lift_state(lift_index=1))