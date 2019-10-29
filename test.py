import gym
from gym import wrappers

env = gym.make("MsPacman-v0")
env = wrappers.Monitor(env, "./gym-results", force=True)
env.reset()
for _ in range(1000):
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    if done: break
print(observation.shape)
print(info)
env.close()
