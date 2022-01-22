from core.actor import Actor
from core.whip import Manager
import time

MINING_SPEED = 10
STARMETAL = 20
OIL = 10
BIG_OIL = 20
GRASS = 12

def main():
    manager = Manager()
    manager.start_keyboard_listener()
    actor = Actor()
    actor.position.monitor.set_coord_map([1,1,1,0,1,1,0,0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,1,1])
    actor.position.update_position()
    
    while True:
        
        print("Точка 1")
        actor.goto(11615.495, 5346.717)
        actor.mine(duration=OIL)
        
        
        print("Точка 2")
        actor.goto(11572.756, 5377.157)
        actor.goto(11551.445, 5346.403)
        actor.mine(duration=BIG_OIL)

        print('Точка 3')
        actor.goto(11523.689, 5326.436)
        actor.mine(duration=OIL)

        print('Точка 4')
        actor.goto(11510.430, 5291.829)
        actor.mine(duration=BIG_OIL)

        print('точка 5')
        actor.goto(11513.987, 5287.432)
        actor.mine(duration=BIG_OIL)

        print('точка 6')
        actor.goto(11523.858, 5286.121)
        actor.mine(duration=BIG_OIL)

        print('Точка 7')
        actor.goto(11531.015, 5277.737)
        actor.mine(duration=OIL)

        print('Точка 8')
        actor.goto(11514.090, 5263.811)
        actor.mine(duration=OIL)

        print('Точка 9')
        actor.goto(11483.474, 5247.959)    
        actor.mine(duration=OIL)
        print('Точка 10')
        actor.goto(11471.914, 5228.829)
        actor.goto(11448.216, 5227.241)
        actor.goto(11436.681, 5210.270)
        actor.mine(duration=GRASS)

        print('Точка 11')
        actor.goto(11400.473, 5194.341)
        actor.goto(11379.456, 5199.916)
        actor.mine(duration=GRASS)

        print('Точка 12')
        actor.goto(11363.336, 5252.456)
        actor.mine(duration=GRASS)
        
        print('Точка 13')
        actor.goto(11313.986, 5251.458)
        actor.mine(duration=GRASS)

        print('Точка 14')
        actor.goto(11269, 5229.003)
        actor.goto(11206.980, 5226.791)
        actor.mine(duration=GRASS)

        print('Точка 15')
        actor.goto(11217.631, 5205.300)
        actor.goto(11190.494, 5190.237)
        actor.goto(11161.155, 5189.012)
        actor.mine(duration=GRASS)

        print('Точка 16')
        actor.goto(11149.558, 5122.118)
        actor.goto(11127.682, 5105.709)
        actor.goto(11069.194, 5121.973)   
        actor.mine(duration=GRASS) 
        
        print('Точка 17')
        actor.goto(11109.650, 5092.443)
        actor.mine(duration=GRASS)
        
        print('Точка 18')
        actor.goto(11101.522, 5041.244)
        actor.mine(duration=GRASS)

        print('Точка 19')
        actor.goto(11082.609, 5047.075)
        actor.goto(11070.378, 5042.667)
        actor.goto(11054.696, 5033.090)
        actor.goto(11013.092, 5039.360)
        actor.mine(duration=GRASS)

        print('Точка 20')
        actor.goto(10990.009, 5022.787)
        actor.mine(duration=8)
        actor.mine(duration=GRASS)
        
        print('Точка 21')
        actor.goto(10982.499, 4996.397)
        actor.goto(10887.707, 4946.187)
        actor.mine(duration=STARMETAL)
        
        actor.goto(10837.271, 4900.684)
        actor.goto(10830.337, 4890.396)
        actor.goto(10853.857, 4876.781)
        actor.mine(duration=STARMETAL)

        print('Точка 22')
        actor.goto(10857.197, 4871.208)
        actor.mine(duration=STARMETAL)
        
        print('Точка 23')
        actor.goto(10854.944, 4867.237)
        actor.mine(duration=STARMETAL)
        
        print('Точка 24')
        
        actor.goto(10805.726, 4935.790)
        actor.goto(10845.920, 4994.616)  
        
        actor.goto(10871.724, 5046.475)
        actor.goto(10887.920, 5043.533)
        print("1")
        actor.goto(10880.182, 5035.351)
        actor.mine(duration=20)
        
        print('Точка 25')
        actor.goto(10884.146, 5037.768)
        actor.mine(duration=20)

        print('Точка 26')
        actor.goto(10888.651, 5038.080)
        actor.mine(duration=20)
        
        print('Точка 27')
        actor.goto(10889.785, 5065.125)
        actor.goto(10944.862, 5127.881)
        actor.goto(10945.932, 5167.389)
        actor.mine(duration=GRASS)
        
        print('Точка 28')
        #actor.goto(10979.371, 5170.572)    
        actor.goto(11020.185, 5190.288)
        actor.goto(11027.443, 5178.898)
        actor.goto(11033.898, 5165.665)
        actor.mine(duration=13)
        
        print('Точка 29')
        actor.goto(11041.823, 5145.408) #надо както поправить
        actor.mine(duration=10)

        print('Точка 30')
        actor.goto(11023.458, 5136.006)
        actor.mine(duration=STARMETAL)

        print('Точка 31')
        actor.goto(11020.576, 5135.396)
        actor.mine(duration=STARMETAL)
        
        print('Точка 32')
        actor.goto(11018.500, 5130.250)
        actor.mine(duration=STARMETAL)

        print("Точка 33")
        actor.goto(11009.003, 5073.260)
        actor.mine(duration=STARMETAL)
        
        print("Точка 34")
        actor.goto(11010.210, 5066.982)
        actor.mine(duration=STARMETAL)
        
        print("Точка 35")
        actor.goto(11009.183, 5062.051)
        actor.mine(duration=STARMETAL)

        print('Точка 36')
        actor.goto(11002.090, 5066.839)
        actor.goto(11004.510, 5102.502)
        
        actor.goto(11018.500, 5130.250)
        actor.goto(11029.630, 5143.912)
        actor.goto(11008.907, 5183.309)#x
        actor.goto(11038.328, 5191.758)
        actor.goto(11042.752, 5183.073)
        actor.mine(duration=STARMETAL)
        
        print('Точка 37')
        actor.goto(11054.464, 5192.147)
        actor.mine(duration=STARMETAL)
        
        print('Точка 38')
        actor.goto(11032.003, 5227.072)
        actor.goto(11051.047, 5241.452)
        #actor.goto(11102.896, 5245.775)
        actor.goto(11103.087, 5247.983)
        actor.goto(11168.207, 5232.209)
        actor.goto(11204.370, 5270.586)
        actor.goto(11217.704, 5271.152)
        actor.goto(11212.917, 5279.033)
        actor.mine(duration=STARMETAL)

        print("Точка 39")
        actor.goto(11218.049, 5284.382)
        actor.mine(duration=STARMETAL)
        
        print("Точка 40")
        actor.goto(11214.134, 5286.854)
        actor.mine(duration=STARMETAL)
        
        print("Точка 41")
        actor.goto(11256.296, 5309.039)
        actor.goto(11275.044, 5313.193)
        actor.mine(duration=STARMETAL)

        
        print("Точка 42")
        actor.goto(11281.005, 5310.565)
        actor.mine(duration=STARMETAL)
        
        print("Точка 43")
        actor.goto(11284.093, 5300.712)
        actor.goto(11272.113, 5299.655)
        actor.mine(duration=STARMETAL)
        
        print("Точка 44")
        actor.goto(11306.544, 5308.945)
        actor.goto(11360.397, 5414.383)
        
        actor.goto(11340.286, 5432.665)
        actor.mine(duration=GRASS)

        print("Точка 45")
        actor.goto(11347.099, 5435.192)
        actor.mine(duration=GRASS)

        print("Точка 46")
        actor.goto(11368.530, 5416.669)
        actor.mine(duration=GRASS)

        print("Точка 47")
        actor.goto(11365.526, 5431.715)
        
        actor.goto(11368.632, 5468.929)
        actor.mine(duration=GRASS)
        
        print("Точка 48")
        actor.goto(11427.451, 5468.803)
        actor.goto(11434.468, 5475.612)
        actor.mine(duration=GRASS)
        
        print("ENDPOINT")
        actor.goto(11515.959, 5442.206)
        actor.goto(11532.860, 5422.133)
    

if __name__ == '__main__':
    main()
