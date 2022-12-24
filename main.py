# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_1 = 'Ruud Guillit' #the player who scored first goal
goal_0 = 32 #time of first goal
player_2 = 'van Basten' #the player who score second goal
goal_1=54 #time of second goal

scorers = f'[{player_1}] scored in the {goal_0}nd minute \n {player_2} scored in the {goal_1}th minute'
print (scorers)


player = 'Michel Vautrot'
name_short = 'M Vautrot'
s1 = slice(6)
first_name = (player[s1])
print (first_name)
s2=slice (7,14)
last_name = (player[s2])
print (last_name)
last_name_len = len(last_name)
print (last_name_len)

s4= slice(3)
chant= (player[s4])
chant_1= chant+'!'
print (chant_1, chant_1,chant_1)