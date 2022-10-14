import argparse
parser = argparse.ArgumentParser(description='Goal_position')
parser.add_argument('goal_position', metavar='goal_position', type=str)
args = parser.parse_args()
name_X= args.goal_position

if name_X == 'goal_A':

   print('started to goal')
else:

   print("Goal location doesn't match")
