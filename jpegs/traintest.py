from detecto import core, utils, visualize

dataset=core.Dataset('jpegs/')
model = core.Model('Drone')

model.fit(dataset)

