from core.actor import Actor
from core.whip import Manager


MINING_SPEED = 10


def main():
    manager = Manager()
    manager.start_keyboard_listener()
    actor = Actor()
    
    actor.position.update_position()
    #actor.position.monitor.set_coord_map([1,1,1,0,1,1,0,0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,1,1])
    actor.position.monitor.set_coord_map([1,1,1,0,1,1,1,0,0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,1])

    print("Точка 1")
    actor.goto(11615.495, 5346.717)
    actor.mine(duration=MINING_SPEED)
    
    
    print("Точка 2")
    actor.goto(11572.756, 5377.157)
    actor.goto(11549, 5347.096)
    actor.mine(duration=20)

    print('Точка 3')
    actor.goto(11523.689, 5326.436)
    #actor.mine(duration=MINING_SPEED)

    print('Точка 4')
    actor.goto(11510.430, 5291.829)

    print('точка 5')
    actor.goto(11513.987, 5287.432)

    print('точка 6')
    actor.goto(11523.858, 5286.121)

    print('Точка 7')
    actor.goto(11531.015, 5277.737)

    print('Точка 8')
    actor.goto(11514.090, 5263.811)
    
    print('Точка 9')
    actor.goto(11483.474, 5247.959)    

    print('Точка 10')
    actor.goto(11471.914, 5228.829)
    actor.goto(11448.216, 5227.241)
    actor.goto(11436.681, 5210.270)

    print('Точка 11')
    actor.goto(11400.473, 5194.341)
    actor.goto(11379.456, 5199.916)

    print('Точка 12')
    actor.goto(11363.336, 5252.456)

    print('Точка 13')
    actor.goto(11313.986, 5251.458)
    
    print('Точка 14')
    actor.goto(11206.980, 5226.791)

    print('Точка 15')
    actor.goto(11217.631, 5205.300)
    actor.goto(11190.494, 5190.237)

    print('Точка 16')
    actor.goto(11161.155, 5189.012)
    actor.goto(11149.558, 5122.118)
    actor.goto(11127.682, 5105.709)
    actor.goto(11069.194, 5121.973)    
    
    print('Точка 17')
    actor.goto(11109.650, 5092.443)

    print('Точка 18')
    actor.goto(11101.522, 5041.244)


if __name__ == '__main__':
    main()
